#!/bin/sh

conda create -n envWorkshop
conda activate envWorkshop

pip install flask

pip freeze > req.txt
cat req.txt

# download from website
pip install -r workshop.txt