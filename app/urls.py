from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_stream/', views.video_stream, name='video_stream'),
    path('add_photos/', views.add_photos, name='add_photos'),
    path('add_photos/<slug:emp_id>/', views.click_photos, name='click_photos'),
    path('train_model/', views.train_model, name='train_model'),
    path('detected/', views.detected, name='detected'),
    path('identify/', views.identify, name='identify'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('stream/<slug:emp_id>/', views.stream, name='stream'),
    path('live_stream/', views.detected_stream, name='live_stream'),
    path('capture_stream/', views.capture_stream, name='capture_stream'),
    path('save_image/', views.save_image, name='save_image'),
    path('predict_image/', views.predict_image, name='predict_image'),
    path('bulk/<slug:emp_id>/', views.bulk, name='bulk'),
    path('bulk_upload_images/', views.bulk_upload_images, name='bulk_upload_images'),
]