from django.db import models

CATEGORIES = (
    ('landing page', 'landing page'),
    ('blog', 'blog'),
    ('portfolio', 'portfolio'),
    ('business', 'business'),
)

class Website(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='business')
    url = models.CharField(max_length=1000)
    details = models.CharField(max_length=1000)
    profile_img = models.ImageField(upload_to='static/assets/img/portfolio/')
    detail_img1 = models.ImageField(upload_to='static/assets/img/portfolio/', null=True, blank=True)
    detail_img2 = models.ImageField(upload_to='static/assets/img/portfolio/', null=True, blank=True)

    def __str__(self):
        return self.name
