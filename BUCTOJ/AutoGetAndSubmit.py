'''
Author: LetMeFly
Date: 2022-01-24 12:51:09
LastEditors: LetMeFly
LastEditTime: 2022-02-21 00:59:01
'''
import requests
from . import Login  # 由账号密码到登录后的cookie
from . import GetContestProblemList  # 获取比赛有多少题目
from . import FromPidToChar  # 从题目的数字编号到字母编号
from . import GetASourceCodeAndChange  # 用Admin获取一道通过的C++代码
from . import SubmitOneCode
import time


def finish1contest(cid: str, cookie_my: requests.cookies.RequestsCookieJar, cookie_admin: requests.cookies.RequestsCookieJar, sleep_time: int) -> None:
    problem_num = GetContestProblemList.getContestProblemList(cid, cookie_my)
    print(f"比赛{cid}共有{problem_num}道题目")
    for pid in range(problem_num):
        pid_str = FromPidToChar.i2s(pid)
        try:
        # if True:
            code = GetASourceCodeAndChange.getASourceCodeAndChange(cid, pid, cookie_admin)
        except:
        # else:
            print(f"Problem{pid_str}暂未有C++通过者")
            continue
        SubmitOneCode.submit(cid, pid, cookie_my, code)
        print(f"Problem{pid_str}已提交")
        time.sleep(sleep_time)
        

def main(cid: str, username_my, password_my, username_admin, password_admin, sleep_time = 15) -> None:
    """
    自动Copy代码并完成比赛 + 不被查重
        Input: 比赛的cid、要自动提交的账号的用户名和密码、Admin的用户名和密码
        Output: 完成一场比赛(前提是每道题都有人提交了C++代码)
    """
    cookie_my = Login.login(username_my, password_my)
    cookie_admin = Login.login(username_admin, password_admin)
    finish1contest(cid, cookie_my, cookie_admin, sleep_time=sleep_time)
    

