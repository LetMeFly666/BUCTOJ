'''
Author: LetMeFly
Date: 2022-01-25 18:07:26
LastEditors: LetMeFly
LastEditTime: 2022-01-26 11:05:42
'''
# __all__ = ['AutoGetAndSubmit', 'FromPidToChar', 'GetASourceCodeAndChange', 'GetContestProblemList', 'Login', 'SubmitOneCode']
from .Login import login
from .AutoGetAndSubmit import main as finish1contest
from .SubmitOneCode import submit
