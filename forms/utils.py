import tinify
from django.core.files.base import ContentFile
from website.settings import TINIFY
from django.core.files.storage import FileSystemStorage

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import os
from django.contrib.staticfiles.storage import staticfiles_storage
from website.settings import *

SERVICE_ACCOUNT_FILE = staticfiles_storage.path('service.json')

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_photo(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [PARENT_FOLDER_ID_IMAGES]
    }
    
    media = MediaFileUpload(file_path, resumable=True)
    
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    file_id = file.get("id")

    service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    return f'https://drive.google.com/uc?id={file_id}'

def upload_gallery(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [PARENT_FOLDER_ID_GALLERY]
    }
    
    media = MediaFileUpload(file_path, resumable=True)
    
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    file_id = file.get("id")

    service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    
    return f'https://drive.google.com/thumbnail?id={file_id}&sz=s4000'

def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [PARENT_FOLDER_ID_DOCUMENT]
    }
    
    media = MediaFileUpload(file_path, resumable=True)
    
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    file_id = file.get("id")

    service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    return f'https://drive.google.com/uc?id={file_id}'

tinify.key = TINIFY

def compress_image(image_file):
    image_file.seek(0)  
    source = tinify.from_buffer(image_file.read())
    compressed_data = source.to_buffer()
    compressed_image = ContentFile(compressed_data, name=image_file.name)
    
    return compressed_image

def image_url(file: object) -> str:
    uploaded_file = file
    try:
        uploaded_file = compress_image(uploaded_file)
    except:
        uploaded_file = file
    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)
    file_path = fs.path(filename)
    file_url = upload_photo(file_path)
    fs.delete(filename)
    return file_url

def file_url(file: object) -> str : 
    uploaded_file = file
    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)
    file_path = fs.path(filename)
    file_url = upload_file(file_path)
    fs.delete(filename)
    return file_url

def gallery_image_url(file: object) -> str:
    uploaded_file = file
    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)
    file_path = fs.path(filename)
    file_url = upload_gallery(file_path)
    fs.delete(filename)
    return file_url

def delete_file(file_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    service.files().delete(fileId=file_id).execute()


import re

def get_file_id(url):
    pattern = r'https://drive\.google\.com/uc\?id=([^&]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None
    
def get_file_gallery_id(url):
    pattern = r'https://drive\.google\.com/thumbnail\?id=([^&]+)&sz=s4000'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None