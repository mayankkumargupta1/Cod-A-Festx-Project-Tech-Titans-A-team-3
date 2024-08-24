import tinify
from django.core.files.base import ContentFile
from .settings import TINIFY

tinify.key = TINIFY

def compress_image(image_file):
    image_file.seek(0)  
    source = tinify.from_buffer(image_file.read())
    compressed_data = source.to_buffer()
    compressed_image = ContentFile(compressed_data, name=image_file.name)
    
    return compressed_image
