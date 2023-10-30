## Simple Recommendation Engine

This repository contains a simple movie recommendation engine. 
The development of this engine is used in articles and talks to demonstrate how 
test driven development and CI/CD can be applied to data analytics and ml models.

To use the notebooks/scripts in this repository you should create a virtual environment with python 3.9 
(this is the latest python version that AWS Glue Supports)

To manage python environments I recommend pyenv (it's forked from rbenv):
- You can get started with pyenv here: https://github.com/pyenv/pyenv#getting-pyenv

Once you have pyenv installed you can follow these steps. From the root of the project run:

1. pyenv install 3.9.15
2. pyenv local 3.9.15
3. pip3 install -r analysis/requirements.txt

### Analysis

You should now be able to run the following command:

`cd analysis/notebooks && jupyter lab`

This should open the jupyter notebooks in the notebooks directory.  You should be able to run the 
`Movie Data Analysis.ipynb` from start to finish without errors.

### Tests

Navigating to run tests from the root you can run the following:

`cd analysis && pytest`

To run a single test from root:

`cd analysis && pytest utils/tests/test_cleaning.py`


### Terraform

To build the resources needed to run the glue job in aws you should move into the tf directory then run:

1. `terraform init`
2. `terraform plan`
3. `terraform apply`

#### Notes:

- The terraform holds its state remotely. You should create an aws bucket in your aws account named `recommendation-engine-terraform-state`
- You should create a dynamo-db table named `recommendation-engine-lock`
  - That table MUST have an id of LockID
- You will need to change the name of your S3 bucket. S3 bucket names must be globally unique
- You need to manually add the `all_movies.csv` from analysis/notebooks/input/all_movies.csv to your S3 bucket once it's created
- You will need to run the ./upload_prepare.sh script manually if you don't let github run the step for you before using the script in AWS