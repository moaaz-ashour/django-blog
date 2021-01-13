# conda install -c conda-forge boto3
# conda install -c conda-forge awscli

# configure AWS with awscli. 
# Go to your ROOT and in Terminal, type: aws configure
# Enter your configs:
"""
    AWS Access Key ID
    AWS Secret Access Key
    Default region name
    Default output format
"""

# Now, let's create a bucket:
import boto3
from decouple import config

aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("django-project-blog-2021") # Get from .env
# go to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
# Go to Bucket section
# Go to create() and copy the code under Request Syntax.
# In my case, I will choose the following:

response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    },
)

# python3 s3_bucket.py 