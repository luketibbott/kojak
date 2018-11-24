# This is a helper file to clean Austin animal shelter data

import re
import numpy as np

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