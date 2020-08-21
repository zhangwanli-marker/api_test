# -*-coding:utf-8-*-
from test_tag.tag.base_tag import BaseApi


class Tag(BaseApi):

    # 创建标签

    def add_tag(self, tagname,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
            "json": {
                "tagname": tagname
            }
        }

        return self.send_api(data)

    # 删除标签
    def delete_tag(self, tagid,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}",
            "json": {
                "tagid": tagid
            }
        }
        return self.send_api(data)

    # 获取标签
    def get_tag(self,token):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}",
            "method": "get"}
        return self.send_api(data)

    # 更新标签名称
    def update_tag(self,tagid,tagname,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
            "json": {
                "tagid": tagid,
                "tagname": tagname
            }
        }
        return self.send_api(data)
