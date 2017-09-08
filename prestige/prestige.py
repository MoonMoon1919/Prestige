#!/usr/bin/env python3.4

import boto3
import sys
import json
import zipfile
import os
from botocore.exceptions import ClientError
import config

img_types = config.IMG_TYPES

s3 = boto3.resource('s3')
client = boto3.client('s3')

def upload_files():
  bucket = 'mm-img-bucket-test'
  current_dir = os.curdir
  walker = os.walk(current_dir)
  length = len(current_dir)
  
  for root, folders, files in walker:
    for file_name in files:
      absolute_img_path = os.path.join(root, file_name)
      shortened_img_path = os.path.join(root[length:], file_name)
      if any(ext in shortened_img_path for ext in img_types):
        if shortened_img_path != 0:
          for images in shortened_img_path:
            try:
              upload = client.put_object(
                        ACL='private',
                        Body=open(absolute_img_path, 'rb').read(),
                        Bucket=bucket,
                        Key=shortened_img_path
                      )
              for obj in upload:
                print("Uploading file %s" % shortened_img_path)
            except ClientError:
              print "balls"

def get_urls():
  print("Getting urls")

upload_files()