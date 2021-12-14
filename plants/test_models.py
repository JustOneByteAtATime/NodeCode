from django.test import TestCase

class NodeCodeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    # This method is clearly designed to fail:
##    def test_false_is_true(self):
##        print("Method: test_false_is_true.")
##        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

from plants.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title= 'Titan Arum', body= 'Totally kidding. We do not have corpse flower cuttings!', zipcode= '58720')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'instantiated (post)title')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

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
