'''
Created on Jun 26, 2013

@author: bbetts
'''

from src.Character import Character
from src.api import do_request
from src.Utils.utils import *
class CharacterController(object):
    '''
    classdocs
    '''

    def get_character(self,name):
        url_return = do_request("character/?name.first_lower=%s&c:resolve=world" %name.lower())
        
        player_id = url_return["character_list"][0]["id"]
        player_name = url_return["character_list"][0]["name"]["first"]
        
        api_result = do_request("single_character_by_id/?id=%s&c:resolve=outfit,world" %player_id)
        
        player = Character(player_id,player_name)
        base = api_result["single_character_by_id_list"][0]
        
        self.get_character_info(base,player)
        self.get_kills_info(base, player)
        
        return player
    
    
    def get_character_info(self,base,player):
        stats_history_base = base["stats"]["stat_history"]
        certs_base = base["certs"]
        
        player.server = get_server(base["world_id"])
        player.score = stats_history_base["score"]["all_time"]
        player.time_played = base["times"]["minutes_played"]
        player.score_per_minute = calculate_per_minute(player.score,player.time_played)
        player.score_per_hour = calculate_per_hour(player.score, player.time_played)
        player.level = base["battle_rank"]["value"]
        player.spent_certs = certs_base["spent_points"]
        player.available_certs = certs_base["available_points"]
        player.earned_certs = certs_base["earned_points"]
        player.gifted_certs = certs_base["gifted_points"]
        player.total_certs = calculate_total_certs(player.spent_certs,player.available_certs)
        player.percentage_to_next = base["certs"]["percent_to_next"]
        player.certs_per_minute = calculate_per_minute(player.total_certs, player.time_played)
        player.certs_per_hour = calculate_per_hour(player.total_certs, player.time_played)
        player.faction = get_faction(base["faction_id"])
        player.percentage_to_next_level = base["battle_rank"]["percent_to_next"]
        player.ribbons = stats_history_base["ribbons"]["all_time"]
        player.facilities_captured = stats_history_base["facility_capture"]["all_time"]
        player.facilities_defended = stats_history_base["facility_defend"]["all_time"]
        player.medals = stats_history_base["medals"]["all_time"]
        try:
            player.outfit = base["outfit"]["name"]
        except:
            player.outfit = "None"
        
    def get_kills_info(self,base,player):
        stats_history_base = base["stats"]["stat_history"]
        
        player.kills = stats_history_base["kills"]["all_time"]
        player.kills_per_minute = calculate_per_minute(player.kills,player.time_played)
        player.kills_per_hour = calculate_per_hour(player.kills,player.time_played)