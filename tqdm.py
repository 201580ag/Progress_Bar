from tqdm import tqdm
import time

for i in tqdm(range(10), desc="Processing"):
    time.sleep(0.1)