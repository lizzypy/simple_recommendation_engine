#!/bin/bash

# Define your bucket and file name
BUCKET_NAME="pydatapipelinebucket-final"
FILE_NAME="analysis/prepare.py"
MODULE="analysis/utils/dist/pydata_engine_utils-0.1.0-py3-none-any.whl"

# Upload the file
aws s3 cp $FILE_NAME s3://$BUCKET_NAME/
aws s3 cp $MODULE s3://$BUCKET_NAME/
