PIL: 画像のExifデータの取得
====

PILは，Pythonで一般的な画像処理ライブラリです．
普段は，ファイルの読み込みにもOpenCVを使うことが多いので，
あまり使っていませんでしたが，
今回画像のExifデータを取得できるということで使ってみました．

Anacondaをインストールしていれば，標準でついてくるかと思います．

``` Python
import PIL
```

で特にエラーメッセージが出なければ，モジュールが使える状態になっています．

``` Python
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
```

Flickrからダウンロードした画像に適用してみましたが，
きちんとExif情報が表示されました．

``` bash
Model NIKON D300
FocalLength (1800, 100)
...
Software Adobe Photoshop CS4 Macintosh
...
ColorSpace 65535
ImageWidth 800
DateTime 2009:11:10 00:59:41
...
```

カメラ情報や日付情報等，画像データに埋め込まれているデータを取ってくることが出来ました．

初めは，GPS情報が分かるのかなと思ってこれをやってみましたが，
結構入ってない画像が多く，Flickrはgeotagという物で位置情報を管理している模様です．

geotagの情報取得については今後の課題です．