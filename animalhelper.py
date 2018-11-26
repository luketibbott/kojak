# This is a helper file to clean Austin animal shelter data

import re
import numpy as np
import pandas as pd

breeds = ['Blue Lacy','Queensland Heeler','Rhod Ridgeback','Retriever','Chinese Sharpei','Black Mouth Cur',
          'Catahoula','Staffordshire','Affenpinscher','Afghan Hound','Airedale Terrier','Akita',
          'Australian Kelpie','Alaskan Malamute','English Bulldog','American Bulldog',
          'American English Coonhound','American Eskimo Dog (Miniature)','American Eskimo Dog (Standard)',
          'American Eskimo Dog (Toy)','American Foxhound','American Hairless Terrier',
          'American Staffordshire Terrier','American Water Spaniel','Anatolian Shepherd Dog',
          'Australian Cattle Dog','Australian Shepherd','Australian Terrier','Basenji','Basset Hound',
          'Beagle','Bearded Collie','Beauceron','Bedlington Terrier','Belgian Malinois','Belgian Sheepdog',
          'Belgian Tervuren','Bergamasco','Berger Picard','Bernese Mountain Dog','Bichon Fris_',
          'Black and Tan Coonhound','Black Russian Terrier','Bloodhound','Bluetick Coonhound','Boerboel',
          'Border Collie','Border Terrier','Borzoi','Boston Terrier','Bouvier des Flandres','Boxer',
          'Boykin Spaniel','Briard','Brittany','Brussels Griffon','Bull Terrier','Bull Terrier (Miniature)',
          'Bulldog','Bullmastiff','Cairn Terrier','Canaan Dog','Cane Corso','Cardigan Welsh Corgi',
          'Cavalier King Charles Spaniel','Cesky Terrier','Chesapeake Bay Retriever','Chihuahua',
          'Chinese Crested Dog','Chinese Shar Pei','Chinook','Chow Chow',"Cirneco dell'Etna",'Clumber Spaniel',
          'Cocker Spaniel','Collie','Coton de Tulear','Curly-Coated Retriever','Dachshund','Dalmatian',
          'Dandie Dinmont Terrier','Doberman Pinsch','Doberman Pinscher','Dogue De Bordeaux',
          'English Cocker Spaniel','English Foxhound','English Setter','English Springer Spaniel',
          'English Toy Spaniel','Entlebucher Mountain Dog','Field Spaniel','Finnish Lapphund','Finnish Spitz',
          'Flat-Coated Retriever','French Bulldog','German Pinscher','German Shepherd',
          'German Shorthaired Pointer','German Wirehaired Pointer','Giant Schnauzer','Glen of Imaal Terrier',
          'Golden Retriever','Gordon Setter','Great Dane','Great Pyrenees','Greater Swiss Mountain Dog',
          'Greyhound','Harrier','Havanese','Ibizan Hound','Icelandic Sheepdog','Irish Red and White Setter',
          'Irish Setter','Irish Terrier','Irish Water Spaniel','Irish Wolfhound','Italian Greyhound',
          'Japanese Chin','Keeshond','Kerry Blue Terrier','Komondor','Kuvasz','Labrador Retriever',
          'Lagotto Romagnolo','Lakeland Terrier','Leonberger','Lhasa Apso','L_wchen','Maltese',
          'Manchester Terrier','Mastiff','Miniature American Shepherd','Miniature Bull Terrier',
          'Miniature Pinscher','Miniature Schnauzer','Neapolitan Mastiff','Newfoundland','Norfolk Terrier',
          'Norwegian Buhund','Norwegian Elkhound','Norwegian Lundehund','Norwich Terrier',
          'Nova Scotia Duck Tolling Retriever','Old English Sheepdog','Otterhound','Papillon',
          'Parson Russell Terrier','Pekingese','Pembroke Welsh Corgi','Petit Basset Griffon Vend_en',
          'Pharaoh Hound','Plott','Pointer','Polish Lowland Sheepdog','Pomeranian','Standard Poodle',
          'Miniature Poodle','Toy Poodle','Portuguese Podengo Pequeno','Portuguese Water Dog','Pug','Puli',
          'Pyrenean Shepherd','Rat Terrier','Redbone Coonhound','Rhodesian Ridgeback','Rottweiler',
          'Russell Terrier','St. Bernard','Saluki','Samoyed','Schipperke','Scottish Deerhound','Scottish Terrier',
          'Sealyham Terrier','Shetland Sheepdog','Shiba Inu','Shih Tzu','Siberian Husky','Silky Terrier',
          'Skye Terrier','Sloughi','Smooth Fox Terrier','Soft-Coated Wheaten Terrier','Spanish Water Dog',
          'Spinone Italiano','Staffordshire Bull Terrier','Standard Schnauzer','Sussex Spaniel',
          'Swedish Vallhund','Tibetan Mastiff','Tibetan Spaniel','Tibetan Terrier','Toy Fox Terrier',
          'Treeing Walker Coonhound','Vizsla','Weimaraner','Welsh Springer Spaniel','Welsh Terrier',
          'West Highland White Terrier','Whippet','Wire Fox Terrier','Wirehaired Pointing Griffon',
          'Wirehaired Vizsla','Xoloitzcuintli','Yorkshire Terrier']
groups = ['Herding','Herding','Hound','Sporting','Non-Sporting','Herding','Herding','Terrier','Toy','Hound',
          'Terrier','Working','Working','Working','Non-Sporting','Non-Sporting','Hound','Non-Sporting',
          'Non-Sporting','Toy','Hound','Terrier','Terrier','Sporting','Working','Herding','Herding','Terrier',
          'Hound','Hound','Hound','Herding','Herding','Terrier','Herding','Herding','Herding','Herding','Herding',
          'Working','Non-Sporting','Hound','Working','Hound','Hound','Working','Herding','Terrier','Hound',
          'Non-Sporting','Herding','Working','Sporting','Herding','Sporting','Toy','Terrier','Terrier',
          'Non-Sporting','Working','Terrier','Working','Working','Herding','Toy','Terrier','Sporting',
          'Toy','Toy','Non-Sporting','Working','Non-Sporting','Hound','Sporting','Sporting','Herding',
          'Non-Sporting','Sporting','Hound','Non-Sporting','Terrier','Working','Working','Working','Sporting',
          'Hound','Sporting','Sporting','Toy','Herding','Sporting','Herding','Non-Sporting','Sporting',
          'Non-Sporting','Working','Herding','Sporting','Sporting','Working','Terrier','Sporting','Sporting',
          'Working','Working','Working','Hound','Hound','Toy','Hound','Herding','Sporting','Sporting','Terrier',
          'Sporting','Hound','Toy','Toy','Non-Sporting','Terrier','Working','Working','Sporting','Sporting',
          'Terrier','Working','Non-Sporting','Non-Sporting','Toy','Terrier','Working','Herding','Terrier','Toy',
          'Terrier','Working','Working','Terrier','Herding','Hound','Non-Sporting','Terrier','Sporting','Herding',
          'Hound','Toy','Terrier','Toy','Herding','Hound','Hound','Hound','Sporting','Herding','Toy',
          'Non-Sporting','Non-Sporting','Toy','Hound','Working','Toy','Herding','Herding','Terrier','Hound',
          'Hound','Working','Terrier','Working','Hound','Working','Non-Sporting','Hound','Terrier','Terrier',
          'Herding','Non-Sporting','Toy','Working','Toy','Terrier','Hound','Terrier','Terrier','Herding',
          'Sporting','Terrier','Working','Sporting','Herding','Working','Non-Sporting','Non-Sporting','Toy',
          'Hound','Sporting','Sporting','Sporting','Terrier','Terrier','Hound','Terrier','Sporting','Sporting',
          'Non-Sporting','Toy']

dog_groups = {d:g for d, g in zip(breeds,groups)}
dog_names = dog_groups.keys()
dog_type = dog_groups.values()

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

def cat_breed(s):
    s = s.lower()

    if 'mix' not in s:
        return 'Purebred'
    elif 'medium hair' in s:
        return 'Medium hair'
    elif 'longhair' in s:
        return 'Long hair'
    else:
        return 'Short hair'

def group_dogs(s):
    mix = 0

    if 'Mix' in s:
        mix = 1
        s = s[:-4]

    if s in dog_groups.keys():
        return dog_groups[s]

    else:
        pass