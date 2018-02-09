#!/usr/bin/env bash

python3 setup.py bdist_wheel
twine upload dist/*