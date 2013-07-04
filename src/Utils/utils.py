'''
Created on Jul 4, 2013

@author: bbetts
'''
from datetime import timedelta
from src.api import do_request
    
def comma_thousands(number):
    try:
        value = format(int(number),",d")
        return value
    except:
        return "Bad Data"
    

def round_to_two_decimal(number):
    return "{:,.2f}".format(number)
    
def get_playtime(time_played):
    return str(timedelta(minutes=time_played))

def to_string(data):
    return str(data)

def get_faction(faction_id):
    url_return = do_request("faction/%s"%faction_id)
    return url_return["faction_list"][0]["name"]["en"]

def get_server(world_id):
    url_return = do_request("world/?world_id=%s" %world_id)
    return url_return["world_list"][0]["name"]["en"]

def calculate_total_certs(spent_certs,available_certs):
    return int(spent_certs) + int(available_certs)

def calculate_per_hour(stat,time_played):
    hours_played = float(time_played) / 60
    return float(stat) / hours_played

def calculate_per_minute(stat,time_played):
    return float(stat) / float(time_played)
    