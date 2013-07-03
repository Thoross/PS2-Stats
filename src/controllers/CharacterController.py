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
        url_return = do_request("character/?name.first_lower=%s&c:resolve=world" %name.lower())
        player_id = url_return["character_list"][0]["id"]
        player_name = url_return["character_list"][0]["name"]["first"]
        player_server = self.get_server(url_return["character_list"][0]["world_id"])
        api_result = do_request("single_character_by_id/?id=%s" %player_id)
        player = Character(player_id,player_name,player_server)
        base = api_result["single_character_by_id_list"][0]
        #player.score = base["experience"][0]["score"]
        player.time_played = base["times"]["minutes_played"]
        '''player.score_per_minute = self.calculate_per_minute(player.score,player.time_played)
        player.score_per_hour = self.calculate_per_hour(player.score, player.time_played)'''
        player.level = base["battle_rank"]["value"]
        player.spent_certs = base["certs"]["spent_points"]
        player.available_certs = base["certs"]["available_points"]
        player.earned_certs = base["certs"]["earned_points"]
        player.gifted_certs = base["certs"]["gifted_points"]
        player.total_certs = self.calculate_total_certs(player.spent_certs,player.available_certs)
        player.percentage_to_next = base["certs"]["percent_to_next"]
        player.certs_per_minute = self.calculate_per_minute(player.total_certs, player.time_played)
        player.certs_per_hour = self.calculate_per_hour(player.total_certs, player.time_played)
        player.faction =self.get_faction(base["faction_id"])
        
        return player
    
    def get_faction(self,faction_id):
        url_return = do_request("faction/%s"%faction_id)
        return url_return["faction_list"][0]["name"]["en"]

    def get_server(self,world_id):
        url_return = do_request("world/?world_id=%s" %world_id)
        return url_return["world_list"][0]["name"]["en"]

    def calculate_total_certs(self,spent_certs,available_certs):
        return int(spent_certs) + int(available_certs)
    
    def calculate_per_hour(self,stat,time_played):
        hours_played = float(time_played) / 60
        return float(stat) / hours_played
    
    def calculate_per_minute(self,stat,time_played):
        return float(stat) / float(time_played)
    
    def to_string(self,value):
        return str(value)
        