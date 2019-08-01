#!/bin/bash

rm -rf _site

echo get the site
wget freejekyllbuilder.com/download/ccram

echo unzip the site
unzip ccram
ls

echo delete existing deploymenet
rm -rf /opt/ccram/website/*
echo deploy
mv _site/* /opt/ccram/website/
echo cleanup
rm ccram

