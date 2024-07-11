from django.db import models

CATEGORY_CHOICES = (
  ('Front-End', 'FrontEnd'),
  ('Back-End', 'Backend'),
  ('WebDesing', 'WebDesing'),
)

class Project(models.Model):
  title = models.CharField(max_length=200)
  category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, blank=True, null=True)
  link = models.URLField()
  date = models.DateField()
  image = models.ImageField(upload_to="projects/")

  def __str__(self):
    return self.title
