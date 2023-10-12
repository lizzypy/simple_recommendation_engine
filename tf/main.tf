terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "pydata_pipeline_bucket" {
  bucket = "pydatapipelinebucket"
  acl    = "private"
}

resource "aws_s3_object" "movie_input_data" {
  bucket = aws_s3_bucket.pydata_pipeline_bucket.id
  key = "all_movies.csv"
  source = "../analysis/input/all_movies.csv"
  acl    = "private"
}

resource "aws_s3_object" "prepare_script" {
  bucket = aws_s3_bucket.pydata_pipeline_bucket.id
  key = "prepare.py"
  source = "../prepare.py"
  acl    = "private"
}

resource "aws_s3_object" "tempdir" {
  bucket = aws_s3_bucket.pydata_pipeline_bucket.id
  key    = "temporary/"
  acl    = "private"
}

module "aws_glue_job" {
  source = "./aws-glue"

  s3_bucket_uri = "s3://${aws_s3_bucket.pydata_pipeline_bucket.bucket}"
}
