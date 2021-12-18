def max_num(s):
  num1, num2 = 0, 0
  for i in range(len(s)):
    if s[i] >= "0" and s[i] <= "9":
      num1 = num1*10 + int(s[i])
    else:
      if(num1>num2):
        num2 = num1
      num1 = 0
  if(num1>num2):
    return num1
  return num2


s = input()
max_num(s)
