import os
import shutil


def find_boat_in_coco():
    label_path = "data/coco/labels/train2014/"
    image_path = "data/coco/images/train2014/"
    dst_image_path = "data/custom/images/"
    dst_label_path = "data/custom/labels/"
    sample_path = "data/samples/"

    label_files = os.listdir(label_path)
    for f in label_files:
        with open(label_path + f, "r") as label:
            for line in label.readlines():
                l = line.split()
                if l[0] == "8":
                    boat_image = image_path + f.replace(".txt", ".jpg")
                    shutil.copy2(boat_image, dst_image_path + f.replace(".txt", ".jpg"))
                    shutil.copy2(boat_image, sample_path + f.replace(".txt", ".jpg"))
                    with open(dst_label_path + f, "w") as ff:
                        ff.write(line)
                    print(boat_image + " saved.")


if __name__ == "__main__":
    find_boat_in_coco()
