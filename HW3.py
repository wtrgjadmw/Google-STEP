import sys

def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index <len(line) and line[index]=='.':
    digitCnt = 0
    number2 = 0
    index+=1
    while index < len(line) and line[index].isdigit():
      number2 = number2 *10 + int(line[index])
      index += 1
      digitCnt +=1 #小数点以下の桁数を数える
    number += number2/(10**digitCnt)
  token = {'type': 'NUMBER', 'number': number}
  return token, index

def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readMulti(line, index):
  token = {'type': 'MULTI'}
  return token, index + 1

def readDivide(line, index):
  token = {'type': 'DIVIDE'}
  return token, index + 1

def readBrackets(line, index):
  index += 1
  index_l = index
  while line[index] != ")" and index < len(line):
    if line[index] == "(":
      readBrackets(line, index)
    index += 1
  index_r = index
  print(line[index_l:index_r])
  tokens = tokenize(line[index_l:index_r])
  new_tokens = eval_part(tokens)
  answer = evaluate(new_tokens)
  new_token = {"type": "number", "number": answer}
  return new_token, index + 1

def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMulti(line, index)
    elif line[index] == '/':
      (token, index) = readDivide(line, index)
    elif line[index] == "(":
      (token, index) = readBrackets(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens

# 3 + 4 * 2 - 1 / 5 -> 3 + 8 - 0.2にする
def eval_part(tokens):
  new_tokens = []
  tmp = tokens[0]['number']
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'PLUS' or tokens[index]['type'] == 'MINUS':
      new_tokens.append({'type': 'NUMBER', 'number': tmp})
      new_tokens.append({'type': tokens[index]['type']})
      if index + 1 < len(tokens):
        tmp = tokens[index + 1]['number']
    elif tokens[index]['type'] == 'MULTI':
      tmp *= tokens[index + 1]['number']
    elif tokens[index]['type'] == 'DIVIDE':
      # tmp /= tokens[index + 1]['number']
      try:
        tmp /= tokens[index + 1]['number']
      except ZeroDivisionError:
        print("ZeroDivisionError!!")
        sys.exit()
    index += 2
  new_tokens.append({'type': 'NUMBER', 'number': tmp})
  return new_tokens


def evaluate(tokens):
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
      else:
        print('Invalid syntax')
    index += 1
  return answer

  
def test(line):
  tokens = tokenize(line)
  new_tokens = eval_part(tokens)
  actual_answer = evaluate(new_tokens)
  expected_answer = eval(line)
  if abs(actual_answer - expected_answer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expected_answer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
  print("==== Test started! ====")
  # test("1")
  # test("1+2")
  # test("1.0+2")
  # test("1.0+2.1")
  # test("1.0+2.1-3")
  # test("1.0+2.1-3.6")
  # test("1.0+2.1-3.6*2.4")
  # test("1.0+2.1/0.7-3.6*2.4/1.2")
  # test("1.0+2.1/0.7-3.6*2.4/1.2/0.6")
  # test("1.0*2.5+2.1/0.7-3.6*2.4/1.2/0.6")
  # test("1.0*2.5+2.1/0.7-3.6*2.4/1.2/0.6-2.4")
  # test("1*2+(2/0.5-3*2/2/1.5-1.2)")
  test("1*2+(2/0.5-(3*2/2/1.5-1.2))")
  # test("1*2+(2/0.5-(3*2/4-1.4)-1.2))")
  print("==== Test finished! ====\n")

run_test()

# while True:
#   line = input()
#   tokens = tokenize(line)
#   new_tokens = eval_part(tokens)
#   answer = evaluate(new_tokens)
#   print("answer = %f\n" % answer)
