"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import unittest

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#class TestCaseExample(unittest.TestCase):
#	def setUp(self):
#		print "call setUp"
#		self.data = 100
#	def tearDown(self):
#		print "call tearDown"
#		self.data = 101
#	def testCase1(self):
#		self.data = self.data+1
#		self.assertEqual(self.data,101)
#	def testCase2(self):
#		self.data = self.data+1
#		self.assert_(self.data > 100)
#	def haha(self):
#		print "call this?"
#
#if __name__ == '__main__':
#				unittest.main()
