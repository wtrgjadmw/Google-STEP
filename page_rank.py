
def page_ranking(pages, links, page_rank):
  for index, link in links.items():
    for index_neighbor in link:
      page_rank[index_neighbor] += 100 / len(link)

  return page_rank


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
  page_rank = [0] * (max_page_id + 1)
  
  route = []
  page_rank = page_ranking(pages, links, page_rank)
  # print(page_rank)
  max_score, high_rank = 0, ""
  for i in range(max_page_id + 1):
    if max_score < page_rank[i]:
      max_score = page_rank[i]
      high_rank = pages[i]

  print(high_rank, max_score)


if __name__ == '__main__':
  main()
