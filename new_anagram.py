def new_find_anagram(word, counted_dict, datalist) :
  word = word.rstrip()
  counted_word = [0] * 26
  ans = []

  for i in range (len(word)) :
    counted_word[ord(word[i]) - ord("a")] += 1

  for i in range (len(counted_dict)) :
    is_anagram = True
    for j in range (26) :
      if counted_word[j] < counted_dict[i][j] :
        is_anagram = False
    if is_anagram :
      ans.append(datalist[i].rstrip())
  
  return ans


f = open("words.txt", "r")
datalist = f.readlines()

counted_dict = [[0] * 26 for i in range(len(datalist))]

for i in range (len(datalist)) :
  data = datalist[i].rstrip()
  for j in range (len(data)) :
    counted_dict[i][ord(data[j]) - ord("a")] += 1

words_f = open("small.txt", "r")
words = words_f.readlines()

for word in words :
  print(new_find_anagram(word.rstrip(), counted_dict, datalist))

# word = input()

# print(new_find_anagram(word, counted_dict, datalist))

