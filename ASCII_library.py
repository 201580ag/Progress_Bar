import sys
import time

for i in range(10):
    sys.stdout.write("\r[" + "=" * (i + 1) + " " * (10 - i - 1) + f"] {i + 1}/10")
    sys.stdout.flush()
    time.sleep(0.1)