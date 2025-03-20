import sys
import heapq
from collections import deque

class Process:
    def __init__(self, pid, arrivalTime, burstTime):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.waitingTime = 0
        self.completedTime = None
        self.complete = False
    
    def __repr__(self):
        return f"{self.pid}: 종료 시간 = {self.completedTime}"

def processSort(processes):
    heap = [(p.arrivalTime, p) for p in processes]
    heapq.heapify(heap)
    sortedProcesses = deque([heapq.heappop(heap)[1] for _ in range(len(heap))])
    return sortedProcesses

def wait(rr):
    for process in rr:
        process.waitingTime += 1

def work(process, time):
    process.burstTime -= 1
    if process.burstTime == 0:
        process.completedTime = time
        process.complete = True
    
    return process

def setRR(processes, rr, time):
    while processes:
        if processes[0].arrivalTime <= time:
            rr.append(processes.popleft())
        else: break

def RoundRobin(processes, tq):
    time = 0
    rr = deque()
    remainingProcess = len(processes)
    completedProcesses = list()
    
    while remainingProcess:
        setRR(processes, rr, time)
        if not rr:
            time += 1
            continue
        
        workingProcess = rr.popleft()
        for _ in range(tq):
            time += 1
            wait(rr)
            workingProcess = work(workingProcess, time)
            
            setRR(processes, rr, time)
            # print(time, workingProcess.pid, workingProcess.burstTime)
            if workingProcess.complete:
                remainingProcess -= 1
                completedProcesses.append(workingProcess)
                break
        if not workingProcess.complete:
            rr.append(workingProcess)

    return completedProcesses

n, tq = map(int, sys.stdin.readline().split())
processes = list()
for _ in range(n):
    pid, arrivalTime, burstTime = map(int, sys.stdin.readline().split())
    processes.append(Process(pid, arrivalTime, burstTime))

processes = processSort(processes)
completedProcesses = RoundRobin(processes, tq)

sumOfWaitingTime = 0
for process in completedProcesses:
    print(process)
    sumOfWaitingTime += process.waitingTime
print(f"평균 대기 시간 = {round(sumOfWaitingTime / n, 2)}")