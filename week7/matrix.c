#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
  int n = atoi(argv[1]);
  int *a = (int*)malloc(n * n * sizeof(int));
  int *b = (int*)malloc(n * n * sizeof(int));
  int *c = (int*)malloc(n * n * sizeof(int));
  struct timespec start, end;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      a[i * n + j] = i * n + j;
      b[i * n + j] = j * n + i;
      c[i * n + j] = 0;
    }
  }
  clock_gettime(CLOCK_REALTIME, &start);

  for (int k = 0; k < n; k++) {
    for (int j = 0; j < n; j++) {
      for (int i = 0; i < n; i++) {
        c[i * n + j] = a[i * n + k] * b[k * n + j];
      }
    }
  }

  clock_gettime(CLOCK_REALTIME, &end);
  double sec = end.tv_sec - start.tv_sec;
  double nsec = end.tv_nsec - start.tv_nsec;
  double time = sec + (nsec / 1000000000);
  printf("time: %fs\n", time);

}