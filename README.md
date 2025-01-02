# Round Robin Scheduling Simulation

This project simulates the **Round Robin Scheduling Algorithm**, a popular CPU scheduling algorithm used in operating systems. The simulation processes tasks with specified arrival times and burst times, calculates their performance metrics, and outputs a Gantt chart and summary statistics.

## Features
- Reads process data from a file.
- Simulates Round Robin scheduling with a configurable quantum.
- Outputs detailed metrics for each process:
  - Waiting Time (WT)
  - Turnaround Time (TAT)
  - Response Time (RT)
- Displays a Gantt chart showing process execution order.
- Calculates average values for WT, TAT, and RT.

## Input Format
The program reads input from a file named `example.txt`. The file should have the following format:
1. The first line specifies the number of processes, `n`.
2. The subsequent `n` lines each specify:
   - Process ID
   - Burst Time
   - Arrival Time

**Example Input (example.txt):**

```
6
p1 7 0
p2 5 1
p3 3 2
p4 1 3
p5 2 4
p6 1 5
```
