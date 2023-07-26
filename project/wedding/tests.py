from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Wedding, Photo, Comment, SitePhotos, File
from .views import MainView, WeddingView
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


class WeddingViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        wedding = Wedding.objects.create(bride_name='Невеста1', groom_name='Жених1', wedding_date='2023-07-20 15:30:00',
                                         wedding_location='Место1', wedding_description='Описание1')
        Photo.objects.create(wedding=wedding, photo_url='photo1.jpg')

        File.objects.create(wedding=wedding, file='ruslan.mp4', mark=1)

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_files(self):
        view = WeddingView()
        request = self.factory.get(reverse('portfolio:wedding'))
        file = view.get_files(request=request)

    def test_template(self):
        view = WeddingView()
        # path = reverse('portfolio:wedding')

        request = self.factory.get('127.0.0.1:8000/portfolio/wedding/1')

        # self.assertTemplateUsed(request, 'wedding_template.html')
        # Будущи мяне у меня йо еще дела поэтому я имею выбор и оставляю тесты на цябя а сам пойду в админке копошиться а у тебя больше выбора не будеть только сможешь тесты делать я поляжу чутка



