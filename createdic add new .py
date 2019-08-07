dic1={1:23}
dic2={4:56}
dic3={}
for d in (dic1,dic2):dic3.update(d)
print(dic3)