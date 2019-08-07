from collections import Counter
d1 = {'a': 100, 'b': 200}
d2 = {'a': 300, 'b': 200}
d3 = {'a': 100, 'b': 100}
d = Counter(d1) + Counter(d2)+ Counter(d3)
print(d)