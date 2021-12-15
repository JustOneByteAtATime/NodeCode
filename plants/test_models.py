from django.test import TestCase
from plants.models import Post
import pytz
from unittest import mock
from django.contrib.auth.models import User
from django.test import tag
from django.conf import settings
import os
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

class PostModelTest(TestCase):
    def setUp(self):
        self.temp_user = User.objects.create_user("TestUser")
        # Set up non-modified objects used by all test methods

    def tearDown(self):
        User.objects.all().delete()

        

    @tag('model')
    def test_title_label(self):
        post = Post.objects.create(title= "temp title", body="temp_body", zipcode="12345",author=self.temp_user)
        self.assertEqual(post.title, "temp title")

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    @tag('model')
    def test_post_record_create_without_image_will_return_default_image(self):
        post = Post.objects.create(title= "temp title", body="temp_body", zipcode="12345",author=self.temp_user,)
        self.assertEqual(post.image.name, 'default_plant.jpg')

    @tag('model')
    def test_post_record_create_without_image_will_get_default_image_file_from_configured_media_location(self):
        post = Post.objects.create(title= "temp title", body="temp_body", zipcode="12345",author=self.temp_user,)
        image_path = os.path.join(settings.MEDIA_ROOT, 'default_plant.jpg')
        self.assertEqual(post.image.path, image_path)

    @tag('model')
    def test_post_record_create_with_image_will_create_image_file_under_images_folder_in_configured_media_location(self):
        post = Post.objects.create(title= "temp title", body="temp_body", zipcode="12345",author=self.temp_user,image=SimpleUploadedFile('test_image.jpg', b''))
        image_path = os.path.join(settings.MEDIA_ROOT, 'images', 'default_plant.jpg')
        self.assertEqual(post.image.path, image_path)


    def test_body_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'instantiated (post)body')

    def test_zipcode_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('zipcode').verbose_name
        self.assertEqual(field_label, 'instantiated (post)zipcode')

    def test_zipcode_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('zipcode').max_length
        self.assertEqual(max_length, 5)

    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEqual(str(post), expected_object_name)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/plants/post/1')
