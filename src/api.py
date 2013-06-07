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

import requests

URL_ROOT = "http://census.soe.com/get/ps2-beta/"

def get_character_id_by_name(name):
    url = URL_ROOT + "character/?name.first_lower=%s&c:show=id" %(name)
    r = requests.get(url)
    obj = r.json()
    try:
        return obj["character_list"][0]["id"]
    except IndexError, e:
        return "None" 
    
def get_certs_by_id(charcter_id):
    url = URL_ROOT + "character/%s?c:show=certs" %(character_id)
    r = requests.get(url)
    obj = r.json()
    try:
        certs = {"certs_earned": obj["character_list"][0]["certs"]["currentpoints"],"percentage_to_next": obj["character_list"][0]["certs"]["percentagetonext"]}
        return certs
    except:
        return
    
if __name__ == "__main__":
    character_id = get_character_id_by_name("thoross")
    print "Character ID: %s" %(character_id)
    certs = get_certs_by_id(character_id)
    print "Certs Earned: %s \nPercentage to Next: %s" %(certs['certs_earned'],certs['percentage_to_next'])