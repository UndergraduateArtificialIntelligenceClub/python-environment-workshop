#!/bin/sh

conda create -n envWorkshop
conda activate envWorkshop

pip install numpy matplotlib pandas

pip freeze > req.txt