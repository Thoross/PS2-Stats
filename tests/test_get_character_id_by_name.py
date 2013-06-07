'''
Created on Jun 6, 2013

@author: Acedia
'''
import unittest
import api


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