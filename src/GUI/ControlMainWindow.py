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
        self.ui.txt_name.returnPressed.connect(self.on_search)
        
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
        '''self.ui.lbl_score_value.setText(self.comma_thousands(player.score))'''
        self.ui.lbl_timeplayed_value.setText(self.get_playtime(int(player.time_played)))
        '''self.ui.lbl_spm_value.setText(self.round_to_two_decimal(player.score_per_minute))
        self.ui.lbl_sph_value.setText(self.round_to_two_decimal(player.score_per_hour))'''
        self.ui.lbl_faction_value.setText(player.faction)
        self.ui.lbl_certs_value.setText(self.comma_thousands(player.earned_certs))
        self.ui.lbl_available_certs_value.setText(self.comma_thousands(player.available_certs))
        self.ui.lbl_total_certs_value.setText(self.comma_thousands(player.total_certs))
        self.ui.lbl_spent_certs_value.setText(self.comma_thousands(player.spent_certs))
        self.ui.lbl_gifted_certs_value.setText(self.comma_thousands(player.gifted_certs))
        self.ui.lbl_cpm_value.setText(self.round_to_two_decimal(player.certs_per_minute))
        self.ui.lbl_cph_value.setText(self.round_to_two_decimal(player.certs_per_hour))
        self.ui.lbl_percentage_to_next_value.setText("%"+ self.round_to_two_decimal(float(player.percentage_to_next)*100))
        self.ui.lbl_server_value.setText(player.server)
        
    def comma_thousands(self,number):    
        return format(int(number),",d")
    
    def round_to_two_decimal(self,number):
        return "%.2f" %float(number)
        
    def get_playtime(self,time_played):
        return str(timedelta(minutes=time_played))