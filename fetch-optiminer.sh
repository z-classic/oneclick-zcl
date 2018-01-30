#!/bin/bash

# Quick, Setup Python
sudo apt-get install wget python-qt4
pip install pyside

wget -v http://download.optiminer.pl/optiminer-equihash-2.1.2.tar.gz
tar xvzf optiminer-equihash-2.1.2

echo 'Optiminer Fetched.'
