import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import QTimer

def update_progress():
    progress_bar.setValue(progress_bar.value() + 10)

app = QApplication(sys.argv)
window = QWidget()
progress_bar = QProgressBar(window)
progress_bar.setGeometry(30, 40, 200, 25)
timer = QTimer()
timer.timeout.connect(update_progress)
timer.start(100)

window.show()
sys.exit(app.exec_())