import pickle
import numpy as np
import random

catboost = pickle.load(open('../cat_boost_reduce.pkl', 'rb'))

name_freqs = pickle.load(open('../name_freqs.pkl', 'rb'))

example = {
    'age': 0,
    'animal_type': 'cat',
    'fixed': 'intact',
    'group': 'short hair',
    'intake_condition': 'Normal',
    'season': 'Spring',
    'intake_type': 'Owner Surrender',
    'hour': '11',
    'name': 'Rio'
}

def predict_animal(features):
    print(features)
    # How often name appears in dataset
    name_frequency = name_freqs[features['name']]

    X = np.array([features['age'], features['animal_type'], features['fixed'], features['group'], features['intake_condition'],
                features['season'], features['intake_type'], features['hour'], name_frequency]).reshape(1, -1)

    prob_adoption = catboost.predict_proba(X)[0, 1]

    best_names = []
    highest_prob = prob_adoption

    for n in name_freqs.keys():
        new_name_freq = name_freqs[n]
        new_X = np.array([features['age'], features['animal_type'], features['fixed'], features['group'], features['intake_condition'],
                features['season'], features['intake_type'], features['hour'], new_name_freq]).reshape(1, -1)
        new_prob = catboost.predict_proba(new_X)[0, 1]
        if new_prob > highest_prob:
            best_names = [n]
            highest_prob = new_prob
        elif new_prob == highest_prob:
            best_names.append(n)
            highest_prob = new_prob

    suggested_name = random.choice(best_names)
    difference = highest_prob - prob_adoption

    result = {'prediction': int(prob_adoption > 0.5),
              'prob_adoption': prob_adoption,
              'suggested_name': suggested_name,
              'suggested_probability': highest_prob,
              'difference': difference
    }

    return result

if __name__ == '__main__':
    print(predict_animal(example))