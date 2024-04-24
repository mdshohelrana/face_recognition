from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
import face_recognition
import cv2
import numpy as np
from django.db.models import Q
import os
from django.conf import settings


last_face = 'no_face'
current_path = os.path.dirname(__file__)
face_list_file = os.path.join(current_path, 'face_list.txt')


def index(request):
    file_path = None
    person_name = None
    input_face_encodings = None
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            file_path = os.path.join(settings.MEDIA_ROOT, 'img', image_file.name)
            with open(file_path, 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)

    known_face_encodings = []
    known_face_names = []
    known_face_ext = []

    profiles = Profile.objects.all()
    for profile in profiles:
        person = profile.image
        image_of_person = face_recognition.load_image_file(f'media/{person}')
        person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
        known_face_encodings.append(person_face_encoding)
        known_face_names.append(f'{person}'.split('.')[0])
        known_face_ext.append(f'{person}'.split('.')[1])

    if file_path:
        input_image = face_recognition.load_image_file(file_path)
        input_face_locations = face_recognition.face_locations(input_image)
        input_face_encodings = face_recognition.face_encodings(input_image, input_face_locations)

        for input_face_encoding in input_face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, input_face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, input_face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                ext = known_face_ext[best_match_index]
                image_name = f'{name}.{ext}'
                profile = Profile.objects.get(image=image_name)
                person_name = f'{profile.first_name} {profile.last_name}'
                    
    context = {
        'name': person_name,
    }
    return render(request, 'core/index.html', context)