from rest_framework.test import APITestCase

from .models import CategoryModel


class CategoryCase(APITestCase):
    def setUp(self) -> None:
        CategoryModel.objects.create(name='Technology')

    def getCat(self):
        obj = CategoryModel.objects.get(name='Technology')
        self.assertEqual(obj.name, 'Technology')
