from django.test import TestCase
from .models import Location,Categories,Image
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):
    '''
    test setup of Location
    '''
    def setUp(self):
        self.New = Location(name='New')

    '''
    test instance of Location
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Location))

    # def tearDown(self):
    #     Tags.objects.all().delete()
    '''
    test to assertain save Location
    '''
    def test_save_location(self):
        self.New.save_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)>0)
    '''
    test to assert that delete is working
    '''
    def test_delete_location(self):
        self.New.save_location()
        self.New.delete_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)== 0)

    '''
    test to assert that Location update
    '''
    def test_update_location(self):
        self.New.save_location()
        new = Location.objects.filter(name='New').update(name='outdated')
        loc = Location.objects.get(name='outdated')
        self.assertEqual(loc.name,'outdated')



class CategoriesTestClass(TestCase):
    '''
    test setup of Categories
    '''
    def setUp(self):
        self.New = Categories(name='New')

    '''
    test instance of category
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Categories))


    '''
    test to assertain save category
    '''
    def test_save_category(self):
        self.New.save_category()
        cat = Categories.objects.all()
        self.assertTrue(len(cat)>0)
    '''
    test to assert that delete is working
    '''
    def test_delete_category(self):
        self.New.save_category()
        self.New.delete_category()
        cat = Categories.objects.all()
        self.assertTrue(len(cat)== 0)

    '''
    test to assert that categorys update
    '''
    def test_update_category(self):
        self.New.save_category()
        new = Categories.objects.filter(name='New').update(name='outdated')
        cat = Categories.objects.get(name='outdated')
        self.assertEqual(cat.name,'outdated')


class ImageTestCLass(TestCase):
    '''
    setup self instance of image
    '''
    def setUp(self):
        self.pic = Image(name='movie',description='Avengers')

    '''
    test instance of image
    '''
    def test_instance(self):
       self.assertTrue(isinstance(self.pic,Image))


    '''
    test save image
    '''

    def test_save_image(self):
        self.pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    '''
    test delete image
    '''

    def test_delete_image(self):
        self.pic.save_image()
        self.pic.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    
