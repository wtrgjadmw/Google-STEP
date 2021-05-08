import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

scores = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]

def new_find_anagram(word, counted_dict) :
  word = word.rstrip()
  counted_word = [0] * 26

  for i in range (len(word)) :
    counted_word[ord(word[i]) - ord("a")] += 1

  for i in range (len(counted_dict)) :
    is_anagram = True
    for j in range (26) :
      if counted_word[j] < counted_dict[i][j] :
        is_anagram = False
    
    if is_anagram:
      return counted_dict[i][26]
  


f = open("words.txt", "r")
datalist = f.readlines()

counted_dict = [[0] * 28 for i in range(len(datalist))]

for i in range (len(datalist)) :
  data = datalist[i].rstrip()
  counted_dict[i][26] = data
  for j in range (len(data)) :
    counted_dict[i][27] += scores[ord(data[j]) - ord("a")]
    counted_dict[i][ord(data[j]) - ord("a")] += 1

counted_dict = sorted(counted_dict, key=lambda counted_data: -counted_data[27])
input_f = open(input_filename, "r")
output_f = open(output_filename, "x")
words = input_f.readlines()

for word in words :
  output_f.write(new_find_anagram(word.rstrip(), counted_dict) + "\n")

# word = input()

# print(new_find_anagram(word, counted_dict, datalist))

