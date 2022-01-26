'''
Author: LetMeFly
Date: 2022-01-24 15:55:51
LastEditors: LetMeFly
LastEditTime: 2022-01-24 16:46:13
'''
import requests


def submit(cid: str, pid: str, cookies: requests.cookies.RequestsCookieJar, code: str) -> None:
    url = "http://182.92.175.181/submit.php"
    data = {
        'cid': cid,
        'pid': pid,
        'language': '1',  # C++
        'source': code
    }
    response = requests.post(url, data=data, cookies=cookies)
    
