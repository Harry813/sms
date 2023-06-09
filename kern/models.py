from django.db import models


class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

