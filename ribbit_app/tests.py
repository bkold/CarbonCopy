from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.conf.urls import url
from ribbit_app.models import Ribbit
from . import views
from django.core.urlresolvers import reverse 

from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from time import time


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
		
class TestWebdriver(LiveServerTestCase):
    def setUp(self):
		self.driver = webdriver.Firefox()
		User.objects.create_superuser(
			username='admin',
			password='admin',
			email='admin@example.com'
        )
        

		
    def tearDown(self):
		# Call tearDown to close the web browser
		self.driver.quit()

    def test_auth_user(self): 
		self.driver.get('http://127.0.0.1:8000/')

		self.driver.implicitly_wait(10)
		username = self.driver.find_element_by_xpath('//input[@placeholder="Username"]')
		username.send_keys("test_new")		# This needs to change evertime 
		password1 = self.driver.find_element_by_id("id_email")
		password1.send_keys("testuser@test.com")
		password1 = self.driver.find_element_by_id("id_password1")
		password1.send_keys("123")
		password2 = self.driver.find_element_by_id("id_password2")
		password2.send_keys("123")
		self.driver.find_element_by_xpath('//input[@value="Create Account"]').click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_link_text("Public Profiles").click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_link_text("My Profile").click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_link_text("Public Posts").click()
		self.driver.find_element_by_xpath('//input[@value="Log Out"]').click()

    def test_login_user(self):
		self.driver.get('http://127.0.0.1:8000/')

		username =  self.driver.find_element_by_id("id_username")
		username.send_keys("root")       #this needs to be a vaild user
		password =  self.driver.find_element_by_id("id_password")
		password.send_keys("123")
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_xpath('//input[@value="Log In"]').click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_link_text("Home").click()
		self.driver.find_element_by_link_text("Public Profiles").click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_link_text("My Profile").click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_link_text("Public Posts").click()
		self.driver.find_element_by_xpath('//input[@value="Log Out"]').click()
