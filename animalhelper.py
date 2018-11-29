# This is a helper file to clean Austin animal shelter data

import re
import numpy as np
import pandas as pd

dictionary_string = ''

# Read dictionary string in from previously parsed file
with open('dog_breeds.txt', 'r') as file:
    for line in file:
        dictionary_string += line

dog_groups = eval(dictionary_string)

# We'll use this set and dictionary below to get a simple color for each animal
standard_colors = {'White', 'Sable', 'Black', 'Brown', 'Tricolor',
       'Yellow', 'Blue', 'Gray', 'Red'}

color_mapper = {'Tan': 'Yellow', 'Chocolate': 'Brown', 'Cream': 'White', 'Gold': 'Yellow', 'Silver': 'Gray',
                    'Fawn': 'Brown', 'Apricot': 'White', 'Liver': 'White', 'Agouti': 'Brown', 'Orange': 'Red',
                    'Ruddy': 'Red', 'Buff': 'Brown', 'Calico': 'Tricolor', 'Torbie': 'Brown', 'Tortie': 'Brown',
                    'Lynx': 'White', 'Seal': 'White', 'Lilac': 'Gray', 'Flame': 'White', 'Pink': 'Red'}

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

    if month in winter:
        return 'winter'

    elif month in spring:
        return 'spring'

    elif month in summer:
        return 'summer'

    else:
        return 'fall'

def encode_response(s):
    if s == 'Adoption':
        return 0
    elif s == 'Transfer':
        return 1
    elif s == 'Return to Owner':
        return 2
    elif s == 'Euthanasia':
        return 3
    elif s == 'Died':
        return 4
    elif s == 'Disposal':
        return 5
    elif s == 'Rto-Adopt':
        return 6
    elif s == 'Missing':
        return 7
    else:
        return 8

def cat_breed(s, m):
    s = s.lower()
    mix = 0
    group = None
    if ('mix' in s) or ('domestic' in s):
        mix = 1
    if 'medium hair' in s:
        group = 'medium hair'
    if 'longhair' in s:
        group = 'long hair'
    else:
        group = 'short hair'

    if m == True:
        return mix
    else:
        return group

def group_dogs(s, m):
    mix = 0
    group = None

    if 'Mix' in s:
        mix = 1
        s = s[:-4]

    if '/' in s:
        s = s.split('/')[0]
        mix = 1
        
    if s in dog_groups.keys():
        group = dog_groups[s]
        
    # Pit bulls are not recognized by the AKC but make up 14,000 observations in our dataset
    if ('Pit Bull' in s) or ('Staffordshire Terrier' in s):
        group = 'Terrier'
    # American Bulldogs are Mastiffs, which AKC considers to be 'Working'
    if 'American Bulldog' in s:
        group = 'Working'

    # Chihuahua is written slightly differently on the wikipedia page than in the data, so we catch it here
    if 'Chihuahua' in s:
        group = 'Toy'
    # Queensland Heeler is another name for Australian Cattle Dog, which belongs to the herding group
    if 'Queensland Heeler' in s:
        group = 'Herding'
    # Some entries are 'Plott hound', others are 'Plott'
    if 'Plott' in s:
        group = 'Hound'

    if group == None:
        group = s
    
    if m:
        return mix
    else:
        return group

def end_color(s):
    # No manipulation needed -- color is already appropriately reduced
    if s in standard_colors:
        return s
    # Map from specific color to more general color
    elif s in color_mapper.keys():
        return color_mapper[s]
    # Failed to get a general color
    return s

def color(s):
    result = end_color(s)

    # Color is buried in a statement with '/' or ' '
    if result not in standard_colors:
        if '/' in s:
            s = s.split('/')[0]
            # Case when space is on left side of '/'
            if ' ' in s:
                s = s.split(' ')[0]
            result = end_color(s)
        # Case when there's no '/', but color has a ' ' in it
        elif ' ' in s:
            s = s.split(' ')[0]
            result = end_color(s)
        
    return result

def impute_fixed_status(s):
    if s == 'unknown':
        return 'fixed'
    else:
        return s
    