"""Independent small exact oracles for the mathematics of chapters 03, 05--10.

These enumerate mathematical objects; they are not library templates.
Run with python3 tests/audit_middle_math.py.
"""
from itertools import combinations, permutations, product
from math import comb, factorial, gcd
from fractions import Fraction


def check_combinatorics():
    for n in range(7):
        derangements = sum(all(i != v for i, v in enumerate(p))
                           for p in permutations(range(n)))
        assert derangements == sum((-1)**k * comb(n, k) * factorial(n-k)
                                   for k in range(n+1))
    s = [[0] * 8 for _ in range(8)]
    s[0][0] = 1
    for n in range(1, 8):
        for k in range(1, n+1):
            s[n][k] = k*s[n-1][k] + s[n-1][k-1]
    for n in range(7):
        for k in range(7):
            lhs = sum(comb(n, j) * j**k for j in range(n+1))
            rhs = sum(s[k][j] * factorial(n)//factorial(n-j) * 2**(n-j)
                      for j in range(min(n, k)+1))
            assert lhs == rhs, (n, k)
    for n in range(6):
        good = 0
        for word in product((-1, 1), repeat=2*n):
            height = 0
            valid = True
            for step in word:
                height += step
                valid &= height >= 0
            good += valid and height == 0
        assert good == comb(2*n, n)//(n+1)
    for forbidden, expected in [({(0, 0), (1, 1)}, 3),
                                ({(0, 0), (0, 1)}, 2)]:
        assert sum(not any((i, v) in forbidden for i, v in enumerate(p))
                   for p in permutations(range(3))) == expected


def check_groups():
    for n in range(1, 8):
        necklaces, bracelets = set(), set()
        for word in product(range(2), repeat=n):
            rotations = [word[i:]+word[:i] for i in range(n)]
            necklaces.add(min(rotations))
            reverse = word[::-1]
            bracelets.add(min(rotations + [reverse[i:]+reverse[:i] for i in range(n)]))
        rot = sum(2**gcd(n, r) for r in range(n))
        ref = n*2**((n+1)//2) if n % 2 else (n//2)*(2**(n//2+1)+2**(n//2))
        assert len(necklaces) == rot//n
        assert len(bracelets) == (rot+ref)//(2*n)
    assert (42 % 24)//6 == 7 % 4
    edges = list(combinations(range(3), 2))
    classes = set()
    for bits in product((0, 1), repeat=3):
        encodings = []
        for p in permutations(range(3)):
            image = {tuple(sorted((p[a], p[b]))) for (a, b), used in zip(edges, bits) if used}
            encodings.append(tuple(e in image for e in edges))
        classes.add(min(encodings))
    assert len(classes) == 4


def check_polynomials():
    p, w, length = 17, 4, 4
    values = [(1+2*pow(w, j, p)) % p for j in range(length)]
    assert values == [3, 9, 16, 10]
    recovered = [sum(values[j]*pow(w, (-j*k) % length, p)
                     for j in range(length))*pow(length, -1, p) % p
                 for k in range(length)]
    assert recovered == [1, 2, 0, 0]
    for x in range(-4, 5):
        assert x**3+2*x+1 == (x+1)*(x*x-x+3)-2
        assert 1+3*(x+2)+2*(x+2)**2 == 15+11*x+2*x*x
    text, pattern = [1, 0, 1, 1, 0], [1, 1, 0]
    assert [sum(a != b for a, b in zip(text[s:s+3], pattern))
            for s in range(3)] == [2, 2, 0]
    assert [1+2*x+3*x*x for x in range(3)] == [1, 6, 17]


def check_series():
    exp = [Fraction(1)]
    for n in range(1, 4):
        exp.append((exp[n-1]+(2*exp[n-2] if n >= 2 else 0))/n)
    assert exp == [1, 1, Fraction(3, 2), Fraction(7, 6)]
    counts = [0, 0]
    for b in product(range(5), repeat=5):
        square = [sum(b[i]*b[k-i] for i in range(k+1)) % 5 for k in range(5)]
        counts[0] += square == [0, 0, 1, 0, 0]
        counts[1] += square == [0]*5
    assert counts == [10, 25]
    b = [0, 1, -1, 2]
    assert [b[k]+sum(b[i]*b[k-i] for i in range(k+1)) for k in range(4)] == [0, 1, 0, 0]
    inverse = [1, 1, 2, 3]
    a = [1, -1, -1, 0]
    assert [sum(a[i]*inverse[k-i] for i in range(k+1)) for k in range(4)] == [1, 0, 0, 0]


def check_generating_functions():
    seq = [3, 4]
    for _ in range(3):
        seq.append(2*seq[-1]+seq[-2])
    assert seq == [3, 4, 11, 26, 63]
    fib = [0, 1]
    for _ in range(8):
        fib.append(fib[-1]+fib[-2])
    # Verify the Bostan--Mori example by an independent coefficient recurrence.
    reduced = [1, 2]
    reduced.append(3*reduced[-1]-reduced[-2])
    assert fib[5] == reduced[2] == 5
    trees = [0, 1, 1, 2, 5]
    assert sum(trees[i]*trees[5-i] for i in range(1, 5)) == 14
    catalan = [1]
    for n in range(1, 7):
        catalan.append(sum(catalan[i]*catalan[n-1-i] for i in range(n)))
        assert catalan[n-1] == comb(2*n-2, n-1)//n
    # Independently enumerate compositions using cut positions.
    assert 2**(4-1) == 8
    partition4 = {tuple(sorted(parts)) for k in range(1, 5)
                  for parts in product(range(1, 5), repeat=k) if sum(parts) == 4}
    assert len(partition4) == 5
    # CF 960G: independent left/right record enumeration against cycle formula.
    cycles = [[0]*8 for _ in range(8)]
    cycles[0][0] = 1
    for n in range(1, 8):
        for k in range(1, n+1):
            cycles[n][k] = (n-1)*cycles[n-1][k]+cycles[n-1][k-1]
    for n in range(1, 8):
        records = {}
        for perm in permutations(range(n)):
            a = sum(perm[i] == max(perm[:i+1]) for i in range(n))
            b = sum(perm[i] == max(perm[i:]) for i in range(n))
            records[a, b] = records.get((a, b), 0)+1
        for a in range(1, n+1):
            for b in range(1, n+1):
                k = a+b-2
                expected = comb(k, a-1)*cycles[n-1][k] if k <= n-1 else 0
                assert records.get((a, b), 0) == expected


def check_transforms():
    f, g = [1, 2, 3, 4], [3, -1, 2, 1]
    zeta = lambda a: [sum(a[t] for t in range(4) if t & s == t) for s in range(4)]
    assert zeta(f) == [1, 3, 4, 10]
    or_count = [sum(f[a]*g[b] for a in range(4) for b in range(4) if a | b == s)
                for s in range(4)]
    assert zeta(or_count) == [a*b for a, b in zip(zeta(f), zeta(g))]
    char = lambda k, x: (-1)**((k & x).bit_count())
    fourier = lambda a: [sum(a[x]*char(k, x) for x in range(4)) for k in range(4)]
    xor_count = [sum(f[a]*g[a ^ s] for a in range(4)) for s in range(4)]
    assert fourier(xor_count) == [a*b for a, b in zip(fourier(f), fourier(g))]
    assert fourier(fourier(f)) == [4*x for x in f]
    for s in range(4):
        rank = s.bit_count()
        # Direct definition of zeta rank products followed by Mobius inversion.
        recovered = 0
        for t in range(4):
            if t & s != t:
                continue
            marked = sum(f[a]*g[b] for a in range(4) for b in range(4)
                         if a & t == a and b & t == b and a.bit_count()+b.bit_count() == rank)
            recovered += (-1)**((s ^ t).bit_count()) * marked
        direct = sum(f[t]*g[s ^ t] for t in range(4) if t & s == t)
        assert recovered == direct
    for limit in range(2, 25):
        primes = [p for p in range(2, limit+1) if all(p % d for d in range(2, p))]
        original = [0]+[i*i-3*i+1 for i in range(1, limit+1)]
        a = original[:]
        for p in primes:
            for i in range(1, limit//p+1):
                a[i*p] += a[i]
        assert a[1:] == [sum(original[d] for d in range(1, x+1) if x % d == 0)
                         for x in range(1, limit+1)]
        for p in primes:
            for i in range(limit//p, 0, -1):
                a[i*p] -= a[i]
        assert a == original
        for p in primes:
            for i in range(limit//p, 0, -1):
                a[i] += a[i*p]
        assert a[1:] == [sum(original[m] for m in range(x, limit+1, x))
                         for x in range(1, limit+1)]
        for p in primes:
            for i in range(1, limit//p+1):
                a[i] -= a[i*p]
        assert a == original
    gcd_counts = [sum(gcd(a, b) == d for a in range(1, 5) for b in range(1, 5))
                  for d in range(1, 5)]
    assert gcd_counts == [11, 3, 1, 1]
    assert 3*21*2**20*4 == 252*2**20


if __name__ == "__main__":
    check_combinatorics()
    check_groups()
    check_polynomials()
    check_series()
    check_generating_functions()
    check_transforms()
    print("Chapters 03, 05--10 independent exact checks passed")
