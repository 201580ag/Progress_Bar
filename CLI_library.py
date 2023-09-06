import sys
import time

def progress_bar(iterable, length=50):
    total = len(iterable)
    for i, item in enumerate(iterable):
        progress = ("#" * int(length * (i + 1) / total)).ljust(length)
        sys.stdout.write(f"\r[{progress}] {i}/{total}")
        sys.stdout.flush()
        yield item

for _ in progress_bar(range(10)):
    time.sleep(0.1)