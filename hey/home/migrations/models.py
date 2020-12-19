from django.db import models

#create your model here
class contact(Models.Models):
    name = models.charField(max_lenght=122)
    email = models.charField(max_lenght=122)
    phone = models.charField(max_lenght=10)
    desc = models.TextField()
    date = models.DataField()
