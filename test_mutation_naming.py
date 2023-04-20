
from core import whatsmyname

def test_mut_nam():
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