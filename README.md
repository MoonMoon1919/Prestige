# Prestige

Copyright M.Moon/Perilune Inc 2017<br>
<br>
Prestige is a CLI tool for uploading images to AWS Simple Storage Service (S3).<br>
It has a built in optimize function that allows you to optimize your photos for web (expressed as a percentage from 1 to 100)<br>
if you have a lot of images to upload, simply run "prestige --upload --bucket $your-bucket-name --acl $(see list)" while in the directory where you images are.<br>
<br>
To install, clone the repo and run:<br>
pip install .<br>
<br>
Commands:<br>
prestige --upload(required) --bucket(required) $your-bucket-name --acl $acl_of_choice --optimize(optional) $integer<br>
<br>
For example:<br>
prestige --upload --bucket max-test-bucket --acl private --optimize 85<br>
<i>this optimizes my photos to 85% quality then uploads to the bucket 'max-test-bucket' with a 'private' acl</i><br>
<br>
prestige --upload --bucket max-test-bucket --acl public-read<br>
<i>this uploads all photos in my current directory to the bucket 'max-test-bucket' with the 'public-read' acl</i><br>
<br>
<b>NOTE: USING '--optimize- REMOVES FILES AUTOMATICALLY!!!!!<br>
IF YOU VALUE YOUR ORIGINAL 100% QUALITY PHOTOS, COPY THE ONES YOU WANT TO UPLOAD & OPTIMIZE TO A DIFFERENT DIRECTORY</b><br>
<br>
After prestige runs it will return a list of URLs where you images can be found in S3<br>
<br>
Current accepted formats:<br>
-jpg/jpeg<br>
-png<br>
<br>
Current accepted ACLs:<br>
-private<br>
-public-read<br>
-public-read-write<br>
-authenticated-read<br>
-aws-exec-read<br>
-bucket-owner-read<br>
-bucket-owner-full-control<br>
<br>
<b>Roadmap</b><br>
-Add Cloudfront integration<br>
