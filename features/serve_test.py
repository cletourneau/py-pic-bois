import unittest
from features.picbois_server import PicboisServer
from hamcrest import assert_that, is_
import requests


class Serve(unittest.TestCase):
    def test_serves_homepage(self):
        result = requests.get('http://localhost:8000/')
        assert_that(result.status_code, is_(200))

    def test_serves_javascript_libraries(self):
        result = requests.get('http://localhost:8000/static/jquery-1.9.1.js')
        assert_that(result.status_code, is_(200))

    @classmethod
    def setUpClass(cls):
        cls._server = PicboisServer(port=8000)
        cls._server.start()

    @classmethod
    def tearDownClass(cls):
        cls._server.shutdown()