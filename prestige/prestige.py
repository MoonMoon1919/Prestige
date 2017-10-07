#Get external libraries
import boto3
import sys
import json
import zipfile
import os
import datetime
import pathlib
from PIL import Image
from botocore.exceptions import ClientError

#Get internal libraries
import prestige.config as config
from prestige.cli import ARGS as args

img_types = config.IMG_TYPES
ACCEPTED_ACLS = config.ACCEPTED_ACLS

s3 = boto3.resource('s3')
client = boto3.client('s3')
my_session = boto3.session.Session()
region = my_session.region_name

def optimize():
  ranger = range(1,100)
  if args.optimize in ranger:

    current_dir = os.curdir
    walker = os.walk(current_dir)
    length = len(current_dir)
    
    for root, folders, files in walker:
      for file_name in files:
        absolute_img_path = os.path.join(root, file_name)
        shortened_img_path = os.path.join(root[length:], file_name) 
        if any(ext in shortened_img_path.lower() for ext in img_types):
          if shortened_img_path != 0:
            f, e = os.path.splitext(absolute_img_path)
            outfile = f + "_optimized.jpg"

            try:
              print("Attempting to optimize '%s'" % shortened_img_path)
              img = Image.open(absolute_img_path)
              img.save(outfile,optimize=True,quality=args.optimize)
              
              print("Comparing file sizes")
              old_img = os.path.getsize(absolute_img_path)
              nu_img = os.path.getsize(outfile)
              
              if old_img >= nu_img:
                try:
                  os.remove(absolute_img_path)
                  print("Optimized image is smaller, removing old image")
                except IOError:
                  print("Could not delete file")
              else:
                try:
                  os.remove(outfile)
                  print("Original image is smaller, removing optimized image")
                except IOError:
                  print("Couldn't open file")
              
            except IOError as e:
              print(e)
            
  else:
    print("Please use a number between 1 and 100")

def upload_files():
  bucket = args.bucket
  current_dir = os.curdir
  walker = os.walk(current_dir)
  length = len(current_dir)

  if args.acl in ACCEPTED_ACLS:
  
    for root, folders, files in walker:
      for file_name in files:
        absolute_img_path = os.path.join(root, file_name)
        shortened_img_path = os.path.join(root[length:], file_name)
        no_slash_path = str(shortened_img_path.strip("/"))
        if any(ext in shortened_img_path.lower() for ext in img_types):
          if shortened_img_path != 0:
            try:
              upload = client.put_object(
                        ACL=args.acl,
                        Body=open(absolute_img_path, 'rb').read(),
                        Bucket=bucket,
                        Key=no_slash_path
                      )
              print("Uploading file %s" % no_slash_path)
            except ClientError as error:
              print(error.response)
  else:
    print("please use one of the following: 'private', 'public-read', 'public-read-write', 'authenticated-read', 'aws-exec-read', 'bucket-owner-read', 'bucket-owner-full-control'")

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
        to_upload.append(shortened_img_path.strip("/"))

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
  except ClientError as error:
    print(error.response['Error']['Message'])

  for obj in to_upload:
   if obj in current_objs:
    print("Files uploaded to S3 successfully")
    return True
  else:
    return False

def get_urls():  
  print('Getting urls')
  print('\n')
  bucket = args.bucket
  current_dir = os.curdir
  walker = os.walk(current_dir)
  length = len(current_dir)

  images = []

  for root, folders, files in walker:
    for file_name in files:
      if file_name != 0:
        shortened_img_path = os.path.join(root[length:], file_name)
        images.append(shortened_img_path)
        
  for item in images:
    no_slash = item.strip("/")
    print("'%s' url: https://s3-%s.amazonaws.com/%s/%s" % (item, region, bucket, no_slash.replace(" ", "+")))

def main():
  if args.upload:
    if args.optimize:
      optimize()
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