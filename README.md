# Thyroid Disease Detection

Thyroid disease is a very common problem in India, more than one crore people are suffering with the disease every year. Thyroid disorder can speed up or slow down the metabolism of the body.

The main objective of this project is to predict if a person is having compensated hypothyroid, primary hypothyroid, secondary hypothyroid or negative (no thyroid) with the help of Machine Learning. Classification algorithms such as Random Forest, XGBoost and KNN Model have been trained on the thyroid dataset, UCI Machine Learning repository. 
After hyperparameter tuning XGBoost model has performed well with better accuracy, precision and recall. Application has deployed on Heroku with the help of flask framework.

# Webpage Link

## For One-User-Input Prediction
AWS: http://tddbulkprediction-env.eba-uqgwbduj.us-east-2.elasticbeanstalk.com/

# Demo

[https://user-images.githubusercontent.com/72372136/134773017-d9d26150-0e68-4c2d-8627-b3a64beeac9b.mp4](https://res.cloudinary.com/dqcvlj2il/video/upload/v1734270071/Screen_Recording_2024-12-15_190658_j6qxdo.mp4)




# Technical Aspects

- Python 3.7 and more
- Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
- Front-end: HTML, CSS 
- Back-end: Flask framework
- IDE: Jupyter Notebook, Pycharm & VSCode
- Database: Cassandra 
- Deployment: Heroku, AWS

# How to run this app 

Code is written in Python 3.7 and more. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.

- Create virtual environment - conda create -n myenv python=3.7
- Activate the environment - conda activate myenv
- Install the packages - pip install -r requirements.txt
- Run the app - python run app.py

# Workflow

## Data Collection

Thyroid Disease Data Set from UCI Machine Learning Repository.

Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease

## Data Pre-processing

- Missing values handling by Simple imputation (KNN Imputer)
- Outliers detection and removal by boxplot and percentile methods
- Categorical features handling by ordinal encoding and label encoding
- Feature scaling done by Standard Scalar method
- Imbalanced dataset handled by SMOTE
- Drop unnecessary columns

## Model Creation and Evaluation

- Various classification algorithms like Random Forest, XGBoost, KNN etc tested.
- Random Forest, XGBoost and KNN were all performed well. XGBoost was chosen for the final model training and testing.
- Hyper parameter tuning was performed using RandomizedSearchCV
- Model performance evaluated based on accuracy, confusion matrix, classification report.


## Database Connection
Cassandra database used for this project.

## Model Deployment
The final model is deployed on Heroku using Flask framework.

## User Interface
### Single User Input Prediction User Interface

### Batch File Prediction User Interface
#### Homepage: A very simple UI with single page. 



# Author

Shubham Chaudhary : https://www.linkedin.com/in/shubham-chaudhary-6352a5189/



