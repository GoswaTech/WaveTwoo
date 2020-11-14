from django.db import models

# Create your models here.
class Cooktsu(models.Model):

    alchemy_name = models.CharField(max_length=23)
    name = models.CharField(max_length=23)

    #terre
    red = models.ForeignKey('Transmutation', on_delete=models.CASCADE, unique=True, related_name="cooktsu_red")
    #eau
    orange = models.ForeignKey('Transmutation', on_delete=models.CASCADE, unique=True, related_name="cooktsu_orange")
    #air
    green = models.ForeignKey('Transmutation', on_delete=models.CASCADE, unique=True, related_name="cooktsu_green")
    #feu
    yellow = models.ForeignKey('Transmutation', on_delete=models.CASCADE, unique=True, related_name="cooktsu_yellow")

    ingredients = models.ManyToManyField('Ingredient')

    def get_red_ingredients(self):
        ingredients = self.ingredients.filter(element='red')
        return ingredients

    def get_orange_ingredients(self):
        ingredients = self.ingredients.filter(element='orange')
        return ingredients

    def get_green_ingredients(self):
        ingredients = self.ingredients.filter(element='green')
        return ingredients
    def get_yellow_ingredients(self):
        ingredients = self.ingredients.filter(element='yellow')
        return ingredients

    def __str__(self):
        return '{0} : {1}'.format(self.name, self.alchemy_name)


class Transmutation(models.Model):

    description = models.TextField(max_length=2047)

    def __str__(self):
        return '{0} {1}'.format(self.id, self.description)



class Ingredient(models.Model):

    ELEMENTS = [
        ('red', 'Terre'),
        ('orange', 'Eau'),
        ('green', 'Air'),
        ('yellow', 'Feu'),
    ]

    name = models.CharField(max_length=63)
    element = models.CharField(max_length=7, choices=ELEMENTS, default=ELEMENTS[0][0])
    quantity = models.OneToOneField('Quantity', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.element)


class Quantity(models.Model):

    value = models.FloatField()
    unit = models.CharField(max_length=31)

    def __str__(self):
        return '{0} {1}'.format(self.value, self.unit)
