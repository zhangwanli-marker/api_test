# -*-coding:utf-8-*-
from test_tag.tag.base_tag import BaseApi


class Tag(BaseApi):

    # 创建标签

    def add_tag(self, tagname, tagid):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }

        return self.send_api(data)

    # 删除标签
    def delete_tag(self, tagid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "json": {
                "tagid": tagid
            }
        }
        return self.send_api(data)

    # 获取标签
    def get_tag(self):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "method": "get"
        }
        return self.send_api(data)

    # 更新标签名称
    def update_tag(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "json": {
                "tagid": 12,
                "tagname": "UI design"
            }
        }
        return self.send_api(data)
