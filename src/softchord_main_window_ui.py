# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/softchord_main_window.ui'
#
# Created: Sat Jan 12 14:09:06 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1087, 809)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "softChord Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Songs in the current songbook:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.song_filter_ef = QtGui.QLineEdit(self.layoutWidget)
        self.song_filter_ef.setObjectName(_fromUtf8("song_filter_ef"))
        self.horizontalLayout_7.addWidget(self.song_filter_ef)
        self.clear_filter_button = QtGui.QToolButton(self.layoutWidget)
        self.clear_filter_button.setText(QtGui.QApplication.translate("MainWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_filter_button.setObjectName(_fromUtf8("clear_filter_button"))
        self.horizontalLayout_7.addWidget(self.clear_filter_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.songs_view = QtGui.QTableView(self.layoutWidget)
        self.songs_view.setMinimumSize(QtCore.QSize(100, 80))
        self.songs_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.songs_view.setObjectName(_fromUtf8("songs_view"))
        self.verticalLayout_3.addWidget(self.songs_view)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.new_song_button = QtGui.QPushButton(self.layoutWidget)
        self.new_song_button.setText(QtGui.QApplication.translate("MainWindow", "New Song", None, QtGui.QApplication.UnicodeUTF8))
        self.new_song_button.setObjectName(_fromUtf8("new_song_button"))
        self.horizontalLayout_2.addWidget(self.new_song_button)
        self.delete_song_button = QtGui.QPushButton(self.layoutWidget)
        self.delete_song_button.setText(QtGui.QApplication.translate("MainWindow", "Delete selected", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_song_button.setObjectName(_fromUtf8("delete_song_button"))
        self.horizontalLayout_2.addWidget(self.delete_song_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Current song:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.song_num_ef = QtGui.QLineEdit(self.layoutWidget1)
        self.song_num_ef.setMaximumSize(QtCore.QSize(50, 16777215))
        self.song_num_ef.setObjectName(_fromUtf8("song_num_ef"))
        self.horizontalLayout.addWidget(self.song_num_ef)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.song_title_ef = QtGui.QLineEdit(self.layoutWidget1)
        self.song_title_ef.setObjectName(_fromUtf8("song_title_ef"))
        self.horizontalLayout.addWidget(self.song_title_ef)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.song_key_menu = QtGui.QComboBox(self.layoutWidget1)
        self.song_key_menu.setMinimumSize(QtCore.QSize(100, 0))
        self.song_key_menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.song_key_menu.setObjectName(_fromUtf8("song_key_menu"))
        self.horizontalLayout_4.addWidget(self.song_key_menu)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Alternative key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.song_alt_key_menu = QtGui.QComboBox(self.layoutWidget1)
        self.song_alt_key_menu.setMinimumSize(QtCore.QSize(50, 0))
        self.song_alt_key_menu.setMaximumSize(QtCore.QSize(60, 16777215))
        self.song_alt_key_menu.setObjectName(_fromUtf8("song_alt_key_menu"))
        self.horizontalLayout_4.addWidget(self.song_alt_key_menu)
        self.label_11 = QtGui.QLabel(self.layoutWidget1)
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.song_subtitle_ef = QtGui.QLineEdit(self.layoutWidget1)
        self.song_subtitle_ef.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.song_subtitle_ef.setObjectName(_fromUtf8("song_subtitle_ef"))
        self.horizontalLayout_4.addWidget(self.song_subtitle_ef)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.chord_editor_button = QtGui.QToolButton(self.layoutWidget1)
        self.chord_editor_button.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter chord editing mode (⌘K).   This mode allows you to modify chords for the current song.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chord_editor_button.setText(QtGui.QApplication.translate("MainWindow", "Edit Chords", None, QtGui.QApplication.UnicodeUTF8))
        self.chord_editor_button.setObjectName(_fromUtf8("chord_editor_button"))
        self.horizontalLayout_6.addWidget(self.chord_editor_button)
        self.lyric_editor_button = QtGui.QToolButton(self.layoutWidget1)
        self.lyric_editor_button.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter lyric editing mode (⌘L).   This mode lets you modify the song text.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lyric_editor_button.setText(QtGui.QApplication.translate("MainWindow", "Edit Text", None, QtGui.QApplication.UnicodeUTF8))
        self.lyric_editor_button.setObjectName(_fromUtf8("lyric_editor_button"))
        self.horizontalLayout_6.addWidget(self.lyric_editor_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label_12 = QtGui.QLabel(self.layoutWidget1)
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Transpose:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        self.transpose_down_button = QtGui.QPushButton(self.layoutWidget1)
        self.transpose_down_button.setToolTip(QtGui.QApplication.translate("MainWindow", "Transpose the whole song one half-step down.", None, QtGui.QApplication.UnicodeUTF8))
        self.transpose_down_button.setText(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.transpose_down_button.setObjectName(_fromUtf8("transpose_down_button"))
        self.horizontalLayout_6.addWidget(self.transpose_down_button)
        self.transpose_up_button = QtGui.QPushButton(self.layoutWidget1)
        self.transpose_up_button.setToolTip(QtGui.QApplication.translate("MainWindow", "Transpose the whole song one half-step up.", None, QtGui.QApplication.UnicodeUTF8))
        self.transpose_up_button.setText(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.transpose_up_button.setObjectName(_fromUtf8("transpose_up_button"))
        self.horizontalLayout_6.addWidget(self.transpose_up_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.chords_editor_label = QtGui.QLabel(self.layoutWidget1)
        self.chords_editor_label.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">To add a new chord:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Press on a lyrics letter to select it, then press one of the following keys: A, B, C, D, E, F, or G.  To assign a sharp or a flat, press the &quot;Up&quot; or &quot;Down&quot; key afterwards to &quot;transpose&quot; the chord.  To create a minor chord, press the &quot;M&quot; key.  To create advanced chords, double-click on the created chord (a dialog box will open).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">To edit a chord:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Click on the chord to select it, then press &quot;M&quot; to toggle major/minor, press another letter to assign a different note, or press &quot;Up&quot; or &quot;Down&quot; keys to transpose it. Double-click on the chord for advanced modifications.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">To move a chord:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Click on the chord to select it, and then use the &quot;Left&quot; or &quot;Right&quot; keys to move it relative to the lyrics below it. Alternatively you can simply drag it to the new place.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">To duplicate a chord:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">While holding the &quot;Option&quot; key, click and drag the chord. Alternatively you can use copy-and-paste.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">To delete a chord:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Click on the chord to select it, and press the &quot;Delete&quot; key.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chords_editor_label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Edit chords of the selected song: </span> <span style=\" font-style:italic;\">(Hover mouse here for help)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chords_editor_label.setWordWrap(True)
        self.chords_editor_label.setObjectName(_fromUtf8("chords_editor_label"))
        self.verticalLayout.addWidget(self.chords_editor_label)
        self.lyrics_editor_label = QtGui.QLabel(self.layoutWidget1)
        self.lyrics_editor_label.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">When in lyric editing mode, you can modify the text (lyrics) of the song.  As text is moved/added/removed, chords get moved automatically to follow their letters.   Remember to go back into the chord editor mode when you need modify chords.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lyrics_editor_label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Edit lyrics of the selected song: </span> <span style=\" font-style:italic;\">(Hover mouse here for help)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lyrics_editor_label.setWordWrap(True)
        self.lyrics_editor_label.setObjectName(_fromUtf8("lyrics_editor_label"))
        self.verticalLayout.addWidget(self.lyrics_editor_label)
        self.lyric_editor_layout = QtGui.QVBoxLayout()
        self.lyric_editor_layout.setObjectName(_fromUtf8("lyric_editor_layout"))
        self.chord_scroll_area = QtGui.QScrollArea(self.layoutWidget1)
        self.chord_scroll_area.setMinimumSize(QtCore.QSize(100, 100))
        self.chord_scroll_area.setToolTip(_fromUtf8(""))
        self.chord_scroll_area.setFrameShape(QtGui.QFrame.StyledPanel)
        self.chord_scroll_area.setFrameShadow(QtGui.QFrame.Sunken)
        self.chord_scroll_area.setWidgetResizable(True)
        self.chord_scroll_area.setObjectName(_fromUtf8("chord_scroll_area"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 558))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.chord_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.lyric_editor_layout.addWidget(self.chord_scroll_area)
        self.verticalLayout.addLayout(self.lyric_editor_layout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zoom_out_button = QtGui.QToolButton(self.layoutWidget1)
        self.zoom_out_button.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoom_out_button.setObjectName(_fromUtf8("zoom_out_button"))
        self.horizontalLayout_3.addWidget(self.zoom_out_button)
        self.zoom_slider = QtGui.QSlider(self.layoutWidget1)
        self.zoom_slider.setOrientation(QtCore.Qt.Horizontal)
        self.zoom_slider.setObjectName(_fromUtf8("zoom_slider"))
        self.horizontalLayout_3.addWidget(self.zoom_slider)
        self.zoom_in_button = QtGui.QToolButton(self.layoutWidget1)
        self.zoom_in_button.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoom_in_button.setObjectName(_fromUtf8("zoom_in_button"))
        self.horizontalLayout_3.addWidget(self.zoom_in_button)
        self.zoom_label = QtGui.QLabel(self.layoutWidget1)
        self.zoom_label.setText(QtGui.QApplication.translate("MainWindow", "Zoom: 100%", None, QtGui.QApplication.UnicodeUTF8))
        self.zoom_label.setObjectName(_fromUtf8("zoom_label"))
        self.horizontalLayout_3.addWidget(self.zoom_label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSong = QtGui.QMenu(self.menubar)
        self.menuSong.setTitle(QtGui.QApplication.translate("MainWindow", "Song", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSong.setObjectName(_fromUtf8("menuSong"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewSong = QtGui.QAction(MainWindow)
        self.actionNewSong.setText(QtGui.QApplication.translate("MainWindow", "New Song", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSong.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSong.setObjectName(_fromUtf8("actionNewSong"))
        self.actionDeleteSong = QtGui.QAction(MainWindow)
        self.actionDeleteSong.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteSong.setObjectName(_fromUtf8("actionDeleteSong"))
        self.actionExportText = QtGui.QAction(MainWindow)
        self.actionExportText.setText(QtGui.QApplication.translate("MainWindow", "Export To TEXT...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportText.setObjectName(_fromUtf8("actionExportText"))
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "Print...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionLyricsFont = QtGui.QAction(MainWindow)
        self.actionLyricsFont.setText(QtGui.QApplication.translate("MainWindow", "Lyrics Font...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLyricsFont.setObjectName(_fromUtf8("actionLyricsFont"))
        self.actionChordsFont = QtGui.QAction(MainWindow)
        self.actionChordsFont.setText(QtGui.QApplication.translate("MainWindow", "Chords Font...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChordsFont.setObjectName(_fromUtf8("actionChordsFont"))
        self.actionImportText = QtGui.QAction(MainWindow)
        self.actionImportText.setText(QtGui.QApplication.translate("MainWindow", "Import From TEXT...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportText.setObjectName(_fromUtf8("actionImportText"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionCloseSongbook = QtGui.QAction(MainWindow)
        self.actionCloseSongbook.setText(QtGui.QApplication.translate("MainWindow", "Close Songbook", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCloseSongbook.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCloseSongbook.setObjectName(_fromUtf8("actionCloseSongbook"))
        self.actionOpenSongbook = QtGui.QAction(MainWindow)
        self.actionOpenSongbook.setText(QtGui.QApplication.translate("MainWindow", "Open Songbook...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSongbook.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSongbook.setObjectName(_fromUtf8("actionOpenSongbook"))
        self.actionNewSongbook = QtGui.QAction(MainWindow)
        self.actionNewSongbook.setText(QtGui.QApplication.translate("MainWindow", "New Songbook...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSongbook.setObjectName(_fromUtf8("actionNewSongbook"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionSaveSongbook = QtGui.QAction(MainWindow)
        self.actionSaveSongbook.setText(QtGui.QApplication.translate("MainWindow", "Save Songbook As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveSongbook.setObjectName(_fromUtf8("actionSaveSongbook"))
        self.actionExportMultiplePdfs = QtGui.QAction(MainWindow)
        self.actionExportMultiplePdfs.setText(QtGui.QApplication.translate("MainWindow", "Export to Multiple PDFs...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportMultiplePdfs.setObjectName(_fromUtf8("actionExportMultiplePdfs"))
        self.actionSelectAll = QtGui.QAction(MainWindow)
        self.actionSelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionSelectAll.setObjectName(_fromUtf8("actionSelectAll"))
        self.actionImportChordPro = QtGui.QAction(MainWindow)
        self.actionImportChordPro.setText(QtGui.QApplication.translate("MainWindow", "Import From ChordPro...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportChordPro.setObjectName(_fromUtf8("actionImportChordPro"))
        self.actionExportChordPro = QtGui.QAction(MainWindow)
        self.actionExportChordPro.setText(QtGui.QApplication.translate("MainWindow", "Export To ChordPro...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportChordPro.setObjectName(_fromUtf8("actionExportChordPro"))
        self.actionSetID = QtGui.QAction(MainWindow)
        self.actionSetID.setText(QtGui.QApplication.translate("MainWindow", "Set Database ID...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSetID.setObjectName(_fromUtf8("actionSetID"))
        self.actionCopySongText = QtGui.QAction(MainWindow)
        self.actionCopySongText.setText(QtGui.QApplication.translate("MainWindow", "Copy Song Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopySongText.setObjectName(_fromUtf8("actionCopySongText"))
        self.actionPasteAsNewSong = QtGui.QAction(MainWindow)
        self.actionPasteAsNewSong.setText(QtGui.QApplication.translate("MainWindow", "Paste As New Song", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPasteAsNewSong.setObjectName(_fromUtf8("actionPasteAsNewSong"))
        self.actionDeleteSongs = QtGui.QAction(MainWindow)
        self.actionDeleteSongs.setText(QtGui.QApplication.translate("MainWindow", "Delete Selected songs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteSongs.setObjectName(_fromUtf8("actionDeleteSongs"))
        self.actionExportSongPDF = QtGui.QAction(MainWindow)
        self.actionExportSongPDF.setText(QtGui.QApplication.translate("MainWindow", "Export to PDF...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportSongPDF.setObjectName(_fromUtf8("actionExportSongPDF"))
        self.actionExportSinglePdf = QtGui.QAction(MainWindow)
        self.actionExportSinglePdf.setText(QtGui.QApplication.translate("MainWindow", "Export to PDF...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportSinglePdf.setObjectName(_fromUtf8("actionExportSinglePdf"))
        self.actionImportClipboard = QtGui.QAction(MainWindow)
        self.actionImportClipboard.setText(QtGui.QApplication.translate("MainWindow", "Import From Clipboard...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportClipboard.setObjectName(_fromUtf8("actionImportClipboard"))
        self.actionExportClipboard = QtGui.QAction(MainWindow)
        self.actionExportClipboard.setText(QtGui.QApplication.translate("MainWindow", "Export To Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportClipboard.setObjectName(_fromUtf8("actionExportClipboard"))
        self.actionZoomIn = QtGui.QAction(MainWindow)
        self.actionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setObjectName(_fromUtf8("actionZoomIn"))
        self.actionZoomOut = QtGui.QAction(MainWindow)
        self.actionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setObjectName(_fromUtf8("actionZoomOut"))
        self.actionZoomActual = QtGui.QAction(MainWindow)
        self.actionZoomActual.setText(QtGui.QApplication.translate("MainWindow", "Actual Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomActual.setObjectName(_fromUtf8("actionZoomActual"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionExportSongToPdf = QtGui.QAction(MainWindow)
        self.actionExportSongToPdf.setText(QtGui.QApplication.translate("MainWindow", "Export To PDF...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportSongToPdf.setObjectName(_fromUtf8("actionExportSongToPdf"))
        self.actionRemoveTrailingSpaces = QtGui.QAction(MainWindow)
        self.actionRemoveTrailingSpaces.setText(QtGui.QApplication.translate("MainWindow", "Remove Trailing Spaces", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveTrailingSpaces.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove trailing spaces from every line in the selected song(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveTrailingSpaces.setObjectName(_fromUtf8("actionRemoveTrailingSpaces"))
        self.actionAppendSongbook = QtGui.QAction(MainWindow)
        self.actionAppendSongbook.setText(QtGui.QApplication.translate("MainWindow", "Append Another Songbook...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAppendSongbook.setObjectName(_fromUtf8("actionAppendSongbook"))
        self.actionRenumberSongs = QtGui.QAction(MainWindow)
        self.actionRenumberSongs.setText(QtGui.QApplication.translate("MainWindow", "Renumber all songs...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRenumberSongs.setObjectName(_fromUtf8("actionRenumberSongs"))
        self.actionChordEditorMode = QtGui.QAction(MainWindow)
        self.actionChordEditorMode.setText(QtGui.QApplication.translate("MainWindow", "Chord Editor Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChordEditorMode.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChordEditorMode.setObjectName(_fromUtf8("actionChordEditorMode"))
        self.actionLyricEditorMode = QtGui.QAction(MainWindow)
        self.actionLyricEditorMode.setText(QtGui.QApplication.translate("MainWindow", "Lyric Editor Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLyricEditorMode.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLyricEditorMode.setObjectName(_fromUtf8("actionLyricEditorMode"))
        self.menuSong.addAction(self.actionSetID)
        self.menuSong.addAction(self.actionDeleteSong)
        self.menuSong.addSeparator()
        self.menuSong.addAction(self.actionExportText)
        self.menuSong.addAction(self.actionExportChordPro)
        self.menuSong.addAction(self.actionExportClipboard)
        self.menuSong.addAction(self.actionExportSongToPdf)
        self.menuFile.addAction(self.actionNewSongbook)
        self.menuFile.addAction(self.actionOpenSongbook)
        self.menuFile.addAction(self.actionCloseSongbook)
        self.menuFile.addAction(self.actionSaveSongbook)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportClipboard)
        self.menuFile.addAction(self.actionImportChordPro)
        self.menuFile.addAction(self.actionImportText)
        self.menuFile.addAction(self.actionAppendSongbook)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExportSinglePdf)
        self.menuFile.addAction(self.actionExportMultiplePdfs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuSettings.addAction(self.actionLyricsFont)
        self.menuSettings.addAction(self.actionChordsFont)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionZoomIn)
        self.menuSettings.addAction(self.actionZoomOut)
        self.menuSettings.addAction(self.actionZoomActual)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCopySongText)
        self.menuEdit.addAction(self.actionPasteAsNewSong)
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionNewSong)
        self.menuEdit.addAction(self.actionDeleteSongs)
        self.menuEdit.addAction(self.actionRemoveTrailingSpaces)
        self.menuEdit.addAction(self.actionRenumberSongs)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionChordEditorMode)
        self.menuEdit.addAction(self.actionLyricEditorMode)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSong.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

