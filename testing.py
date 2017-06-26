s = "hi's my name is bill"
arr = s.split(" ")
s = ""
for word in arr:
    s += word[::-1] + " "

print(s[:-1])
