#wap to remove duplicates in a string using dictionary
#ip :- missisippi
#op :- misp
s = input()
char_dict = {}
r= ""
for ch in s:
    if ch not in char_dict:
        char_dict[ch] = True
        r += ch

print(r)
