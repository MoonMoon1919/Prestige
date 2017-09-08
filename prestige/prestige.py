#Get external libraries
import boto3
import sys
import json
import zipfile
import os
import datetime
from botocore.exceptions import ClientError

#Get internal libraries
import prestige.config as config
from prestige.cli import ARGS as args

img_types = config.IMG_TYPES

s3 = boto3.resource('s3')
client = boto3.client('s3')

def upload_files():
  bucket = args.bucket
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
            except ClientError as error:
              print(error.response)

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def check_upload():
  bucket = args.bucket
  current_dir = os.curdir
  walker = os.walk(current_dir)
  length = len(current_dir)

  to_upload = []

  for root, folders, files in walker:
    for file_name in files:
      if file_name != 0:
        shortened_img_path = os.path.join(root[length:], file_name)
        to_upload.append(shortened_img_path)

  current_objs = []

  try:
    current_objects = client.list_objects(
                        Bucket='mm-img-bucket-test'
                      )
    dump_response = json.dumps(current_objects, default=datetime_handler, indent=4)
    load_response = json.loads(dump_response)
    objects = load_response['Contents']

    for obj in objects:
      current_objs.append(obj['Key'])  
  except ClientError:
    print(error.response)

  for obj in to_upload:
   if obj in current_objs:
    print("Files uploaded to S3 successfully")
    return True
  else:
    return False

def get_urls():
  print("Getting urls")

def photo_optim():
  print("Im optimizing photos!")

def main():
  if args.upload:
    if args.optimize:
      photo_optim()
      upload_files()
      if check_upload():
        get_urls()
      else:
        print("Files not uploaded successfully")
    else:
      upload_files()
      if check_upload():
        get_urls()

if __name__ == "__main__":
  main()