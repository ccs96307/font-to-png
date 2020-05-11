#!/bin/bash
# This script will clean your "fonts" folder!


# Make a new directory
if [ -d "./fonts" ];
then
    echo fonts folder exists.
else
    mkdir fonts
    echo Makes the fonts folder.
fi


# Download a free english font file
cd fonts
wget https://www.1001freefonts.com/d/26673/atozimple.zip
unzip atozimple.zip
shopt -s extglob
rm -fr !(Atozimple\ Bold.otf)
echo Download Finished.
