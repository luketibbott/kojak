import pickle
import numpy as np

catboost = pickle.load(open('../cat_boost_reduce.pkl', 'rb'))

name_freqs = pickle.load(open('../name_freqs.pkl', 'rb'))


example = {
    'age': 1700,
    'animal_type': 'cat',
    'fixed': 'intact',
    'group': 'long hair',
    'intake_condition': 'sick',
    'season': 'winter',
    'intake_type': 'surrender by owner',
    'hour_in': 11,
    'name': 'bella'
}

def predict_animal(features):

    # How often name appears in dataset
    name_frequency = name_freqs[example['name']]

    X = np.array([features['age'], features['animal_type'], features['fixed'], features['group'], features['intake_condition'],
                features['season'], features['intake_type'], features['hour_in'], name_frequency]).reshape(1, -1)

    prob_adoption = catboost.predict_proba(X)[0, 1]

    result = {'prediction': int(prob_adoption > 0.5),
              'prob_adoption': prob_adoption
    }

    return result

if __name__ == '__main__':
    print(predict_animal(example))