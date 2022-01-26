'''
Author: LetMeFly
Date: 2022-01-24 15:18:26
LastEditors: LetMeFly
LastEditTime: 2022-01-26 11:00:24
Description:
    从题目编号(数字)到题目编号(字母)
        0: A
    1: B
    2: C
    ...
    25: Z
    26: AA
    27: AB
    ...
    51: AZ
    52: BA
    ...
    701: ZZ
    702: ''
    703: ''
    
    只有前701道题有编号，也就是说字母编号只有两位
    低位从A~Z，相当于26进制
    高位从''(空)到A~Z，相当于27进制
    表达范围：[0, 27 * 26) = [0, 701]
'''
def i2s(num: int) -> str:
    if num < 26:
        return chr(ord('A') + num)
    else:
        return chr(ord('A') + num // 26 - 1) + chr(ord('A') + num % 26)
