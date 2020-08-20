# coding=utf-8
import requests


class BaseApi:
    def send_request(self, req: dict):
        # 请求封装
        return requests.request(**req).json()
