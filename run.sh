#!/usr/bin/env bash

rm -rf qualitis.zip
zip -q -r qualitis.zip *
sudo -u hdfs spark-submit --master yarn --deploy-mode client --py-files qualitis.zip run.py