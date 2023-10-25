#!/usr/bin/env python3
import os
import kong_pdk.pdk.kong as kong

Schema = (
    {"x-hello-from-python": {"type": "string"}},
    
)

version = '0.1.0'
priority = 1000001

# This is an example plugin that add a header to the response

class Plugin(object):
    def __init__(self, config):
        self.config = config

    def access(self, kong: kong.kong):
      #  kong.service.set_header("application/json")
        kong.service.request.set_header('x-hello-from-python','test')
        
        kong.log('access')
        kong.log(kong.router.get_service())
       

# add below section to allow this plugin optionally be running in a dedicated process
if __name__ == "__main__":
    from kong_pdk.cli import start_dedicated_server
    start_dedicated_server("py-hello", Plugin, version, priority, Schema)
