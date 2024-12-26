from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.core.exceptions import ValidationError

def validate_image(file):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    ext = file.name.split('.')[-1].lower()
    if f".{ext}" not in valid_extensions:
        raise ValidationError("Unsupported file extension. Please upload an image file.")
    
class UploadedContent(models.Model):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, validators=[validate_image])
    file = models.FileField(upload_to='files/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.photo or self.file}"
