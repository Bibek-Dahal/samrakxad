from django.core.files.storage import FileSystemStorage
def upload_file(image):
    fs = FileSystemStorage()
    # img_name = image.name
    file = fs.save('randomimagename', image)
    file_url = fs.url(file)
    return file_url