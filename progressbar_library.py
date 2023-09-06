import progressbar
import time

bar = progressbar.ProgressBar()

for i in bar(range(10)):
    time.sleep(0.1)