# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jul 13 21:20:28 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 612)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 621, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_name = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_name.sizePolicy().hasHeightForWidth())
        self.txt_name.setSizePolicy(sizePolicy)
        self.txt_name.setMaxLength(200)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 2, 0, 1, 1)
        self.lbl_txt_name = QtGui.QLabel(self.gridLayoutWidget)
        self.lbl_txt_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbl_txt_name.setObjectName("lbl_txt_name")
        self.gridLayout.addWidget(self.lbl_txt_name, 0, 0, 1, 1)
        self.btn_search = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout.addWidget(self.btn_search, 2, 1, 1, 1)
        self.btn_clear = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 2, 2, 1, 1)
        self.tab_character = QtGui.QTabWidget(self.centralwidget)
        self.tab_character.setGeometry(QtCore.QRect(10, 80, 621, 501))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_character.sizePolicy().hasHeightForWidth())
        self.tab_character.setSizePolicy(sizePolicy)
        self.tab_character.setTabPosition(QtGui.QTabWidget.North)
        self.tab_character.setTabShape(QtGui.QTabWidget.Rounded)
        self.tab_character.setObjectName("tab_character")
        self.tab_character_info = QtGui.QWidget()
        self.tab_character_info.setObjectName("tab_character_info")
        self.gridLayoutWidget_3 = QtGui.QWidget(self.tab_character_info)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 611, 471))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_outfit_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_outfit_value.setText("")
        self.lbl_outfit_value.setObjectName("lbl_outfit_value")
        self.gridLayout_3.addWidget(self.lbl_outfit_value, 5, 1, 1, 1)
        self.lbl_facility_captured_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_facility_captured_value.setText("")
        self.lbl_facility_captured_value.setObjectName("lbl_facility_captured_value")
        self.gridLayout_3.addWidget(self.lbl_facility_captured_value, 0, 5, 1, 1)
        self.lbl_sph_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_sph_value.setText("")
        self.lbl_sph_value.setObjectName("lbl_sph_value")
        self.gridLayout_3.addWidget(self.lbl_sph_value, 6, 5, 1, 1)
        self.lbl_gifted_certs = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_gifted_certs.setObjectName("lbl_gifted_certs")
        self.gridLayout_3.addWidget(self.lbl_gifted_certs, 2, 2, 1, 1)
        self.lbl_name = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout_3.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.lbl_name_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_name_value.setText("")
        self.lbl_name_value.setObjectName("lbl_name_value")
        self.gridLayout_3.addWidget(self.lbl_name_value, 0, 1, 1, 1)
        self.lbl_total_certs_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_total_certs_value.setText("")
        self.lbl_total_certs_value.setObjectName("lbl_total_certs_value")
        self.gridLayout_3.addWidget(self.lbl_total_certs_value, 0, 3, 1, 1)
        self.lbl_faction_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_faction_value.setText("")
        self.lbl_faction_value.setObjectName("lbl_faction_value")
        self.gridLayout_3.addWidget(self.lbl_faction_value, 1, 1, 1, 1)
        self.lbl_faction = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_faction.setObjectName("lbl_faction")
        self.gridLayout_3.addWidget(self.lbl_faction, 1, 0, 1, 1)
        self.lbl_server = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_server.setObjectName("lbl_server")
        self.gridLayout_3.addWidget(self.lbl_server, 2, 0, 1, 1)
        self.lbl_percent_to_next_rank_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_percent_to_next_rank_value.setText("")
        self.lbl_percent_to_next_rank_value.setObjectName("lbl_percent_to_next_rank_value")
        self.gridLayout_3.addWidget(self.lbl_percent_to_next_rank_value, 4, 1, 1, 1)
        self.lbl_cph = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_cph.setObjectName("lbl_cph")
        self.gridLayout_3.addWidget(self.lbl_cph, 7, 2, 1, 1)
        self.lbl_facility_captured = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_facility_captured.setObjectName("lbl_facility_captured")
        self.gridLayout_3.addWidget(self.lbl_facility_captured, 0, 4, 1, 1)
        self.lbl_facility_defended_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_facility_defended_value.setText("")
        self.lbl_facility_defended_value.setObjectName("lbl_facility_defended_value")
        self.gridLayout_3.addWidget(self.lbl_facility_defended_value, 1, 5, 1, 1)
        self.lbl_earned_certs = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_earned_certs.setObjectName("lbl_earned_certs")
        self.gridLayout_3.addWidget(self.lbl_earned_certs, 1, 2, 1, 1)
        self.lbl_spm_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_spm_value.setText("")
        self.lbl_spm_value.setObjectName("lbl_spm_value")
        self.gridLayout_3.addWidget(self.lbl_spm_value, 5, 5, 1, 1)
        self.lbl_server_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_server_value.setText("")
        self.lbl_server_value.setObjectName("lbl_server_value")
        self.gridLayout_3.addWidget(self.lbl_server_value, 2, 1, 1, 1)
        self.lbl_timeplayed_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_timeplayed_value.setText("")
        self.lbl_timeplayed_value.setObjectName("lbl_timeplayed_value")
        self.gridLayout_3.addWidget(self.lbl_timeplayed_value, 6, 1, 1, 1)
        self.lbl_total_certs = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_total_certs.setObjectName("lbl_total_certs")
        self.gridLayout_3.addWidget(self.lbl_total_certs, 0, 2, 1, 1)
        self.lbl_faciliy_defended = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_faciliy_defended.setObjectName("lbl_faciliy_defended")
        self.gridLayout_3.addWidget(self.lbl_faciliy_defended, 1, 4, 1, 1)
        self.lbl_rank_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_rank_value.setText("")
        self.lbl_rank_value.setObjectName("lbl_rank_value")
        self.gridLayout_3.addWidget(self.lbl_rank_value, 3, 1, 1, 1)
        self.lbl_timeplayed = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_timeplayed.setObjectName("lbl_timeplayed")
        self.gridLayout_3.addWidget(self.lbl_timeplayed, 6, 0, 1, 1)
        self.lbl_percent_to_next_rank = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_percent_to_next_rank.setObjectName("lbl_percent_to_next_rank")
        self.gridLayout_3.addWidget(self.lbl_percent_to_next_rank, 4, 0, 1, 1)
        self.lbl_spent_certs = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_spent_certs.setObjectName("lbl_spent_certs")
        self.gridLayout_3.addWidget(self.lbl_spent_certs, 3, 2, 1, 1)
        self.lbl_earned_certs_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_earned_certs_value.setText("")
        self.lbl_earned_certs_value.setObjectName("lbl_earned_certs_value")
        self.gridLayout_3.addWidget(self.lbl_earned_certs_value, 1, 3, 1, 1)
        self.lbl_ribbons_earned = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_ribbons_earned.setObjectName("lbl_ribbons_earned")
        self.gridLayout_3.addWidget(self.lbl_ribbons_earned, 2, 4, 1, 1)
        self.lbl_percent_to_next_cert_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_percent_to_next_cert_value.setText("")
        self.lbl_percent_to_next_cert_value.setObjectName("lbl_percent_to_next_cert_value")
        self.gridLayout_3.addWidget(self.lbl_percent_to_next_cert_value, 5, 3, 1, 1)
        self.lbl_ribbons_earned_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_ribbons_earned_value.setText("")
        self.lbl_ribbons_earned_value.setObjectName("lbl_ribbons_earned_value")
        self.gridLayout_3.addWidget(self.lbl_ribbons_earned_value, 2, 5, 1, 1)
        self.lbl_available_certs_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_available_certs_value.setText("")
        self.lbl_available_certs_value.setObjectName("lbl_available_certs_value")
        self.gridLayout_3.addWidget(self.lbl_available_certs_value, 4, 3, 1, 1)
        self.lbl_medals_earned = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_medals_earned.setObjectName("lbl_medals_earned")
        self.gridLayout_3.addWidget(self.lbl_medals_earned, 3, 4, 1, 1)
        self.lbl_rank = QtGui.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_rank.sizePolicy().hasHeightForWidth())
        self.lbl_rank.setSizePolicy(sizePolicy)
        self.lbl_rank.setObjectName("lbl_rank")
        self.gridLayout_3.addWidget(self.lbl_rank, 3, 0, 1, 1)
        self.lbl_outfit = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_outfit.setObjectName("lbl_outfit")
        self.gridLayout_3.addWidget(self.lbl_outfit, 5, 0, 1, 1)
        self.lbl_available_certs = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_available_certs.setObjectName("lbl_available_certs")
        self.gridLayout_3.addWidget(self.lbl_available_certs, 4, 2, 1, 1)
        self.lbl_spent_certs_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_spent_certs_value.setText("")
        self.lbl_spent_certs_value.setObjectName("lbl_spent_certs_value")
        self.gridLayout_3.addWidget(self.lbl_spent_certs_value, 3, 3, 1, 1)
        self.lbl_cpm = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_cpm.setObjectName("lbl_cpm")
        self.gridLayout_3.addWidget(self.lbl_cpm, 6, 2, 1, 1)
        self.lbl_gifted_certs_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_gifted_certs_value.setText("")
        self.lbl_gifted_certs_value.setObjectName("lbl_gifted_certs_value")
        self.gridLayout_3.addWidget(self.lbl_gifted_certs_value, 2, 3, 1, 1)
        self.lbl_cpm_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_cpm_value.setText("")
        self.lbl_cpm_value.setObjectName("lbl_cpm_value")
        self.gridLayout_3.addWidget(self.lbl_cpm_value, 6, 3, 1, 1)
        self.lbl_percent_to_next_cert = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_percent_to_next_cert.setObjectName("lbl_percent_to_next_cert")
        self.gridLayout_3.addWidget(self.lbl_percent_to_next_cert, 5, 2, 1, 1)
        self.lbl_cph_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_cph_value.setText("")
        self.lbl_cph_value.setObjectName("lbl_cph_value")
        self.gridLayout_3.addWidget(self.lbl_cph_value, 7, 3, 1, 1)
        self.lbl_score_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_score_value.setText("")
        self.lbl_score_value.setObjectName("lbl_score_value")
        self.gridLayout_3.addWidget(self.lbl_score_value, 4, 5, 1, 1)
        self.lbl_medals_earned_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_medals_earned_value.setText("")
        self.lbl_medals_earned_value.setObjectName("lbl_medals_earned_value")
        self.gridLayout_3.addWidget(self.lbl_medals_earned_value, 3, 5, 1, 1)
        self.lbl_score = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_score.setObjectName("lbl_score")
        self.gridLayout_3.addWidget(self.lbl_score, 4, 4, 1, 1)
        self.lbl_spm = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_spm.setObjectName("lbl_spm")
        self.gridLayout_3.addWidget(self.lbl_spm, 5, 4, 1, 1)
        self.lbl_sph = QtGui.QLabel(self.gridLayoutWidget_3)
        self.lbl_sph.setObjectName("lbl_sph")
        self.gridLayout_3.addWidget(self.lbl_sph, 6, 4, 1, 1)
        self.tab_character.addTab(self.tab_character_info, "")
        self.tab_KDR = QtGui.QWidget()
        self.tab_KDR.setObjectName("tab_KDR")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_KDR)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 611, 471))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_kills_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kills_value.setText("")
        self.lbl_kills_value.setObjectName("lbl_kills_value")
        self.gridLayout_2.addWidget(self.lbl_kills_value, 0, 1, 1, 1)
        self.lbl_kills = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kills.setObjectName("lbl_kills")
        self.gridLayout_2.addWidget(self.lbl_kills, 0, 0, 1, 1)
        self.lbl_dph = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_dph.setObjectName("lbl_dph")
        self.gridLayout_2.addWidget(self.lbl_dph, 2, 2, 1, 1)
        self.lbl_deaths = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_deaths.setObjectName("lbl_deaths")
        self.gridLayout_2.addWidget(self.lbl_deaths, 0, 2, 1, 1)
        self.lbl_dph_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_dph_value.setText("")
        self.lbl_dph_value.setObjectName("lbl_dph_value")
        self.gridLayout_2.addWidget(self.lbl_dph_value, 2, 3, 1, 1)
        self.lbl_kph = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kph.setObjectName("lbl_kph")
        self.gridLayout_2.addWidget(self.lbl_kph, 2, 0, 1, 1)
        self.lbl_kpm_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kpm_value.setText("")
        self.lbl_kpm_value.setObjectName("lbl_kpm_value")
        self.gridLayout_2.addWidget(self.lbl_kpm_value, 1, 1, 1, 1)
        self.lbl_kph_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kph_value.setText("")
        self.lbl_kph_value.setObjectName("lbl_kph_value")
        self.gridLayout_2.addWidget(self.lbl_kph_value, 2, 1, 1, 1)
        self.lbl_death_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_death_value.setText("")
        self.lbl_death_value.setObjectName("lbl_death_value")
        self.gridLayout_2.addWidget(self.lbl_death_value, 0, 3, 1, 1)
        self.lbl_kdr = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kdr.setObjectName("lbl_kdr")
        self.gridLayout_2.addWidget(self.lbl_kdr, 6, 2, 1, 1)
        self.lbl_dpm = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_dpm.setObjectName("lbl_dpm")
        self.gridLayout_2.addWidget(self.lbl_dpm, 1, 2, 1, 1)
        self.lbl_kpm = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kpm.setObjectName("lbl_kpm")
        self.gridLayout_2.addWidget(self.lbl_kpm, 1, 0, 1, 1)
        self.lbl_TR_kills = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_kills.setObjectName("lbl_TR_kills")
        self.gridLayout_2.addWidget(self.lbl_TR_kills, 4, 0, 1, 1)
        self.lbl_NC_kills = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_kills.setObjectName("lbl_NC_kills")
        self.gridLayout_2.addWidget(self.lbl_NC_kills, 3, 0, 1, 1)
        self.lbl_dpm_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_dpm_value.setText("")
        self.lbl_dpm_value.setObjectName("lbl_dpm_value")
        self.gridLayout_2.addWidget(self.lbl_dpm_value, 1, 3, 1, 1)
        self.lbl_assists = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_assists.setObjectName("lbl_assists")
        self.gridLayout_2.addWidget(self.lbl_assists, 6, 0, 1, 1)
        self.lbl_VS_kills = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_kills.setObjectName("lbl_VS_kills")
        self.gridLayout_2.addWidget(self.lbl_VS_kills, 5, 0, 1, 1)
        self.lbl_NC_deaths = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_deaths.setObjectName("lbl_NC_deaths")
        self.gridLayout_2.addWidget(self.lbl_NC_deaths, 3, 2, 1, 1)
        self.lbl_TR_deaths = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_deaths.setObjectName("lbl_TR_deaths")
        self.gridLayout_2.addWidget(self.lbl_TR_deaths, 4, 2, 1, 1)
        self.lbl_VS_deaths = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_deaths.setObjectName("lbl_VS_deaths")
        self.gridLayout_2.addWidget(self.lbl_VS_deaths, 5, 2, 1, 1)
        self.lbl_NC_kills_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_kills_value.setText("")
        self.lbl_NC_kills_value.setObjectName("lbl_NC_kills_value")
        self.gridLayout_2.addWidget(self.lbl_NC_kills_value, 3, 1, 1, 1)
        self.lbl_TR_kills_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_kills_value.setText("")
        self.lbl_TR_kills_value.setObjectName("lbl_TR_kills_value")
        self.gridLayout_2.addWidget(self.lbl_TR_kills_value, 4, 1, 1, 1)
        self.lbl_VS_kills_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_kills_value.setText("")
        self.lbl_VS_kills_value.setObjectName("lbl_VS_kills_value")
        self.gridLayout_2.addWidget(self.lbl_VS_kills_value, 5, 1, 1, 1)
        self.lbl_NC_deaths_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_deaths_value.setText("")
        self.lbl_NC_deaths_value.setObjectName("lbl_NC_deaths_value")
        self.gridLayout_2.addWidget(self.lbl_NC_deaths_value, 3, 3, 1, 1)
        self.lbl_TR_deaths_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_deaths_value.setText("")
        self.lbl_TR_deaths_value.setObjectName("lbl_TR_deaths_value")
        self.gridLayout_2.addWidget(self.lbl_TR_deaths_value, 4, 3, 1, 1)
        self.lbl_VS_deaths_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_deaths_value.setText("")
        self.lbl_VS_deaths_value.setObjectName("lbl_VS_deaths_value")
        self.gridLayout_2.addWidget(self.lbl_VS_deaths_value, 5, 3, 1, 1)
        self.lbl_assists_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_assists_value.setText("")
        self.lbl_assists_value.setObjectName("lbl_assists_value")
        self.gridLayout_2.addWidget(self.lbl_assists_value, 6, 1, 1, 1)
        self.lbl_kdr_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_kdr_value.setText("")
        self.lbl_kdr_value.setObjectName("lbl_kdr_value")
        self.gridLayout_2.addWidget(self.lbl_kdr_value, 6, 3, 1, 1)
        self.lbl_VS_dominations_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_dominations_value.setText("")
        self.lbl_VS_dominations_value.setObjectName("lbl_VS_dominations_value")
        self.gridLayout_2.addWidget(self.lbl_VS_dominations_value, 7, 5, 1, 1)
        self.lbl_VS_dominations = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_dominations.setObjectName("lbl_VS_dominations")
        self.gridLayout_2.addWidget(self.lbl_VS_dominations, 7, 4, 1, 1)
        self.lbl_TR_dominations = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_dominations.setObjectName("lbl_TR_dominations")
        self.gridLayout_2.addWidget(self.lbl_TR_dominations, 6, 4, 1, 1)
        self.lbl_NC_domination = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_domination.setObjectName("lbl_NC_domination")
        self.gridLayout_2.addWidget(self.lbl_NC_domination, 5, 4, 1, 1)
        self.lbl_TR_dominations_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_dominations_value.setText("")
        self.lbl_TR_dominations_value.setObjectName("lbl_TR_dominations_value")
        self.gridLayout_2.addWidget(self.lbl_TR_dominations_value, 6, 5, 1, 1)
        self.lbl_NC_domination_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_domination_value.setText("")
        self.lbl_NC_domination_value.setObjectName("lbl_NC_domination_value")
        self.gridLayout_2.addWidget(self.lbl_NC_domination_value, 5, 5, 1, 1)
        self.lbl_TR_revenge = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_revenge.setObjectName("lbl_TR_revenge")
        self.gridLayout_2.addWidget(self.lbl_TR_revenge, 3, 4, 1, 1)
        self.lbl_NC_revenge = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_revenge.setObjectName("lbl_NC_revenge")
        self.gridLayout_2.addWidget(self.lbl_NC_revenge, 2, 4, 1, 1)
        self.lbl_NC_revenge_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_NC_revenge_value.setText("")
        self.lbl_NC_revenge_value.setObjectName("lbl_NC_revenge_value")
        self.gridLayout_2.addWidget(self.lbl_NC_revenge_value, 2, 5, 1, 1)
        self.lbl_TR_revenge_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_TR_revenge_value.setText("")
        self.lbl_TR_revenge_value.setObjectName("lbl_TR_revenge_value")
        self.gridLayout_2.addWidget(self.lbl_TR_revenge_value, 3, 5, 1, 1)
        self.lbl_VS_revenge = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_revenge.setObjectName("lbl_VS_revenge")
        self.gridLayout_2.addWidget(self.lbl_VS_revenge, 4, 4, 1, 1)
        self.lbl_VS_revenge_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_VS_revenge_value.setText("")
        self.lbl_VS_revenge_value.setObjectName("lbl_VS_revenge_value")
        self.gridLayout_2.addWidget(self.lbl_VS_revenge_value, 4, 5, 1, 1)
        self.lbl_revenge = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_revenge.setObjectName("lbl_revenge")
        self.gridLayout_2.addWidget(self.lbl_revenge, 0, 4, 1, 1)
        self.lbl_revenge_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_revenge_value.setText("")
        self.lbl_revenge_value.setObjectName("lbl_revenge_value")
        self.gridLayout_2.addWidget(self.lbl_revenge_value, 0, 5, 1, 1)
        self.lbl_dominations = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_dominations.setObjectName("lbl_dominations")
        self.gridLayout_2.addWidget(self.lbl_dominations, 1, 4, 1, 1)
        self.lbl_dominations_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lbl_dominations_value.setText("")
        self.lbl_dominations_value.setObjectName("lbl_dominations_value")
        self.gridLayout_2.addWidget(self.lbl_dominations_value, 1, 5, 1, 1)
        self.tab_character.addTab(self.tab_KDR, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtGui.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.ExportCSV = QtGui.QAction(MainWindow)
        self.ExportCSV.setObjectName("ExportCSV")
        self.actionText_File = QtGui.QAction(MainWindow)
        self.actionText_File.setObjectName("actionText_File")
        self.menuFile.addAction(self.actionQuit)
        self.menuExport.addAction(self.ExportCSV)
        self.menuExport.addAction(self.actionText_File)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_character.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.txt_name.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Thoross", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_txt_name.setText(QtGui.QApplication.translate("MainWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_gifted_certs.setText(QtGui.QApplication.translate("MainWindow", "Certs Gifted:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_name.setText(QtGui.QApplication.translate("MainWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_faction.setText(QtGui.QApplication.translate("MainWindow", "Faction:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_server.setText(QtGui.QApplication.translate("MainWindow", "Server:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_cph.setText(QtGui.QApplication.translate("MainWindow", "Certs Per Hour:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_facility_captured.setText(QtGui.QApplication.translate("MainWindow", "Facilities Captured:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_earned_certs.setText(QtGui.QApplication.translate("MainWindow", "Certs Earned:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_total_certs.setText(QtGui.QApplication.translate("MainWindow", "Total Certs \n"
"Accumulated:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_faciliy_defended.setText(QtGui.QApplication.translate("MainWindow", "Facilities Defended:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_timeplayed.setText(QtGui.QApplication.translate("MainWindow", "Time Played:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_percent_to_next_rank.setText(QtGui.QApplication.translate("MainWindow", "Percent to \n"
"Next Rank:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_spent_certs.setText(QtGui.QApplication.translate("MainWindow", "Certs Spent:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_ribbons_earned.setText(QtGui.QApplication.translate("MainWindow", "Ribbons Earned:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_medals_earned.setText(QtGui.QApplication.translate("MainWindow", "Medals Earned:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_rank.setText(QtGui.QApplication.translate("MainWindow", "Rank:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_outfit.setText(QtGui.QApplication.translate("MainWindow", "Outfit:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_available_certs.setText(QtGui.QApplication.translate("MainWindow", "Available Certs:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_cpm.setText(QtGui.QApplication.translate("MainWindow", "Certs Per Minute:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_percent_to_next_cert.setText(QtGui.QApplication.translate("MainWindow", "Percent to \n"
"Next Cert:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_score.setText(QtGui.QApplication.translate("MainWindow", "Score:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_spm.setText(QtGui.QApplication.translate("MainWindow", "Score Per Minute:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_sph.setText(QtGui.QApplication.translate("MainWindow", "Score Per Hour:", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_character.setTabText(self.tab_character.indexOf(self.tab_character_info), QtGui.QApplication.translate("MainWindow", "Character Info", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_kills.setText(QtGui.QApplication.translate("MainWindow", "Kills:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_dph.setText(QtGui.QApplication.translate("MainWindow", "Deaths \n"
"Per Hour:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_deaths.setText(QtGui.QApplication.translate("MainWindow", "Deaths:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_kph.setText(QtGui.QApplication.translate("MainWindow", "Kills Per Hour:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_kdr.setText(QtGui.QApplication.translate("MainWindow", "Kill Death \n"
"Ratio:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_dpm.setText(QtGui.QApplication.translate("MainWindow", "Deaths \n"
"Per Minute:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_kpm.setText(QtGui.QApplication.translate("MainWindow", "Kills Per Minute:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_TR_kills.setText(QtGui.QApplication.translate("MainWindow", "TR Kills:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_NC_kills.setText(QtGui.QApplication.translate("MainWindow", "NC Kills:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_assists.setText(QtGui.QApplication.translate("MainWindow", "Assists:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_VS_kills.setText(QtGui.QApplication.translate("MainWindow", "VS Kills:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_NC_deaths.setText(QtGui.QApplication.translate("MainWindow", "NC Deaths:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_TR_deaths.setText(QtGui.QApplication.translate("MainWindow", "TR Deaths:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_VS_deaths.setText(QtGui.QApplication.translate("MainWindow", "VS Deaths:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_VS_dominations.setText(QtGui.QApplication.translate("MainWindow", "VS Dominations:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_TR_dominations.setText(QtGui.QApplication.translate("MainWindow", "TR Dominations:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_NC_domination.setText(QtGui.QApplication.translate("MainWindow", "NC Dominations:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_TR_revenge.setText(QtGui.QApplication.translate("MainWindow", "TR Revenge Count:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_NC_revenge.setText(QtGui.QApplication.translate("MainWindow", "NC Revenge Count:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_VS_revenge.setText(QtGui.QApplication.translate("MainWindow", "VS Revenge Count:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_revenge.setText(QtGui.QApplication.translate("MainWindow", "Total Revenge \n"
"Count:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_dominations.setText(QtGui.QApplication.translate("MainWindow", "Total Dominations:", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_character.setTabText(self.tab_character.indexOf(self.tab_KDR), QtGui.QApplication.translate("MainWindow", "Kills and Deaths", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.ExportCSV.setText(QtGui.QApplication.translate("MainWindow", "CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionText_File.setText(QtGui.QApplication.translate("MainWindow", "Text File", None, QtGui.QApplication.UnicodeUTF8))

