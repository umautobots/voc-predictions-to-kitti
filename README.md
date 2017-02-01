# VOC predictions to KITTI

Script to create voc style predictions to kitti style.

## VOC

VOC predictions are stored line by line, *one file per detection class*

<image identifier> <confidence> <left> <top> <right> <bottom>

e.g

$ head -2 path/to/output/VOC2012/Main/comp4_det_trainval_car.txt
213222 0.501 851.6 207.0 1072.3 298.9
213222 0.124 238.5 187.9 419.2 274.8

## KITTI

KITTI predictions are stored line by line, *one file per image, e.g

$ head -2 ~/test-kitti-container/my-kitti-labels/000000.txt
Car -1 -1 -10.000000 541.131 197.575 649.552 232.957 -1 -1 -1 -1 -1 -1 -1 0.903
Car -1 -1 -10.000000 299.747 215.436 422.328 248.200 -1 -1 -1 -1 -1 -1 -1 0.388

Furthermore, KITTI expects the files to be named in a %6d.txt, so any filenames from VOC need to be mapped to this style.

VOC

mkdir /mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k-yas/evaluate-on-kitti/kitti-labels


/mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k-yas/evaluate-on-kitti/VOC2012/Main/comp4_det_trainval_car.txt


To run:

```
$ mkdir /path/to/output-labels
$ . doit.sh /path/to/voc-labels /path/to/output-labels
```

for example

```
$ mkdir /mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k-yas/evaluate-on-kitti/kitti-labels
$ . doit.sh \
  /mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k-yas/evaluate-on-kitti/VOC2012/Main \
  /mnt/ngv/training-runs/2017-01-30-mxnet-rcnn-gta25k-yas/evaluate-on-kitti/kitti-labels
```

