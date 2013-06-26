'''
Created on Jun 25, 2013

@author: bbetts
'''
import pygtk
pygtk.require('2.0')
import gtk
from src.controllers.CharacterController import CharacterController
from datetime import timedelta

class appFrame:
    
    def callback(self,widget,data=None):
        name = self.name_entry.get_text()
        characterController = CharacterController()
        player = characterController.get_character(name)
        self.make_fields_visible(player)
               
    def delete_event(self,widget,event,data=None):
        return False
    
    def destroy(self,widget,data=None):
        gtk.main_quit()
        
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event",self.delete_event)
        self.window.connect("destroy",self.destroy)
        
        self.window.set_border_width(10)
        self.table = gtk.Table(10,2,False)
        self.table.set_col_spacing(1,2)
        self.window.add(self.table)
        
        self.name_entry = gtk.Entry(max=0)
        self.table.attach(self.name_entry,0,3,0,1)
        self.name_entry.show()        
        
        self.button2 = gtk.Button("Search")
        self.button2.connect("clicked",self.callback,None)
        self.table.attach(self.button2,0,3,1,2)
        self.button2.show()
        
        self.id_label = gtk.Label("ID:")
        self.id_label.set_visible(False)
        self.table.attach(self.id_label,0,1,2,3)
                
        self.id_value = gtk.Label("")
        self.id_value.set_visible(False)
        self.table.attach(self.id_value,1,2,2,3)
                
        self.name_label = gtk.Label("Name:")
        self.name_label.set_visible(False)
        self.table.attach(self.name_label,0,1,3,4)
                
        self.name_value_label = gtk.Label("")
        self.name_value_label.set_visible(False)
        self.table.attach(self.name_value_label,1,2,3,4)
                
        self.score_label = gtk.Label("Score:")
        self.score_label.set_visible(False)
        self.table.attach(self.score_label,0,1,4,5)
                
        self.score_value = gtk.Label("")
        self.score_value.set_visible(False)
        self.table.attach(self.score_value,1,2,4,5)
        
        self.score_per_minute_label = gtk.Label("Score Per Minute")
        self.score_per_minute_label.set_visible(False)
        self.table.attach(self.score_per_minute_label,0,1,5,6)
        
        self.score_per_minute_value = gtk.Label("")
        self.score_per_minute_value.set_visible(False)
        self.table.attach(self.score_per_minute_value,1,2,5,6)
        
        self.score_per_hour_label = gtk.Label("Score Per Hour")
        self.score_per_hour_label.set_visible(False)
        self.table.attach(self.score_per_hour_label,0,1,6,7)
        
        self.score_per_hour_value = gtk.Label("")
        self.score_per_hour_value.set_visible(False)
        self.table.attach(self.score_per_hour_value,1,2,6,7)
        
        self.time_played_label = gtk.Label("Time Played:")
        self.time_played_label.set_visible(False)
        self.table.attach(self.time_played_label,0,1,7,8)
        
        self.time_played_value = gtk.Label("")
        self.time_played_value.set_visible(False)
        self.table.attach(self.time_played_value,1,2,7,8)
                
        self.table.show()
        self.window.show()
        
    def main(self):
        gtk.main()
        
    def make_fields_visible(self,player):
        self.id_label.set_visible(True)
        
        self.id_value.set_text(player.character_id)
        self.id_value.set_visible(True)
        
        self.name_label.set_visible(True)
        
        self.name_value_label.set_text(player.name)
        self.name_value_label.set_visible(True)
        
        self.score_label.set_visible(True)
        
        self.score_value.set_text(player.score)
        self.score_value.set_visible(True)
        
        self.score_per_minute_label.set_visible(True)
        
        self.score_per_minute_value.set_text("%.2f"%player.score_per_minute)
        self.score_per_minute_value.set_visible(True)
        
        self.score_per_hour_label.set_visible(True)
        
        self.score_per_hour_value.set_text("%.2f" %player.score_per_hour)
        self.score_per_hour_value.set_visible(True)
        
        self.time_played_label.set_visible(True)
        
        self.time_played_value.set_text(str(timedelta(seconds=int(player.time_played))))
        self.time_played_value.set_visible(True)
        
    def to_string(self,item):
        return str(item)