#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// int city_number = 3000;

double** read_input_file(char* filename) {
  FILE *fp = fopen(filename, "r");
  if (fp == NULL) {
    printf("ファイルオープン終了");
    exit(1);
  }
  double cities[0]; 
  double x, y;
  // while(fscanf(fp, "%lf,%lf", &x, &y) != EOF) {
    // ファイルを一行ずつ読み込んで配列にする方法がわからなかったのでc言語でやるのは諦めました。
  //   cities += {x, y};
  // }
  fclose(fp);
  return cities;
} 