from django.test import TestCase
from django.test.client import Client

from django.contrib.auth import get_user_model
User = get_user_model()


STATUS_CODES = {
    "OK": 200,
    "NOT FOUND": 404,
}


class TestLocationsLinks(TestCase):

    fixtures = ["db_test_data.json"]

    def setUp(self) -> None:
        self._client = Client()
        user = User.objects.all().first()
        self._client.force_login(user)

    def tearDown(self) -> None:
        self._client.logout()

    def test_localities_link(self):
        response = self._client.get("/admin/locations/locality/")
        self.assertEqual(STATUS_CODES["OK"], response.status_code)

    def test_districts_link(self):
        response = self._client.get("/admin/locations/district/")
        self.assertEqual(STATUS_CODES["OK"], response.status_code)

    def test_regions_link(self):
        response = self._client.get("/admin/locations/region/")
        self.assertEqual(STATUS_CODES["OK"], response.status_code)

    def test_countries_link(self):
        response = self._client.get("/admin/locations/country/")
        self.assertEqual(STATUS_CODES["OK"], response.status_code)
