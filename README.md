# Multi-Agent AI Workflow System

This project demonstrates a multi-agent AI workflow system that coordinates validation, summarization, and structured output generation across business workflows.

The system uses Python with LangGraph-style workflow orchestration, CrewAI agent profiles, and asynchronous task execution to process multiple tasks efficiently.

---

## Project Goal

The goal of this project is to automate business task processing using multiple agents.

Each task goes through:

1. Validation Agent
2. Summarization Agent
3. Structured Output Agent

The final result includes validation status, summary, and structured business output.

---

## Features

- Loads workflow tasks from a CSV file
- Validates missing or incomplete task information
- Summarizes task content
- Generates structured output for downstream business workflows
- Uses LangGraph to orchestrate the workflow
- Uses CrewAI-style agent profiles to define agent roles and responsibilities
- Uses asynchronous execution to process multiple tasks faster
- Displays results in a terminal table
- Saves final workflow results into a JSON file
- Includes a benchmark script to compare sequential vs async processing

---

## Technologies Used

- Python
- LangGraph
- CrewAI
- Pandas
- Pydantic
- Python Dotenv
- Rich
- Git
- GitHub

---

## Project Structure

```text
multi-agent-ai-workflow-system/
│
├── data/
│   └── sample_tasks.csv
│
├── outputs/
│   └── workflow_results.json
│
├── src/
│   ├── agents.py
│   ├── benchmark.py
│   ├── crewai_profiles.py
│   ├── main.py
│   ├── utils.py
│   └── workflow.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How to Run This Project

Follow these steps from the project root folder.

### 1. Open the project folder

Open VS Code and make sure your terminal is inside this folder:

```bash
multi-agent-ai-workflow-system
```

On Windows PowerShell, your path may look like this:

```powershell
C:\Users\shaik\OneDrive\Desktop\Projects\multi-agent-ai-workflow-system
```

---

### 2. Create a virtual environment

Run this command:

```powershell
py -3.11 -m venv venv
```

---

### 3. Activate the virtual environment

Run this command:

```powershell
.\venv\Scripts\activate
```

After activation, your terminal should show:

```powershell
(venv)
```

---

### 4. Install required packages

Run this command:

```powershell
pip install -r requirements.txt
```

---

### 5. Run the project

Run this command:

```powershell
python -m src.main
```

---

### 6. Expected terminal output

You should see a table like this:

```text
Multi-Agent AI Workflow Results
```

The table will show:

- Task ID
- Department
- Task Type
- Priority
- Validation Status

---

### 7. Output file

After running the project, the system creates this output file:

```text
outputs/workflow_results.json
```

This file contains the final processed workflow results in JSON format.

---

## How to Run the Performance Benchmark

This project includes a benchmark script to compare sequential processing and asynchronous processing.

Run this command:

```powershell
python -m src.benchmark
```

Example benchmark result:

```text
Performance Benchmark Results
--------------------------------
Sequential Processing Time: 1.67 seconds
Async Processing Time:      0.36 seconds
Efficiency Improvement:     78.28% faster
```

This shows that asynchronous task execution improves workflow throughput and reduces turnaround time.

---

## Example Input Data

The input file is located at:

```text
data/sample_tasks.csv
```

Example columns:

```text
task_id, department, task_type, input_text, priority
```

---

## Example Workflow

For every task, the system performs the following process:

```text
CSV Input Data
      ↓
Validation Agent
      ↓
Summarization Agent
      ↓
Structured Output Agent
      ↓
Terminal Table + JSON Output
```

---

## Agent Responsibilities

### Validation Agent

Checks whether each task has missing, incomplete, or inconsistent information.

### Summarization Agent

Creates a short business summary from the task description.

### Structured Output Agent

Converts the processed task into clean structured output for downstream business use.

---

## GitHub Commands Used

Initialize Git:

```powershell
git init
```

Add files:

```powershell
git add .
```

Commit files:

```powershell
git commit -m "Initial project setup"
```

Connect to GitHub:

```powershell
git remote add origin https://github.com/krishshaik7-24/multi-agent-ai-workflow-system.git
```

Push to GitHub:

```powershell
git push -u origin main
```

For future updates:

```powershell
git add .
git commit -m "Update project files"
git push
```

---

## Final Output

The final project successfully processes business workflow tasks through multiple agents and saves structured workflow results for downstream business use.

It also demonstrates asynchronous workflow execution, agent orchestration, validation logic, summarization, structured output generation, and benchmark-based performance improvement.

---

## Resume Summary

Designed and developed a Multi-Agent AI Workflow System using LangGraph and CrewAI-style agent profiles to coordinate data validation, summarization, and structured output generation across workflows.

Implemented asynchronous task execution and agent orchestration, improving workflow processing speed by 78.28% in benchmark testing.

Integrated validation steps within the workflow to ensure consistent outputs and reliable automation for downstream business processes.

---

## Author

Karishma Shaik