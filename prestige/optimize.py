#!/usr/bin/env python3.4

#Get external libraries
import boto3
import sys
import json
import zipfile
import os
import datetime
from PIL import Image
from botocore.exceptions import ClientError

img_types = ['.jpg', '.jpeg', '.png']

def optimize():
  current_dir = os.curdir
  walker = os.walk(current_dir)
  length = len(current_dir)

  for root, folders, files in walker:
    for file_name in files:
      absolute_img_path = os.path.join(root, file_name)
      shortened_img_path = os.path.join(root[length:], file_name)
      if any(ext in shortened_img_path.lower() for ext in img_types):
        if shortened_img_path != 0:
          f, e = os.path.splitext(shortened_img_path)
          outfile = f + "_optimized.jpg"
          try:
            print("Attempting to optimize %s" % shortened_img_path)
            img = Image.open(shortened_img_path)
            img.save(outfile,optimize=True,quality=85)

            print("Comparing file sizes")
            old_img = os.path.getsize(shortened_img_path)
            nu_img = os.path.getsize(outfile)
            if old_img >= nu_img:
              try:
                os.remove(shortened_img_path)
                print("Optimized image is smaller, removing old image")
              except IOError:
                print("Could not delete file")
            else:
              try:
                os.remove(outfile)
                print("Original image is smaller, removing optimized image")
              except IOError:
                print("Couldn't open file")
          except IOError:
            print("IOError")
