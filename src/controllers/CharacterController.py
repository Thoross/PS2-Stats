'''
PS2-Stats : Python module for PlanetSide 2 Stat tracking.

Copyright (C) 2013 Brendan Betts (brendan.betts@live.com)

License: GNU LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

Created on Jun 26, 2013
'''

from src.Character import Character
from src.api import do_request
from src.Utils.utils import *


class CharacterController(object):

    def get_character(self, name):
        url_return = do_request("character/?name.first_lower=%s&c:resolve=world" % name.lower())

        try:
            player_id = url_return["character_list"][0]["id"]
            player_name = url_return["character_list"][0]["name"]["first"]

            api_result = do_request("single_character_by_id/?id=%s&c:resolve=outfit,world" % player_id)

            player = Character(player_id, player_name)
            base = api_result["single_character_by_id_list"][0]

            self.get_character_info(base, player)
            self.get_kills_info(base, player)

            return player

        except:

            return "Not found."

    def get_character_info(self,base,player):
        stats_history_base = base["stats"]["stat_history"]
        certs_base = base["certs"]
        
        player.server = get_server(base["world_id"])
        player.score = stats_history_base["score"]["all_time"]
        player.time_played = base["times"]["minutes_played"]
        player.score_per_minute = calculate_per_minute(player.score, player.time_played)
        player.score_per_hour = calculate_per_hour(player.score, player.time_played)
        player.level = base["battle_rank"]["value"]
        player.spent_certs = certs_base["spent_points"]
        player.available_certs = certs_base["available_points"]
        player.earned_certs = certs_base["earned_points"]
        player.gifted_certs = certs_base["gifted_points"]
        player.total_certs = calculate_total_certs(player.spent_certs, player.available_certs)
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
        except IndexError:
            player.outfit = "None"
        
    def get_kills_info(self, base, player):
        stats_history_base = base["stats"]["stat_history"]
        stats_by_faction_base = base["stats"]["stat_by_faction"]
        stats_base = base["stats"]["stat"]
        
        player.kills = stats_history_base["kills"]["all_time"]
        player.kills_per_minute = calculate_per_minute(player.kills, player.time_played)
        player.kills_per_hour = calculate_per_hour(player.kills, player.time_played)
        player.deaths = stats_history_base["deaths"]["all_time"]
        player.deaths_per_minute = calculate_per_minute(player.deaths, player.time_played)
        player.deaths_per_hour = calculate_per_hour(player.deaths, player.time_played)
        player.kill_death_ratio = float(player.kills) / float(player.deaths)
        player.kdrph = float(player.kills_per_hour) / float(player.deaths_per_hour)
        player.kdrpm = float(player.kills_per_minute) / float(player.deaths_per_minute)
        
        stats_by_faction = get_list_as_dict(stats_by_faction_base)
        stats = get_list_as_dict(stats_base)
        
        player.assists = stats["assist_count"]["value_forever"]
        player.assists_per_hour = calculate_per_hour(player.assists, player.time_played)
        player.assists_per_minute = calculate_per_minute(player.assists, player.time_played)
            
        player.kills_per_faction = get_faction_stat(stats_by_faction,"kills")
        player.killed_by_faction = calculate_total_faction_deaths(stats_by_faction_base)
        player.dominations_per_faction = get_faction_stat(stats_by_faction,"domination_count")
        player.revenge_count_per_faction = get_faction_stat(stats_by_faction,"revenge_count")
        player.dominations = calculate_total_faction_stat(player.dominations_per_faction)
        player.revenge_count = calculate_total_faction_stat(player.revenge_count_per_faction)