from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Wedding, Photo, Comment, SitePhotos
from .views import MainView
from .forms import CommentForm


class MainViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        wedding = Wedding.objects.create(bride_name='Невеста1', groom_name='Жених1', wedding_date='2023-07-20 15:30:00', wedding_location='Место1', wedding_description='Описание1')
        Photo.objects.create(wedding=wedding, photo_url='photo1.jpg')
        Comment.objects.create(commenter_name='John Doe', comment_text='Test comment 1', comment_date='2023-07-21 10:00:00', is_accepted=True)


    def setUp(self):
        self.factory = RequestFactory()

    def test_get_queryset(self):
        view = MainView()
        queryset = view.get_queryset()
        self.assertEqual(queryset.count(), 1)

    def test_get_wedding_photos(self):
        view = MainView()
        weddings = Wedding.objects.all()
        wedding_photos = view.get_wedding_photos(weddings)
        self.assertEqual(len(wedding_photos), 1)

    def test_get_context_data(self):
        view = MainView()
        request = self.factory.get(reverse('main'))
        context = view.get_context_data(request=request)

        self.assertIn('title', context)
        self.assertIn('weddings', context)
        self.assertIn('wedding_photos', context)
        self.assertIn('comments', context)
        self.assertIn('form', context)

        self.assertEqual(len(context['weddings']), 1)
        self.assertEqual(len(context['comments']), 1)

    def test_post_valid_form(self):
        view = MainView()
        form_data = {
            'commenter_name': 'Jane Smith',
            'comment_text': 'Test comment 2',
            'comment_date': '2023-07-22 12:00:00',
            'is_accepted': True
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

        request = self.factory.post(reverse('main'), data=form_data)
        request.session = {}
        response = view.post(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)

    def test_post_invalid_form(self):
        view = MainView()
        form_data = {
            'commenter_name': 'Jane Smith',
            'comment_date': '2023-07-22 12:00:00',
            'is_accepted': True
        }
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

        request = self.factory.post(reverse('main'), data=form_data)
        request.session = {}
        response = view.post(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
