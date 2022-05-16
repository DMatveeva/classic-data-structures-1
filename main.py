hf = 0
value = 'hello'
for letter in value:
    hf += ord(letter)
a = hf % 17
print(a)