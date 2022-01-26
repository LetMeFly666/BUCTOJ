'''
Author: LetMeFly
Date: 2022-01-24 16:04:55
LastEditors: LetMeFly
LastEditTime: 2022-01-24 17:01:41
'''
import requests
from bs4 import BeautifulSoup
import random
import string
try:
    import lxml
    features = 'lxml'
except:
    featrues = None

import requests
from bs4 import BeautifulSoup
try:
    import lxml
    features = 'lxml'
except:
    featrues = None


def getASourceCode(cid: str, pid: str, cookies: requests.cookies.RequestsCookieJar) -> str:
    """
    通过admin的cookie获得一个通过的C++代码(前提是有人通过)
    """
    url = f"http://182.92.175.181/status.php?cid={cid}&problem_id={pid}&user_id=&language=1&jresult=4&showsim=0"
    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    table = soup.find('table', attrs={"id": "vueAppFuckSafari"})
    tr = table.find('tbody').find('tr')
    td = tr.find_all('td')[6]
    a = td.find_all('a')[1]
    href = 'http://182.92.175.181/' + a.get('href')
    response = requests.get(href, cookies=cookies)
    soup = BeautifulSoup(response.text, features)
    code = soup.find('pre').string
    return code


def randText() -> str:
    return "".join(random.choice(string.ascii_letters + string.digits + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{()}-+*-.><") for _ in range(2048))


def getASourceCodeAndChange(cid: str, pid: str, cookies: requests.cookies.RequestsCookieJar) -> str:
    code = getASourceCode(cid=cid, pid=pid, cookies=cookies)
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
