from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnickersTest(SimpleTestCase):
    def check_status_code(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) # (actual, expected)

    def test_home_status(self):
        self.check_status_code('home')

    def test_about_status(self):
        self.check_status_code('about')

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_template(self):
        url = reverse('about')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')

        