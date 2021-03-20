from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # on_delete는 연결된 유저객체가 없어질 때 그와 연결된 profile 객체가 어떤 행동을 보일것인지 담당함 / CASCADE는 profile도 없어지게 설정하는 것

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True) #nickname은 unique(하나만)가지도록 함, null은 무조건 있어야 한다는 뜻
    message = models.CharField(max_length=100, null=True)