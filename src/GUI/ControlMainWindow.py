'''
Created on Jul 2, 2013

@author: bbetts
'''
from PySide.QtGui import QMainWindow
from src.GUI.mainwindow import Ui_MainWindow
from src.controllers.CharacterController import CharacterController
from datetime import timedelta
from src.Utils.utils import *
import sys

class ControlMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(ControlMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_search.clicked.connect(self.on_search)
        self.ui.txt_name.returnPressed.connect(self.on_search)
        self.ui.btn_clear.clicked.connect(self.on_clear)
        self.ui.actionText_File.triggered.connect(self.export_to_file)
        self.ui.actionQuit.triggered.connect(sys.exit)
        
    def export_to_file(self):
        controller = CharacterController()
        player = controller.get_character(self.ui.lbl_name_value.text())
        
        
    def on_search(self):
        controller = CharacterController()
        if self.ui.txt_name.text() != "":
            name = self.ui.txt_name.text()
            player = controller.get_character(name)
            self.set_character_info(player)
            self.set_kills_info(player)
            
    def on_clear(self):
        self.ui.txt_name.clear()
        self.ui.txt_name.hasFocus()
        self.clear_character_info_tab()   
        self.clear_kills_info_tab()     
        
    def set_character_info(self,player):    
        self.ui.lbl_name_value.setText(player.name)
        self.ui.lbl_rank_value.setText(player.level)
        self.ui.lbl_score_value.setText(comma_thousands(player.score))
        self.ui.lbl_timeplayed_value.setText(get_playtime(int(player.time_played)))
        self.ui.lbl_spm_value.setText(round_to_two_decimal(player.score_per_minute))
        self.ui.lbl_sph_value.setText(round_to_two_decimal(player.score_per_hour))
        self.ui.lbl_faction_value.setText(player.faction)
        self.ui.lbl_earned_certs_value.setText(comma_thousands(player.earned_certs))
        self.ui.lbl_available_certs_value.setText(comma_thousands(player.available_certs))
        self.ui.lbl_total_certs_value.setText(comma_thousands(player.total_certs))
        self.ui.lbl_spent_certs_value.setText(comma_thousands(player.spent_certs))
        self.ui.lbl_gifted_certs_value.setText(comma_thousands(player.gifted_certs))
        self.ui.lbl_cpm_value.setText(round_to_two_decimal(player.certs_per_minute))
        self.ui.lbl_cph_value.setText(round_to_two_decimal(player.certs_per_hour))
        self.ui.lbl_percent_to_next_cert_value.setText(round_to_two_decimal(float(player.percentage_to_next)*100)+"%")
        self.ui.lbl_server_value.setText(player.server)
        self.ui.lbl_outfit_value.setText(player.outfit)
        self.ui.lbl_percent_to_next_rank_value.setText(player.percentage_to_next_level+"%")
        self.ui.lbl_facility_defended_value.setText(comma_thousands(player.facilities_defended))
        self.ui.lbl_facility_captured_value.setText(comma_thousands(player.facilities_captured))
        self.ui.lbl_medals_earned_value.setText(comma_thousands(player.medals))
        self.ui.lbl_ribbons_earned_value.setText(comma_thousands(player.ribbons))
        
    def set_kills_info(self,player):
        self.ui.lbl_kills_value.setText(comma_thousands(player.kills))
        self.ui.lbl_kph_value.setText(round_to_two_decimal(player.kills_per_hour))
        self.ui.lbl_kpm_value.setText(round_to_two_decimal(player.kills_per_minute))
        self.ui.lbl_death_value.setText(comma_thousands(player.deaths))
        self.ui.lbl_dpm_value.setText(round_to_two_decimal(player.deaths_per_minute))
        self.ui.lbl_dph_value.setText(round_to_two_decimal(player.deaths_per_hour))
        self.ui.lbl_kdr_value.setText(round_to_two_decimal(player.kill_death_ratio))
        self.ui.lbl_assists_value.setText(comma_thousands(player.assists))
        self.display_faction_stats(player)
        
    def clear_character_info_tab(self):
        self.ui.lbl_name_value.clear()
        self.ui.lbl_available_certs_value.clear()
        self.ui.lbl_earned_certs_value.clear()
        self.ui.lbl_rank_value.clear()
        self.ui.lbl_cph_value.clear()
        self.ui.lbl_spent_certs_value.clear()
        self.ui.lbl_total_certs_value.clear()
        self.ui.lbl_server_value.clear()
        self.ui.lbl_faction_value.clear()
        self.ui.lbl_timeplayed_value.clear()
        self.ui.lbl_gifted_certs_value.clear()
        self.ui.lbl_percent_to_next_cert_value.clear()
        self.ui.lbl_cpm_value.clear()
        self.ui.lbl_outfit_value.clear()
        self.ui.lbl_percent_to_next_rank_value.clear()
        self.ui.lbl_score_value.clear()
        self.ui.lbl_spm_value.clear()
        self.ui.lbl_sph_value.clear()
        self.ui.lbl_facility_defended_value.clear()
        self.ui.lbl_facility_captured_value.clear()
        self.ui.lbl_medals_earned_value.clear()
        self.ui.lbl_ribbons_earned_value.clear()
    
    def clear_kills_info_tab(self):
        self.ui.lbl_kills_value.clear()
        self.ui.lbl_kph_value.clear()
        self.ui.lbl_kpm_value.clear()
        self.ui.lbl_death_value.clear()
        self.ui.lbl_dpm_value.clear()
        self.ui.lbl_dph_value.clear()
        self.ui.lbl_kdr_value.clear()
        
    def display_faction_stats(self,player):
        if player.faction == "New Conglomerate":
            self.ui.lbl_NC_kills.setVisible(False)
            self.ui.lbl_NC_kills_value.setVisible(False)
            self.ui.lbl_NC_deaths.setVisible(False)
            self.ui.lbl_NC_deaths_value.setVisible(False)
            self.ui.lbl_TR_kills_value.setText(comma_thousands(player.kills_per_faction["TR"]))
            self.ui.lbl_VS_kills_value.setText(comma_thousands(player.kills_per_faction["VS"]))
               
        elif player.faction == "Terran Republic":
            self.ui.lbl_TR_kills.setVisible(False)
            self.ui.lbl_TR_kills_value.setVisible(False)
            self.ui.lbl_TR_deaths_value.setVisible(False)
            self.ui.lbl_TR_deaths.setVisible(False)
            self.ui.lbl_VS_kills_value.setText(comma_thousands(player.kills_per_faction["VS"]))
            self.ui.lbl_NC_kills_value.setText(comma_thousands(player.kills_per_faction["NC"]))
            
        else:
            self.ui.lbl_VS_kills.setVisible(False)
            self.ui.lbl_VS_kills_value.setVisible(False)
            self.ui.lbl_VS_deaths.setVisible(False)
            self.ui.lbl_VS_deaths_value.setVisible(False)
            self.ui.lbl_TR_kills_value.setText(comma_thousands(player.kills_per_faction["TR"]))
            self.ui.lbl_NC_kills_value.setText(comma_thousands(player.kills_per_faction["NC"]))
