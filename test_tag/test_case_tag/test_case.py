#-*-coding:utf-8-*-
import pytest

from test_tag.tag.wework import WeWork


class TestTag:

    def setup(self):
        pass
    @pytest.fixture(scope="session")
    def token(self):
        yield WeWork().get_token()


    def test_add_tag(self):
        pass

    def test_delete_tag(self):
        pass

    def test_updata_tag(self):
        pass

    def test_get_tag(self):
        pass