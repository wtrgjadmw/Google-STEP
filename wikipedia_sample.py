import sys

def read_pages():
  pages = {}
  max_page_id = 0
  with open('data/pages.txt') as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[int(page[0])] = page[1]
      max_page_id = max(max_page_id, int(page[0]))
  return pages, max_page_id

def read_links():
  links = {}
  with open('data/links.txt') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      link[0], link[1] = int(link[0]), int(link[1])
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}
  return links

def bfs(pages, links, arrived_time, prev_spot, searched_word):
  for k, v in pages.items():
    if v == 'Google':
      index_google = k
    if v == searched_word:
      index_item = k

  try:
    index_item
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
        elif arrived_time[index_neighbor] > arrived_time[index_tmp] + 1:
          arrived_time[index_neighbor] = arrived_time[index_tmp] + 1
          prev_spot[index_neighbor] = index_tmp

    return arrived_time, prev_spot, index_item
  except NameError:
    print("The graph doesn't have the word")
    exit(1)

def print_route(max_page_id, pages, links, searched_word):
  arrived_time = [-1] * (max_page_id + 1)
  prev_spot = [""] * (max_page_id + 1)
  route = []
  arrived_time, prev_spot, tmp = bfs(pages, links, arrived_time, prev_spot, searched_word)
  if arrived_time[tmp] == -1:
    print("is not connected")
  else:
    while pages[tmp] != "Google":
      route.append(pages[tmp])
      tmp = prev_spot[tmp]
    route.append(pages[tmp])
    route.reverse()
    print(route)

def main():
  searched_word = sys.argv[1]
  pages, max_page_id = read_pages()
  links = read_links()
  print_route(max_page_id, pages, links, searched_word)

if __name__ == '__main__':
  main()
