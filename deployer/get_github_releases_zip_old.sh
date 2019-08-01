#!/bin/bash
#from the gist

rm -rf _site

echo get the site
curl -s https://api.github.com/repos/bootladder/blog/releases/latest | grep browser_download_url

curl -s https://api.github.com/repos/bootladder/blog/releases/latest \
| grep "browser_download_url" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -


echo unzip the site
unzip _site.zip
echo delete existing deploymenet
rm -rf /opt/bootladder-blog/website/*
echo deploy
mv _site/* /opt/bootladder-blog/website/
echo cleanup
rm _site.zip
