'''
Created on Jun 26, 2013

@author: bbetts
'''

from src.Character import Character
from src.api import do_request

class CharacterController(object):
    '''
    classdocs
    '''

    def get_character(self,name):
        url_return = do_request("character/?name.first_lower=%s" %name.lower())
        base = url_return["character_list"][0]
        player_id = base["id"]
        player_name = base["name"]["first"]
        player = Character(player_id,player_name)
        player.score = base["experience"][0]["score"]
        player.time_played = base["stats"]["play_time"]["value"]
        player.score_per_minute = self.calculate_per_minute(player.score,player.time_played)
        player.score_per_hour = self.calculate_per_hour(player.score, player.time_played)
        return player
        
    def calculate_per_hour(self,stat,time_played):
        hours_played = float(time_played) / 3600
        return float(stat) / hours_played
    def calculate_per_minute(self,stat,time_played):
        minutes_played = float(time_played) / 60
        return float(stat) / minutes_played
        
        