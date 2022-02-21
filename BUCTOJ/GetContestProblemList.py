'''
Author: LetMeFly
Date: 2022-01-24 15:01:27
LastEditors: LetMeFly
LastEditTime: 2022-02-21 17:12:04
Description: 获取某场比赛的题面数量
'''
import requests
from bs4 import BeautifulSoup

try:
    import lxml
    features = 'lxml'
except:
    features = None


def getContestProblemList(cid: str, cookies='') -> int:
    from . import Config
    base_url = Config.get_info("base_url")
    response = requests.get(f'{base_url}contest.php?cid='+str(cid), cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    table = soup.find('table')
    return len(table.find('tbody').find_all('tr'))
