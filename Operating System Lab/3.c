#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int pid;
    int arrivalTime;
    int burstTime;
    int remainingTime;
    int completionTime;
    int waitingTime;
    int turnaroundTime;
} Process;

void calculateSJF(Process p[], int n);
void calculateRoundRobin(Process p[], int n, int quantum);
void displayResults(Process p[], int n);

int main() {
    int n, choice, quantum;
    printf("Enter number of processes: ");
    scanf("%d", &n);

    Process processes[n];
    for (int i = 0; i < n; i++) {
        printf("Enter Arrival Time and Burst Time for Process %d: ", i + 1);
        scanf("%d%d", &processes[i].arrivalTime, &processes[i].burstTime);
        processes[i].pid = i + 1;
        processes[i].remainingTime = processes[i].burstTime;
    }

    printf("\nChoose Scheduling Algorithm:\n1. Shortest Job First (Preemptive)\n2. Round Robin\nEnter choice: ");
    scanf("%d", &choice);

    if (choice == 2) {
        printf("Enter Time Quantum for Round Robin: ");
        scanf("%d", &quantum);
    }

    switch (choice) {
        case 1:
            calculateSJF(processes, n);
            break;
        case 2:
            calculateRoundRobin(processes, n, quantum);
            break;
        default:
            printf("Invalid choice.\n");
            return 1;
    }

    displayResults(processes, n);
    return 0;
}

// Shortest Job First (Preemptive) Scheduling
void calculateSJF(Process p[], int n) {
    int time = 0, completed = 0, minIndex;
    bool isFound;

    while (completed != n) {
        minIndex = -1;
        int minRemainingTime = 1e9;
        isFound = false;

        for (int i = 0; i < n; i++) {
            if (p[i].arrivalTime <= time && p[i].remainingTime > 0 && p[i].remainingTime < minRemainingTime) {
                minRemainingTime = p[i].remainingTime;
                minIndex = i;
                isFound = true;
            }
        }

        if (isFound) {
            p[minIndex].remainingTime--;
            time++;

            if (p[minIndex].remainingTime == 0) {
                p[minIndex].completionTime = time;
                p[minIndex].turnaroundTime = p[minIndex].completionTime - p[minIndex].arrivalTime;
                p[minIndex].waitingTime = p[minIndex].turnaroundTime - p[minIndex].burstTime;
                completed++;
            }
        } else {
            time++;
        }
    }
}

// Round Robin Scheduling
void calculateRoundRobin(Process p[], int n, int quantum) {
    int time = 0, completed = 0;
    while (completed < n) {
        bool isProgressed = false;
        for (int i = 0; i < n; i++) {
            if (p[i].arrivalTime <= time && p[i].remainingTime > 0) {
                if (p[i].remainingTime > quantum) {
                    time += quantum;
                    p[i].remainingTime -= quantum;
                } else {
                    time += p[i].remainingTime;
                    p[i].remainingTime = 0;
                    p[i].completionTime = time;
                    p[i].turnaroundTime = p[i].completionTime - p[i].arrivalTime;
                    p[i].waitingTime = p[i].turnaroundTime - p[i].burstTime;
                    completed++;
                }
                isProgressed = true;
            }
        }
        if (!isProgressed) {
            time++;
        }
    }
}

// Display results
void displayResults(Process p[], int n) {
    float totalWaitingTime = 0, totalTurnaroundTime = 0;
    printf("\nPID\tArrival\tBurst\tCompletion\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++) {
        totalWaitingTime += p[i].waitingTime;
        totalTurnaroundTime += p[i].turnaroundTime;
        printf("%d\t%d\t%d\t%d\t\t%d\t%d\n", p[i].pid, p[i].arrivalTime, p[i].burstTime,
               p[i].completionTime, p[i].waitingTime, p[i].turnaroundTime);
    }

    printf("\nAverage Waiting Time: %.2f\n", totalWaitingTime / n);
    printf("Average Turnaround Time: %.2f\n", totalTurnaroundTime / n);
}
