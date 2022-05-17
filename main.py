hf = 0
value = '2'
for letter in value:
    hf += ord(letter)
a = hf % 17
print(a)