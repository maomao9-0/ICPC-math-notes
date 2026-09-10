"""Independent small-instance checks for chapters 00–03; not library templates."""
from itertools import combinations, product
from math import comb, gcd, isqrt, lcm


def check_foundations():
    for n in range(1, 15):
        assert sum(range(n + 1)) == n * (n + 1) // 2
        assert sum(k * comb(n, k) for k in range(n + 1)) == n * 2 ** (n - 1)
        if n >= 2:
            assert sum(k * (k - 1) * comb(n, k) for k in range(n + 1)) == n * (n - 1) * 2 ** (n - 2)
    assert [(x, y) for x in range(7) for y in range(6) if 6*x+9*y == 45] == [(0, 5), (3, 3), (6, 1)]
    # Enumerate the subgroup of reachable flip configurations on every graph <=4 vertices.
    for n in range(1, 5):
        edges = list(combinations(range(n), 2))
        for bits in range(1 << len(edges)):
            chosen = [e for i, e in enumerate(edges) if bits >> i & 1]
            reach = {0}
            for a, b in chosen:
                reach |= {v ^ (1 << a) ^ (1 << b) for v in list(reach)}
            components = []
            unseen = set(range(n))
            while unseen:
                comp = {unseen.pop()}
                changed = True
                while changed:
                    changed = False
                    for a, b in chosen:
                        if (a in comp) != (b in comp):
                            comp |= {a, b}
                            unseen -= {a, b}
                            changed = True
                components.append(sum(1 << a for a in comp))
            valid = {v for v in range(1 << n) if all((v & c).bit_count() % 2 == 0 for c in components)}
            assert reach == valid
    print('00: induction/counting identities, bounded solutions, every flip graph through 4 vertices passed')


def valuation(n, p):
    if n == 0:
        return float('inf')
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def check_modular():
    for m in range(1, 25):
        for a in range(m):
            for b in range(m):
                solutions = [x for x in range(m) if (a*x-b) % m == 0]
                g = gcd(a, m)
                assert len(solutions) == (g if b % g == 0 else 0)
    for m, n in product(range(1, 12), repeat=2):
        for a, b in product(range(m), range(n)):
            solutions = [x for x in range(lcm(m, n)) if x % m == a and x % n == b]
            assert len(solutions) == int((a-b) % gcd(m, n) == 0)
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        for k in range(1, 12):
            for a in range(1, p):
                roots = [x for x in range(p) if pow(x, k, p) == a]
                g = gcd(k, p-1)
                assert len(roots) == (g if pow(a, (p-1)//g, p) == 1 else 0)
        for x, y, n in product(range(1, 15), range(1, 15), range(1, 10)):
            if p > 2 and x != y and (x-y) % p == 0 and x*y % p:
                assert valuation(x**n-y**n, p) == valuation(x-y, p)+valuation(n, p)
    assert [x for x in range(8) if x*x % 8 == 1] == [1, 3, 5, 7]
    assert [x for x in range(7) if pow(x, 4, 7) == 4] == [3, 4]
    assert [x for x in range(13) if x*x % 13 == 10] == [6, 7]
    assert pow(6, 2**10, 72) == 0
    assert min(t for t in range(50, 100) if t % 6 == 1 and t % 8 == 3) == 67
    print('01: exhaustive congruence/CRT/root counts, LTE, Hensel examples and tower threshold passed')


def factors(n):
    result = {}
    for p in range(2, isqrt(n) + 1):
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
    if n > 1:
        result[n] = 1
    return result


def mu(n):
    f = factors(n)
    return 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)


def check_number_theory():
    for n in range(1, 201):
        divisors = [d for d in range(1, n+1) if n % d == 0]
        assert sum(mu(d) for d in divisors) == (n == 1)
        assert sum(sum(gcd(a, d) == 1 for a in range(1, d+1)) for d in divisors) == n
        represented = any(a*a+b*b == n for a in range(isqrt(n)+1) for b in range(isqrt(n)+1))
        assert represented == all(p % 4 != 3 or e % 2 == 0 for p, e in factors(n).items())
    for n in range(1, 30):
        assert sum(mu(d)*(n//d)**2 for d in range(1, n+1)) == sum(gcd(x, y) == 1 for x in range(1, n+1) for y in range(1, n+1))
        assert sum(i*(n//i) for i in range(1, n+1)) == sum(d for k in range(1, n+1) for d in range(1, k+1) if k % d == 0)
    assert sum(mu(d)*(12//d)**2 for d in range(1, 13) if 12 % d == 0) == 96
    assert [x for x in range(1, 11) if gcd(x, 12) == 2] == [2, 10]
    assert pow(2, 1023, 2047) == 1
    assert [sum(mu(d)*(i//d)**3 for d in range(1,i+1)) for i in range(1,5)] == [1,7,25,55]
    for maximum in range(2, 80):
        nonsquares = {a**e for e in range(3,maximum.bit_length(),2) for a in range(2,maximum+1) if a**e <= maximum and isqrt(a**e)**2 != a**e}
        for n in range(2,maximum+1):
            elegant = sum(gcd(*factors(x).values()) == 1 for x in range(2,n+1))
            assert elegant == n-isqrt(n)-sum(x <= n for x in nonsquares)
    print('02: Möbius/totient double counts, gcd and floor models, two-square criterion through 200 passed')


def check_sieves():
    for N in range(1, 101):
        primes = [p for p in range(2, N+1) if len(factors(p)) == 1 and factors(p).get(p) == 1]
        states = sorted({N//i for i in range(1, N+1)}, reverse=True)
        for k in [0, 1, 2]:
            g = {w: sum(i**k for i in range(2, w+1)) for w in states}
            for p in primes:
                for w in states:
                    if w >= p*p:
                        g[w] -= p**k * (g[w//p]-sum(q**k for q in primes if q < p))
            assert all(g[w] == sum(p**k for p in primes if p <= w) for w in states)
        for f in [lambda n: 1, mu, lambda n: sum(gcd(a,n) == 1 for a in range(1,n+1)), lambda n: len([d for d in range(1,n+1) if n%d == 0])]:
            def S(x, y):
                result = sum(f(p) for p in primes[y:] if p <= x)
                for i in range(y, len(primes)):
                    p = primes[i]
                    if p*p > x:
                        break
                    pe = p
                    while pe*p <= x:
                        result += f(pe)*S(x//pe, i+1)+f(pe*p)
                        pe *= p
                return result
            assert 1+S(N,0) == sum(f(n) for n in range(1,N+1))
        def M(x):
            if x == 1:
                return 1
            result, left = 1, 2
            while left <= x:
                right = x//(x//left)
                result -= (right-left+1)*M(x//left)
                left = right+1
            return result
        assert M(N) == sum(mu(n) for n in range(1,N+1))
        perfect = {a**b for a in range(2,N+1) for b in range(2,N.bit_length()) if a**b <= N}
        count = 0
        for e in range(2, N.bit_length()):
            root = max(a for a in range(1,N+1) if a**e <= N)
            count -= mu(e)*(root-1)
        assert len(perfect) == count
        assert sum(len([d for d in range(1,n+1) if n%d == 0]) for n in range(1,N+1)) == sum(sum(2**len(factors(n)) for n in range(1,N//(a*a)+1)) for a in range(1,isqrt(N)+1))
    print('03: prime-power prime sums, Min_25 decomposition, Mertens recurrence, perfect powers and sparse support through 100 passed')


if __name__ == '__main__':
    check_foundations()
    check_modular()
    check_number_theory()
    check_sieves()
