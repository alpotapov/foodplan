from django.db import models


class User(models.Model):
    fake_user_id = models.IntegerField()
    name = models.CharField(max_length=30)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    lactose_intolerance = models.BooleanField(default=False)

    def __str__(self):
        return "User ID: " + self.fake_user_id.__str__() + ", Name: " + self.name


# class User:
#     def __init__(self, user_id, name, vegetarian, vegan, diabetes, lactose_intolerance):
#         self.user_id = user_id
#         self.name = name
#         self.vegetarian = vegetarian
#         self.vegan = vegan
#         self.diabetes = diabetes
#
# user0 = User(user_id = 0, name="Christian", vegetarian=False, vegan=False, diabetes=False, lactose_intolerance=False)
# user1 = User(user_id = 1, name="Anna", vegetarian=True, vegan=False, diabetes=False, lactose_intolerance=True)