#!/bin/bash

export ENVIRONMENT=LOCAL_TESTING
cd src/python_project
python3.9 -m pytest . --cov=.