'''
Created on Jun 27, 2013

@author: bbetts
'''
import pygtk
pygtk.require("2.0")
import gtk
import os

class GTKGUI(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.builder = gtk.Builder()
        self.builder.add_from_file(os.path.realpath("GUI/PS2GUI.glade"))                                    
        dic = {"search_clicked":self.search_clicked,
               "clear_clicked":self.clear_clicked}
        self.builder.connect_signals(dic)
        
        
     
    
    def main(self):
        gtk.main()

    def search_clicked(self):
        pass
    
    def clear_clicked(self):
        pass