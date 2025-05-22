from PIL import Image
from PIL.ExifTags import TAGS

def extract_exif_data(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        metadata = {}
        if exif_data:
            for tag, val in exif_data.items():
                metadata[TAGS.get(tag)] = val
        return metadata
    except Exception as e:
        return {"error": str(e)}