from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=100, null=False)
    capacity = models.IntegerField(null=False)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100, null=False)
    capacity = models.IntegerField(null=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
