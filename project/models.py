from django.db import models

# Create your models here.
class ProjectImages(models.Model):
    "Images model to stored each image related to the project"
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    project_img = models.ImageField(upload_to="project/images")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Project(models.Model):
    """Project model to list all software projects created"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    project_img = models.ForeignKey(ProjectImages, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

