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

import unittest
from src import api 


class Test(unittest.TestCase):

     def setUp(self):
         self.player_id = '5428010618040559457'

     def test_get_player_id(self):
        character_id = api.get_character_id_by_name("thoross")
        self.assertEquals(self.player_id, character_id)
    
     def test_blank_player_id(self):
        character_id = '' 
        self.assertRaises()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()