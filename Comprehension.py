t="hi hello raju"
v=[]
c=[]
s=[]
x = [v.append(i) if i in 'aeiou' else s.append(i) if i == " " else c.append(i) for i in t]
print(v)
print(c)
print(s)