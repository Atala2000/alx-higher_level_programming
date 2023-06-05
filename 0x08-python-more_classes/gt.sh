#!/usr/bin/bash
echo What is the comment
read Comment
git add .
git commit -m "$Comment"
git push
