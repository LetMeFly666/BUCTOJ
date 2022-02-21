'''
Author: LetMeFly
Date: 2022-01-24 14:57:01
LastEditors: LetMeFly
LastEditTime: 2022-02-21 17:08:29
'''
import hashlib
import requests



def password2md5(passowrd):
    return hashlib.md5(str(passowrd).encode('utf-8')).hexdigest()


def login(user_id: str, password: str) -> requests.cookies.RequestsCookieJar:
    """
    通过账号和密码返回cookie
    """
    from . import Config  # 不可以放到文件头部进行import！！！
    base_url = Config.get_info("base_url")
    url = f'{base_url}login.php'
    data = {'user_id': user_id, 'password': password2md5(password)}
    response = requests.post(url, data=data)
    return response.cookies
