from core import whatsmyname


a = whatsmyname("diangelo", 0)
assert a == "diangelo.a"

a = whatsmyname("diangelo", 5)
assert a == "diangelo.f"

a = whatsmyname("diangelo", 25)
assert a == "diangelo.z"

a = whatsmyname("diangelo", 26)
assert a == "diangelo.a0"

a = whatsmyname("diangelo", 27)
assert a == "diangelo.aa"

a = whatsmyname("diangelo", 30)
assert a == "diangelo.ad"

a = whatsmyname("diangelo", 75)
assert a == "diangelo.bw"

a = whatsmyname("diangelo", 175)
assert a == "diangelo.fs"