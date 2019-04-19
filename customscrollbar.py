import sys
from PyQt5.QtWidgets import QScrollBar

class CustomScrollBar(QScrollBar):
    def init(self, parent=None, **kwargs):
        QScrollBar.init(self, parent, **kwargs)

        self.setStyleSheet("""
                QScrollBar:horizontal {
                    border: none;
                    border-radius: 5px solid grey;
                    background: none;
                    height: 26px;
                    margin: 0px 26px 0 26px;
                }

                QScrollBar::handle:horizontal {
                    background: lightgray;
                    min-width: 26px;
                }

                QScrollBar::add-line:horizontal {
                    background: none;
                    width: 26px;
                    subcontrol-position: right;
                    subcontrol-origin: margin;
                    
                }

                QScrollBar::sub-line:horizontal {
                    background: none;
                    width: 26px;
                    subcontrol-position: top left;
                    subcontrol-origin: margin;
                    position: absolute;
                }

                QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
                    width: 26px;
                    height: 26px;
                    background: none;
                    image: url('./glass.png');
                }

                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    background: none;
                }

                /* VERTICAL */
                QScrollBar:vertical {
                    border: none;
                    background: none;
                    width: 26px;
                    margin: 26px 0 26px 0;
                }

                QScrollBar::handle:vertical {
                    background: lightgray;
                    min-height: 26px;
                }

                QScrollBar::add-line:vertical {
                    background: none;
                    height: 26px;
                    subcontrol-position: bottom;
                    subcontrol-origin: margin;
                }

                QScrollBar::sub-line:vertical {
                    background: none;
                    height: 26px;
                    subcontrol-position: top left;
                    subcontrol-origin: margin;
                    position: absolute;
                }

                QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
                    width: 26px;
                    height: 26px;
                    background: none;
                    image: url('./glass.png');
                }

                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }

            """)