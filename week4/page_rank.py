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

def page_ranking(pages, links, page_rank):
  for index, link in links.items():
    for index_neighbor in link:
      page_rank[index_neighbor] += 100 / len(link)
  return page_rank

def print_highrank(pages, links, max_page_id):
  page_rank = page_ranking(pages, links, [0] * (max_page_id + 1))
  # ALEX_NOTE:  the logic for choosing max_score below only works for positive numbers
  #             (which is okay here).
  #             However, if you initialize max_score with the first element,
  #             then it will work with any numbering space.
  max_score, high_rank = 0, ""
  for i in range(max_page_id + 1):
    if max_score < page_rank[i]:
      max_score = page_rank[i]
      high_rank = pages[i]
  print(high_rank, max_score)

def main():
  pages, max_page_id = read_pages()
  links = read_links()

  print_highrank(pages, links, max_page_id)

if __name__ == '__main__':
  main()
