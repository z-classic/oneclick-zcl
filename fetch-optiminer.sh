#!/bin/bash


# Quick, Setup Python
sudo apt-get install cmake wget python-qt4 libqt4-dev
pip2.7 install setuptools pyside

# Fetch fresh
rm -rf optiminer-equihash-2.1.2.tar.gz

wget -v http://download.optiminer.pl/optiminer-equihash-2.1.2.tar.gz
tar xvzf optiminer-equihash-2.1.2.tar.gz

echo 'Optiminer Fetched.'
