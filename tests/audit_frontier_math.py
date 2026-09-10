"""Independent small exact oracles for frontier chapter examples.

Uses only the Python standard library; these are validation tools, not book templates.
"""
from itertools import combinations, permutations, product
from fractions import Fraction
from math import comb, factorial, gcd


def pmul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def pmod(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def ppow(a, k, m):
    out = 1
    while k:
        if k & 1:
            out = pmod(pmul(out, a), m)
        a = pmod(pmul(a, a), m)
        k >>= 1
    return out


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def binary_polynomials():
    assert pmod(pmul(2, 3), 7) == 1
    for degree in range(1, 8):
        for f in range(1 << degree, 1 << (degree + 1)):
            trial = all(pmod(f, g) for d in range(1, degree // 2 + 1)
                        for g in range(1 << d, 1 << (d + 1)))
            # Check every proper divisor degree, independently of prime-factor pruning.
            cert = ppow(2, 1 << degree, f) == pmod(2, f)
            cert &= all(pgcd(f, ppow(2, 1 << d, f) ^ 2) == 1
                        for d in range(1, degree) if degree % d == 0)
            assert trial == cert, (degree, f)
    f = pmul(pmul(3, 7), 11)
    assert pgcd(f, 2**2 ^ 2) == 3  # x^2-x
    r = pmul(7, 11)
    assert pgcd(r, (1 << 4) ^ 2) == 7
    cube = pmul(pmul(3, 3), 3)
    assert next(k for k in range(1, 20) if pmod((1 << k) ^ 1, cube) == 0) == 4
    print("chapter 15: binary irreducibility exhaustively checked through degree 7; examples passed")


def submasks(s):
    t = s
    while True:
        yield t
        if not t:
            return
        t = (t - 1) & s


def convolution(f, g):
    return [sum(f[t] * g[s ^ t] for t in submasks(s)) for s in range(len(f))]


def ranked(f, g):
    size = len(f)
    n = size.bit_length() - 1
    layers = []
    for values in (f, g):
        z = [[values[s] if s.bit_count() == k else 0 for s in range(size)]
             for k in range(n + 1)]
        for k in range(n + 1):
            for i in range(n):
                for s in range(size):
                    if s >> i & 1:
                        z[k][s] += z[k][s ^ (1 << i)]
        layers.append(z)
    a, b = layers
    h = [[sum(a[i][s] * b[k-i][s] for i in range(k+1)) for s in range(size)]
         for k in range(n+1)]
    for k in range(n+1):
        for i in range(n):
            for s in range(size):
                if s >> i & 1:
                    h[k][s] -= h[k][s ^ (1 << i)]
    return [h[s.bit_count()][s] for s in range(size)]


def partition_exp(g):
    if len(g) == 1:
        return [1]
    m = len(g) // 2
    a = partition_exp(g[:m])
    return a + convolution(a, g[m:])


def connected(a):
    c = [0] * len(a)
    for s in range(1, len(a)):
        v = s & -s
        c[s] = a[s] - sum(c[t] * a[s ^ t] for t in submasks(s)
                          if t != s and t & v)
    return c


def determinant(a):
    n = len(a)
    out = 0
    for perm in permutations(range(n)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = sign
        for i, j in enumerate(perm):
            term *= a[i][j]
        out += term
    return out


def sadd(a, b):
    return [a[i]+b[i] for i in range(len(a))]


def scale(a, c):
    return [c*x for x in a]


def smul(a, b):
    return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(len(a))]


def sinv(a):
    b = [Fraction(1, a[0])] + [Fraction(0)]*(len(a)-1)
    for i in range(1, len(a)):
        b[i] = -sum(a[j]*b[i-j] for j in range(1, i+1))/a[0]
    return b


def sdiff(a):
    return [a[i+1]*(i+1) for i in range(len(a)-1)] + [Fraction(0)]


def spow(a, k):
    b = [Fraction(1)] + [Fraction(0)]*(len(a)-1)
    for _ in range(k):
        b = smul(b, a)
    return b


def sexp(a):
    assert a[0] == 0
    b = [Fraction(1)] + [Fraction(0)]*(len(a)-1)
    for i in range(1, len(a)):
        b[i] = sum(j*a[j]*b[i-j] for j in range(1, i+1))/i
    return b


def rectangular_series(d, size=10):
    one = [Fraction(1)] + [Fraction(0)]*(size-1)
    z = [Fraction(0), Fraction(1)] + [Fraction(0)]*(size-2)
    j = [Fraction(1)] + [Fraction(1, 2)]*(size-1)
    logh = [Fraction(0)] + [Fraction(1)+Fraction(1, 2*k)-(Fraction(1, 2) if k == 1 else 0)
                            for k in range(1, size)]
    h = sexp(logh)
    t = smul(z, smul(j, j))
    b = [Fraction(0)]*size
    for r in range(size):
        b = sadd(b, scale(spow(t, r), Fraction(1, factorial(r)*factorial(r+d))))
    value = smul(smul(h, spow(j, d)), b)
    q = sadd(sdiff(logh), scale(smul(sdiff(j), sinv(j)), d))
    tp = sdiff(t)
    za = sadd(smul(z, smul(sdiff(tp), sinv(tp))),
              scale(sadd(one, scale(smul(z, smul(sdiff(j), sinv(j))), 2)), -(d+1)))
    zb = smul(smul(tp, tp), sinv(smul(j, j)))
    coeff_d1 = scale(sadd(scale(smul(z, q), 2), za), -1)
    coeff_d0 = sadd(sadd(smul(z, sadd(smul(q, q), scale(sdiff(q), -1))), smul(za, q)), scale(zb, -1))
    residual = sadd(sadd(smul(z, sdiff(sdiff(value))), smul(coeff_d1, sdiff(value))), smul(coeff_d0, value))
    assert all(x == 0 for x in residual[:size-3]), (d, residual)
    return value


def grafy_sum(n):
    ans = 0
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                multi = factorial(n)//(factorial(i)*factorial(j)*factorial(k)*factorial(n-i-j-k))
                ans += multi*4**i*(-4)**j*(-2)**k*comb(n-i-j, k)*factorial(k)*factorial(2*n-2*i-j-2*k)
    assert ans % 4**n == 0
    return ans // 4**n


def capstones():
    def avoids_one(seq):
        span = {0}
        for v in seq:
            span |= {w ^ v for w in span}
        return 1 not in span
    for bits in range(1, 4):
        limit = min(4, 1 << bits)
        qs = [1]
        for r in range(1, limit+1):
            qs.append(qs[-1]*((1 << r)-1))
        gs = []
        for s in range(limit+1):
            count = Fraction(0)
            falling = 1
            for r in range(min(s, bits-1)+1):
                if r:
                    falling *= (1 << (bits-r))-1
                count += Fraction((1 << (r*(r+1)//2))*falling*qs[s], qs[r]*qs[s-r])
            gs.append(count)
            assert count == sum(avoids_one(seq) for seq in product(range(1 << bits), repeat=s))
            signed = [1]
            for j in range(s):
                nxt = [0]*(len(signed)+1)
                for i, v in enumerate(signed):
                    nxt[i] -= j*v
                    nxt[i+1] += v
                signed = nxt
            f = sum(signed[t]*gs[t] for t in range(s+1))
            assert f == sum(avoids_one(seq) for seq in permutations(range(1 << bits), s))
    for n in range(1, 4):
        for m in range(n, 4):
            direct = 0
            for mask in range(1 << (n*m)):
                rows = [sum(mask >> (i*m+j) & 1 for j in range(m)) for i in range(n)]
                cols = [sum(mask >> (i*m+j) & 1 for i in range(n)) for j in range(m)]
                direct += max(rows) <= 2 and max(cols) <= 2
            formula = factorial(n)*factorial(m)*rectangular_series(m-n)[n]
            assert direct == formula, (n, m, direct, formula)
    for d in range(6):
        rectangular_series(d)
    for n in range(3, 6):
        choices = [list(combinations([j for j in range(n) if j != i], 2)) for i in range(n)]
        direct = sum(all(sum(j in row for row in graph) == 2 for j in range(n)) for graph in product(*choices))
        assert direct == grafy_sum(n), (n, direct, grafy_sum(n))
    assert grafy_sum(3) == 1 and grafy_sum(4) == 9
    for n in range(1, 7):
        for k in range(n):
            direct = sum(a.bit_count()+b.bit_count()-(a+b).bit_count() == k
                         for a in range(1 << n) for b in range(1 << n))
            formula = 3**n if k == 0 else 0
            for t in range(1, k+1):
                if t <= n-k:
                    formula += comb(k-1, t-1)*comb(n-k, t)*3**(n-2*t)
                if t-1 <= n-k:
                    formula += comb(k-1, t-1)*comb(n-k, t-1)*3**(n-2*t+1)
            assert direct == formula, (n, k)
    # Invertibility of all q-factorials actually used by make 1.
    power = 1
    for _ in range(200000):
        power = power*2 % 998244353
        assert power != 1
    print("chapter 19: make-1 distinct/replacement enumeration, rectangular graph enumeration/DE, Grafy through n=5, carry pairs through n=6, q-units passed")


def holonomic():
    for n in range(30):
        assert (n+1)*comb(2*n+2, n+1) == 2*(2*n+1)*comb(2*n, n)
        assert sum(comb(n, k)**2 for k in range(n+1)) == comb(2*n, n)
        assert sum((comb(n+1, k)-2*(comb(n, k) if k <= n else 0))
                   for k in range(n+2)) == 0
    involutions = [1, 1]
    for n in range(2, 9):
        involutions.append(involutions[-1] + (n-1)*involutions[-2])
    for n in range(8):
        direct = sum(all(perm[perm[i]] == i for i in range(n)) for perm in permutations(range(n)))
        assert direct == involutions[n]
    assert involutions[:6] == [1, 1, 2, 4, 10, 26]
    assert comb(6, 3) % 3 == 2
    print("chapter 18: binomial identities through n=29, involutions by permutation enumeration through n=7 passed")


def graph_algebra():
    for values in product(range(-1, 2), repeat=6):
        a = [[0] * 4 for _ in range(4)]
        for (i, j), v in zip(combinations(range(4), 2), values):
            a[i][j], a[j][i] = v, -v
        pf = a[0][1]*a[2][3]-a[0][2]*a[1][3]+a[0][3]*a[1][2]
        assert determinant(a) == pf * pf
    assert sum((x-y) % 5 == 0 for x in range(5) for y in range(5)) == 5
    for y in range(6):
        a = [[0, y, y*y, 0], [-y, 0, 0, y*y], [-y*y, 0, 0, y], [0, -y*y, -y, 0]]
        assert determinant(a) == (y*y-y**4)**2
    print("chapter 17: Pfaffian identity checked on all 729 small alternating matrices; PIT/weighted examples passed")


def set_series():
    for n in range(1, 5):
        size = 1 << n
        for seed in range(12):
            f = [(s * s + seed * s + 3) % 7 - 3 for s in range(size)]
            g = [(s * 3 + seed) % 5 - 2 for s in range(size)]
            assert ranked(f, g) == convolution(f, g)
            g[0] = 0
            a = partition_exp(g)
            assert connected(a) == g
    assert convolution([0, 2, 3, 0], [0, 5, 7, 0])[3] == 29
    assert partition_exp([0] + [1]*7)[7] == 5
    assert connected([1, 1, 1, 2, 1, 2, 2, 8])[7] == 4
    assert connected([1, 2, 2, 6])[3] == 2
    print("chapter 16: ranked/direct convolution and partition inverse checked through n=4; examples passed")


if __name__ == "__main__":
    binary_polynomials()
    set_series()
    graph_algebra()
    holonomic()
    capstones()
