#!/usr/bin/env bash

docker run -it --rm --name run-voc-predictions-to-kitti \
  -v `pwd`:/usr/src/myapp:ro \
  -v $1:/input/VOC:ro \
  -v $2:/output/KITTI \
  -w /usr/src/myapp \
  python:3.6 python doit.py
