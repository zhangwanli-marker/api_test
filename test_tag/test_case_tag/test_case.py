# -*-coding:utf-8-*-
import pytest
from requests import Session

from test_tag.tag.tag import Tag
from test_tag.tag.wework import WeWork


class TestTag:

    def setup(self):
        self.tag = Tag()

    @pytest.fixture(scope="session")
    def token(self):
        yield WeWork().get_token()

    # 新增标签测试
    def test_add_tag(self, token, tagname="zhangwanli", tagid=12, ):
        print(self.tag.add_tag(tagname, token))
        assert "created" == self.tag.add_tag(tagname, token)["errmsg"]

    # 删除标签测试
    def test_delete_tag(self, tagid, token):
        assert "deleted" == self.tag.delete_tag(tagid, token)["errmsg"]

    # 更新标签测试
    def test_updata_tag(self, tagid, tagname, token):
        assert "updated" == self.tag.update_tag(tagid, tagname, token)["errmsg"]

    # 获取标签列表测试
    def test_get_tag(self, token):

        assert "ok" == self.tag.get_tag(token)["errmsg"]

    def create_muti_data(self):
        data = [("wanli" + str(x), "10%03d" % x) for x in range(10)]
        return data

    # 集成测试
    @pytest.mark.parametrize("tagname", "tagid", create_muti_data("xx"))
    def test_all(self, tagname, tagid, token):

        try:

            assert "create" == self.test_add_tag(tagname, token)["errmsg"]
        except AssertionError as e:
            if "UserTag Name Already Exist" in e.__str__():
                self.test_delete_tag(tagid, token)
            assert "create" == self.test_add_tag(tagname, token)["errmsg"]

        assert "updated" == self.test_updata_tag(tagid, "change", token)
        assert "deleted" == self.test_delete_tag(tagid, token)["errmsg"]






    #
    #     assert "change" == self.test_get_tag(token)["taglist"]["tagid"]
    #     list_len = len(self.tag.get_tag(token)["taglist"])
    #     list1 = []
    #     for i in range(list_len):
    #         list1.append(self.tag.get_tag(token)["taglist"][i]["tagname"])
    #
    #     print(list1)