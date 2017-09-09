# Prestige

Copyright M.Moon/Perilune Inc 2017<br>
<br>
Prestige is a CLI tool for uploading images to AWS Simple Storage Service (S3).<br>
It has a built in optimize function that allows you to optimize your photos for web (expressed as a percentage from 1 to 100)<br>
if you have a lot of images to upload, simply run "prestige --upload --bucket $your-bucket-name" while in the directory where you images are.<br>
<br>
To install, clone the repo and run:<br>
pip install .<br>
<br>
Commands:<br>
prestige --upload(required) --bucket(required) $your-bucket-name --optimize(optional) $integer<br>
<br>
For example:<br>
prestige --upload --bucket max-test-bucket --optimize 85 <i>this optimizes my photos to 85% quality then uploads to the bucket 'max-test-bucket'</i><br>
prestige --upload --bucket max-test-bucket <i>this uploads all photos in my current directory to the bucket 'max-test-bucket'</i><br>
<br>
<b>NOTE: USING '--optimize- REMOVES FILES AUTOMATICALLY!!!!!<br>
IF YOU VALUE YOUR ORIGINAL 100% QUALITY PHOTOS, COPY THE ONES YOU WANT TO UPLOAD & OPTIMIZE TO A DIFFERENT DIRECTORY</b><br>
<br>
Current accepted formats:<br>
-jpg/jpeg
-png