from django.test import TestCase
from myapp.models import Influencer

# Create your tests here.
class InfluencerTestCase(TestCase):
    def setUp(self):
        Influencer.objects.create(
            handle = '@adil',
            name = 'Adil Saleem',
            followers = '12.M',
            likes = '12B',
            profile_picture = 'http://picture.from.tiktok.com/inssad'
        )

        Influencer.objects.create(
            handle = '@andleeb',
            name = 'Andleeb Riaz',
            followers = '12.M',
            likes = '12B',
            profile_picture = 'http://picture.from.tiktok.com/inssad'
        )


    def test_influencer_has_proper_greetings(self):
        adil = Influencer.objects.get(name='Adil Saleem')
        self.assertEqual(adil.message(), 'Hello from Adil Saleem')

    def test_influencer_has_proper_image_link(self):
        andleeb = Influencer.objects.get(name='Andleeb Riaz')
        self.assertEqual(andleeb.picture_valid(), True)