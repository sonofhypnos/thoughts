#!/bin/bash

#./convert_notebooks.sh # NOTE: not converting by default, because it's slow

/home/tassilo/.cache/pypoetry/virtualenvs/thoughts-nVi2q3I2-py3.10/bin/python generate_blog.py

git add .
git commit -m "Update blog"

git push
