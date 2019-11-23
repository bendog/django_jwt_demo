from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField("Date of birth", auto_now=False, auto_now_add=False)
    nick_name = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("profile_detail", kwargs={"pk": self.pk})
