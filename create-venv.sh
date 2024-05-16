#!/bin/bash

pyenv install 3.6
pyenv virtualenv-delete -f mvnfeed
pyenv virtualenv 3.6 mvnfeed
pyenv activate  mvnfeed
pip install --upgrade pip
pip3 install setuptools
