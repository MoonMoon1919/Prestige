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

def get_files():
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
              upload = s3.Bucket(bucket).upload_file(absolute_img_path, shortened_img_path)
            except ClientError:
              print "balls"

get_files()