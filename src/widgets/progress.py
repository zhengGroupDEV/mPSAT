'''
Description: progress bar
Author: Rainyl
LastEditTime: 2022-08-02 11:37:11
'''
from PySide6.QtCore import QRect, Qt, QSize, QTimer
from PySide6.QtGui import QColor, QPainter, QPen, QFont, QPaintEvent
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QProgressBar


class CircularProgress(QProgressBar):
    def __init__(
        self,
        parent = None,
        progress_width = 10,
        progress_color = "#ff79c6",
        enable_text = True,
        font_family = "Segoe UI",
        font_size = 12,
        suffix = "%",
        text_color = "#ff79c6",
        enable_bg = True,
        bg_color = "#44475a"
    ):
        super(CircularProgress, self).__init__(parent=parent)
        self.progress_width = progress_width
        self.progress_color = progress_color
        self.busy_step = 1

        self.timer = QTimer(self)
        self.timer.setInterval(5)
        self.timer.timeout.connect(self.update_busy)
        self.counter = 0
        self.chunk_size = 150
        # Text
        self.enable_text = enable_text
        self.font_family = font_family
        self.font_size = font_size
        self.suffix = suffix
        self.text_color = text_color
        self.enable_bg = enable_bg
        self.bg_color = bg_color

    def update_busy(self):
        self.counter += 1
        self.update()

    def paintEvent(self, e):
        width = self.width() - self.progress_width
        height = self.height() - self.progress_width
        margin = self.progress_width / 2

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family, self.font_size))

        paint.setPen(Qt.NoPen)

        pen = QPen()             
        pen.setWidth(self.progress_width)
        pen.setCapStyle(Qt.RoundCap)

        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        pen.setColor(QColor("#FFFFFF"))
        paint.setPen(pen)
        if self.maximum() == 0:
            if not self.timer.isActive():
                self.timer.start()
            paint.drawArc(margin, margin, width, height, -(self.counter + self.busy_step) % 360 * 16, -self.chunk_size * 16)
        else:
            value = self.value() * (360 / self.maximum())
            paint.drawArc(margin, margin, width, height, 90 * 16, value * 16)

        # if self.enable_text:
        #     pen.setColor(QColor(self.text_color))
        #     paint.setPen(pen)
        #     paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        paint.end()

    def closeEvent(self, event) -> None:
        self.timer.stop()
        return super().closeEvent(event)

    def parent_finished(self):
        self.close()
