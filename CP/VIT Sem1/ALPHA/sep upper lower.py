'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.'''


s = input("")
upper,lower = 0,0
for i in s:
  if(i>='A' and i<='Z'):
    upper = upper + 1
  if(i>='a' and i<='z'):
    lower = lower + 1
print(f"NUMBER OF UPPER: {upper}")
print(f"NUMBER OF LOWER: {lower}")

Vaasu Bisht
NUMBER OF UPPER: 2
NUMBER OF LOWER: 8

----------------------------------------

s = input("")
d={'upper':0,'lower':0}
for i in s:
  if(i>='A' and i<='Z'):
    d['upper'] = d['upper'] + 1
  if(i>='a' and i<='z'):
    d['lower'] = d['lower'] + 1

print(f"NUMBER OF UPPER: {d['upper']}")
print(f"NUMBER OF LOWER: {d['lower']}")

Vaasu Bisht
NUMBER OF UPPER: 2
NUMBER OF LOWER: 8
