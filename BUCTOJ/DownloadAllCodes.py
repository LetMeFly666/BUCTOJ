'''
Author: LetMeFly
Date: 2024-06-03 23:24:40
LastEditors: LetMeFly
LastEditTime: 2024-06-03 23:34:21
'''
import requests
from bs4 import BeautifulSoup
try:
    import lxml
    features = 'lxml'
except:
    features = None
from os.path import exists
from os import mkdir


def get1page(url) -> list:
    """
    获取一页的所有提交，返回“所有提交的列表”
    列表中每个元素都是html的tr
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('table', attrs={"id": "result-tab"})
    trs = table.find('tbody').find_all('tr')
    return trs


def getAllpages(baseurl):
    results = []

    thisPage = get1page(baseurl)
    while True:
        results += thisPage
        if not thisPage or len(thisPage) == 1:
            break
        prevtop = thisPage[0].find('td').get_text()
        top = thisPage[-1].find('td').get_text()
        print(top, prevtop)
        newUrl = baseurl + f'&top={top}&pretop={prevtop}'
        thisPage = get1page(newUrl)
        if thisPage:
            thisPage = thisPage[1:]
    return results


def get1codeBySubmissionId(submissionId, cookies):
    from . import Config
    base_url = Config.get_info("base_url")
    response = requests.get(f'{base_url}showsource.php?id={submissionId}', cookies=cookies)
    soup = BeautifulSoup(response.text, 'lxml')
    code = soup.find('pre')
    return code.get_text()


def saveAllCodes(baseurl, cookies):
    results = getAllpages(baseurl)
    print(f'Total num: {len(results)}')
    if not exists('results'):
        mkdir('results')
    for thisSubmission in results:
        submissionId = thisSubmission.find('td').get_text()
        userid = thisSubmission.find_all('td')[1].get_text()
        print(f'Getting {userid}\'s submssion {submissionId}')
        code = get1codeBySubmissionId(submissionId, cookies=cookies)
        with open(f'results/{userid}-{submissionId}.java', 'w', encoding='utf-8') as f:
            f.write(code)

