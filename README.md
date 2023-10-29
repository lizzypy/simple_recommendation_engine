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