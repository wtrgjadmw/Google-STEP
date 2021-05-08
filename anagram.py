def find_anagram(word, dict) :
  sorted_word = "".join(sorted(word))

  left = 0
  right = len(dict)

  while right >= left :
    mid = (left + right) // 2
    
    if dict[mid][0] < sorted_word :
      left = mid + 1
      continue
    elif dict[mid][0] > sorted_word :
      right = mid - 1
      continue
    
    return dict[mid][1:]
  
  return "This word doesn't have anagram"
  

f = open("words.txt", "r")
datalist = f.readlines()

sorted_dict = []

for data in datalist :
  data = data.rstrip()
  sorted_dict.append(["".join(sorted(data)), data])

sorted_dict = sorted(sorted_dict, key=lambda sorted_data: sorted_data[0])

tmp_sorted_word = ""
tmp_index = -1

new_sorted_dict = []

for i in range (len(sorted_dict)) :
  if tmp_sorted_word == sorted_dict[i][0] :
    new_sorted_dict[tmp_index].append(sorted_dict[i][1])
  else :
    tmp_sorted_word = sorted_dict[i][0]
    new_sorted_dict.append([tmp_sorted_word, sorted_dict[i][1]])
    tmp_index += 1

word = input()

print(find_anagram(word, new_sorted_dict))

