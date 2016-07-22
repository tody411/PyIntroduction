# -*- coding: utf-8 -*-
## @package pil_exif
#
#  pil_exif utility package.
#  @author      Tody
#  @date        2016/07/22


from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

## Exifデータの取得．
def getExif(file_path):
    image = Image.open(file_path)

    exif = image._getexif()

    if exif is None:
        return

    exif_data = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)

        # GPS情報は個別に扱う．
        if tag == "GPSInfo":
            gps_data = {}
            for t in value:
                gps_tag = GPSTAGS.get(t, t)
                gps_data[gps_tag] = value[t]

            exif_data[tag] = gps_data
        else:
            exif_data[tag] = value

    return exif_data

if __name__ == '__main__':
    exif_data = getExif("sample.jpg")
    for key, value in exif_data.items():
        print(key, value)