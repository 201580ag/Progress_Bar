from rich.progress import Progress
import time

with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=10)
    while not progress.finished:
        progress.update(task, completed=1)
        time.sleep(3)