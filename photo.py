from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                metadata = {}
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[tag_name] = value

                
                if 'DateTime' in metadata:
                    print(f"Дата и время: {metadata['DateTime']}")
                if 'GPSInfo' in metadata:
                    gps_info = metadata['GPSInfo']
                    latitude = gps_info[2]
                    longitude = gps_info[4]
                    print(f"Широта: {latitude}, Долгота: {longitude}")
                return metadata
            else:
                print("Метаданные не найдены в изображении.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    image_path = "путь_к_фото.jpeg" 
    exif_data = get_image_metadata(image_path)
    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            print(f"Тег: {tag_name}, Значение: {value}")




