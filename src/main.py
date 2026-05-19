import asyncio
from pathlib import Path

from rich.console import Console
from rich.table import Table

from src.utils import load_tasks, save_json
from src.workflow import run_all_tasks


console = Console()


def show_results_table(results):
    table = Table(title="Multi-Agent AI Workflow Results")

    table.add_column("Task ID", style="bold")
    table.add_column("Department")
    table.add_column("Task Type")
    table.add_column("Priority")
    table.add_column("Validation Status")

    for item in results:
        validation_status = item["workflow_results"]["content_validation"]["status"]

        table.add_row(
            str(item["task_id"]),
            str(item["department"]),
            str(item["task_type"]),
            str(item["priority"]),
            str(validation_status),
        )

    console.print(table)


async def main():
    input_file = "data/sample_tasks.csv"
    output_file = "outputs/workflow_results.json"

    console.print("[bold green]Starting Multi-Agent AI Workflow System...[/bold green]")

    tasks = load_tasks(input_file)
    results = await run_all_tasks(tasks)

    save_json(results, output_file)
    show_results_table(results)

    console.print(f"[bold cyan]Workflow completed successfully.[/bold cyan]")
    console.print(f"[bold cyan]Results saved to:[/bold cyan] {Path(output_file).resolve()}")


if __name__ == "__main__":
    asyncio.run(main())