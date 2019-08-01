#!/bin/bash
#from the gist

rm -rf _site

echo get the site
curl -s https://api.github.com/repos/ccram-website/ccram-website/releases/latest | grep browser_download_url

curl -s https://api.github.com/repos/ccram-website/ccram-website/releases/latest \
| grep "browser_download_url" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -


echo unzip the site
unzip _site.zip
echo delete existing deploymenet
rm -rf /opt/ccram/website/*
echo deploy
mv _site/* /opt/ccram/website/
echo cleanup
rm _site.zip
