import csv
import glob

from collections import defaultdict

CONVERT_LABEL = {
    'car': 'Car',
    'person': 'Pedestrian',
    'bicycle': 'Cyclist',
}


def main():
    paths = glob.glob("/input/VOC/*.txt")

    by_image_id = defaultdict(list)

    for path in paths:
        # e.g '/input/VOC/comp4_det_trainval_cat.txt'
        det_class = path.split("_")[-1].split('.')[0]
        print(det_class)
        with open(path) as f:
            f_csv = csv.reader(f, delimiter=' ')
            for voc_row in f_csv:
                image_id, confidence, x1, y1, x2, y2 = voc_row
                by_image_id[image_id].append(voc_row + [det_class])

    in_order = sorted(by_image_id.keys())

    for index, image_id in enumerate(in_order):
        kitti_name = f"{image_id}.txt"
        with open(f"/output/KITTI/{kitti_name}", 'w') as out_f:
            out_f_csv = csv.writer(out_f, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            for voc_row in by_image_id[image_id]:
                image_id, confidence, x1, y1, x2, y2, label = voc_row
                # notice we subtract 1 from each coordinate
                # to get from 1-based pixel coordinates of VOC to 0 based of KITTI
                out_f_csv.writerow([CONVERT_LABEL.get(label, label), -1, -1, -1] +
                                   [f"{float(coord) - 1:.2f}" for coord in [x1, y1, x2, y2]] +
                                   [-1, -1, -1, -1, -1, -1, -1, f"{float(confidence):.3f}"])


if __name__ == '__main__':
    main()
