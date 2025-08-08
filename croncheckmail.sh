#!/bin/bash
cd /frame
source /frame/venv/bin/activate
PYTHONPATH=/frame/venv/lib/python3.11/site-packages
sudo -E /frame/venv/bin/python3 /frame/getmail.py
