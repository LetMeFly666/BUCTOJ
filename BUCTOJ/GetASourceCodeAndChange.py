'''
Author: LetMeFly
Date: 2022-01-24 16:04:55
LastEditors: LetMeFly
LastEditTime: 2022-02-21 17:11:20
'''
import requests
from bs4 import BeautifulSoup
import random
import string
from . import FromPidToChar  # 从题目的数字编号到字母编号
try:
    import lxml
    features = 'lxml'
except:
    featrues = None


def getASourceCode_0(cid: str, pid_str: str, cookies: requests.cookies.RequestsCookieJar) -> str:
    """
    通过admin的cookie获得一个通过的C++代码(前提是有人通过)
    """
    from . import Config
    base_url = Config.get_info("base_url")
    url = f"{base_url}status.php?cid={cid}&problem_id={pid_str}&user_id=&language=1&jresult=4&showsim=0"
    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    table = soup.find('table', attrs={"id": "vueAppFuckSafari"})
    tr = table.find('tbody').find('tr')
    td = tr.find_all('td')[6]
    a = td.find_all('a')[1]
    from . import Config
    base_url = Config.get_info("base_url")
    href = base_url + a.get('href')
    response = requests.get(href, cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    code = soup.find('pre').string
    return code


def getASourceCode(cid: str, pid: str, cookies: requests.cookies.RequestsCookieJar) -> str:
    """
    通过admin的cookie获得一个通过的C++代码(前提是有人通过)
    """
    from . import Config
    base_url = Config.get_info("base_url")
    url_problem_in_content = f"{base_url}problem.php?cid={cid}&pid={pid}"
    response_problem_in_content = requests.get(url_problem_in_content, cookies=cookies)
    soup_problem_in_content = BeautifulSoup(response_problem_in_content.text, features)
    a_problem_in_content = soup_problem_in_content.find_all("a", attrs={"class": "small"})
    real_pid = str(a_problem_in_content[2].get("href")).split("id=")[1].split("&")[0]
    # print(real_pid)
    url = f"{base_url}status.php?problem_id={real_pid}&user_id=&language=1&jresult=4&showsim=0"
    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    table = soup.find('table', attrs={"id": "vueAppFuckSafari"})
    tr = table.find('tbody').find('tr')
    td = tr.find_all('td')[6]
    a = td.find_all('a')[1]
    href = base_url + a.get('href')
    response = requests.get(href, cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    code = soup.find('pre').string
    return code


def randText() -> str:
    return "".join(random.choice(string.ascii_letters + string.digits + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{()}-+*-.><") for _ in range(2048))


def getASourceCodeAndChange(cid: str, pid: str, cookies: requests.cookies.RequestsCookieJar) -> str:
    try:
    # if True:
        code = getASourceCode(cid=cid, pid=pid, cookies=cookies)
    except:
    # else:
        pid_str = FromPidToChar.i2s(pid)
        code = getASourceCode_0(cid=cid, pid_str=pid, cookies=cookies)
    pre = f"""// LetMeFly_PySubmiter
#include <bits/stdc++.h>
using namespace std;
#define mem(a) memset(a, 0, sizeof(a))
#define dbg(x) cout << #x << " = " << x << endl
#define fi(i, l, r) for (int i = l; i < r; i++)
#define cd(a) scanf("%d", &a)
typedef long long ll;
#ifdef LetMeFly_PySubmiter
{randText()}
#endif
"""
    return pre + code
