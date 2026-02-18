# 1
text = input()
digits = 0
for c in text:
    if c.isdigit():
        digits += 1
print(digits)

# 2
text = input()
letters = 0
for c in text:
    if c.isalpha():
        letters += 1
print(letters)

# 3
text = input()
new = ""
for c in text:
    if c.lower() not in "aeiou":
        new += c
print(new)

# 4
text = input()
words = text.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)

# 5
text = input()
res = ""
for c in text:
    if c.isupper():
        res += c.lower()
    else:
        res += c.upper()
print(res)
