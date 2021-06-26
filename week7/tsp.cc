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
  vector<int> visitation_order(0);
  return visitation_order;
}