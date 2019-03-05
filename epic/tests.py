from django.test import TestCase
from .models import Image,Location,Categories
class ImageTestCLass(TestCase):
    '''
    setup self instance of image
    '''
    def setUp(self):
        self.pic = Image(name='Movie',description='Home alone')

    '''
    test instance of image
    '''
    def test_instance(self):
       self.assertTrue(isinstance(self.pic,Image))
