# kojak

This is the repository for a project that predicts shelter animal outcomes. 

## Notebooks

animal-eda.ipynb - initial EDA of data
clean-engineer.ipynb - Cleaning and feature engineering
MVP.ipynb - MVP of multiclass model
Model.ipynb -- Random Forest and XGBoost versions of model
Categoricals.ipynb -- Create dummy-variable and non-dummy-variable versions of data
Catboost.ipynb -- Catboost modeling (using non-dummy-variable version of data)
feature-playground.ipynb -- Experiment with adding and removing features to lessen Catboost model complexity
name-frequency.ipynb -- Create name frequency Counter object that maps each name in dataset to frequency of that name
re-clean.ipynb -- Re-clean all data to ensure mistake wasn't made in cleaning

## Files

breeds.py -- Uses Wikipedia module to write breed group data to .txt file
parse_breeds.py -- Reads file from breeds.py to create a dictionary mapping specific dog breeds to dog groups
animalhelper.py -- helper file that includes cleaning, engineering, and breed/color parsing functions

## Flask
api.py -- Takes user inputs and runs them through the model to get hard and soft predictions. Varies the name over all names in dataset and returns the name that increases probability of adoption the most.
animal_app.py -- Flask app program. Implements a predict function that calls api.py to return prediction values via a POST request.  
