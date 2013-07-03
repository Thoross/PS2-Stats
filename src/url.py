'''
PS2-Stats : Python module for PlanetSide 2 Stat tracking.

Copyright (C) 2013 Brendan Betts (brendan.betts@live.com)

License: GNU LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

Created on Jun 7, 2013
'''
class url(object):
    '''
    classdocs
    '''
   

    def __init__(self,parameters):
        '''
        Constructor
        '''
        url_root = "http://census.soe.com/get/ps2/"
        self.full = url_root + parameters