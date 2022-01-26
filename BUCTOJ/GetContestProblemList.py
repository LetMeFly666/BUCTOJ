'''
Author: LetMeFly
Date: 2022-01-24 15:01:27
LastEditors: LetMeFly
LastEditTime: 2022-01-26 11:00:58
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
    response = requests.get('http://182.92.175.181/contest.php?cid='+str(cid), cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    table = soup.find('table')
    return len(table.find('tbody').find_all('tr'))
