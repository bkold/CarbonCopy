"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.conf.urls import url
from ribbit_app.models import Ribbit
from . import views
from django.core.urlresolvers import reverse 

class TestAccess(TestCase):
	def setUp(self):
		self.c = Client()
		
	def test_entries_access(self):
		#no account
		response = self.c.get('/')
		self.assertEqual(response.status_code,200)
		
		response = self.c.get('/login')
		self.assertEqual(response.status_code,302)
			#redirect to '/'
		
		response = self.c.get('/logout')
		self.assertEqual(response.status_code,302)
			#redirect to '/'
		
		response = self.c.get('/signup')
		self.assertEqual(response.status_code,302)
			#redirect to '/'
		
		response = self.c.get('/public')
		self.assertEqual(response.status_code,302)
			#redirect to '/'
		
		response = self.c.get('/submit')
		self.assertEqual(response.status_code,302)
			#redirect to '/'
		
		response = self.c.get('/users')
		self.assertEqual(response.status_code,301)
			#redirect to '/'
		
		response = self.c.get('/follow')
		self.assertEqual(response.status_code,302)
			#redirect to '/'
	
class TestLogedInAccess(TestCase):
	def setUp(self):
		self.c = Client()
		self.user = User.objects.create_user(username="testMan", email="testMan@test.com", password="123")
	
	def test_entry_created(self):
		#####not loged in
		response = self.c.get(reverse('b'))
		self.assertEqual(response.status_code, 200)
		
		response = self.c.get(reverse('logn'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		response = self.c.get(reverse('logot'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		response = self.c.get(reverse('sign'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		response = self.c.get(reverse('pub'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		response = self.c.get(reverse('us'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		response = self.c.get(reverse('fol'))
		self.assertEqual(response.status_code, 302)	
			#redirect to '/'	
		
		#####login
		self.c.login(username='testMan', password='123')		
		response = self.c.get(reverse('b'))
		self.assertEqual(response.status_code, 200)
		
		self.c.login(username='testMan', password='123')	
		response = self.c.get(reverse('logn'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		self.c.login(username='testMan', password='123')	
		response = self.c.get(reverse('logot'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		self.c.login(username='testMan', password='123')	
		response = self.c.get(reverse('sign'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/'
		
		self.c.login(username='testMan', password='123')	
		response = self.c.get(reverse('pub'))
		self.assertEqual(response.status_code, 200)
		
		self.c.login(username='testMan', password='123')	
		response = self.c.get(reverse('us'))
		self.assertEqual(response.status_code, 200)
		
		self.c.login(username='testMan', password='123')	
		response = self.c.get(reverse('fol'))
		self.assertEqual(response.status_code, 302)
			#redirect to '/users'
		
	def test_entries_template_context(self):
		
		#####upload test
		Ribbit.objects.create(content='test post 2', pic='{{MEDIA_URL}}uploaded_files/test.jpg', brightness='20', user=self.user) 		
		response = self.c.get(reverse('sub'))
		
