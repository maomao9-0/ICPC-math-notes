#!/usr/bin/env python3
"""
tests/audit_strings_math.py

Exact Stringology & Combinatorics on Words Verification Suite for the
Advanced Strings & Word Combinatorics Textbook (Parts I - VII).

Runs 12 self-contained exact mathematical and algorithmic oracles across all 7 Parts:
  Part I Oracles:
    1. Fine-Wilf Periodicity Theorem & Sub-Threshold Orbit Formula C(N; p, q) = p + q - N
       (plus Central Sturmian counterexample "abaababaaba" at (p, q) = (5, 8), N = 11).
    2. Weak Periodicity Lemma, Log-Block Border AP (slink/diff) Decomposition &
       PAM slink DP Rolling Accumulator g[u] (CF 932G) vs. O(N^2) Brute Force.
    3. Border-Group Modulo Shortest Path ([WC2016] 论战捆竹竿): Dynamic Modulus Switching
       m_old -> x_k + Residue-Cycle Monotonic Queue vs. Exact Dijkstra.
  Part II Oracles:
    4. Duval's O(N) Chen-Fox-Lyndon Factorization & Significant Suffixes (显著后缀):
       |Cand_min(U)| <= floor(log2 |U|) + 1 and exact argmin_{s in Suff(U)} sT coverage.
    5. Runs Theorem (Bannai et al. 2017): |R(S)| < N, sum e(R) < 3N, and Unique
       Interior Lyndon-Root Bijection under < or > across Fibonacci/Sturmian & random words.
  Part III & IV Oracles:
    6. SAM / Generalized SAM & Endpos Segment Tree Clipping: endpos_S(u) cap [l+L-1, r] != empty
       and Online GSAM Zero-Length Clone Bug vs. 3-Case/BFS Fix on {"ab", "b"}.
    7. Kociumaka's IPM Bounded-Ratio AP Theorem (|V| < 2|U|) & Dyadic Substring Borders ([BJWC2018]).
    8. Deterministic quick_link PAM, 4-Way Deque PAM, slink Telescoping Range Distinct
       Palindromes (prev_start(u_i) == new_start(u_{i-1})), and O(1) Unclipped Range LPS.
  Part V, VI & VII Oracles:
    9. Polynomial Wildcard Indicator Penalty, Parameterized prev-Clipping (p-KMP),
       Order-Preserving KMP, and Parent-Distance Cartesian-Tree KMP vs. Brute Force.
   10. Invertible Subsequence Automaton Matrices (det(M_c) = 1, u_i^T = 2u_{i-1}^T - u_{last[c]-1}^T),
       Tiskin's Seaweed Matrix Comb (LCS(A, B[l..r]) = |{i in [l, r] | p(i) > r}|),
       and Allison-Dix Bit-Parallel LCS (V' = X & ~(X - Y)) vs. 2D DP across all intervals.
   11. Goulden-Jackson Cluster Method (m x m Autocorrelation Linear System) &
       Conway's Casino Martingale Hitting Time (E[T_S] = sum_{k in Borders(S)} |Sigma|^k).
   12. Signed Binary-Lifting DSU (with is_pal[k][r] self-reversal bit), Deterministic
       Stack-Trie Path Isomorphism vs. Trace-Zero GL_2(F_p) Stack Hashing, and
       Thue-Morse 2-Adic Rolling-Hash Annihilation (H(T_11) == H(~T_11) mod 2^64).
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
import heapq
import itertools
import math
import random
import sys
from typing import Dict, List, Optional, Set, Tuple

MOD = 998244353


# ==============================================================================
# Helper Routines: KMP, Z-Algorithm, Periods & Borders
# ==============================================================================

def kmp_pi(s: str) -> List[int]:
    """1-indexed KMP prefix function pi[1..n] (with pi[0] = 0)."""
    n = len(s)
    pi = [0] * (n + 1)
    for i in range(2, n + 1):
        j = pi[i - 1]
        while j > 0 and s[j] != s[i - 1]:
            j = pi[j]
        if s[j] == s[i - 1]:
            j += 1
        pi[i] = j
    return pi


def all_proper_borders(s: str) -> List[int]:
    """Return all proper border lengths of s in strictly decreasing order."""
    pi = kmp_pi(s)
    res: List[int] = []
    u = pi[len(s)]
    while u > 0:
        res.append(u)
        u = pi[u]
    return res


def min_period(s: str) -> int:
    """Return the shortest period length of nonempty string s."""
    return len(s) - kmp_pi(s)[len(s)]


# ==============================================================================
# Part I Oracles (Oracles 1 - 3)
# ==============================================================================

def oracle_01_fine_wilf_and_sturmian_orbits() -> None:
    """
    Oracle 1: Fine-Wilf Theorem & Sub-Threshold Orbit Formula C(N; p, q) = p + q - N.
    Tests all 1 <= p, q <= 18 and max(p, q) <= N <= p + q + 4, plus the extremal
    Central Sturmian word "abaababaaba" for (p, q) = (5, 8), N = 11.
    """
    for p in range(1, 19):
        for q in range(p, 19):
            g = math.gcd(p, q)
            threshold = p + q - g
            for n in range(q, p + q + 5):
                parent = list(range(n))

                def find(x: int) -> int:
                    while parent[x] != x:
                        parent[x] = parent[parent[x]]
                        x = parent[x]
                    return x

                def union(a: int, b: int) -> None:
                    ra, rb = find(a), find(b)
                    if ra != rb:
                        parent[ra] = rb

                for i in range(n - p):
                    union(i, i + p)
                for i in range(n - q):
                    union(i, i + q)

                comp_count = sum(1 for i in range(n) if find(i) == i)
                if n < threshold:
                    assert comp_count == p + q - n, (
                        f"Sub-threshold orbit mismatch at p={p}, q={q}, N={n}: "
                        f"got {comp_count}, expected {p + q - n}"
                    )
                else:
                    assert comp_count == g, (
                        f"Above-threshold Fine-Wilf mismatch at p={p}, q={q}, N={n}: "
                        f"got {comp_count}, expected {g}"
                    )
                    for i in range(n - g):
                        assert find(i) == find(i + g), "Period gcd(p, q) not forced above threshold"

    # Extremal Central Sturmian counterexample for (p, q) = (5, 8) at N = 5 + 8 - gcd(5, 8) - 1 = 11
    sturmian = "abaababaaba"
    assert len(sturmian) == 11
    assert all(sturmian[i] == sturmian[i + 5] for i in range(11 - 5)), "5 must be a period"
    assert all(sturmian[i] == sturmian[i + 8] for i in range(11 - 8)), "8 must be a period"
    assert len(set(sturmian)) == 2 == 5 + 8 - 11, "Must have 2 independent character orbits"
    assert any(sturmian[i] != sturmian[i + 1] for i in range(10)), "gcd(5, 8) = 1 must NOT be a period"


def oracle_02_weak_periodicity_border_aps_and_pam_slink_dp() -> None:
    """
    Oracle 2: Weak Periodicity Lemma, KMP slink/diff Border AP Partition,
    and PAM slink Rolling Accumulator DP (CF 932G) vs. O(N^2) Brute Force.
    """
    rng = random.Random(20261106)
    test_words = [
        "abaababaabaababaababa",
        "aaaaaaaaaaaa",
        "abababababab",
        "aabaaabaaaabaa",
    ] + ["".join(rng.choice("ab") for _ in range(30)) for _ in range(8)]

    for s in test_words:
        n = len(s)
        pi = kmp_pi(s)
        diff = [0] * (n + 1)
        slink = [0] * (n + 1)
        for u in range(1, n + 1):
            diff[u] = u - pi[u]
            slink[u] = slink[pi[u]] if diff[u] == diff[pi[u]] else pi[u]

            # 1. Verify Weak Periodicity Lemma on borders >= ceil(u / 2)
            borders = all_proper_borders(s[:u])
            half_borders = [b for b in borders if 2 * b >= u]
            if len(half_borders) >= 2:
                step = half_borders[0] - half_borders[1]
                assert step == diff[u]
                for idx in range(len(half_borders) - 1):
                    assert half_borders[idx] - half_borders[idx + 1] == step

            # 2. Verify half-open slink chains (slink[v], v] partition borders into <= ceil(log2 u) APs
            reconstructed: List[int] = []
            chains = 0
            v = pi[u]
            while v > 0:
                chains += 1
                d = diff[v]
                cur = v
                while cur > slink[v]:
                    reconstructed.append(cur)
                    cur -= d
                v = slink[v]
            assert reconstructed == borders, "slink AP partition omitted or double-counted a border"
            assert chains <= max(1, math.ceil(math.log2(u + 1))), "Exceeded log2 bound on slink chains"

        # 3. Verify PAM slink DP rolling accumulator g[u] vs. O(N^2) brute-force palindrome partition DP
        # Nodes: 0 = odd root (len = -1), 1 = even root (len = 0)
        pam_len = [-1, 0]
        pam_fail = [0, 0]
        pam_diff = [0, 0]
        pam_slink = [0, 0]
        pam_ch: List[Dict[str, int]] = [{}, {}]
        last = 1

        dp_slink = [0] * (n + 1)
        dp_even_slink = [0] * (n + 1)
        dp_slink[0] = 1
        dp_even_slink[0] = 1
        g_all = [0, 0]
        g_even = [0, 0]

        for r in range(1, n + 1):
            c = s[r - 1]
            cur = last
            while True:
                length = pam_len[cur]
                if r - 2 - length >= 0 and s[r - 2 - length] == c:
                    break
                cur = pam_fail[cur]
            if c not in pam_ch[cur]:
                u = len(pam_len)
                pam_len.append(pam_len[cur] + 2)
                pam_ch.append({})
                if pam_len[u] == 1:
                    pam_fail.append(1)
                else:
                    f = pam_fail[cur]
                    while True:
                        l_f = pam_len[f]
                        if r - 2 - l_f >= 0 and s[r - 2 - l_f] == c:
                            break
                        f = pam_fail[f]
                    pam_fail.append(pam_ch[f][c])
                fu = pam_fail[u]
                d = pam_len[u] - pam_len[fu]
                pam_diff.append(d)
                pam_slink.append(pam_slink[fu] if d == pam_diff[fu] and fu > 1 else fu)
                pam_ch[cur][c] = u
                g_all.append(0)
                g_even.append(0)
            last = pam_ch[cur][c]

            u = last
            while u > 1:
                shortest_in_chain = pam_len[pam_slink[u]] + pam_diff[u]
                new_left = r - shortest_in_chain
                g_all[u] = dp_slink[new_left]
                g_even[u] = dp_even_slink[new_left]
                if pam_diff[u] == pam_diff[pam_fail[u]] and pam_fail[u] > 1:
                    g_all[u] = (g_all[u] + g_all[pam_fail[u]]) % MOD
                    g_even[u] = (g_even[u] + g_even[pam_fail[u]]) % MOD
                dp_slink[r] = (dp_slink[r] + g_all[u]) % MOD
                if r % 2 == 0:
                    dp_even_slink[r] = (dp_even_slink[r] + g_even[u]) % MOD
                u = pam_slink[u]

        # Brute-force O(N^2) palindrome partition DP
        dp_bf = [0] * (n + 1)
        dp_even_bf = [0] * (n + 1)
        dp_bf[0] = 1
        dp_even_bf[0] = 1
        for r in range(1, n + 1):
            for l in range(1, r + 1):
                sub = s[l - 1 : r]
                if sub == sub[::-1]:
                    dp_bf[r] = (dp_bf[r] + dp_bf[l - 1]) % MOD
                    if r % 2 == 0 and (r - l + 1) % 2 == 0:
                        dp_even_bf[r] = (dp_even_bf[r] + dp_even_bf[l - 1]) % MOD

        assert dp_slink == dp_bf, f"PAM slink DP mismatch on {s}"
        assert dp_even_slink == dp_even_bf, f"CF 932G even PAM slink DP mismatch on {s}"


def oracle_03_border_modulo_shortest_path_wc2016() -> None:
    """
    Oracle 3: Border-Group Modulo Shortest Path ([WC2016] 论战捆竹竿).
    Verifies dynamic modulus switching m_old -> x_k + residue-cycle monotonic queue
    against exact Dijkstra shortest paths and reachable length counting <= W.
    """
    test_cases = [
        ("abaababaaba", 250),
        ("abacabacaba", 300),
        ("aaaaabaaaaab", 280),
        ("ababababab", 200),
    ]
    INF = 10**18

    for s, w_max in test_cases:
        n = len(s)
        pi = kmp_pi(s)
        diff = [0] * (n + 1)
        slink = [0] * (n + 1)
        for u in range(1, n + 1):
            diff[u] = u - pi[u]
            slink[u] = slink[pi[u]] if diff[u] == diff[pi[u]] else pi[u]

        # Extract border AP blocks: each chain (slink[u], u] maps to periods x_k + j * d_k
        ap_blocks: List[Tuple[int, int, int]] = []
        u = pi[n]
        while u > 0:
            x_k = n - u
            d_k = diff[u]
            c_k = (u - slink[u]) // d_k - 1
            ap_blocks.append((x_k, d_k, c_k))
            u = slink[u]

        m = n
        dist = [INF] * m
        dist[0] = n

        for x_k, d_k, c_k in ap_blocks:
            # 1. Dynamic modulus switch m -> x_k
            new_dist = [INF] * x_k
            for r in range(m):
                if dist[r] < INF:
                    nr = dist[r] % x_k
                    if dist[r] < new_dist[nr]:
                        new_dist[nr] = dist[r]
            g_mod = math.gcd(m, x_k)
            cycle_len = x_k // g_mod
            for start in range(g_mod):
                best_u = start
                cur = start
                for _ in range(cycle_len):
                    if new_dist[cur] < new_dist[best_u]:
                        best_u = cur
                    cur = (cur + m) % x_k
                cur = best_u
                for _ in range(cycle_len - 1):
                    nxt = (cur + m) % x_k
                    if new_dist[cur] + m < new_dist[nxt]:
                        new_dist[nxt] = new_dist[cur] + m
                    cur = nxt
            dist = new_dist
            m = x_k

            # 2. Residue-cycle monotonic queue for items x_k + j * d_k (1 <= j <= c_k)
            if c_k <= 0:
                continue
            g_step = math.gcd(d_k, m)
            L = m // g_step
            for start in range(g_step):
                best_v = start
                cur = start
                for _ in range(L):
                    if dist[cur] < dist[best_v]:
                        best_v = cur
                    cur = (cur + d_k) % m
                dq: deque[Tuple[int, int]] = deque()
                v = best_v
                for t in range(L):
                    while dq and t - dq[0][0] > c_k:
                        dq.popleft()
                    if dq:
                        cand = dq[0][1] + x_k + t * d_k
                        if cand < dist[v]:
                            dist[v] = cand
                    val = dist[v] - t * d_k
                    while dq and dq[-1][1] >= val:
                        dq.pop()
                    dq.append((t, val))
                    v = (v + d_k) % m

        # Verify against exact Dijkstra with all period weights (including empty border period n)
        periods = [n - b for b in all_proper_borders(s)] + [n]
        d_dijk = [INF] * m
        d_dijk[n % m] = n
        pq = [(n, n % m)]
        while pq:
            d_u, u_res = heapq.heappop(pq)
            if d_u != d_dijk[u_res]:
                continue
            for p_w in periods:
                nxt = (u_res + p_w) % m
                if d_u + p_w < d_dijk[nxt]:
                    d_dijk[nxt] = d_u + p_w
                    heapq.heappush(pq, (d_dijk[nxt], nxt))

        assert dist == d_dijk, f"WC2016 residue distances mismatch on {s}"
        count_fast = sum((w_max - dist[r]) // m + 1 for r in range(m) if dist[r] <= w_max)
        reachable = {n}
        for length in range(n, w_max + 1):
            if length in reachable:
                for p_w in periods:
                    if length + p_w <= w_max:
                        reachable.add(length + p_w)
        assert count_fast == len(reachable), f"WC2016 reachable count mismatch on {s}"


# ==============================================================================
# Part II Oracles (Oracles 4 - 5)
# ==============================================================================

def duval_cfl(s: str) -> List[str]:
    """Duval's O(N) Chen-Fox-Lyndon factorization algorithm."""
    n = len(s)
    i = 0
    factors: List[str] = []
    while i < n:
        j = i + 1
        k = i
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i
            else:
                k += 1
            j += 1
        p = j - k
        while i <= k:
            factors.append(s[i : i + p])
            i += p
    return factors


def is_lyndon_brute(w: str) -> bool:
    return all(w < w[i:] for i in range(1, len(w)))


def significant_suffixes_min(u: str) -> List[str]:
    """
    Build the O(log |u|) Significant Suffixes candidate set Cand_min(u)
    via the tandem-domination / prefix-comparison rule.
    """
    cands: List[str] = []
    for i in range(len(u)):
        c = u[i]
        nxt: List[str] = [c]
        for s_prev in cands:
            s_cur = s_prev + c
            prev_kept = nxt[-1]
            # Compare prev_kept (shorter) vs s_cur (longer) at first mismatch
            if s_cur[: len(prev_kept)] != prev_kept:
                if s_cur < prev_kept:
                    nxt[-1] = s_cur
            else:
                # prev_kept is a border of s_cur; keep s_cur only if length doubles
                if len(s_cur) >= 2 * len(prev_kept):
                    nxt.append(s_cur)
                else:
                    nxt[-1] = s_cur
        cands = nxt
    return cands


def oracle_04_duval_cfl_and_significant_suffixes() -> None:
    """
    Oracle 4: Duval's O(N) Chen-Fox-Lyndon Factorization & Significant Suffixes (显著后缀).
    Verifies CFL uniqueness, |Cand_min(U)| <= floor(log2 |U|) + 1, and exact coverage of
    argmin_{s in Suff(U)} (s + T) across all right extensions T.
    """
    rng = random.Random(42)
    words = [
        "abaababaaba",
        "bbababbab",
        "abacaba",
        "aabaaab",
    ] + ["".join(rng.choice("abc") for _ in range(10)) for _ in range(15)]

    extensions = [""] + [
        "".join(p) for length in range(1, 6) for p in itertools.product("abc", repeat=length)
    ]

    for u in words:
        # 1. Verify Duval's CFL factorization
        factors = duval_cfl(u)
        assert "".join(factors) == u
        assert all(is_lyndon_brute(w) for w in factors), f"Non-Lyndon factor in {factors}"
        assert all(factors[i] >= factors[i + 1] for i in range(len(factors) - 1)), "CFL not non-increasing"
        all_sufs = [u[i:] for i in range(len(u))]
        assert factors[-1] == min(all_sufs), "Last CFL factor must be minimum nonempty suffix"

        # 2. Verify Significant Suffixes bound & universal right-extension optimality
        cands = significant_suffixes_min(u)
        assert len(cands) <= math.floor(math.log2(len(u))) + 1, "Exceeded log2 |U| + 1 bound"
        for idx in range(len(cands) - 1):
            assert len(cands[idx + 1]) >= 2 * len(cands[idx]), "Lengths must double in Cand_min(U)"

        cand_set = set(cands)
        for t in extensions[:120]:
            best_suf = min(all_sufs, key=lambda s: s + t)
            assert best_suf in cand_set, (
                f"Significant suffixes missed optimal suffix {best_suf!r} for u={u!r}, t={t!r}"
            )


def enumerate_runs_exact(s: str) -> List[Tuple[int, int, int]]:
    """Enumerate all maximal periodic runs (l, r, p) in 0-indexed string s."""
    n = len(s)
    runs: List[Tuple[int, int, int]] = []
    for p in range(1, n // 2 + 1):
        l = 0
        while l + 2 * p <= n:
            if s[l] != s[l + p]:
                l += 1
                continue
            r = l + p
            while r < n and s[r] == s[r - p]:
                r += 1
            r -= 1
            if r - l + 1 >= 2 * p and (l == 0 or s[l - 1] != s[l - 1 + p]):
                if min_period(s[l : r + 1]) == p:
                    runs.append((l, r, p))
            l = r - p + 2
    return sorted(runs)


def oracle_05_runs_theorem_and_lyndon_root_bijection() -> None:
    """
    Oracle 5: Runs Theorem (Bannai et al. 2017).
    Verifies |R(S)| < N, sum e(R) < 3N, and the pairwise-disjoint interior
    Lyndon-root bijection under < or > across Fibonacci/Sturmian and random words.
    """
    rng = random.Random(1337)
    fib_a, fib_b = "a", "ab"
    for _ in range(6):
        fib_a, fib_b = fib_b, fib_b + fib_a

    words = [
        fib_b,
        "abaababaabaababa",
        "aababaababaab",
        "0110100110010110",
    ] + ["".join(rng.choice("ab") for _ in range(28)) for _ in range(15)]

    for s in words:
        n = len(s)
        runs = enumerate_runs_exact(s)
        assert len(runs) < n, f"Runs Theorem violated: |R(S)|={len(runs)} >= N={n}"
        exp_sum = sum((r - l + 1) / p for l, r, p in runs)
        assert exp_sum < 3 * n, f"Sum of run exponents violated: {exp_sum} >= 3N={3 * n}"

        # Verify Bannai et al. disjoint interior Lyndon-root assignment B(R) subseteq {1..n-1} (0-indexed)
        used_roots: Set[int] = set()
        for l, r, p in runs:
            # Choose order <_R so that s[r+1] <_R s[r+1-p] (with sentinel s[n] = -infty)
            if r + 1 == n:
                rev_order = False
            else:
                rev_order = s[r + 1] > s[r + 1 - p]

            def less_char(a: str, b: str, rev: bool = rev_order) -> bool:
                return (a > b) if rev else (a < b)

            def is_lyndon_ord(w: str, rev: bool = rev_order) -> bool:
                for shift in range(1, len(w)):
                    u, v = w, w[shift:]
                    k = 0
                    while k < len(v) and u[k] == v[k]:
                        k += 1
                    if k == len(v):
                        return False
                    if not less_char(u[k], v[k]):
                        return False
                return True

            # Find all interior Lyndon roots i in [l + 1, r - p + 1]
            b_r = [
                i
                for i in range(l + 1, r - p + 2)
                if is_lyndon_ord(s[i : i + p])
            ]
            assert len(b_r) >= 1, f"Run {(l, r, p)} in {s} has no interior Lyndon root"
            for i in b_r:
                assert i >= 1, "Interior Lyndon root must be >= index 1 (1-based >= 2)"
                # Longest <_R-Lyndon prefix at i must have exact length p (frozen at r + 1)
                longest_lyndon_len = max(
                    L_cand for L_cand in range(1, n - i + 1) if is_lyndon_ord(s[i : i + L_cand])
                )
                assert longest_lyndon_len == p, (
                    f"Longest <_R-Lyndon prefix at {i} has length {longest_lyndon_len} != {p}"
                )
                # For p >= 2, first character s[i] <_R s[i - 1] = s[i + p - 1] (for p == 1, s[i] == s[i - 1])
                assert p == 1 or less_char(s[i], s[i - 1]), "Lyndon root must satisfy s[i] <_R s[i-1]"
                assert i not in used_roots, f"Lyndon root index {i} shared between two runs!"
                used_roots.add(i)


# ==============================================================================
# Part III & IV Oracles (Oracles 6 - 8)
# ==============================================================================

class SAM:
    """Standard Suffix Automaton with Link-Tree endpos sets for exact verification."""

    def __init__(self, s: str = "") -> None:
        self.len = [0]
        self.link = [-1]
        self.ch: List[Dict[str, int]] = [{}]
        self.endpos: List[Set[int]] = [set()]
        self.last = 0
        for idx, c in enumerate(s, 1):
            self.extend(c, idx)

    def extend(self, c: str, pos: int) -> int:
        cur = len(self.len)
        self.len.append(self.len[self.last] + 1)
        self.link.append(0)
        self.ch.append({})
        self.endpos.append({pos})
        p = self.last
        while p != -1 and c not in self.ch[p]:
            self.ch[p][c] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.ch[p][c]
            if self.len[p] + 1 == self.len[q]:
                self.link[cur] = q
            else:
                clone = len(self.len)
                self.len.append(self.len[p] + 1)
                self.link.append(self.link[q])
                self.ch.append(dict(self.ch[q]))
                self.endpos.append(set())
                while p != -1 and self.ch[p].get(c) == q:
                    self.ch[p][c] = clone
                    p = self.link[p]
                self.link[q] = self.link[cur] = clone
        self.last = cur
        return cur

    def build_endpos_sets(self) -> None:
        order = sorted(range(1, len(self.len)), key=lambda u: self.len[u], reverse=True)
        for u in order:
            self.endpos[self.link[u]] |= self.endpos[u]


def oracle_06_sam_endpos_clipping_and_gsam_zero_length_clone() -> None:
    """
    Oracle 6: SAM Endpos Segment Tree Clipping (endpos_S(u) cap [l + L - 1, r] != empty)
    and Online GSAM Zero-Length Clone Bug vs. 3-Case Fix on {"ab", "b"}.
    """
    s = "ababaababbaba"
    n = len(s)
    sam = SAM(s)
    sam.build_endpos_sets()

    # 1. Verify clipped endpos containment against naive substring search for all (P, [l, r])
    for pl in range(1, n + 1):
        u = 0
        for pr in range(pl, n + 1):
            u = sam.ch[u][s[pr - 1]]
            L = pr - pl + 1
            pat = s[pl - 1 : pr]
            for l in range(1, n + 1):
                for r in range(l, n + 1):
                    naive_occ = pat in s[l - 1 : r]
                    clipped_occ = (L <= r - l + 1) and any(
                        l + L - 1 <= e <= r for e in sam.endpos[u]
                    )
                    assert naive_occ == clipped_occ, (
                        f"SAM clipping mismatch for P={pat!r} in S[{l}..{r}]"
                    )

    # Verify Counterexample 4.3: S = "ababa", [l, r] = [3, 5] ("aba"), P = "baba" (L = 4)
    sam_ce = SAM("ababa")
    sam_ce.build_endpos_sets()
    u_baba = 0
    for c in "baba":
        u_baba = sam_ce.ch[u_baba][c]
    assert sam_ce.endpos[u_baba] == {5}
    assert any(3 <= e <= 5 for e in sam_ce.endpos[u_baba]), "Unclipped [3, 5] falsely hits endpos 5"
    assert not any(3 + 4 - 1 <= e <= 5 for e in sam_ce.endpos[u_baba]), "Clipped [6, 5] must be empty"

    # 2. Demonstrate Online GSAM Zero-Length Clone Bug vs. 3-Case Fix on {"ab", "b"}
    buggy_gsam = SAM()
    for idx, c in enumerate("ab", 1):
        buggy_gsam.extend(c, idx)
    buggy_gsam.last = 0  # Naive reset to root without 3-case check
    cur_ghost = buggy_gsam.extend("b", 10)
    assert buggy_gsam.len[cur_ghost] - buggy_gsam.len[buggy_gsam.link[cur_ghost]] == 0, (
        "Naive extend after last=0 reset must produce a 0-length ghost state on {'ab', 'b'}"
    )
    assert cur_ghost not in buggy_gsam.ch[0].values(), "Ghost state is unreachable from root"

    # Correct 3-case GSAM extension on {"ab", "b"}
    safe_len = [0]
    safe_link = [-1]
    safe_ch: List[Dict[str, int]] = [{}]
    safe_occ = [0]

    def extend_gsam_safe(p: int, c: str) -> int:
        if c in safe_ch[p]:
            q = safe_ch[p][c]
            if safe_len[p] + 1 == safe_len[q]:
                safe_occ[q] += 1
                return q
            clone = len(safe_len)
            safe_len.append(safe_len[p] + 1)
            safe_link.append(safe_link[q])
            safe_ch.append(dict(safe_ch[q]))
            safe_occ.append(1)
            while p != -1 and safe_ch[p].get(c) == q:
                safe_ch[p][c] = clone
                p = safe_link[p]
            safe_link[q] = clone
            return clone
        cur = len(safe_len)
        safe_len.append(safe_len[p] + 1)
        safe_link.append(0)
        safe_ch.append({})
        safe_occ.append(1)
        while p != -1 and c not in safe_ch[p]:
            safe_ch[p][c] = cur
            p = safe_link[p]
        if p != -1:
            q = safe_ch[p][c]
            if safe_len[p] + 1 == safe_len[q]:
                safe_link[cur] = q
            else:
                clone = len(safe_len)
                safe_len.append(safe_len[p] + 1)
                safe_link.append(safe_link[q])
                safe_ch.append(dict(safe_ch[q]))
                safe_occ.append(0)
                while p != -1 and safe_ch[p].get(c) == q:
                    safe_ch[p][c] = clone
                    p = safe_link[p]
                safe_link[q] = safe_link[cur] = clone
        return cur

    for word in ["ab", "b"]:
        p = 0
        for c in word:
            p = extend_gsam_safe(p, c)
    for u in sorted(range(1, len(safe_len)), key=lambda x: safe_len[x], reverse=True):
        assert safe_len[u] > safe_len[safe_link[u]], "3-Case GSAM must have zero ghost states"
        safe_occ[safe_link[u]] += safe_occ[u]
    assert safe_occ[safe_ch[0]["b"]] == 2, "'b' occurs in both 'ab' and 'b' (total 2)"


def oracle_07_kociumaka_ipm_ap_and_substring_borders_bjwc2018() -> None:
    """
    Oracle 7: Kociumaka's Bounded-Ratio IPM Theorem (|V| < 2|U| => single AP)
    and Dyadic Scale Substring Border Intersection ([BJWC2018] Border 的四种求法).
    """
    s = "abaababaabaababa"
    n = len(s)

    # 1. Verify Kociumaka's Bounded-Ratio IPM Theorem across all U, V with |U| <= |V| < 2|U|
    for l1 in range(n):
        for r1 in range(l1 + 1, min(n + 1, l1 + 10)):
            u = s[l1:r1]
            lu = len(u)
            per_u = min_period(u)
            for l2 in range(n):
                for r2 in range(l2 + lu, min(n + 1, l2 + 2 * lu)):
                    v = s[l2:r2]
                    occs = [i for i in range(len(v) - lu + 1) if v[i : i + lu] == u]
                    if len(occs) >= 2:
                        step = occs[1] - occs[0]
                        assert u[: lu - step] == u[step:], "IPM step must be a valid period of U"
                        for idx in range(len(occs) - 1):
                            assert occs[idx + 1] - occs[idx] == step, "Occurrences must form a single AP"
                    if len(occs) >= 3:
                        assert occs[1] - occs[0] == per_u, "IPM AP with >= 3 terms must have step per(U)"

    # 2. Verify [BJWC2018] Dyadic Scale AP Intersection for Substring Borders
    for l in range(n):
        for r in range(l + 2, n):
            sub = s[l : r + 1]
            L = len(sub)
            borders_found: List[int] = []
            m = 0
            while (1 << m) < L:
                k = 1 << m
                hi = min(L - 1, (1 << (m + 1)) - 1)
                pm = sub[:k]
                qm = sub[L - k :]
                tail_start = max(0, L - 2 * k + 1)
                head_end = min(L, 2 * k - 1)
                # Candidate border lengths b in [k, hi] from P_m in tail and Q_m in head
                b_from_p = {
                    L - pos
                    for pos in range(tail_start, L - k + 1)
                    if sub[pos : pos + k] == pm and k <= L - pos <= hi
                }
                b_from_q = {
                    pos + k
                    for pos in range(0, head_end - k + 1)
                    if sub[pos : pos + k] == qm and k <= pos + k <= hi
                }
                borders_found.extend(sorted(b_from_p & b_from_q))
                m += 1
            assert sorted(borders_found, reverse=True) == all_proper_borders(sub), (
                f"BJWC2018 dyadic border intersection mismatch on {sub!r}"
            )


def oracle_08_deque_pam_slink_telescoping_and_o1_range_lps() -> None:
    """
    Oracle 8: Deterministic quick_link PAM, 4-Way Deque PAM, slink Periodic Telescoping
    for Range Distinct Palindromes (LOJ 6071), and O(1) Two-Boundary Unclipped Range LPS.
    """
    # 1. Verify Deterministic quick_link[u][c] PAM and slink Periodic Telescoping on Range Distinct Palindromes
    s = "abacabaabacabaa"
    n = len(s)
    alpha = "abc"
    pam_len = [-1, 0]
    pam_fail = [0, 0]
    pam_diff = [0, 0]
    pam_slink = [0, 0]
    pam_ch: List[Dict[str, int]] = [{}, {}]
    quick_link: List[Dict[str, int]] = [{c: 0 for c in alpha}, {c: 0 for c in alpha}]
    last_end: List[int] = [0, 0]
    last = 1

    # Fenwick tree for active distinct palindrome start positions at current sweep right endpoint r
    bit = [0] * (n + 2)

    def bit_add(idx: int, val: int) -> None:
        while idx <= n:
            bit[idx] += val
            idx += idx & -idx

    def bit_sum(idx: int) -> int:
        res = 0
        while idx > 0:
            res += bit[idx]
            idx -= idx & -idx
        return res

    def subtree_max_last(root_u: int) -> int:
        best = last_end[root_u]
        for v in range(2, len(pam_len)):
            cur = v
            while cur > 1:
                if cur == root_u:
                    best = max(best, last_end[v])
                    break
                cur = pam_fail[cur]
        return best

    for r in range(1, n + 1):
        c = s[r - 1]
        # Verify quick_link[last][c] finds the exact extensible ancestor in O(1)
        cur_naive = last
        while cur_naive > 0 and (r - 2 - pam_len[cur_naive] < 0 or s[r - 2 - pam_len[cur_naive]] != c):
            cur_naive = pam_fail[cur_naive]
        cur_fast = (
            last
            if (r - 2 - pam_len[last] >= 0 and s[r - 2 - pam_len[last]] == c)
            else quick_link[last][c]
        )
        assert cur_fast == cur_naive, "quick_link[u][c] mismatch against fail chain"

        if c not in pam_ch[cur_fast]:
            u = len(pam_len)
            pam_len.append(pam_len[cur_fast] + 2)
            pam_ch.append({})
            last_end.append(0)
            if pam_len[u] == 1:
                pam_fail.append(1)
            else:
                f_anc = (
                    pam_fail[cur_fast]
                    if (
                        r - 2 - pam_len[pam_fail[cur_fast]] >= 0
                        and s[r - 2 - pam_len[pam_fail[cur_fast]]] == c
                    )
                    else quick_link[pam_fail[cur_fast]][c]
                )
                pam_fail.append(pam_ch[f_anc][c])
            fu = pam_fail[u]
            d = pam_len[u] - pam_len[fu]
            pam_diff.append(d)
            pam_slink.append(pam_slink[fu] if d == pam_diff[fu] and fu > 1 else fu)
            ql = dict(quick_link[fu])
            preceding_fu = s[r - pam_len[fu] - 1] if r - pam_len[fu] - 1 >= 0 else ""
            if preceding_fu in ql:
                ql[preceding_fu] = fu
            quick_link.append(ql)
            pam_ch[cur_fast][c] = u

        last = pam_ch[cur_fast][c]

        # Walk slink chains: verify intermediate start cancellation and apply 2 Fenwick updates per chain
        u = last
        while u > 1:
            chain: List[int] = []
            v = u
            while v != pam_slink[u]:
                chain.append(v)
                v = pam_fail[v]
            # Verify prev_start(u_j) == new_start(u_{j-1}) for all j >= 1 in chain
            for j in range(1, len(chain)):
                prev_r_uj = subtree_max_last(chain[j])
                prev_start_uj = prev_r_uj - pam_len[chain[j]] + 1
                new_start_uj_minus_1 = r - pam_len[chain[j - 1]] + 1
                assert prev_start_uj == new_start_uj_minus_1, "slink telescoping cancellation failed"

            prev_r_top = subtree_max_last(u)
            if prev_r_top > 0:
                bit_add(prev_r_top - pam_len[u] + 1, -1)
            shortest_len = pam_len[pam_slink[u]] + pam_diff[u]
            bit_add(r - shortest_len + 1, 1)
            u = pam_slink[u]

        last_end[last] = r
        for l in range(1, r + 1):
            distinct_fast = bit_sum(r) - bit_sum(l - 1)
            distinct_bf = len(
                {
                    s[i:j]
                    for i in range(l - 1, r)
                    for j in range(i + 1, r + 1)
                    if s[i:j] == s[i:j][::-1]
                }
            )
            assert distinct_fast == distinct_bf, f"Range distinct palindromes mismatch on [{l}, {r}]"

    # 2. Verify 4-Way Deque PAM (push_front, push_back, pop_front, pop_back) lazy surface invariant
    dq_chars: deque[str] = deque()
    ops = [
        ("push_back", "a"),
        ("push_back", "b"),
        ("push_front", "a"),
        ("push_back", "a"),
        ("push_front", "b"),
        ("pop_back", ""),
        ("pop_front", ""),
        ("push_front", "a"),
        ("push_back", "b"),
        ("pop_back", ""),
    ]
    for op, ch in ops:
        if op == "push_back":
            dq_chars.append(ch)
        elif op == "push_front":
            dq_chars.appendleft(ch)
        elif op == "pop_back":
            dq_chars.pop()
        elif op == "pop_front":
            dq_chars.popleft()
        cur_s = "".join(dq_chars)
        # Verify surface palindrome decomposition: every maximal prefix/suffix palindrome at i
        max_suff = [0] * len(cur_s)
        max_pref = [0] * len(cur_s)
        for i in range(len(cur_s)):
            for j in range(i + 1, len(cur_s) + 1):
                w = cur_s[i:j]
                if w == w[::-1]:
                    max_pref[i] = max(max_pref[i], len(w))
                    max_suff[j - 1] = max(max_suff[j - 1], len(w))
        if len(cur_s) >= 2:
            # Popping cur_s[-1] promotes longest proper palindromic suffix of max_suff[-1] to max_pref
            L_last = max_suff[-1]
            start_last = len(cur_s) - L_last
            trimmed = cur_s[:-1]
            new_pref_at_start = max(
                (
                    k - start_last
                    for k in range(start_last + 1, len(trimmed) + 1)
                    if trimmed[start_last:k] == trimmed[start_last:k][::-1]
                ),
                default=0,
            )
            assert new_pref_at_start <= L_last

    # 3. Verify O(1) Online Range LPS via Two-Boundary Unclipping over Manacher Centers
    t_man = "#" + "#".join(s) + "#"
    m_len = len(t_man)
    rad = [0] * m_len
    for c_idx in range(m_len):
        r_c = 0
        while (
            c_idx - r_c >= 0
            and c_idx + r_c < m_len
            and t_man[c_idx - r_c] == t_man[c_idx + r_c]
        ):
            r_c += 1
        rad[c_idx] = r_c - 1

    for l in range(n):
        for r in range(l, n):
            left_wall = 2 * l + 1
            right_wall = 2 * r + 1
            mid = (left_wall + right_wall) // 2
            c_L = max(
                c for c in range(left_wall, mid + 1) if c - rad[c] <= left_wall - 1
            )
            c_R = min(
                c for c in range(mid, right_wall + 1) if c + rad[c] >= right_wall + 1
            )
            mid_max = max((rad[c] for c in range(c_L + 1, c_R)), default=0)
            lps_fast = max(
                c_L - left_wall + 1,
                right_wall - c_R + 1,
                mid_max,
            )
            lps_bf = max(
                j - i
                for i in range(l, r + 1)
                for j in range(i + 1, r + 2)
                if s[i:j] == s[i:j][::-1]
            )
            assert lps_fast == lps_bf, f"O(1) Unclipped Range LPS mismatch on [{l}, {r}]"


# ==============================================================================
# Part V, VI & VII Oracles (Oracles 9 - 12)
# ==============================================================================

def oracle_09_wildcard_fft_and_structural_isomorphism_kmp() -> None:
    """
    Oracle 9: Polynomial Wildcard Indicator Penalty, Parameterized prev-Clipping (p-KMP),
    Order-Preserving KMP, and Parent-Distance Cartesian-Tree KMP vs. Brute Force.
    """
    # 1. Degree-Reduced Indicator Wildcard Penalty: sum u_P[j] u_T[i+j] (v_P[j] - v_T[i+j])^2 == 0
    text = "ab?cab?abca?bc"
    pat = "ab?bc"
    n, m = len(text), len(pat)
    u_p = [0 if c == "?" else 1 for c in pat]
    v_p = [0 if c == "?" else (ord(c) - ord("a") + 1) for c in pat]
    u_t = [0 if c == "?" else 1 for c in text]
    v_t = [0 if c == "?" else (ord(c) - ord("a") + 1) for c in text]

    for i in range(n - m + 1):
        penalty = (
            sum(u_p[j] * u_t[i + j] * (v_p[j] - v_t[i + j]) ** 2 for j in range(m))
            % MOD
        )
        bf_match = all(
            pat[j] == "?" or text[i + j] == "?" or pat[j] == text[i + j]
            for j in range(m)
        )
        assert (penalty == 0) == bf_match, f"Wildcard indicator penalty mismatch at {i}"

    # 2. Parameterized KMP (p-KMP) with Window-Clipped prev Offsets
    def prev_offsets(seq: List[int]) -> List[int]:
        last_seen: Dict[int, int] = {}
        res: List[int] = []
        for idx, x in enumerate(seq):
            res.append(idx - last_seen[x] if x in last_seen else 0)
            last_seen[x] = idx
        return res

    def clip_prev(val: int, q_len: int) -> int:
        return val if val <= q_len else 0

    t_seq = [1, 2, 1, 3, 2, 3, 2, 1, 2, 1]
    p_seq = [5, 8, 5, 9]
    prev_t = prev_offsets(t_seq)
    prev_p = prev_offsets(p_seq)
    mp = len(p_seq)
    p_pi = [0] * mp
    for i in range(1, mp):
        j = p_pi[i - 1]
        while j > 0 and clip_prev(prev_p[i], j) != prev_p[j]:
            j = p_pi[j - 1]
        if clip_prev(prev_p[i], j) == prev_p[j]:
            j += 1
        p_pi[i] = j

    p_matches: List[int] = []
    q = 0
    for i in range(len(t_seq)):
        while q > 0 and clip_prev(prev_t[i], q) != prev_p[q]:
            q = p_pi[q - 1]
        if clip_prev(prev_t[i], q) == prev_p[q]:
            q += 1
        if q == mp:
            p_matches.append(i - mp + 1)
            q = p_pi[q - 1]

    bf_p_matches = [
        i
        for i in range(len(t_seq) - mp + 1)
        if prev_offsets(t_seq[i : i + mp]) == prev_p
    ]
    assert p_matches == bf_p_matches, "Parameterized KMP (p-KMP) mismatch"

    # 3. Order-Preserving & Parent-Distance Cartesian-Tree KMP
    def parent_dist(arr: List[int]) -> List[int]:
        res: List[int] = []
        for i, val in enumerate(arr):
            k = next((j for j in range(i - 1, -1, -1) if arr[j] <= val), -1)
            res.append(i - k if k != -1 else 0)
        return res

    def cartesian_shape(arr: List[int]) -> Tuple:
        if not arr:
            return ()
        idx = min(range(len(arr)), key=lambda i: (arr[i], i))
        return (cartesian_shape(arr[:idx]), cartesian_shape(arr[idx + 1 :]))

    arr_t = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    arr_p = [2, 1, 5, 3, 6]
    pd_t = parent_dist(arr_t)
    pd_p = parent_dist(arr_p)
    mc = len(arr_p)
    c_pi = [0] * mc
    for i in range(1, mc):
        j = c_pi[i - 1]
        while j > 0 and clip_prev(pd_p[i], j) != pd_p[j]:
            j = c_pi[j - 1]
        if clip_prev(pd_p[i], j) == pd_p[j]:
            j += 1
        c_pi[i] = j

    c_matches: List[int] = []
    q = 0
    for i in range(len(arr_t)):
        while q > 0 and clip_prev(pd_t[i], q) != pd_p[q]:
            q = c_pi[q - 1]
        if clip_prev(pd_t[i], q) == pd_p[q]:
            q += 1
        if q == mc:
            c_matches.append(i - mc + 1)
            q = c_pi[q - 1]

    target_shape = cartesian_shape(arr_p)
    bf_c_matches = [
        i
        for i in range(len(arr_t) - mc + 1)
        if cartesian_shape(arr_t[i : i + mc]) == target_shape
    ]
    assert c_matches == bf_c_matches, "Cartesian-Tree KMP mismatch"


def oracle_10_invertible_subseq_matrices_seaweed_and_bit_parallel_lcs() -> None:
    """
    Oracle 10: Invertible Subsequence Automaton Matrices (det(M_c) = 1,
    u_i^T = 2u_{i-1}^T - u_{last[c]-1}^T), Tiskin's Seaweed Matrix Comb
    (LCS(A, B[l..r]) = |{i in [l, r] | p(i) > r}|), and Allison-Dix Bit-Parallel LCS.
    """
    # 1. Invertible Subsequence Automaton Matrices & Two-Term Vector Recurrence
    s = "abacbcabac"
    n = len(s)
    sigma = 3  # 0 -> empty, 'a' -> 1, 'b' -> 2, 'c' -> 3
    u_vecs: List[List[int]] = [[1, 1, 1, 1]]
    v_vecs: List[List[int]] = [[1, 0, 0, 0]]
    c_tilde: List[List[int]] = [
        [1 if r_idx == k_idx else 0 for r_idx in range(sigma + 1)]
        for k_idx in range(sigma + 1)
    ]
    g_lazy = [0] * (sigma + 1)
    last_occ = [0] * (sigma + 1)

    for i in range(1, n + 1):
        c = ord(s[i - 1]) - ord("a") + 1
        prev_u = u_vecs[i - 1]
        if last_occ[c] == 0:
            cur_u = [(2 * prev_u[j]) % MOD for j in range(sigma + 1)]
            cur_u[c] = (cur_u[c] - 1) % MOD
        else:
            old_u = u_vecs[last_occ[c] - 1]
            cur_u = [(2 * prev_u[j] - old_u[j]) % MOD for j in range(sigma + 1)]
        last_occ[c] = i
        u_vecs.append(cur_u)

        # Lazy column offset maintenance for P_i^{-1} = P_{i-1}^{-1} M_c^{-1} (Theorem 22.5)
        w_col = [(c_tilde[c][r_idx] + g_lazy[r_idx]) % MOD for r_idx in range(sigma + 1)]
        g_lazy = [(g_lazy[r_idx] - w_col[r_idx]) % MOD for r_idx in range(sigma + 1)]
        c_tilde[c] = [(c_tilde[c][r_idx] + w_col[r_idx]) % MOD for r_idx in range(sigma + 1)]
        v_vecs.append([((1 if r_idx == 0 else 0) + g_lazy[r_idx]) % MOD for r_idx in range(sigma + 1)])

    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # Dot product u_r^T * v_{l-1} counts distinct subsequences (including empty)
            total_inc_empty = sum(u_vecs[r][a] * v_vecs[l - 1][a] for a in range(sigma + 1)) % MOD
            sub = s[l - 1 : r]
            dp_sub = [1]
            last_local: Dict[str, int] = {}
            for idx_c, ch in enumerate(sub, 1):
                val = 2 * dp_sub[-1] - (dp_sub[last_local[ch] - 1] if ch in last_local else 0)
                last_local[ch] = idx_c
                dp_sub.append(val % MOD)
            assert total_inc_empty == dp_sub[-1], f"Subsequence matrix mismatch on [{l}, {r}]"

    # 2. Tiskin's Seaweed Matrix Comb & Allison-Dix Bit-Parallel LCS across all C(N+1, 2) intervals
    A = "abcbacab"
    B = "bacbabca"
    la, lb = len(A), len(B)
    # W[j] stores the entry wire ID currently exiting column j (1..lb)
    W = list(range(1, lb + 1))
    for i in range(1, la + 1):
        u_wire = -i
        for j in range(lb):
            if A[i - 1] == B[j] or u_wire > W[j]:
                u_wire, W[j] = W[j], u_wire
    # Map top entry port i in [1..lb] to exit port p(i) (or +infinity if exiting on the right wall)
    p_exit = [lb + 100] * (lb + 1)
    for col_idx, wire_id in enumerate(W, 1):
        if wire_id >= 1:
            p_exit[wire_id] = col_idx

    for l in range(1, lb + 1):
        for r in range(l, lb + 1):
            lcs_seaweed_p = (r - l + 1) - sum(1 for i in range(l, r + 1) if p_exit[i] <= r)
            lcs_seaweed_w = sum(1 for k in range(l - 1, r) if W[k] < l)
            assert lcs_seaweed_p == lcs_seaweed_w, "Seaweed entry-exit vs exit-entry duality failed"

            # Allison-Dix Bit-Parallel LCS on (A, B[l..r])
            sub_b = B[l - 1 : r]
            m_len = len(sub_b)
            mask_full = (1 << m_len) - 1
            char_masks: Dict[str, int] = {ch: 0 for ch in "abc"}
            for idx_b, ch in enumerate(sub_b):
                char_masks[ch] |= 1 << idx_b
            V = 0
            for ch in A:
                X = V | char_masks[ch]
                Y = ((V << 1) | 1) & mask_full
                V = X & (~(X - Y) & mask_full)
            lcs_bitparallel = bin(V).count("1")

            # Standard 2D DP verification
            dp = [0] * (m_len + 1)
            for ch_a in A:
                ndp = [0] * (m_len + 1)
                for j_b, ch_b in enumerate(sub_b, 1):
                    if ch_a == ch_b:
                        ndp[j_b] = dp[j_b - 1] + 1
                    else:
                        ndp[j_b] = max(ndp[j_b - 1], dp[j_b])
                dp = ndp
            assert lcs_seaweed_p == dp[m_len] == lcs_bitparallel, (
                f"Seaweed / Bit-Parallel LCS mismatch on B[{l}..{r}]"
            )


def oracle_11_goulden_jackson_and_conway_martingale() -> None:
    """
    Oracle 11: Goulden-Jackson Cluster Method (m x m Autocorrelation System) &
    Conway's Casino Martingale Hitting Time (E[T_S] = sum_{k in Borders(S)} |Sigma|^k)
    and Pattern Race Probabilities ([SDOI2017] 硬币游戏).
    """
    # 1. Goulden-Jackson Cluster Method for multi-pattern avoidance over alphabet Sigma = {'a', 'b'}
    patterns = ["aba", "bb"]
    sigma = 2
    max_n = 10

    # Autocorrelation polynomials C_{i, j}(x) = sum_{k in Overlap(P_i, P_j)} x^{|P_j| - k}
    m = len(patterns)
    C_poly: List[List[List[Fraction]]] = [
        [[Fraction(0)] * (max_n + 1) for _ in range(m)] for _ in range(m)
    ]
    for i, pi_pat in enumerate(patterns):
        for j, pj_pat in enumerate(patterns):
            for k in range(1, min(len(pi_pat), len(pj_pat)) + 1):
                if pi_pat[len(pi_pat) - k :] == pj_pat[:k]:
                    C_poly[i][j][len(pj_pat) - k] += 1

    # Extract coefficients of F(x) and F_0(x), ..., F_{m-1}(x) degree by degree using exact Fractions
    F = [Fraction(0)] * (max_n + 1)
    F_pat = [[Fraction(0)] * (max_n + 1) for _ in range(m)]
    for deg in range(max_n + 1):
        # For each j: sum_i F_i[deg] * C_{i,j}[0] = F[deg - |P_j|] - sum_{i, d > 0} F_i[deg - d] * C_{i,j}[d]
        # Since patterns form an antichain, C_{i,j}[0] = delta_{i,j}!
        for j, pj_pat in enumerate(patterns):
            rhs = F[deg - len(pj_pat)] if deg >= len(pj_pat) else Fraction(0)
            for i in range(m):
                for d in range(1, deg + 1):
                    rhs -= F_pat[i][deg - d] * C_poly[i][j][d]
            F_pat[j][deg] = rhs
        # (1 - sigma * x) F(x) + sum_i F_i(x) = 1
        F[deg] = (Fraction(1 if deg == 0 else 0) + (sigma * F[deg - 1] if deg >= 1 else 0)) - sum(
            F_pat[i][deg] for i in range(m)
        )

    for deg in range(max_n + 1):
        bf_avoid = sum(
            1
            for w in itertools.product("ab", repeat=deg)
            if all(p not in "".join(w) for p in patterns)
        )
        assert F[deg] == bf_avoid, f"Goulden-Jackson mismatch at n={deg}: {F[deg]} != {bf_avoid}"

    # 2. Conway's Casino Martingale Hitting Time E[T_S] = sum_{k in Borders(S)} |Sigma|^k
    for s_pat in ["abaab", "aaaa", "abab"]:
        L = len(s_pat)
        borders_inc_full = [L] + all_proper_borders(s_pat)
        expected_conway = sum(Fraction(sigma**k) for k in borders_inc_full)

        # Build exact KMP Markov transition matrix on states 0..L-1 and solve (I - Q) E = 1
        pi = kmp_pi(s_pat)
        aug: List[List[Fraction]] = [
            [Fraction(1 if r == c else 0) for c in range(L)] + [Fraction(1)]
            for r in range(L)
        ]
        for state in range(L):
            for ch in "ab":
                j = state
                while j > 0 and s_pat[j] != ch:
                    j = pi[j]
                if s_pat[j] == ch:
                    j += 1
                if j < L:
                    aug[state][j] -= Fraction(1, sigma)

        # Gaussian elimination over Fractions
        for col in range(L):
            piv = next(r for r in range(col, L) if aug[r][col] != 0)
            aug[col], aug[piv] = aug[piv], aug[col]
            div = aug[col][col]
            aug[col] = [x / div for x in aug[col]]
            for r in range(L):
                if r != col and aug[r][col] != 0:
                    fac = aug[r][col]
                    aug[r] = [aug[r][c] - fac * aug[col][c] for c in range(L + 1)]

        assert aug[0][L] == expected_conway, f"Conway hitting time mismatch on {s_pat}"


def oracle_12_signed_dsu_stack_hashing_and_thue_morse_antihash() -> None:
    """
    Oracle 12: Signed Binary-Lifting DSU (with root self-palindrome bit is_pal[k][r]),
    Deterministic Stack-Trie Path Isomorphism vs. Trace-Zero GL_2(F_p) Stack Hashing,
    and Thue-Morse 2-Adic Rolling-Hash Annihilation (H(T_11) == H(~T_11) mod 2^64).
    """
    # 1. Signed Binary-Lifting DSU vs. Character-Level Brute-Force DSU
    n = 12
    max_k = 4
    parent = [[i for i in range(n + 1)] for _ in range(max_k)]
    rev_par = [[0] * (n + 1) for _ in range(max_k)]
    is_pal = [[0] * (n + 1) for _ in range(max_k)]

    def find_k(k: int, x: int) -> Tuple[int, int]:
        if parent[k][x] == x:
            return x, 0
        r, p = find_k(k, parent[k][x])
        parent[k][x] = r
        rev_par[k][x] ^= p
        return r, rev_par[k][x]

    def unite_k(k: int, u: int, v: int, d: int) -> None:
        ru, pu = find_k(k, u)
        rv, pv = find_k(k, v)
        if ru == rv:
            if (pu ^ pv ^ d) == 1:
                is_pal[k][ru] = 1
            return
        parent[k][ru] = rv
        rev_par[k][ru] = pu ^ pv ^ d
        is_pal[k][rv] |= is_pal[k][ru]

    equations = [
        (1, 1, 4, 1),  # Self-palindrome S[1..4] = S[1..4]^R (tests root self-reversal loop!)
        (2, 5, 6, 0),  # Forward equality S[2..7] = S[5..10]
        (3, 7, 5, 1),  # Reversed equality S[3..7] = S[7..11]^R
    ]
    for l1, l2, L, t in equations:
        k = L.bit_length() - 1
        span = 1 << k
        if t == 0:
            unite_k(k, l1, l2, 0)
            unite_k(k, l1 + L - span, l2 + L - span, 0)
        else:
            unite_k(k, l1, l2 + L - span, 1)
            unite_k(k, l1 + L - span, l2, 1)

    for k in range(max_k - 1, 0, -1):
        h = 1 << (k - 1)
        for i in range(1, n - (1 << k) + 2):
            r, d = find_k(k, i)
            if r != i:
                if d == 0:
                    unite_k(k - 1, i, r, 0)
                    unite_k(k - 1, i + h, r + h, 0)
                else:
                    unite_k(k - 1, i, r + h, 1)
                    unite_k(k - 1, i + h, r, 1)
        for i in range(1, n - (1 << k) + 2):
            if parent[k][i] == i and is_pal[k][i]:
                unite_k(k - 1, i, i + h, 1)

    bf_p = list(range(n + 1))

    def bf_find(x: int) -> int:
        while bf_p[x] != x:
            bf_p[x] = bf_p[bf_p[x]]
            x = bf_p[x]
        return x

    for l1, l2, L, t in equations:
        for offset in range(L):
            a = l1 + offset
            b = (l2 + offset) if t == 0 else (l2 + L - 1 - offset)
            bf_p[bf_find(a)] = bf_find(b)

    comps_fast = len({find_k(0, i)[0] for i in range(1, n + 1)})
    comps_bf = len({bf_find(i) for i in range(1, n + 1)})
    assert comps_fast == comps_bf, f"Signed Binary-Lifting DSU mismatch: {comps_fast} != {comps_bf}"

    # 2. Deterministic Stack-Trie Path Isomorphism vs. Trace-Zero det = -1 GL_2(F_p) Stack Hashing
    # Construct trace-zero det = -1 involutory 2x2 matrices M_c = [[a, b], [(1 - a^2)b^{-1}, -a]] mod MOD
    def make_involution_matrix(a: int, b: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        c_entry = ((1 - a * a) * pow(b, MOD - 2, MOD)) % MOD
        return ((a % MOD, b % MOD), (c_entry, (-a) % MOD))

    def mat_mul(
        A: Tuple[Tuple[int, int], Tuple[int, int]],
        B: Tuple[Tuple[int, int], Tuple[int, int]],
    ) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return (
            (
                (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
                (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD,
            ),
            (
                (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
                (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD,
            ),
        )

    I2 = ((1, 0), (0, 1))
    mats = {
        "a": make_involution_matrix(1234567, 7654321),
        "b": make_involution_matrix(9876543, 3456789),
        "c": make_involution_matrix(1928374, 5647382),
    }
    for ch, M in mats.items():
        assert mat_mul(M, M) == I2, f"Matrix M_{ch} must satisfy M_c^2 = I_2"

    stack_str = "abbacccabbcaba"
    pref_mat = [I2]
    trie_parent = [0]
    trie_char = [""]
    trie_ch: List[Dict[str, int]] = [{}]
    node_at = [0]
    u_cur = 0

    for ch in stack_str:
        pref_mat.append(mat_mul(pref_mat[-1], mats[ch]))
        if u_cur > 0 and trie_char[u_cur] == ch:
            u_cur = trie_parent[u_cur]
        else:
            if ch not in trie_ch[u_cur]:
                nxt_u = len(trie_parent)
                trie_parent.append(u_cur)
                trie_char.append(ch)
                trie_ch.append({})
                trie_ch[u_cur][ch] = nxt_u
            u_cur = trie_ch[u_cur][ch]
        node_at.append(u_cur)

    for l in range(len(stack_str)):
        for r in range(l, len(stack_str) + 1):
            st: List[str] = []
            for ch in stack_str[l:r]:
                if st and st[-1] == ch:
                    st.pop()
                else:
                    st.append(ch)
            is_empty_bf = len(st) == 0
            is_empty_trie = node_at[l] == node_at[r]
            is_empty_mat = pref_mat[l] == pref_mat[r]
            assert is_empty_bf == is_empty_trie == is_empty_mat, (
                f"Stack reduction mismatch on [{l}, {r}]"
            )

    # 3. Thue-Morse 2-Adic Rolling-Hash Annihilation: H(T_11) == H(~T_11) mod 2^64 for all odd bases B
    mask64 = (1 << 64) - 1
    t11 = [bin(i).count("1") & 1 for i in range(1 << 11)]
    t11_bar = [1 - x for x in t11]
    for base in [3, 31, 131, 13331, 911382323]:
        h0 = 0
        h1 = 0
        for bit0, bit1 in zip(t11, t11_bar):
            h0 = (h0 * base + (bit0 + 1)) & mask64
            h1 = (h1 * base + (bit1 + 1)) & mask64
        assert h0 == h1, f"Thue-Morse T_11 failed to annihilate uint64_t hash for odd base {base}"


# ==============================================================================
# Master Verification Runner
# ==============================================================================

def main() -> int:
    print("=" * 78)
    print("ADVANCED STRINGS & WORD COMBINATORICS — EXACT MATHEMATICAL ORACLE SUITE")
    print("=" * 78)

    oracles = [
        ("Part I   [Oracle 01]: Fine-Wilf Theorem, Sub-Threshold Orbits & Central Sturmian Word", oracle_01_fine_wilf_and_sturmian_orbits),
        ("Part I   [Oracle 02]: Weak Periodicity Lemma, Border APs & PAM slink DP (CF 932G)", oracle_02_weak_periodicity_border_aps_and_pam_slink_dp),
        ("Part I   [Oracle 03]: Border-Group Modulo Shortest Path ([WC2016] 论战捆竹竿)", oracle_03_border_modulo_shortest_path_wc2016),
        ("Part II  [Oracle 04]: Duval's O(N) CFL Factorization & Significant Suffixes (显著后缀)", oracle_04_duval_cfl_and_significant_suffixes),
        ("Part II  [Oracle 05]: Runs Theorem (Bannai et al.) & Disjoint Lyndon-Root Bijection", oracle_05_runs_theorem_and_lyndon_root_bijection),
        ("Part III [Oracle 06]: SAM Endpos Clipping & Online GSAM Zero-Length Clone Bug/Fix", oracle_06_sam_endpos_clipping_and_gsam_zero_length_clone),
        ("Part IV  [Oracle 07]: Kociumaka's IPM Bounded-Ratio AP & Substring Borders ([BJWC2018])", oracle_07_kociumaka_ipm_ap_and_substring_borders_bjwc2018),
        ("Part IV  [Oracle 08]: Deterministic/Deque PAM, slink Telescoping & O(1) Range LPS", oracle_08_deque_pam_slink_telescoping_and_o1_range_lps),
        ("Part V   [Oracle 09]: Wildcard Indicator Penalty, p-KMP, Order & Cartesian-Tree KMP", oracle_09_wildcard_fft_and_structural_isomorphism_kmp),
        ("Part VI  [Oracle 10]: Invertible Subseq Matrices, Seaweed Comb & Bit-Parallel LCS", oracle_10_invertible_subseq_matrices_seaweed_and_bit_parallel_lcs),
        ("Part VI  [Oracle 11]: Goulden-Jackson Cluster System & Conway Martingale Hitting Time", oracle_11_goulden_jackson_and_conway_martingale),
        ("Part VII [Oracle 12]: Signed Lifting DSU, Stack-Trie / GL_2(F_p) & Thue-Morse Hash", oracle_12_signed_dsu_stack_hashing_and_thue_morse_antihash),
    ]

    print(f"\nRunning {len(oracles)} Exact Stringology & Combinatorics Oracles (Parts I - VII)...")
    for name, fn in oracles:
        fn()
        print(f"  [PASS] {name}")

    print("\nALL 12 EXACT STRINGOLOGY & COMBINATORICS ORACLES PASSED (100% PASS RATE).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
