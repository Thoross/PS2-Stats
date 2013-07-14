'''
PS2-Stats : Python module for PlanetSide 2 Stat tracking.

Copyright (C) 2013 Brendan Betts (brendan.betts@live.com)

License: GNU LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

Created on Jun 24, 2013
'''

class Character(object):
    
    # The key is the profile_id that comes from the api.
    classes = {'2':"Infiltrator", '4':"Light Assault",'5':"Combat Medic","6":"Engineer","7":"Heavy Assault","8":"MAX"}

    def __init__(self,character_id,name):
        '''
        Constructor
        '''
        self.character_id = character_id
        self.name = name
        self.faction = ""
        self.server = ""
        self.outfit = ""
        self.level = 0
        self.percentage_to_next_level = 0.00
        self.score = 0
        self.score_per_minute = 0.00
        self.score_per_hour = 0.00
        self.time_played = 0
        self.kill_death_ratio = 0.00
        self.kills = 0
        self.kills_per_minute = 0.00
        self.kills_per_hours = 0.00
        self.kills_per_class = {}
        self.kills_per_faction = {}
        self.deaths = 0
        self.suicides = 0
        self.killed_by_faction = {}
        self.killed_by_class = {}
        self.killed_by_weapon_list = []
        self.deaths_per_minute = 0.00
        self.deaths_per_hour = 0.00
        self.deaths_per_class = {}
        self.damage_given = 0
        self.damage_given_per_faction = {}
        self.damage_taken = 0
        self.damage_taken_per_faction = {}
        self.total_certs = 0
        self.spent_certs = 0
        self.available_certs = 0
        self.earned_certs = 0
        self.gifted_certs = 0
        self.certs_per_minute = 0.00
        self.certs_per_hour = 0.00
        self.certs_percentage_to_next = 0.00
        self.hit_count = 0
        self.hit_count_per_class = {}
        self.fire_count = 0
        self.fire_count_per_class = {}
        self.accuracy_percentage = 0.00
        self.infantry_accuracy_percentage = 0.00
        self.vehicle_accuracy_percentage = 0.00
        self.vehicle_list = []
        self.weapon_list = []
        self.facilities_captured = 0
        self.facilities_defended = 0
        self.ribbons = 0
        self.medals = 0
        self.stats = []
        self.stat_by_faction = []
        self.assists = 0
        self.assists_per_minute = 0.00
        self.assists_per_hour = 0.00
        self.headshots = 0
        self.headshots_by_empire = {}
        self.dominations = 0
        self.dominations_per_faction = {}
        self.revenge_count = 0
        self.revenge_count_per_faction = {}