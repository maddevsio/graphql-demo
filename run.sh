#!/bin/bash
MYPWD=${PWD} 
source $MYPWD/venv/bin/activate
export FLASK_APP=demoapp.py
export FLASK_DEBUG=1
python -m flask run

