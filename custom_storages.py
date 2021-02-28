from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    To store static files in a location from the settings.py
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    To store media files in a location from the settings.py
    """
    location = settings.MEDIAFILES_LOCATION
