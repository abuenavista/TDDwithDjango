from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string		#for decode()

from lists.views import home_page

# Create your tests here.

#silly test
#class SmokeTest(TestCase):
#	"""docstring for SmokeTest"""
#	def test_bad_maths(self):
#		self.assertEqual(1+1,3)

class HomePageTest(TestCase):
	"""docstring for HomePageTest"""

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/') 
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>To-Do lists</title>', response.content)
		#self.assertTrue(response.content.endswith(b'</html>'))

		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)