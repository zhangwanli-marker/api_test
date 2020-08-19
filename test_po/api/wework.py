# -*-coding:utf-8-*-
from test_po.api.baseapi import BaseApi


class Wework(BaseApi):
    def get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwb6742d3e92e042f3",
                "corpsecret": "Q2DM37uRfG6ojcNmkTgjLIrw2e4gmaRsLhbmSQgBi3g"
            }

        }

        res = self.send_request(data)
        # ����tokenֵ
        try:

            yield res['access_token']
        except Exception as e:
            raise ValueError("requests token error")
