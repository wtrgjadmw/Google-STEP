def dfs(pages, links, arrived_time, searched_word):
  for k, v in pages.items():
    if v == 'Google':
      index_google = k
    if v == searched_word:
      index_item = k
      
  arrived_time[index_google] = 0
  stack = [index_google]
  
  while stack:
    index_tmp = stack.pop()
    for index_neighbor in links[index_tmp]:
      if arrived_time[index_neighbor] < 0:
        arrived_time[index_neighbor] = arrived_time[index_tmp] + 1
        if index_neighbor in links:
          stack.append(index_neighbor)
      else:
        arrived_time[index_neighbor] = min(arrived_time[index_neighbor], arrived_time[index_tmp] + 1)
  
  return arrived_time[index_item]

def bfs(pages, links, arrived_time, prev_spot, searched_word):
  for k, v in pages.items():
    if v == 'Google':
      index_google = k
    if v == searched_word:
      index_item = k
      
  arrived_time[index_google] = 0
  queue = [index_google]
  
  while queue:
    index_tmp = queue.pop(0)
    for index_neighbor in links[index_tmp]:
      if arrived_time[index_neighbor] < 0:
        arrived_time[index_neighbor] = arrived_time[index_tmp] + 1
        prev_spot[index_neighbor] = index_tmp
        if index_neighbor in links:
          queue.append(index_neighbor)
      else:
        if arrived_time[index_neighbor] > arrived_time[index_tmp] + 1:
          arrived_time[index_neighbor] = arrived_time[index_tmp] + 1
          prev_spot[index_neighbor] = index_tmp

  return arrived_time, prev_spot, index_item

def main():
  pages = {}
  links = {}

  max_page_id = 0
  with open('data/pages.txt') as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[int(page[0])] = page[1]
      max_page_id = max(max_page_id, int(page[0]))

  with open('data/links.txt') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      link[0], link[1] = int(link[0]), int(link[1])
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}

  arrived_time = [-1] * (max_page_id + 1)
  prev_spot = [""] * (max_page_id + 1)
  
  route = []
  arrived_time, prev_spot, tmp = bfs(pages, links, arrived_time, prev_spot, "渋谷")
  if arrived_time[tmp] == -1:
    print("is not connected")
  else:
    while pages[tmp] != "Google":
      route.append(pages[tmp])
      tmp = prev_spot[tmp]
    route.append(pages[tmp])
    route.reverse()
    print(route)


if __name__ == '__main__':
  main()
