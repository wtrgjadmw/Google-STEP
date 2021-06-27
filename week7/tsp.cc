#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <string>

using namespace std;

vector<vector<double> > read_input_file(string filename) {
  ifstream file(filename);
  if (!file) {
    cout << "file not found" << endl;
    exit(1);
  }
  string line;
  vector<vector<double> > cities(2);
  getline(file, line);
  while(getline(file, line)) {
    auto comma_index = line.find(',');
    string x = line.substr(0, comma_index);
    string y = line.substr(comma_index + 1, line.size() - x.size() - 1);
    cities[0].push_back(stod(x));
    cities[1].push_back(stod(y));
  }
  return cities;
}

void write_output_file(string filename, vector<int> visitation_order) {
  ofstream file(filename);
  if (!file) {
    cerr << "file not found" << endl;
    exit(1);
  }
  file << "index" << endl;
  for (int i = 0; i < visitation_order.size(); i++) {
    file << visitation_order[i] << endl;
  }
  return;
}

double distance(vector<vector<double> > cities, int city1_index, int city2_index) {
  return sqrt(powf(cities[0][city1_index] - cities[0][city2_index], 2) + powf(cities[1][city1_index] - cities[1][city2_index], 2));
}

vector<vector<double> > distance_matrix(vector<vector<double> > cities) {
  int n = cities.size();
  vector<vector<double> > dist(n, vector<double>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      dist[i][j] = distance(cities, i, j);
      dist[j][i] = distance(cities, i, j);
    }
  }
  return dist;
}

double loop_distance(vector<vector<double> > dist, vector<int> visitation_order) {
  int n = dist.size();
  double res = 0;
  for (int i = 0; i < n; i++) {
    res += dist[visitation_order[i-1]][visitation_order[i]];
  }
  res += dist[visitation_order[n-1]][visitation_order[0]];
  return res;
}

vector<int> initialize_visitation_order(vector<vector<double> > cities) {
  int n = cities.size();
  vector<vector<double> > dist = distance_matrix(cities);
  int city_now = 0;
  vector<bool> visited_cities(n, false);
  vector<int> visitation_order(0);
  visited_cities[city_now] = true;
  for (int i = 0; i < n - 1; i++) {
    double min_dist = 100000000;
    int city_next = 0;
    for (int j = 0; j < n; j++) {
      if (!visited_cities[j]) {
        min_dist = min(min_dist, dist[city_now][city_next]);
        city_next = j;
      }
    }
    visited_cities[city_next] = true;
    visitation_order.push_back(city_next);
  }
  return visitation_order;
}

vector<int> exchange_two_node(vector<int> visitation_order, int i, int j, vector<vector<double> > dist) {
  int n = visitation_order.size();
  int front = visitation_order[i];
  int back = visitation_order[j];
  int front_next = visitation_order[i + 1];
  int back_next = visitation_order[(j + 1) % n];
  double dist_front = dist[front][front_next];
  double dist_back = dist[back][back_next];
  double dist_front_new = dist[front][back];
  double dist_back_new = dist[front_next][back_next];
  if (dist_front + dist_back > dist_front_new + dist_back_new) {
    vector<int> visitation_order_tmp = visitation_order;
    for (int k = i + 1; k < j + 1; k++) {
      visitation_order[k] = visitation_order_tmp[i + j + 1 - k];
    }
  }
  return visitation_order;
}

vector<int> solve(vector<vector<double> > cities) {
  int n = cities.size();
  vector<vector<double> > dist = distance_matrix(cities);
  vector<int> visitation_order = initialize_visitation_order(cities);
  for (int i = 0; i < 100; i++) {
    for (int j = 0; j < n - 2; j++) {
      for (int k = j + 2; k < n; k++) {
        visitation_order = exchange_two_node(visitation_order, j, k, dist);
      }
    }
  }
  double loop_dist = loop_distance(dist, visitation_order);
  printf("%lf\n", loop_dist);
  return visitation_order;
}

int main() {
  vector<vector<double> > cities = read_input_file("../week5/input_0.csv");
  vector<int> visitation_order = solve(cities);
  write_output_file("../week5/output_0.csv", visitation_order);
}