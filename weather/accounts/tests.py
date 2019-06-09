from django.test import TestCase
from django.test.client import Client

from django.contrib.auth import get_user_model
User = get_user_model()


STATUS_CODES = {
    "OK": 200,
    "NOT FOUND": 404,
}


class TestAuthLinks(TestCase):

    fixtures = ["db_test_data.json"]

    def setUp(self) -> None:
        self._client = Client()
        user = User.objects.all().first()
        self._client.force_login(user)

    def tearDown(self) -> None:
        self._client.logout()

    def test_groups_access(self):
        response = self._client.get("/admin/auth/group/")
        self.assertEqual(STATUS_CODES["OK"], response.status_code)

    def test_users_link(self):
        response = self._client.get("/admin/accounts/user/")
        self.assertEqual(STATUS_CODES["OK"], response.status_code)

    def test_bad_link1(self):
        response = self._client.get("/admin/ssd/abc/")
        self.assertEqual(STATUS_CODES["NOT FOUND"], response.status_code)

    def test_bad_link2(self):
        response = self._client.get("/admin/records/sadasd")
        self.assertEqual(STATUS_CODES["NOT FOUND"], response.status_code)
