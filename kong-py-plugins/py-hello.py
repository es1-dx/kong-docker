#!/usr/bin/env python3
import os
import kong_pdk.pdk.kong as kong
import requests

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])


Schema = (
    {"x-hello-from-python": {"type": "string"}},
    
)

version = '0.1.0'
priority = 0

# This is an example plugin that add a header to the response

class Plugin(object):
    def __init__(self, config):
        self.config = config

    def access(self, kong: kong.kong):
        # header追加サンプル
        kong.service.request.set_header('x-hello-from-python','test')

        # API コールサンプル
        try:
        
           url = "http://localhost:8000/any2"
           params = {}
           headers = {'x-search': 'Tokyo'}
        
           response = requests.get(url, params=params, headers=headers)
        
           if response.status_code == 200:
               data = response.json()
               kong.log(str(data))
           else:
               kong.log('API Error')
        except Exception as e:
           kong.log(e)

        # Service情報取得サンプル
        try:
           r = kong.router.get_service()

           service_name = str(r["name"])
           path = str(r["host"])
           
           kong.log.err(service_name)
           kong.log.err(path)
        except Exception as e:
           kong.log(e)

        # サービスに行かずに戻すサンプル
        #kong.response.exit(407, "Test")
       

# add below section to allow this plugin optionally be running in a dedicated process
if __name__ == "__main__":
    from kong_pdk.cli import start_dedicated_server
    start_dedicated_server("py-hello", Plugin, version, priority, Schema)
