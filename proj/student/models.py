from django.db import models


class Blank(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    course = models.IntegerField()
    phoneNumber = models.IntegerField()

    def to_json(self):
        return {
            "First Name": self.firstName,
            "Last Name": self.lastName,
            "Course": self.course,
            "Phone Number": self.phoneNumber
        }
