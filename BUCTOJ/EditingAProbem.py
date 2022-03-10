'''
Author: LetMeFly
Date: 2022-03-09 17:19:51
LastEditors: LetMeFly
LastEditTime: 2022-03-10 18:00:15
'''
from bs4 import BeautifulSoup
from typing import Tuple
import requests


def get_postkey_and_csrf(cookies: requests.cookies.RequestsCookieJar) -> Tuple[str, str]:
    """
    通过Admin的Cookie获取新建问题需要的postkey和csrf
    """
    from . import Config
    base_url = Config.get_info("base_url")
    add_problem_url = base_url + "admin/problem_add_page.php"
    response_postkey = requests.get(url=add_problem_url, cookies=cookies)
    soup_postkey = BeautifulSoup(response_postkey.text, "lxml")
    postkey = soup_postkey.find("input", attrs={"name": "postkey"}).get("value")
    
    csrf_url = base_url + "csrf.php"
    response_csrf = requests.get(url=csrf_url, cookies=cookies)
    soup_csrf = BeautifulSoup(response_csrf.text, "lxml")
    csrf = soup_csrf.find("input").get("value")
    
    return (postkey, csrf)


def create1problem(cookies: requests.cookies.RequestsCookieJar, title: str, description: str, input: str, output: str, sample_input = "", sample_output = "", hint = "", time_limit = 1, memory_limit = 128, spj = 0, source = "", contest_id = "") -> str:
    """
    通过Admin的Cookie创建一道新的题目
    
    Parameters:
        cookies - 管理号的cookies，可通过from BUCTOJ import login来获得
        title - 题目
        time_limit - 时间限制，默认时间为1s
        memory_limit - 内存限制，默认为128M
        description - 题目描述
        input - 输入描述
        output - 输出描述
        sample_input - 样例输入，默认为空
        sample_output - 样例输出，默认为空
        hint - 提示，默认为空
        spj - 是否为special judge， 默认为0
        source - 来源/分类，默认为空
        contest_id - 属于哪场竞赛/作业，默认为空
    
    Returns:
        problem_id - 新创建的问题的problem_id
    """
    postkey, csrf = get_postkey_and_csrf(cookies)

    from . import Config
    base_url = Config.get_info("base_url")
    url = base_url + 'admin/problem_add.php'
    data = {
        "problem_id": "New Problem",
        "title": title,
        "time_limit": time_limit,
        "memory_limit": memory_limit,
        "description": description,
        "input": input,
        "output": output,
        "sample_input": sample_input,
        "sample_output": sample_output,
        "test_input": "",
        "test_output": "",
        "hint": hint,
        "spj": spj,
        "source": source,
        "contest_id": contest_id,
        "postkey": postkey,
        "submit": "保存",
        "csrf": csrf
    }
    response = requests.post(url=url, cookies=cookies, data=data)
    soup = BeautifulSoup(response.text, "lxml")
    href = soup.find("a").get("href")
    problem_id = href.split("javascript:phpfm(")[1].split(");")[0]

    data["problem_id"] = problem_id
    data["postkey"], data["csrf"] = get_postkey_and_csrf(cookies)
    url = base_url + 'admin/problem_edit.php'
    response = requests.post(url=url, cookies=cookies, data=data)
    return problem_id


