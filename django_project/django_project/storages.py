from storages.backends.s3boto3 import S3Boto3Storage

# An AWS Elemental MediaStore container is a namespace that holds folders and objects

class MediaStore(S3Boto3Storage):
    # location = 'media/profile_pics'
    # location is defined by image upload_to attribute in Profile. users > models.py
    file_overwrite = False