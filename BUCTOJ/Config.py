'''
Author: LetMeFly
Date: 2022-02-21 15:39:38
LastEditors: LetMeFly
LastEditTime: 2022-02-21 17:00:52
'''

global info
info = {
    "base_url": "https://buctcoder.com/"
}

def set_info(key: str, value: str) -> None:
    info[key] = value

def get_info(key: str) -> str:
    return info.get(key, None)
