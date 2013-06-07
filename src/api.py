'''
Created on Jun 6, 2013

@author: Brendan Betts
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