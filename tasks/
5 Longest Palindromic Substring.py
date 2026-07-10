s = "babad"
max_length = 0
max_s = ""
for left in range(0, len(s)+1):
    for right in range(left, len(s)+1):
        if len(s[left:right]) > max_length and s[left:right] == s[left:right][::-1]:
            max_length = len(s[left:right])
            max_s = s[left:right]
print(max_s)



