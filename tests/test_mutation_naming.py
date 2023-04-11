



# input species name string

# output name with correct suffix

a1 = 'ox'
a2 = 0

b1 = 'ox.a'
b2 = 0

c1 = 'ox.b.a'
c2 = 0

d1 = 'ox'
d2 = 1

e1 = 'ox.a'
e2 = 1

f1 = 'ox.b.a'
f2 = 1

g1 = 'ox'
g2 = 4

h1 = 'ox.a'
h2 = 4

i1 = 'ox.b.a'
i2 = 4

def whatsmyname(name, mutation_count):

    def ltr_to_nbr(l):
        alphamap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                    'g': 7, 'h': 8, 'i':9}
        
        for k,v in alphamap.items():
            if k == l:
                return v
            
    def nbr_to_ltr(n):
        alphamap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                    'g': 7, 'h': 8, 'i':9}
        
        for k,v in alphamap.items():
            if v == n:
                return k
            
    if mutation_count == 0:
        mutation_name = name + ".a"
        return mutation_name

    elif mutation_count > 0:

        # increment ct and change to letter
        n = mutation_count + 1
        n = nbr_to_ltr(n)

        mutation_name = name + "." + n
    
        return mutation_name



# TEST 1
m = whatsmyname(a1, a2)
assert m == "ox.a"
print("TEST 1 pass")

# TEST 2
m = whatsmyname(b1, b2)
assert m == "ox.a.a"
print("TEST 2 pass")

# TEST 3
m = whatsmyname(c1, c2)
assert m == "ox.b.a.a"
print("TEST 3 pass")

# TEST 4
m = whatsmyname(d1, d2)
assert m == "ox.b"
print("TEST 4 pass")

# TEST 5
m = whatsmyname(e1, e2)
assert m == "ox.a.b"
print("TEST 5 pass")

# TEST 6
m = whatsmyname(f1, f2)
assert m =='ox.b.a.b'
print("TEST 6 pass")

# TEST 7
m = whatsmyname(g1, g2)
assert m =='ox.e'
print("TEST 7 pass")

# TEST 8
m = whatsmyname(h1, h2)
assert m =='ox.a.e'
print("TEST 8 pass")

# TEST 9
m = whatsmyname(i1, i2)
assert m =='ox.b.a.e'
print("TEST 9 pass")