class Process:
    def __init__(self, pos, at, bt):
        self.AT = at
        self.BT = bt
        self.ST = [-1] * 20
        self.WT = 0
        self.FT = 0
        self.TAT = 0
        self.RT = 0
        self.pos = pos


def main():
    with open("example.txt", "r") as f:
        n = int(f.readline().strip())
        processes = []
        for i in range(n):
            data = f.readline().strip().split()
            processes.append(Process(data[0], int(data[2]), int(data[1])))
        quantum = 2

    time = 0
    c = n
    s = [[-1] * 20 for _ in range(n)]
    b = [p.BT for p in processes]
    a = [p.AT for p in processes]

    tot_wt = 0
    tot_tat = 0
    gantt_chart = []
    gantt_times = [0]

    while c != 0:
        mini = float('inf')
        flag = False
        index = -1

        for i in range(n):
            if a[i] <= time + 0.1 and b[i] > 0 and a[i] < mini:
                mini = a[i]
                index = i
                flag = True

        if not flag:
            time += 1
            continue

        gantt_chart.append(processes[index].pos)

        j = 0
        while s[index][j] != -1:
            j += 1
        if s[index][j] == -1:
            s[index][j] = time
            processes[index].ST[j] = time

        if b[index] <= quantum:
            time += b[index]
            gantt_times.append(time)
            b[index] = 0
        else:
            time += quantum
            gantt_times.append(time)
            b[index] -= quantum

        if b[index] > 0:
            a[index] = time + 0.1

        if b[index] == 0:
            c -= 1
            p = processes[index]
            p.FT = time
            p.WT = p.FT - p.AT - p.BT
            p.TAT = p.BT + p.WT
            p.RT = p.ST[0] - p.AT
            tot_wt += p.WT
            tot_tat += p.TAT

    with open("solution.txt", "w") as out:
        out.write("Gantt Chart\n")
        out.write("|" + "|".join(f" {pid} " for pid in gantt_chart) + "|\n")
        out.write("".join(f"{t:>4}" for t in gantt_times) + "\n\n")

        out.write(f"{'ProcessID':<12}{'ArrivalTime':<15}{'WaitingTime':<15}{'TurnaroundTime':<18}{'ResponseTime':<15}\n")
        for p in processes:
            out.write(f"{p.pos:<12}{p.AT:<15}{p.WT:<15}{p.TAT:<18}{p.RT:<15}\n")

        avg_wt = tot_wt / n
        avg_tat = tot_tat / n
        avg_rt = sum(p.RT for p in processes) / n
        out.write(f"\n{'Average':<12}{'':<15}{avg_wt:<15.4f}{avg_tat:<18.4f}{avg_rt:<15.4f}\n")


if __name__ == "__main__":
    main()