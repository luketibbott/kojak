# This is a helper file to clean Austin animal shelter data

import re
import numpy as np
import pandas as pd

def get_days(s):
    # takes string s in format similar to "11 years" and returns an int that represents the number of days described in s

    try:
        digits = re.match(r'(\d{1,3})', s).groups()[0]
    except:
        return np.nan

    units = s.split(' ')[1]

    if units == 'days' or units == 'day':
        return int(digits)

    elif units == 'weeks' or units == 'week':
        return int(digits)*7

    elif units == 'months' or units == 'month':
        return int(digits)*30
    
    elif units == 'years' or units == 'year':
        return int(digits)*365

def encode_name(s):
    if str(s) == 'None': 
        return 0
    else:
        return 1

def get_gender(s):
    if 'female' in s.lower():
        return 1
    else:
        return 0

def get_fixed_status(s):
    s = s.lower()

    if 'intact' in s:
        return 'intact'
    elif 'neutered' in s or 'spayed' in s:
        return 'fixed'
    else:
        return 'unknown'

def get_season(d):
    d = pd.to_datetime(d)

    month = d.month

    winter = {1, 2, 3}
    spring = {4, 5, 6}
    summer = {7, 8, 9}
    fall = {10, 11, 12}

    if month in winter:
        return 'winter'

    elif month in spring:
        return 'spring'

    elif month in summer:
        return 'summer'
        
    else:
        return 'fall'
