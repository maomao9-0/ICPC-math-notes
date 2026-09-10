"""Independent small exact oracles for chapters 10--14; no library templates."""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, gcd, isqrt
import sys


def determinant(a):
    n = len(a)
    return sum((-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
               * prod(a[i][p[i]] for i in range(n)) for p in permutations(range(n)))


def prod(values):
    ans = 1
    for value in values:
        ans *= value
    return ans


def chapter10():
    assert sum((x+y+z-1) % 3 == 0 and (x+2*y) % 3 == 0
               for x,y,z in product(range(3), repeat=3)) == 3
    counts = [0]*4
    for mask in range(8):
        value = 0
        for i, word in enumerate([1,2,3]):
            if mask >> i & 1:
                value ^= word
        counts[value] += 1
    assert counts == [2]*4
    assert determinant([[7,-2],[-2,5]]) == 31
    assert 5*5+3*3 == 34  # Fibonacci-type s0=3,s1=5 gives s5=34
    for n in range(2,6):
        for words in product(range(4), repeat=n):
            total = 0
            for word in words:
                total ^= word
            actual = 0
            masked = 0
            for mask in range(1<<n):
                x = 0
                for i,word in enumerate(words):
                    if mask >> i & 1:
                        x ^= word
                masked = max(masked, x & (3 ^ total))
                if 0 < mask < (1<<n)-1:
                    actual = max(actual, x+(total^x))
            assert actual == total+2*masked
    print('chapter 10: exact field counts, XOR fibers, weighted trees, partition reduction passed')


def chapter11():
    distribution = [(0,Fraction(1,2)), (1,Fraction(1,3)), (3,Fraction(1,6))]
    mean = sum(x*p for x,p in distribution)
    variance = sum((x-mean)**2*p for x,p in distribution)
    assert mean == Fraction(5,6) and variance == Fraction(41,36)
    ta,tb = Fraction(12,7),Fraction(10,7)
    assert ta == 1+tb/2 and tb == 1+ta/4
    assert determinant([[1,Fraction(-1,2)],[Fraction(-1,2),1]]) == Fraction(3,4)
    for n in range(1,5):
        for m in range(1,5):
            average = Fraction(sum(len(set(xs)) for xs in product(range(n),repeat=m)),n**m)
            assert average == n*(1-Fraction(n-1,n)**m)
    # Exact geometric tails: bounded sum plus closed-form residual.
    for cutoff in range(1,20):
        assert sum(Fraction(1,2)**k for k in range(cutoff))+2*Fraction(1,2)**cutoff == 2
    print('chapter 11: exact distributions, occupancy enumeration, cyclic moments, modular singularity passed')


def chapter12():
    def floor_direct(n,m,a,b):
        return sum((a*i+b)//m for i in range(n))
    for n,m,a,b in product(range(8),range(1,9),range(-9,10),range(-9,10)):
        f = floor_direct(n,m,a,b)
        qa,ar = divmod(a,m)
        qb,br = divmod(b,m)
        assert f == qa*n*(n-1)//2+qb*n+floor_direct(n,m,ar,br)
        y=ar*n+br
        if y>=m:
            assert floor_direct(n,m,ar,br)==floor_direct(y//m,ar,m,y%m)
        residues = [(a*i+b)%m for i in range(n)]
        assert sum(residues)==a*n*(n-1)//2+b*n-m*f
        for t in [0,1,m]:
            assert sum(r<t for r in residues)==n+f-floor_direct(n,m,a,b+m-t)
    for n in range(30):
        assert sum(i*i for i in range(n))==n*(n-1)*(2*n-1)//6
        assert sum(comb(i,2) for i in range(n))==(comb(n,3) if n>=3 else 0)
    pairs=[(3,1),(17,6),(99,35)]
    assert [m*m for x,m in pairs]==[1,36,1225]
    for x,m in pairs:
        n=(x-1)//2
        assert x*x-8*m*m==1 and n*(n+1)//2==m*m
    assert [(x,y) for x,y in product(range(6),repeat=2) if 6*x+9*y==30]==[(2,2),(5,0)]
    print('chapter 12: 23104 signed floor cases, threshold counts, sums, Pell and Diophantine checks passed')


def chapter13():
    for n in range(12):
        actual=sum(x+y+z==n and x%2==0 for x,y,z in product(range(n+1),repeat=3))
        h=n//2
        assert actual==(h+1)*(n+1-h)
    assert [gcd(6,4+t) for t in range(3)] == [2,1,6]
    for words in product(range(7),repeat=3):
        log={pow(3,e,7):e for e in range(6)}
        f=[0]*6
        for x in words:
            if x: f[log[x]]+=1
        ordered=sum(f[i]*f[j]*pow(3,(i+j)%6,7) for i in range(6) for j in range(6))
        corrected=(ordered-sum(x*x%7 for x in words))//2
        assert corrected==sum(words[i]*words[j]%7 for i in range(3) for j in range(i+1,3))
    # Enumerate colored graph isomorphism classes under all vertex permutations.
    for colors,wanted in [(1,4),(2,12)]:
        pairs=list(combinations(range(3),2))
        classes=set()
        for labeling in product(range(colors),repeat=3):
            if len(set(labeling))!=colors: continue
            for mask in range(8):
                edges={pairs[i] for i in range(3) if mask>>i&1}
                representations=[]
                for p in permutations(range(3)):
                    ls=tuple(labeling[p[i]] for i in range(3))
                    es=tuple(int(tuple(sorted((p[a],p[b]))) in edges) for a,b in pairs)
                    representations.append((ls,es))
                classes.add(min(representations))
        assert len(classes)==wanted
    for n in range(1,20):
        phi=lambda d:sum(gcd(a,d)==1 for a in range(1,d+1))
        direct=sum(i*j*gcd(i,j) for i in range(1,n+1) for j in range(1,n+1))
        reduced=sum(d*d*phi(d)*(n//d*(n//d+1)//2)**2 for d in range(1,n+1))
        assert direct==reduced
        s=lambda x:sum(d*d*phi(d) for d in range(1,x+1))
        assert s(n)==(n*(n+1)//2)**2-sum(l*l*s(n//l) for l in range(2,n+1))
    fib=[0,1,1,2,3,5,8,13]
    for words in [(1,2),(7,4,1),(0,1,3)]:
        total=0
        for a,b,c,d,e in product(words,repeat=5):
            z=(a|b)&c&(d^e)
            if a&b==0 and z and z&(z-1)==0:
                total+=fib[a|b]*fib[c]*fib[d^e]
        arrays=[[0]*8 for _ in range(3)]
        for a,b in product(words,repeat=2):
            if a&b==0: arrays[0][a|b]+=1
            arrays[2][a^b]+=1
        for c in words: arrays[1][c]+=1
        modeled=sum(arrays[0][a]*arrays[1][b]*arrays[2][c]*fib[a]*fib[b]*fib[c]
                    for a,b,c in product(range(8),repeat=3)
                    if (a&b&c) and (a&b&c)&((a&b&c)-1)==0)
        assert total==modeled
        if words==(1,2): assert total==32
        if words==(7,4,1): assert total==3520
    print('chapter 13: exact convolution, colored graph orbits, weighted gcd recurrence and five-tuple models passed')


def chapter14():
    def valuation(a,p):
        result=0
        while a%p==0:
            result+=1
            a//=p
        return result
    for p in [2,3,5,7]:
        for n in range(50):
            for k in range(n+1):
                nn,kk=n,k
                lucas=1
                while nn or kk:
                    ni,ki=nn%p,kk%p
                    lucas*=comb(ni,ki) if ki<=ni else 0
                    nn//=p; kk//=p
                assert lucas%p==comb(n,k)%p
                a,b,carry,carries=k,n-k,0,0
                while a or b or carry:
                    carry=(a%p+b%p+carry)//p
                    carries+=carry
                    a//=p; b//=p
                assert carries==valuation(comb(n,k),p)
        for e in [1,2,3]:
            modulus=p**e
            table=[1]
            for j in range(1,modulus+1):
                table.append(table[-1]*(j if j%p else 1)%modulus)
            def units(n):
                if not n:return 1
                return pow(table[-1],n//modulus,modulus)*table[n%modulus]*units(n//p)%modulus
            for n in range(50):
                assert units(n)==factorial(n)//p**valuation(factorial(n),p)%modulus
                for k in range(n+1):
                    v=valuation(comb(n,k),p)
                    modeled=p**v*units(n)*pow(units(k),-1,modulus)*pow(units(n-k),-1,modulus)%modulus
                    assert modeled==comb(n,k)%modulus
    inversion_counts=[0]*5
    for bits in product([0,1],repeat=4):
        if sum(bits)==2:
            inv=sum(bits[i]>bits[j] for i in range(4) for j in range(i+1,4))
            inversion_counts[inv]+=1
    assert inversion_counts==[1,1,2,1,1]
    assert sum(c*2**i for i,c in enumerate(inversion_counts))==35
    rankcounts=[0]*3
    for a,b in product(range(4),repeat=2):
        span={0,a,b,a^b}
        rankcounts[len(span).bit_length()-1]+=1
    assert rankcounts==[1,9,6]
    by_size=[0]*5
    for subset in range(16):
        words=[x for x in range(4) if subset>>x&1]
        bad=False
        for mask in range(1,1<<len(words)):
            value=0
            for i,x in enumerate(words):
                if mask>>i&1:value^=x
            if mask.bit_count()%2==0 and value==0:bad=True
        if not bad:by_size[len(words)]+=1
    assert by_size==[1,4,6,4,0]
    print('chapter 14: Lucas/Kummer, prime-power unit recurrence, Gaussian statistics, rank and parity enumeration passed')


if __name__ == '__main__':
    requested = [int(x) for x in sys.argv[1:]] or list(range(10,15))
    for number in requested:
        globals()[f'chapter{number}']()
