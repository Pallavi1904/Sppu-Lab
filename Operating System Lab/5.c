#include <stdio.h>
void main() {
    int n, m; // n: number of processes, m: number of resources
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    printf("Enter the number of resources: ");
    scanf("%d", &m);

    int available[m], max[n][m], allocation[n][m], need[n][m];

    // Input the available resources
    printf("Enter the available resources: ");
    for (int i = 0; i < m; i++) {
        scanf("%d", &available[i]);
    }

    // Input the maximum demand of each process
    printf("Enter the maximum demand matrix:\n");
    for (int i = 0; i < n; i++) {
        printf("For process P%d:\n", i);
        for (int j = 0; j < m; j++) {
            scanf("%d", &max[i][j]);
        }
    }

    // Input the allocation matrix
    printf("Enter the allocation matrix:\n");
    for (int i = 0; i < n; i++) {
        printf("For process P%d:\n", i);
        for (int j = 0; j < m; j++) {
            scanf("%d", &allocation[i][j]);
            // Calculate need matrix
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    // Initialize a safety sequence
    int safetySeq[n], finish[n];
    for (int i = 0; i < n; i++) {
        safetySeq[i] = -1; // Initialize with -1
        finish[i] = 0;     // Initialize finish array
    }

    int work[m];
    for (int i = 0; i < m; i++) {
        work[i] = available[i];
    }

    int count = 0, iteration = 0;

    while (count < n && iteration < n) {
        for (int i = 0; i < n; i++) {
            if (finish[i] == 0) {
                int j;
                for (j = 0; j < m; j++) {
                    if (need[i][j] > work[j]) {
                        break;
                    }
                }
                if (j == m) {
                    // Process can complete
                    for (int k = 0; k < m; k++) {
                        work[k] += allocation[i][k];
                    }
                    safetySeq[count++] = i;
                    finish[i] = 1;
                }
            }
        }
        iteration++;
    }

    if (count == n) {
        printf("Safe Sequence: ");
        for (int i = 0; i < n; i++) {
            printf("P%d", safetySeq[i]);
            if (i != n - 1) {
                printf(" -> ");
            }
        }
        printf("\n");
    } else {
        printf("Unsafe state: Deadlock detected!\n");
    }
}

