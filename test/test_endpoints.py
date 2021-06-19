from __future__ import absolute_import
import unittest
import os
import sys

from os import listdir
from os.path import isfile, join

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from main import app


class TestCases(unittest.TestCase):
    def test_static_pages(self):
        for f in listdir("app/static"):
            filePath = join("app/static", f)

            if(isfile(filePath)):
                response = app.test_client().get(join("static", f))
                f = open(filePath, "rb")
                self.assertEqual(f.read(), response.data)
                f.close()
