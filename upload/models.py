from django.db import models
from django.conf import settings
#from .validations import validation_content

# Create your models here.
def validation_content(value):
    content = value
    if content == 'abc':
        raise ValidationError('Cannot be abc')
    return value

class Upload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=150, validators=[validation_content])
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def clean(self, *args, **kwargs):
        content = self.content
        if content == 'abc':
            raise ValidationError("Cannot be abc")
        return super(Upload, self).clean(*args, **kwargs)