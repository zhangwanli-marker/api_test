# -*-coding:utf-8-*-
import random
import re

import pytest

from test_po.api.access import AccessApi
from test_po.api.wework import Wework


class TestWework:
    @pytest.fixture(scope="session")
    def token(self):
        yield Wework().get_token()

    def set_up(self):
        self.access = AccessApi()

    # def test_creat_data(self):
    #     data = [(str(random.randint(0, 99999)), "zhangsan1", \
    #              str(random.randint(13800000000, 13800099999))) for x in range(3)]
    #     return data

    def create_muti_data(self):
        data = [("wu12345wu" + str(x), "zhangsan1", "138%08d" % x) for x in range(5)]
        return data

    @pytest.mark.parametrize("userid,name,mobile,", create_muti_data("xx"))
    def test_all(self, userid, name, mobile, token, department=None):
        try:

            # 创建成员，对结果断言
            assert "created" == self.access.test_add_member(userid, name, mobile, token)['errmsg']
        except AssertionError as e:
            if "userid existed" in e.__str__():

                self.access.test_delete(userid, token)
            if "mobile existed" in e.__str__():
                # delete_userid = re.findall(":(.*)'$", e.__str__())
                delete_userid = re.findall("mobile existed:(.*)'$", e.__str__())
                print(type(delete_userid))
                print(delete_userid)
                self.access.test_delete(delete_userid[0], token)
            assert "created" == self.access.test_add_member(userid, name, token, mobile)['errmsg']
        # 查询成员信息，对结果进行断言
        print(name)

        assert name == self.access.test_get_member(userid, token)['name']
        # # 更新一个成员
        assert "updated" == self.access.test_update(userid, "wangwu", token)['errmsg']
        assert "wangwu" == self.access.test_get_member(userid, token)["name"]
        # # 删除
        assert "deleted" == self.access.test_delete(userid, token)["errmsg"]
        # # 查询
        assert 60111 == self.access.test_get_member(userid, token)["errcode"]
