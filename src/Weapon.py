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

class Weapon(object):

    def __init__(self,weapon_id,name):
        '''
        Constructor
        '''
        self.weapon_id = weapon_id
        self.name = name
        self.description = ''
        self.time_played = 0
        self.kills = 0
        self.kills_per_minute = 0.00
        self.kills_per_hour = 0.00
        self.kills_per_empire = {}
        self.score = 0
        self.score_per_minute = 0.00
        self.score_per_hour = 0.00
        self.fire_count = 0
        self.hit_count = 0
        self.accuracy_percentage = 0.00
        self.headshots = 0
        self.damage_given = 0
        self.damage_given_per_faction = {}
        self.damage_taken = 0
        self.damage_taken_per_faction = {}