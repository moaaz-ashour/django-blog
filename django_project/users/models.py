from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    #override save() method
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # get profile image of current instance
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         # define output img size
    #         output_size = (300, 300)
    #         # resize
    #         img.thumbnail(output_size)
    #         # save back to same path
    #         img.save(self.image.path)