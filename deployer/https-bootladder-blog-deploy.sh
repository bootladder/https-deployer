#!/bin/bash
#from the gist
set -e

rm -rf _site

echo get the site
wget https://freejekyllbuilder.com/download/bootladder-blog -O bootladder-blog 2> /dev/null

echo unzip the site
unzip bootladder-blog > /dev/null
ls

echo delete existing deploymenet
rm -rf /opt/bootladder-blog/website/*

echo deploy
mv _site/* /opt/bootladder-blog/website/

echo cleanup
rm bootladder-blog
