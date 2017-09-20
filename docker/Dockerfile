FROM tunein/python36builder:latest

##Python app
ARG prestige_token

##AWS
ARG access_key
ARG secret_key
ARG region

##App stuff
ARG build_token
ARG user
ARG repo
ARG enviro
ARG acl_type
ARG bucket_name

ENV acl=$acl_type
ENV bucket=bucket_name

RUN mkdir ~/.aws && touch ~/.aws/config && touch ~/.aws/credentials
RUN echo -en "[default]\nregion = $region" >> ~/.aws/config
RUN echo -en "[default]\naws_access_key_id = $access_key\naws_secret_access_key = $secret_key" >> ~/.aws/credentials

WORKDIR /home

##Get the application
RUN git clone https://$prestige_token:x-oauth-basic@github.com/MoonMoon1919/Prestige.git

##Install the app
WORKDIR Prestige
RUN pip3 install .

WORKDIR /home

######################Application Portion#################
RUN git clone https://$build_token:x-oauth-basic@github.com/$user/$repo.git

WORKDIR $repo/src/assets/img

ENTRYPOINT prestige --upload --bucket $bucket --acl $acl