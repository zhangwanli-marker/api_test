# -*-coding:utf-8-*-
import requests


class BaseApi:
    def send_request(self, req: dict):
        # �����װ
        return requests.request(**req).json()
