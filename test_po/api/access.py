# -*-coding:utf-8-*-
from test_po.api.baseapi import BaseApi


class AccessApi(BaseApi):

    def test_add_member(self, userid, name, mobile, token, department=None):
        print("执行添加成员")

        if department is None:
            department = [1]
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
            }
        }
        res = self.send_request(data)
        print(res)
        return res

    def test_get_member(self, userid, token):
        print("执行获取成员")

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": token,
                "userid": userid
            }
        }

        res = self.send_request(data)
        print(res)
        return res

    def test_update(self, userid, name, token):
        print("执行更新成员")
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
            "json": {
                "userid": userid,
                "name": name,
            }
        }

        res = self.send_request(data)
        print(res)
        return res

    def test_delete(self, userid, token):
        print("执行删除成员")
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
        }
        res = self.send_request(data)
        print(res)
        return res
