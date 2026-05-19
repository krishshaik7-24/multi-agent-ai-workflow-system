import asyncio
import time
from typing import Dict, Any, List

from src.utils import load_tasks
from src.workflow import run_single_task, run_all_tasks


async def run_tasks_sequentially(tasks: List[Dict[str, Any]]):
    results = []

    for task in tasks:
        result = await run_single_task(task)
        results.append(result)

    return results


async def benchmark_workflow():
    input_file = "data/sample_tasks.csv"
    tasks = load_tasks(input_file)

    print("Starting performance benchmark...")

    sequential_start = time.perf_counter()
    await run_tasks_sequentially(tasks)
    sequential_end = time.perf_counter()

    async_start = time.perf_counter()
    await run_all_tasks(tasks)
    async_end = time.perf_counter()

    sequential_time = sequential_end - sequential_start
    async_time = async_end - async_start

    improvement = ((sequential_time - async_time) / sequential_time) * 100

    print("\nPerformance Benchmark Results")
    print("--------------------------------")
    print(f"Sequential Processing Time: {sequential_time:.2f} seconds")
    print(f"Async Processing Time:      {async_time:.2f} seconds")
    print(f"Efficiency Improvement:     {improvement:.2f}% faster")


if __name__ == "__main__":
    asyncio.run(benchmark_workflow())