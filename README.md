# Prestige

![](http://images.amcnetworks.com/ifc.com/wp-content/uploads/2012/09/tumblr_m9zkssGhlV1rnw1mso2_500.gif)  

Copyright M.Moon/Perilune Inc 2017  

---

## About

- CLI tool for uploading images to AWS Simple Storage Service (S3)  
- Built in optimize function that allows you to optimize your photos for web (expressed as a percentage from 1 to 100)  
- Simply run "prestige --upload --bucket $your-bucket-name --acl $(see list)" while in the directory where you images are  

---

##  Installing  

- clone the repo and run  
- pip install -r requirements.txt  
- pip install .  


---

## Commands  

- --upload (required)
- --bucket (required) (must include bucket name)
- --acl (required) (include ACL of choice from list)
- --optimize (optional) (optimizes images using Pillow) (must include integer for % of previous quality)

---

## Examples

- prestige --upload(required) --bucket(required) $your-bucket-name --acl(required) $acl_of_choice --optimize(optional) $integer 
- prestige --upload --bucket max-test-bucket --acl private --optimize 85  
- prestige --upload --bucket max-test-bucket --acl public-read  


NOTE: USING '--optimize- REMOVES FILES AUTOMATICALLY!!!!!  
IF YOU VALUE YOUR ORIGINAL 100% QUALITY PHOTOS, COPY THE ONES YOU WANT TO UPLOAD & OPTIMIZE TO A DIFFERENT DIRECTORY  


After prestige runs it will return a list of URLs where you images can be found in S3

---

## Dockerfile how to:

If you have the AWS CLI tool installed, run this command, if not, place your access and secret keys where the configure commands are

- docker run --rm -e AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id) \
	-e AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key) \
	-e AWS_DEFAULT_REGION=$YOURREGION -v `pwd`:/app moonmoon1919/prestige:0.1 \
	--upload --bucket mm-img-bucket-test --acl private --optimize 85  

Using Docker allows you to put Prestige in a CICD pipeline and not have to worry about dependency management on a build agent.  

---  
  
## Current accepted formats   
- jpg/jpeg  
- png  
  
## Current accepted ACLs  
- private  
- public-read  
- public-read-write  
- authenticated-read  
- aws-exec-read  
- bucket-owner-read  
- bucket-owner-full-control  

---

## Roadmap

-Add Cloudfront integration  