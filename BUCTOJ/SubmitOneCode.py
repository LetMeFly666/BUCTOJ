'''
Author: LetMeFly
Date: 2022-01-24 15:55:51
LastEditors: LetMeFly
LastEditTime: 2022-02-21 17:12:32
'''
import requests


def submit(cid: str, pid: str, cookies: requests.cookies.RequestsCookieJar, code: str) -> None:
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
    
