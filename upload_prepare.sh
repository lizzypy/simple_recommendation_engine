#!/bin/bash

# Define your bucket and file name
BUCKET_NAME="pydatapipelinebucket-final"
FILE_NAME="analysis/prepare.py"

# Upload the file
aws s3 cp $FILE_NAME s3://$BUCKET_NAME/
