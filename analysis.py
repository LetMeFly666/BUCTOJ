'''
Author: LetMeFly
Date: 2024-06-03 22:26:21
LastEditors: LetMeFly
LastEditTime: 2024-06-03 22:31:02
'''
import os
allResults = []
notTryCatchResults = []


def iftryCatch(code):
    return 'try' in code and 'catch' in code

for file in os.listdir('results'):
    filename = f'results/{file}'
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()
    userid = file.split('-')[0]
    submissionId = file.split('.')[0].split('-')[1]
    thisTuple = (userid, submissionId, iftryCatch(code))
    allResults.append(thisTuple)
    if not thisTuple[2]:
        notTryCatchResults.append(thisTuple)

print(notTryCatchResults)
with open('allResults.txt', 'w', encoding='utf-8') as f:
    f.write(f'{allResults}')
with open('notTryCatchResults.txt', 'w', encoding='utf-8') as f:
    f.write(f'{notTryCatchResults}')