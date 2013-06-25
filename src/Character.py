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
    '''
    classdocs
    '''
    

    def __init__(self,id,name):
        '''
        Constructor
        '''
        self.id = id
        self.name = name
        self.level = 0
        self.score = 0
        self.score_per_minute = 0.00
        self.score_per_hour = 0.00
        self.time_played = 0
        self.kill_death_ratio = 0.00
        self.kills = 0
        self.kills_per_minute = 0.00
        self.kills_per_hours = 0.00
        self.kills_per_class = {}
        self.deaths = 0
        self.deaths_per_minute = 0.00
        self.deaths_per_hour = 0.00
        self.deaths_per_class = {}
        self.damage_given = 0
        self.damage_taken = 0
        self.certs = 0
        self.percentage_to_next = 0.00
        self.vehicle_list = []
        self.weapon_list = []
        
        
        
        