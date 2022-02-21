'''
Author: LetMeFly
Date: 2022-01-25 18:07:26
LastEditors: LetMeFly
LastEditTime: 2022-02-21 16:58:44
'''
# __all__ = ['AutoGetAndSubmit', 'FromPidToChar', 'GetASourceCodeAndChange', 'GetContestProblemList', 'Login', 'SubmitOneCode']
from .Login import login
from .AutoGetAndSubmit import main as finish1contest
from .SubmitOneCode import submit
