resource "aws_s3_bucket" "pydata_pipeline_bucket" {
  bucket = var.pipelinebucket
  acl    = "private"
}

resource "aws_s3_object" "tempdir" {
  bucket = aws_s3_bucket.pydata_pipeline_bucket.id
  key    = "temporary/"
  acl    = "private"
}
