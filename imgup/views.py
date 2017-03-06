from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render

from PIL import Image

from forms import UploadImageForm
from models import UploadModel

import os

import app_settings as aps


def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if(file.content_type not in aps.file_types):
                return render(request, 'upload.html', {
                              'form': form, 'message': 'Invalid file. Only \
                              JPEG, PNG, TIFF & BMP formats acceptable'})
            else:
                try:
                    '''
                    Reduce image size to max size of 300x300 (app settings)
                    '''
                    img = Image.open(file)
                    h, w = img.size
                    if(max(h, w) > aps.max_img_size):
                        ratio = aps.max_img_size * 1.0 / max(h, w)
                        img = img.resize(
                            (int(h * ratio), int(w * ratio)), Image.ANTIALIAS)
                    img.save(aps.img_storage + file.name)
                    reopen = open(aps.img_storage + file.name, "rb")
                    dfile = File(reopen)
                    UploadModel.objects.create(
                        username=request.POST['username'], image=dfile)
                    # Move file from memory to trash
                    os.rename(dfile.name, '/tmp/' + file.name)

                    return render(request, 'msg.html')

                except Exception as e:
                    return render(request, 'msg.html', {
                                  'message': "Image upload failed. \
                                  Unknown Error: " + str(e)})
    else:
        form = UploadImageForm()
        return render(request, 'upload.html', {'form': form})
