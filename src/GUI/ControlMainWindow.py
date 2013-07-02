'''
Created on Jul 2, 2013

@author: bbetts
'''
from PySide.QtGui import QMainWindow
from src.GUI.mainwindow import Ui_MainWindow
from src.controllers.CharacterController import CharacterController
from datetime import timedelta

class ControlMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(ControlMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_search.clicked.connect(self.on_search)
        
    def on_search(self):
        controller = CharacterController()
        if self.ui.txt_name.text() != "":
            name = self.ui.txt_name.text()
            player = controller.get_character(name)
            self.set_values(player)
    
    def set_values(self,player):
        self.ui.lbl_character_value.setText(player.character_id)
        self.ui.lbl_name_value.setText(player.name)
        self.ui.lbl_rank_value.setText(player.level)
        self.ui.lbl_score_value.setText(format(int(player.score),",d"))
        self.ui.lbl_timeplayed_value.setText(self.get_playtime(int(player.time_played)))
        self.ui.lbl_spm_value.setText("%.2f" % player.score_per_minute)
        self.ui.lbl_sph_value.setText("%.2f" % player.score_per_hour)
        self.ui.lbl_faction_value.setText(player.faction.upper())
        self.ui.lbl_certs_value.setText(format(int(player.certs),",d"))
        self.ui.lbl_cpm_value.setText("%.2f" % player.certs_per_minute)
        self.ui.lbl_cph_value.setText("%.2f" % player.certs_per_hour)
        self.ui.lbl_percentage_to_next_value.setText("%"+player.percentage_to_next)
        
    def get_playtime(self,time_played):
        return str(timedelta(seconds=time_played))