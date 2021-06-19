import math
import random

def read_input_file(filename):
  cities = []
  with open(filename) as f:
    next(f)
    line = f.readline()
    while line:
      coordinate = line.split(',')
      cities.append(list(map(float, coordinate)))
      line = f.readline()
  return cities

def write_output_file(filename, visitation_order):
  with open(filename, 'w') as f:
    f.write("index\n")
    for v in visitation_order:
      f.write(str(v) + "\n")
  return

def distance(city1, city2):
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def distance_matrix(cities):
  n = len(cities)
  dist = [[0] * n for i in range(n)]
  for i in range(n):
    for j in range(i, n):
      dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
  return dist

def loop_distance(dist, visitation_order):
  n = len(dist)
  res = 0
  for i in range(1, n):
    res += dist[visitation_order[i-1]][visitation_order[i]]
  res += dist[visitation_order[n-1]][visitation_order[0]]
  return res

def initialize_visitation_order(cities):
  n = len(cities)
  dist = distance_matrix(cities)
  city_now = 0
  unvisited_cities = set(range(1, n))
  visitation_order = [0]
  while len(unvisited_cities) > 0:
    min_dist = 10 ** 10
    city_next = 0
    for unvisited_city in unvisited_cities:
      min_dist = min(min_dist, dist[city_now][unvisited_city])
      city_next = unvisited_city
    unvisited_cities.remove(city_next)
    visitation_order.append(city_next)
  return visitation_order

def exchange_two_node(visitation_order, i, j, dist):
  n = len(visitation_order)
  front, back = visitation_order[i], visitation_order[j]
  front_next = visitation_order[i + 1]
  back_next = visitation_order[(j + 1) % n]
  dist_front = dist[front][front_next]
  dist_back = dist[back][back_next]
  dist_front_new = dist[front][back]
  dist_back_new = dist[front_next][back_next]
  if dist_front + dist_back > dist_front_new + dist_back_new:
    tmp = visitation_order[i + 1 : j + 1]
    tmp.reverse()
    visitation_order[i + 1 : j + 1] = tmp
  return visitation_order

def solve(cities):
  n = len(cities)
  dist = distance_matrix(cities)
  visitation_order = initialize_visitation_order(cities)
  for i in range(100):
    for j in range(n-2):
      for k in range(j+2, n):
        visitation_order = exchange_two_node(visitation_order, j, k, dist)
  res = loop_distance(dist, visitation_order)
  return res, visitation_order

  
def main():
  cities = read_input_file("input_6.csv")
  dist, visitation_order = solve(cities)
  print(dist)
  write_output_file("output_6.csv", visitation_order)

if __name__ == '__main__':
  main()


