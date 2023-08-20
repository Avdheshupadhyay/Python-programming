d1={"a":1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}
d4={}
for i in (d1,d2,d3):
    d4.update(i)
print(d4)
    