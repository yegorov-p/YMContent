#!/usr/bin/env bash

cd docs
make clean
make html
cd ..
python setup.py bdist_wheel
python3 setup.py bdist_wheel
twine upload dist/*
rm dist/*