from django.core.validators import MinValueValidator, MaxValueValidator  
from datetime import timedelta, time, date, datetime
from django.core.exceptions import ValidationError
from apps.common.models import BaseModel
from django.utils.text import slugify
from apps.user.models import User
from django.db import models

class Category(BaseModel):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='category/')
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Course(BaseModel):
    BEGIN_TIME = [
        (time(8, 0), '08:30'),
        (time(10, 0), '10:30'),
        (time(13, 0), '13:30'),
        (time(15, 0), '15:30'),
        (time(18, 0), '17:30'),
        (time(19, 0), '19:30')
    ]
    DURATION = [
        (2, '2 soat'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    created_by_admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.TextField()
    photo = models.FileField(upload_to='course/')
    group_number = models.IntegerField(default=0)
    begin_time = models.TimeField(choices=BEGIN_TIME)
    duration = models.IntegerField(choices=DURATION, default=2)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)

    @property
    def end_time(self):
        end_time = datetime.combine(date.today(), self.begin_time) + timedelta(hours=self.duration)
        return end_time.time()
    
    def clean(self):
        if self.end_time > time(22, 0):
            raise ValidationError({'end_time': 'Dars 22:00 gacha tugashi kerak.'})
        if self.duration != 2:
            raise ValidationError({'duration': "Dars davomi 2 soat bo'lishi kerak."})
        
    def __str__(self):
        return self.desc

class Price(BaseModel):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    lessons = models.IntegerField(default=0)
    status_name = models.CharField(max_length=255)

    @property
    def count_lessons(self):
        return self.lessons.count()

    def __str__(self):
        return self.name 

class Blog(BaseModel):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    imgs = models.FileField(upload_to='blogs/')

    def __str__(self):
        return self.name 
