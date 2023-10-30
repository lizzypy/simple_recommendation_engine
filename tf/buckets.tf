resource "aws_s3_bucket" "pydata_pipeline_bucket_final" {
  bucket = var.pipelinebucket
  acl    = "private"
}

resource "aws_s3_object" "tempdir" {
  bucket = aws_s3_bucket.pydata_pipeline_bucket_final.id
  key    = "temporary/"
  acl    = "private"
}
