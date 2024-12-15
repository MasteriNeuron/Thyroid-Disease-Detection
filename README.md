# Thyroid Disease Detection

Thyroid disease is a very common problem in India, more than one crore people are suffering with the disease every year. Thyroid disorder can speed up or slow down the metabolism of the body.

The main objective of this project is to predict if a person is having compensated hypothyroid, primary hypothyroid, secondary hypothyroid or negative (no thyroid) with the help of Machine Learning. Classification algorithms such as Random Forest, XGBoost and KNN Model have been trained on the thyroid dataset, UCI Machine Learning repository. 
After hyperparameter tuning XGBoost model has performed well with better accuracy, precision and recall. Application has deployed on Heroku with the help of flask framework.

# Webpage Link

## For One-User-Input Prediction
AWS: http://tddbulkprediction-env.eba-uqgwbduj.us-east-2.elasticbeanstalk.com/

# Demo
https://res.cloudinary.com/dqcvlj2il/video/upload/v1734270071/Screen_Recording_2024-12-15_190658_j6qxdo.mp4




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
The final model is deployed on AWS using Flask framework.

## User Interface
* UI Overview<br>
The user interface for the Thyroid Disease Detection system will consist of three main pages designed to facilitate bulk prediction and display results efficiently.

* Index Page <br>
The Index page serves as the entry point for the application. It will provide users with options to upload data for bulk prediction or access other functionalities, including navigation to the result page.

* Result Page<br>
The Result page will display the outcomes of the bulk prediction process. There will be two primary actions available on this page:
Download Result (Bulk): This button allows the user to download the full set of prediction results in CSV format.
View Predicted Results: This button provides users with the option to view the predicted results directly on the page.
Additionally, the predicted results will be displayed on this page, providing users with immediate insights into the predictions made by the system.



### Batch File Prediction User Interface
#### Homepage:
![Screenshot 2024-12-15 181722](https://github.com/user-attachments/assets/7540ab1f-f738-4e82-8633-c251af0561e6)
![Screenshot 2024-12-15 181735](https://github.com/user-attachments/assets/9ddab04d-059b-4ce4-8874-aa42720df8f1)

#### Prediction Page:
![Screenshot 2024-12-15 181854](https://github.com/user-attachments/assets/0049f4b5-423f-4229-851e-dcba2b8f0454)

#### Result Page
![Screenshot 2024-12-15 182042](https://github.com/user-attachments/assets/ee18b509-605e-45b3-8961-cec6bdabd5a2)




# Author

Shubham Chaudhary : https://www.linkedin.com/in/shubham-chaudhary-6352a5189/



