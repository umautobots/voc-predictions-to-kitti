# VOC predictions to KITTI

Script to create [VOC](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/index.html) style predictions to
[KITTI](http://www.cvlibs.net/datasets/kitti/eval_object.php)
style, which is handy if you wish to run KITTI's
evaluation function ([e.g](https://github.com/umautobots/nn-dockerfiles/tree/master/kitti-evaluate)).

See [our instructions for reproducing training and evaluation for Driving in the Matrix](https://github.com/umautobots/driving-in-the-matrix) for our use case of this script.

It is assumed the network has been evaluated on KITTI in VOC format ([e.g](https://github.com/umautobots/nn-dockerfiles/tree/master/mxnet-rcnn))
so there should be 7481 images named like 000000.jpg.

## VOC

VOC predictions are stored line by line, *one file per detection class*

```
<image identifier> <confidence> <left> <top> <right> <bottom>
```

e.g

```
$ head -2 path/to/output/VOC2012/Main/comp4_det_trainval_car.txt
213222 0.501 851.6 207.0 1072.3 298.9
213222 0.124 238.5 187.9 419.2 274.8
```

## KITTI

KITTI predictions are stored line by line, *one file per image*, e.g

```
$ head -2 ~/test-kitti-container/my-kitti-labels/000000.txt
Car -1 -1 -10.000000 541.131 197.575 649.552 232.957 -1 -1 -1 -1 -1 -1 -1 0.903
Car -1 -1 -10.000000 299.747 215.436 422.328 248.200 -1 -1 -1 -1 -1 -1 -1 0.388
```

To run:

```
$ mkdir /path/to/output-labels
$ . doit.sh /path/to/voc-labels /path/to/output-labels
```

for example

```
$ mkdir /mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k/evaluate-on-kitti/kitti-labels
$ . doit.sh \
  /mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k/evaluate-on-kitti/VOC2012/Main \
  /mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k/evaluate-on-kitti/kitti-labels
```

