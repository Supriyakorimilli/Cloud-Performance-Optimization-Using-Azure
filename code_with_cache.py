from cachetools import cached, LRUCache
import math
import time
import psutil

# Define a cache with a maximum size of 200 items
cache = LRUCache(maxsize=200)

def perform_complex_calculation(x, y):
    # Simulate a complex calculation
    time.sleep(1)
    # Simulate computation time
    result = math.sin(x) ** 2 + math.cos(y) ** 2
    return result

@cached(cache)
def expensive_math_operation(x, y):
    # This function uses a complex mathematical computation that we'll cache
    return perform_complex_calculation(x, y)

def get_cpu_memory_usage():
    # Get the percentage of the CPU usage and memory usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage, memory_usage

if __name__ == "__main__":
    with open("with_cache_performance.csv", "w") as f:
        f.write("CPU After, Memory After, Response Time\n")
        for _ in range(10):
            # Run 10 cycles
            start_time = time.time()
            result = expensive_math_operation(3, 4)
            response_time = time.time() - start_time
            cpu_after, memory_after = get_cpu_memory_usage()
            f.write(f"{cpu_after}, {memory_after}, {response_time}\n")
            time.sleep(1)  # Delay between iterations
