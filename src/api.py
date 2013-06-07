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
from src.url import url

URL_ROOT = "http://census.soe.com/get/ps2-beta/"



def do_request(request_url):
    r = requests.get(request_url)
    return r.json()

def get_character_id_by_name(name):
    parameters = "character/?name.first_lower=%s&c:show=id" %(name)
    request_url = url(parameters)
    obj = do_request(request_url.full)
    try:
        return obj["character_list"][0]["id"]
    except IndexError, e:
        return "None" 
    
def get_certs_by_id(charcter_id):
    parameters = "character/%s?c:show=certs" %(character_id)
    request_url = url(parameters)
    obj = do_request(request_url.full)
    try:
        certs = {"certs_earned": obj["character_list"][0]["certs"]["currentpoints"],"percentage_to_next": obj["character_list"][0]["certs"]["percentagetonext"]}
        return certs
    except:
        return

def get_resources(character_id):
    request_url = url("character/%s?c:show=currency" %(character_id))
    obj = do_request(request_url.full)
    try:
        resources = {"aerospace":obj["character_list"][0]["currency"]["aerospace"], "infantry" :obj["character_list"][0]["currency"]["infantry"], "mechanized":obj["character_list"][0]["currency"]["mechanized"] }
        return resources
    except:
        return    
def get_experience(character_id):
    request_url = url("character/%s?c:show=experience" %(character_id))
    obj = do_request(request_url.full)
    try:
        experience = {"level" : obj["character_list"][0]["experience"][0]["rank"], "score" : obj["character_list"][0]["experience"][0]["score"]}
        return experience
    except:
        return
        
if __name__ == "__main__":
    character_id = get_character_id_by_name("sorter")
    print "Character ID: %s" %(character_id)
    certs = get_certs_by_id(character_id)
    print "Certs Earned: %s \nPercentage to Next: %s" %(certs['certs_earned'],certs['percentage_to_next'])
    resources = get_resources(character_id)
    print "Resources:\n  Aerospace: %s \n  Infantry: %s \n  Mechanized: %s" %(resources["aerospace"],resources["infantry"],resources["mechanized"])
    experience = get_experience(character_id)
    print "Experience: \n  Level: %s\n  Score: %s" %(experience["level"],experience["score"])
    