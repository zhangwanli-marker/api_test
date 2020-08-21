#-*-coding:utf-8-*-
import requests


class WeWork:
    def get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwb6742d3e92e042f3",
                "corpsecret": "Q2DM37uRfG6ojcNmkTgjLIrw2e4gmaRsLhbmSQgBi3g"
            }
        }
        res = requests.request(**data).json()
        try:
            return res['access_token']
        except Exception as e:
            raise ValueError("requests token error")
