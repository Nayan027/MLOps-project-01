# MLOps-project-01: Vehicle Insurance Data Pipeline

Welcome! This project is a hands-on demonstration of how to build and deploy a machine learning pipeline for vehicle insurance data. It covers everything from data processing to model deployment and CI/CD automation.

This is an End to end Project implementing Machine Learning Operations to develop a production grade project.

---

## 📁 Project Setup and Structure

### Step 1: Project Template
- Start by executing the `template.py` file to create the initial project template, which includes the required folder structure and placeholder files.

### Step 2: Package Management
- Write the setup code for importing local packages in `setup.py` and `pyproject.toml` files.

### Step 3: Virtual Environment and Dependencies
- Create a virtual environment, activate it and install required dependencies from `requirements.txt`:
  
  creation:        conda create -n vehicle python=3.10 -y
  activation:      conda activate vehicle
  install req.:    pip install -r requirements.txt
  
- Verify the local packages by running:
  
  verify:          pip list

---

## 📊 MongoDB Setup and Data Management

### Step 4: MongoDB Atlas Configuration
1. Sign up for [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create a new project.
2. Set up a free M0 cluster (512MB), configure the username and password, and allow access from 
   any IP address (`0.0.0.0/0`).
3. Retrieve the MongoDB connection string for Python and save it (replace `<password>` with your password).

### Step 5: Pushing Data to MongoDB
1. Create a folder named `notebook`, add the dataset, and create a notebook file `mongoDB_demo.ipynb`.
2. Use the notebook to push data to the MongoDB database.
3. Verify the data in MongoDB Atlas under Database > Browse Collections (named Proj1, Proj1-Data).

---

## 📝 Logging, Exception Handling, and EDA

### Step 6: Set Up Logging and Exception Handling
- Create logging and exception handling modules. Test them on a demo file named `demo.py`, where we test different steps 
  as we move forward with our project.

### Step 7: Exploratory Data Analysis (EDA) and Feature Engineering
- Analyze and engineer features in the `EDA` and `Feature Engg` notebook for further processing in the pipeline.
- This is where we understand the nature of our dataset i.e. Feature's Properties > Useful Transformation Techniques and
  Best Algorithm for Model Building.

---

## 📥 Data Ingestion

### Step 8: Data Ingestion Pipeline
- Define MongoDB connection functions in `configuration.mongo_db_connections.py`.
- Develop data ingestion components in the `data_access` and `components.data_ingestion.py` files to fetch 
  and transform  data.
- Update `entity/config_entity.py` and `entity/artifact_entity.py` with relevant ingestion configurations.
- Run `demo.py` after setting up MongoDB connection as an environment variable.

### Setting Environment Variables
- Set MongoDB URL:

  # For Conda-env:
  setting environment variable : set MONGODB_URL = "mongodb+srv://<username>:<password>......" 
  checking if it's set or not  : echo %MONGODB_URL%

- This saves the url as env. var. temporarily i.e. until the terminal is running (to set permanently use "setx")


  # For PowerShell:
  setting environment variable : $env:MONGODB_URL = "mongodb+srv://<username>:<password>......"
  checking if it's set or not  : echo $env:MONGODB_URL

- **Note**: On Windows, you can also set environment variables through the system settings i.e. Manually.

---

## 🔍 Data Validation, Transformation & Model Training

### Step 9: Data Validation
- Define schema in `config.schema.yaml` and implement data validation functions in `utils.main_utils.py`.

### Step 10: Data Transformation
- Implement data transformation logic in `components.data_transformation.py` and create `estimator.py` in the `entity` folder.

### Step 11: Model Training
- Define and implement model training steps in `components.model_trainer.py` using code from `estimator.py`.

---

## 🌐 AWS Setup for Model Evaluation & Deployment

### Step 12: AWS Setup
1. Log in to the AWS console, create an IAM user, and grant `AdministratorAccess`.
2. Set AWS credentials as environment variables.
   
  # For Conda-env
   setx AWS_ACCESS_KEY_ID "YOUR_AWS_ACCESS_KEY_ID"
   setx AWS_SECRET_ACCESS_KEY "YOUR_AWS_SECRET_ACCESS_KEY"
   

3. Configure S3 Bucket and add access keys in `constants.__init__.py`.

### Step 13: Model Evaluation and Pushing to S3
- Create an S3 bucket named `my-model-mlopsproj` in the `us-east-1` region.
- Develop code to push/pull models to/from the S3 bucket in `src.aws_storage` and `entity/s3_estimator.py`.

---

## 🚀 Model Evaluation, Model Pusher, and Prediction Pipeline

### Step 14: Model Evaluation & Model Pusher
- Implement model evaluation and deployment components.






















---

This README provides a structured walkthrough of the MLOps project, showcasing the end-to-end pipeline, cloud integration, CI/CD setup, and robust data handling capabilities.
