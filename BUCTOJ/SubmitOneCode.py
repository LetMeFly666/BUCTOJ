'''
Author: LetMeFly
Date: 2022-01-24 15:55:51
LastEditors: LetMeFly
LastEditTime: 2022-05-02 18:57:26
'''
import requests


def submit(cid: str, pid: str, cookies: requests.cookies.RequestsCookieJar,
           code: str) -> None:
    from . import Config
    base_url = Config.get_info("base_url")
    url = f"{base_url}submit.php"
    data = {
        'cid': cid,
        'pid': pid,
        'language': '1',  # C++
        'source': code
    }
    response = requests.post(url, data=data, cookies=cookies)


def submitById(cookies: requests.cookies.RequestsCookieJar, id: str, code: str,
               language: str) -> None:
    from . import Config
    base_url = Config.get_info("base_url")
    url = f"{base_url}submit.php"
    languageTable = {
        "C": "0",
        "C++": "1",
        "Java": "3",
        "Python": "6",
        "PHP": "7",
        "JavaScript": "16",
        "Go": "17",
        "SQL": "18",
    }
    if language in languageTable:
        language = languageTable[language]
    data = {
        'id': id,
        'language': language,
        'source': code,
    }
    response = requests.post(url, data=data, cookies=cookies)
    return response
