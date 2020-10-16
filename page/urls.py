from django.urls import path
from .views import load_design_1, edit_content, add_image, upload_image,load_webpage

urlpatterns = [
    path('design1/edit-content/', edit_content, name="edit_content"),
    path('design1/add-image/', add_image, name="add_image"),
    path('design1/upload-image/', upload_image, name="upload_image"),
    path('design1/<str:action>/', load_design_1, name="design1"),
    path('<str:slug>/', load_webpage, name="load_webpage"),



]
