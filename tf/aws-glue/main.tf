resource "aws_iam_policy" "glue_s3_full_access" {
  name        = "glue-s3-full-access"
  description = "IAM policy for full access to S3"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "s3:*",
        Effect = "Allow",
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role" "glue_role" {
  name = "glue-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "glue.amazonaws.com"
        }
      }
    ]
  })

  inline_policy {
    name        = "s3-full-access"
    policy      = aws_iam_policy.glue_s3_full_access.policy
  }
}

resource "aws_glue_job" "preparematrix" {
  name         = "preparematrix-job"
  description  = "Prepare Matrix AWS Glue Job"
  role_arn     = aws_iam_role.glue_role.arn
  max_capacity = "1.0"
  execution_property {
    max_concurrent_runs = 1
  }

  command {
    name    = "pythonshell"
    script_location = "${var.s3_bucket_uri}/prepare.py"
    python_version = "3.9"
  }

  default_arguments = {
    "--job-language" = "python"
    "--TempDir" = "${var.s3_bucket_uri}/temporary"
    "library-set" = "analytics"
  }

  glue_version = "1.0"
}
