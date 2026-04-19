import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import tqdm
import pandas as pd

# -------------------- Function to run in threads --------------------
def square_number(item):
    idx, num = item
    thread_name = threading.current_thread().name
    print(f"[{thread_name}] Processing index {idx}, number {num}")
    time.sleep(1)  # simulate I/O-bound delay
    result = num ** 2
    print(f"[{thread_name}] Done index {idx}, result {result}")
    return {idx: {"result": result, "thread": thread_name}}  # include thread info

# -------------------- Input Data --------------------
numbers = pd.Series([2, 3, 4, 5], index=[101, 102, 103, 104])
numbers = numbers.dropna()  # drop missing
input_dict = numbers.to_dict()
print(f"Input dictionary: {input_dict}\n")

# -------------------- Thread Pool Executor --------------------
geocoded = {}
max_workers = 2  # run 2 threads in parallel
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Submit tasks
    futures = {executor.submit(square_number, item): item for item in input_dict.items()}
    print(f"Submitted {len(futures)} tasks to the thread pool\n")

    # Process results as they complete
    for future in tqdm.tqdm(as_completed(futures), total=len(input_dict)):
        result = future.result()  # get result from thread
        print(f"[Main] Received result: {result}")
        geocoded.update(result)  # merge into master dict

# -------------------- Convert results to DataFrame --------------------
print("\nFinal geocoded dictionary:", geocoded)
df = pd.DataFrame.from_dict(geocoded, orient="index")
df.index.name = "id"
print("\nFinal DataFrame:\n", df)
