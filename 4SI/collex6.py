lst = [1, 1, 2, 3, 3]
a = tuple(lst)
print(a)
b = list(a)
print(b)
print(len(b))
c = set(b)
print(c)
print(len(c))
rng = range(1, 11)
e = list(rng)
print(e)
directory = dict([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])
print(directory)
t = list(directory.items())
print(t)
v = list(directory.values())
print(v)
k = list(directory.keys())
print(k)
s = "antidisestablishmentarianism"
s2 = "".join(sorted(s))
print(s2)
strg = "the quick brown fox jumped over the lazy dog"
w = strg.split()
print(w)