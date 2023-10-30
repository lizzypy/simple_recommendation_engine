terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    encrypt        = true
    bucket         = "recommendation-engine-terraform-state"
    key            = "recommendation-engine-tf"
    dynamodb_table = "recommendation-engine-lock"
    region         = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}

module "aws_glue_job" {
  source = "./modules/aws-glue"

  s3_bucket_uri = "s3://${aws_s3_bucket.pydata_pipeline_bucket_final.bucket}"
}
