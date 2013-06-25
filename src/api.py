'''
PS2-Stats : Python module for PlanetSide 2 Stat tracking.

Copyright (C) 2013 Brendan Betts (brendan.betts@live.com)

License: GNU LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

Created on Jun 6, 2013
'''

import requests
from src.url import url


def do_request(request_parameters):
    request_url = url(request_parameters)
    r = requests.get(request_url.full)
    return r.json()   