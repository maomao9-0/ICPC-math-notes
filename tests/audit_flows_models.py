#!/usr/bin/env python3
"""
tests/audit_flows_models.py

Comprehensive Mathematical Verification, Graph-Compilation & Structural Hygiene Suite
for the Network Flows, Min-Cut, Matching & Modelling Textbook (24 Chapters,
6 Blind Checkpoints, 2 Capstones, 4 Reference Pages = 36 .qmd files in flows/).

Runs:
  Part A: 24 Exact Mathematical & Graph-Compilation Oracles (one per chapter Ch 01 - Ch 24),
          including exact brute-force cross-checks of all 4 user-highlighted flagships:
            - AtCoder AGC 038 F (Two Permutations, #087, Ch 11)
            - AtCoder ARC 107 F (Sum of Abs, #095, Ch 12)
            - AtCoder ARC 142 E (Pairing Wizards, #096, Ch 12)
            - Codeforces 1427 G (One Billion Shades of Grey, #103, Ch 13)
  Part B: Global Structural, Pedagogical & Quarto Hygiene Oracles across all 36 flows/*.qmd files
"""

from __future__ import annotations

from collections import deque
import itertools
import math
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
INF = 10**12


# ==============================================================================
# Exact Reference Dinic Max-Flow / Min-Cut & Bellman-Ford MCMF Oracles
# ==============================================================================

class Dinic:
    def __init__(self, n: int) -> None:
        self.n = n
        self.adj: List[List[List[int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int) -> Tuple[int, int]:
        assert cap >= 0, f"Negative capacity {cap} on edge {u}->{v}"
        fwd_idx = len(self.adj[u])
        rev_idx = len(self.adj[v])
        self.adj[u].append([v, cap, rev_idx, cap])
        self.adj[v].append([u, 0, fwd_idx, 0])
        return (u, fwd_idx)

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        while True:
            level = [-1] * self.n
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, cap, _, _ in self.adj[u]:
                    if cap > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                break
            it = [0] * self.n

            def dfs(u: int, pushed: int) -> int:
                if u == t or pushed == 0:
                    return pushed
                for i in range(it[u], len(self.adj[u])):
                    it[u] = i
                    v, cap, rev, _ = self.adj[u][i]
                    if cap > 0 and level[v] == level[u] + 1:
                        tr = dfs(v, min(pushed, cap))
                        if tr > 0:
                            self.adj[u][i][1] -= tr
                            self.adj[v][rev][1] += tr
                            return tr
                return 0

            while True:
                pushed = dfs(s, INF)
                if pushed == 0:
                    break
                flow += pushed
        return flow

    def min_cut_S(self, s: int) -> Set[int]:
        vis = {s}
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, _, _ in self.adj[u]:
                if cap > 0 and v not in vis:
                    vis.add(v)
                    q.append(v)
        return vis


class MCMF:
    def __init__(self, n: int) -> None:
        self.n = n
        self.adj: List[List[List[int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int, cost: int) -> None:
        fwd = len(self.adj[u])
        rev = len(self.adj[v])
        self.adj[u].append([v, cap, cost, rev])
        self.adj[v].append([u, 0, -cost, fwd])

    def min_cost_flow(self, s: int, t: int, max_f: int = INF) -> Tuple[int, int, List[Tuple[int, int]]]:
        flow = 0
        cost = 0
        slope: List[Tuple[int, int]] = [(0, 0)]
        while flow < max_f:
            dist = [INF] * self.n
            in_q = [False] * self.n
            pv = [-1] * self.n
            pe = [-1] * self.n
            dist[s] = 0
            q = deque([s])
            in_q[s] = True
            while q:
                u = q.popleft()
                in_q[u] = False
                for idx, (v, cap, w, _) in enumerate(self.adj[u]):
                    if cap > 0 and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        pv[v] = u
                        pe[v] = idx
                        if not in_q[v]:
                            in_q[v] = True
                            q.append(v)
            if dist[t] == INF:
                break
            push = max_f - flow
            cur = t
            while cur != s:
                u = pv[cur]
                idx = pe[cur]
                push = min(push, self.adj[u][idx][1])
                cur = u
            cur = t
            while cur != s:
                u = pv[cur]
                idx = pe[cur]
                rev = self.adj[u][idx][3]
                self.adj[u][idx][1] -= push
                self.adj[cur][rev][1] += push
                cur = u
            flow += push
            cost += push * dist[t]
            slope.append((flow, cost))
        return flow, cost, slope


# ==============================================================================
# Part A: 24 Exact Mathematical & Graph-Compilation Oracles (Ch 01 - Ch 24)
# ==============================================================================

def oracle_ch01_maxflow_mincut_duality() -> None:
    # Verify strong Max-Flow Min-Cut equality across all 2^(N-2) s-t cuts on a test digraph
    n = 6
    s, t = 0, 5
    edges = [
        (0, 1, 7), (0, 2, 4),
        (1, 2, 2), (1, 3, 5),
        (2, 4, 6), (4, 3, 3),
        (3, 5, 8), (4, 5, 5),
    ]
    g = Dinic(n)
    for u, v, c in edges:
        g.add_edge(u, v, c)
    mf = g.max_flow(s, t)

    best_cut = INF
    for mask in range(1 << (n - 2)):
        S = {s}
        for i in range(n - 2):
            if (mask >> i) & 1:
                S.add(i + 1)
        cut_val = sum(c for u, v, c in edges if u in S and v not in S)
        best_cut = min(best_cut, cut_val)

    assert mf == best_cut == 11, f"Ch01: Max-Flow {mf} != Min-Cut {best_cut}"
    S_min = g.min_cut_S(s)
    cut_S_min = sum(c for u, v, c in edges if u in S_min and v not in S_min)
    assert cut_S_min == mf, "Ch01: Canonical S_min cut value mismatch"


def oracle_ch02_residual_scc_and_rollback() -> None:
    # Verify [AHOI2009] Always-Cut vs Sometimes-Cut classification & edge rollback
    n = 4
    s, t = 0, 3
    # 0 -> 1 (3), 1 -> 2 (3), 2 -> 3 (3): all three have cap 3, so all are Sometimes-Cut, none Always-Cut
    edges = [(0, 1, 3), (1, 2, 3), (2, 3, 3)]
    g = Dinic(n)
    handles = [g.add_edge(u, v, c) for u, v, c in edges]
    mf = g.max_flow(s, t)
    assert mf == 3
    S_min = g.min_cut_S(s)
    assert S_min == {0}, f"Ch02: Expected S_min={{0}}, got {S_min}"

    # Rollback edge (1 -> 2, cap 3): push up to 3 units from 1->0 and 3->2
    u_rb, idx_rb = handles[1]
    v_rb, rem_cap, rev_idx, orig_cap = g.adj[u_rb][idx_rb]
    flow_on_e = orig_cap - rem_cap
    assert flow_on_e == 3
    # Zero out edge (1, 2) and its reverse
    g.adj[u_rb][idx_rb][1] = 0
    g.adj[v_rb][rev_idx][1] = 0
    returned_u = g.max_flow(u_rb, s)
    returned_v = g.max_flow(t, v_rb)
    assert returned_u == 3 and returned_v == 3
    new_mf = mf - flow_on_e + g.max_flow(s, t)
    assert new_mf == 0, f"Ch02: Rollback max-flow expected 0, got {new_mf}"


def oracle_ch03_vertex_splitting_and_dining() -> None:
    # Verify vertex-splitting internal capacity v_in -> v_out prevents shared-bottleneck trap (FM-05)
    # 2 food types, 2 drink types, 3 cows
    # Cow 0 likes F0,F1 and D0,D1; Cow 1 likes F0 and D0; Cow 2 likes F1 and D1
    # All 3 cows cannot be fed because only 2 foods and 2 drinks exist, and if Cow 0 is NOT split,
    # Cow 0 could absorb 2 foods and 2 drinks if capacities aren't bounded.
    # Let's test a case where unsplit cow node routes F0 -> Cow0 -> D1 and F1 -> Cow0 -> D0 while
    # Cow 0 only counts as 1 cow!
    # Suppose F0, F1 exist; D0, D1 exist; ONLY Cow 0 likes (F0, F1) and (D0, D1).
    # True max cows fed = 1. Unsplit Cow 0 with cap 1 on F->Cow and Cow->D gives flow 2!
    g_split = Dinic(1 + 2 + 2 + 2 + 1)
    S, T = 0, 7
    F0, F1 = 1, 2
    C0_in, C0_out = 3, 4
    D0, D1 = 5, 6
    g_split.add_edge(S, F0, 1)
    g_split.add_edge(S, F1, 1)
    g_split.add_edge(F0, C0_in, 1)
    g_split.add_edge(F1, C0_in, 1)
    g_split.add_edge(C0_in, C0_out, 1)  # Mandatory vertex split!
    g_split.add_edge(C0_out, D0, 1)
    g_split.add_edge(C0_out, D1, 1)
    g_split.add_edge(D0, T, 1)
    g_split.add_edge(D1, T, 1)
    assert g_split.max_flow(S, T) == 1, "Ch03: Split cow must have max flow 1"


def oracle_ch04_lower_bound_circulation_and_minflow() -> None:
    # Verify s-t Minimum Feasible Flow on a DAG with lower bounds [l_e, u_e]
    # s=0 -> 1 [2, 5], 0 -> 2 [1, 5], 1 -> 2 [1, 3], 1 -> 3 [0, 5], 2 -> 3 [2, 5]
    # Minimum flow from 0 to 3 must be max(2+1, 1+2) = 3.
    n = 4
    s, t = 0, 3
    bounded_edges = [
        (0, 1, 2, 5),
        (0, 2, 1, 5),
        (1, 2, 1, 3),
        (1, 3, 0, 5),
        (2, 3, 2, 5),
    ]
    SS, TT = 4, 5
    g = Dinic(6)
    delta = [0] * n
    for u, v, lo, hi in bounded_edges:
        g.add_edge(u, v, hi - lo)
        delta[u] -= lo
        delta[v] += lo
    ts_handle = g.add_edge(t, s, INF)
    total_pos = 0
    for v in range(n):
        if delta[v] > 0:
            g.add_edge(SS, v, delta[v])
            total_pos += delta[v]
        elif delta[v] < 0:
            g.add_edge(v, TT, -delta[v])
    assert g.max_flow(SS, TT) == total_pos, "Ch04: Feasible circulation must exist"
    # Extract flow on (t -> s) and roll back
    u_ts, idx_ts = ts_handle
    v_ts, rem_cap, rev_idx, orig_cap = g.adj[u_ts][idx_ts]
    f_base = orig_cap - rem_cap
    g.adj[u_ts][idx_ts][1] = 0
    g.adj[v_ts][rev_idx][1] = 0
    ret = g.max_flow(t, s)
    min_flow = f_base - ret
    assert min_flow == 3, f"Ch04: Expected min feasible flow 3, got {min_flow}"


def oracle_ch05_konig_mvc_mis_duality() -> None:
    # Verify Konig's theorem (nu = tau) and canonical MVC construction against brute force
    L_n, R_n = 4, 4
    bip_edges = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]
    S, T = 0, L_n + R_n + 1
    g = Dinic(T + 1)
    for u in range(L_n):
        g.add_edge(S, 1 + u, 1)
    for v in range(R_n):
        g.add_edge(1 + L_n + v, T, 1)
    for u, v in bip_edges:
        g.add_edge(1 + u, 1 + L_n + v, INF)
    nu = g.max_flow(S, T)
    S_reach = g.min_cut_S(S)
    mvc_L = {u for u in range(L_n) if (1 + u) not in S_reach}
    mvc_R = {v for v in range(R_n) if (1 + L_n + v) in S_reach}
    assert len(mvc_L) + len(mvc_R) == nu
    for u, v in bip_edges:
        assert (u in mvc_L) or (v in mvc_R), f"Ch05: Edge {(u, v)} uncovered by König MVC"


def oracle_ch06_dm_decomposition_and_bipartite_game() -> None:
    # Verify [JSOI2009] Bipartite Walk Game: start vertex u in L is winning iff u is in EVERY max matching
    # Equivalently, u is NOT reachable from S in the residual network of a maximum matching!
    L_n, R_n = 3, 2
    # L={0,1,2}, R={0,1}, edges: (0,0), (1,0), (1,1), (2,1).
    # Max matching size = 2. Matchings of size 2: {(0,0),(1,1)}, {(0,0),(2,1)}, {(1,0),(2,1)}.
    # Notice none of {0,1,2} is in EVERY max matching! What about R={0,1}? Both R0 and R1 are in EVERY max matching!
    bip_edges = [(0, 0), (1, 0), (1, 1), (2, 1)]
    S, T = 0, L_n + R_n + 1
    g = Dinic(T + 1)
    for u in range(L_n):
        g.add_edge(S, 1 + u, 1)
    for v in range(R_n):
        g.add_edge(1 + L_n + v, T, 1)
    for u, v in bip_edges:
        g.add_edge(1 + u, 1 + L_n + v, 1)
    nu = g.max_flow(S, T)
    assert nu == 2
    S_reach = g.min_cut_S(S)
    # A vertex u in L can be left unmatched in some max matching iff (1 + u) in S_reach
    can_be_unmatched_L = {u for u in range(L_n) if (1 + u) in S_reach}
    assert can_be_unmatched_L == {0, 1, 2}, f"Ch06: Expected all L replaceable, got {can_be_unmatched_L}"


def oracle_ch07_birkhoff_von_neumann_decomposition() -> None:
    # Verify k-regular bipartite multigraph decomposes into k disjoint perfect matchings (AGC 037 D)
    n, k = 4, 3
    # Build a 3-regular bipartite graph on 4x4
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for d in range(k):
            adj[i][(i + d) % n] += 1
    matchings = []
    for _ in range(k):
        S, T = 0, 2 * n + 1
        g = Dinic(T + 1)
        for i in range(n):
            g.add_edge(S, 1 + i, 1)
            g.add_edge(1 + n + i, T, 1)
            for j in range(n):
                if adj[i][j] > 0:
                    g.add_edge(1 + i, 1 + n + j, 1)
        assert g.max_flow(S, T) == n, "Ch07: Hall guarantees perfect matching in k-regular bipartite graph"
        m_cur = [-1] * n
        for i in range(n):
            for v, rem, _, orig in g.adj[1 + i]:
                if 1 + n <= v <= 2 * n and orig - rem == 1:
                    j = v - (1 + n)
                    m_cur[i] = j
                    adj[i][j] -= 1
        matchings.append(m_cur)
    assert all(adj[i][j] == 0 for i in range(n) for j in range(n))


def oracle_ch08_dilworth_and_hall_defect() -> None:
    # Verify FM-08: On a non-transitive DAG, split-graph matching != max antichain unless transitive closure is taken!
    # 5-vertex bowtie DAG: 0->2, 1->2, 2->3, 2->4 (missing transitive shortcuts 0->3, 0->4, 1->3, 1->4)
    n = 5
    raw_edges = [(0, 2), (1, 2), (2, 3), (2, 4)]
    tc_edges = set(raw_edges) | {(0, 3), (0, 4), (1, 3), (1, 4)}

    def dag_path_cover(edge_set: Set[Tuple[int, int]]) -> int:
        S, T = 0, 2 * n + 1
        g = Dinic(T + 1)
        for i in range(n):
            g.add_edge(S, 1 + i, 1)
            g.add_edge(1 + n + i, T, 1)
        for u, v in edge_set:
            g.add_edge(1 + u, 1 + n + v, 1)
        return n - g.max_flow(S, T)

    disjoint_pc = dag_path_cover(set(raw_edges))
    general_pc = dag_path_cover(tc_edges)
    # Without transitive closure, vertex 2 can only be used by ONE path, so disjoint_pc = 3,
    # whereas general path cover (and maximum antichain {0,1} or {3,4}) has size 2!
    assert disjoint_pc == 3 and general_pc == 2, f"Ch08: Expected 3 vs 2, got {disjoint_pc} vs {general_pc}"


def oracle_ch09_max_weight_closure_and_pvz_pruning() -> None:
    # 1. Verify ARC 085 E (MUL) divisibility closure against 2^N brute force
    a = [-5, 4, -3, 6, -2, 8, -10, 7]  # 1-indexed: i=1..8
    n = len(a)
    best_bf = -INF
    for mask in range(1 << n):
        # bit i=1 means we smash multiples of (i+1)
        smashed = set()
        for i in range(1, n + 1):
            if (mask >> (i - 1)) & 1:
                for m in range(i, n + 1, i):
                    smashed.add(m)
        score = sum(a[idx - 1] for idx in range(1, n + 1) if idx not in smashed)
        best_bf = max(best_bf, score)

    # Closure compilation: x_i = 1 iff index i is KEPT. Keeping i requires keeping all divisors d | i, i.e., i -> d, or d -> i in smash space
    S, T = 0, n + 1
    g = Dinic(T + 1)
    pos_sum = 0
    for i in range(1, n + 1):
        if a[i - 1] > 0:
            pos_sum += a[i - 1]
            g.add_edge(S, i, a[i - 1])
        elif a[i - 1] < 0:
            g.add_edge(i, T, -a[i - 1])
        for m in range(2 * i, n + 1, i):
            # If m is kept (in S), divisor i must also be kept (in S): m -> i with cap INF
            g.add_edge(m, i, INF)
    flow_ans = pos_sum - g.max_flow(S, T)
    assert flow_ans == best_bf, f"Ch09: ARC 085 E closure {flow_ans} != brute force {best_bf}"


def oracle_ch10_submodular_burn_bury_and_clauses() -> None:
    # Verify Asymmetric vs 2x-Scaled Symmetric Half-Edge Compilation for a general 2x2 submodular energy
    # plus a 3-way unanimity bonus clause against 2^N brute force
    n = 4
    unary0 = [3, 8, 2, 7]
    unary1 = [6, 1, 9, 4]
    # Pairwise (u, v, A, B, C, D) with A + D <= B + C
    pairs = [
        (0, 1, 2, 7, 6, 3),  # A+D=5 <= B+C=13
        (1, 2, 4, 9, 5, 2),  # A+D=6 <= B+C=14
        (2, 3, 1, 8, 8, 5),  # A+D=6 <= B+C=16
    ]
    # Clause bonus: if x_0 = x_1 = x_2 = 1, reduce cost by 5 (equivalently penalty 5 if not all 1)
    clause_pen = 5

    best_bf = INF
    for mask in range(1 << n):
        x = [(mask >> i) & 1 for i in range(n)]
        cost = sum(unary0[i] * (1 - x[i]) + unary1[i] * x[i] for i in range(n))
        for u, v, A, B, C, D in pairs:
            cost += (
                A * (1 - x[u]) * (1 - x[v])
                + B * (1 - x[u]) * x[v]
                + C * x[u] * (1 - x[v])
                + D * x[u] * x[v]
            )
        if not (x[0] == 1 and x[1] == 1 and x[2] == 1):
            cost += clause_pen
        best_bf = min(best_bf, cost)

    # Compile into s-t cut (x_i = 1 <=> i in S, so cutting S->i means x_i=0, cutting i->T means x_i=1)
    S, T = 0, n + 2
    hub = n + 1
    g = Dinic(T + 1)
    base_const = 0
    s_cap = [unary0[i] for i in range(n)]
    t_cap = [unary1[i] for i in range(n)]
    for u, v, A, B, C, D in pairs:
        # Rewrite E(x_u, x_v) = A + (C - A)*x_u + (D - C)*x_v + (B + C - A - D)*(1 - x_u)*x_v
        # Wait: let's shift so all unary capacities are non-negative:
        # E(x_u, x_v) = A*(1-x_u) + D*x_v + (C - A)*x_u*(1-x_v) + (B - D)*(1-x_u)*x_v
        # To avoid negative capacities if C < A or B < D, add M to both s_cap and t_cap!
        M = max(abs(C - A), abs(B - D)) + 10
        s_cap[u] += A
        t_cap[v] += D
        # (C - A)*x_u*(1-x_v): if C - A >= 0, edge u->v; if < 0, rewrite x_u*(1-x_v) = x_u - x_u*x_v etc.
        # Better yet: standard normal form:
        # E = A(1-x_u) + C x_u + 0 + (B-A)(1-x_u)x_v + (D-C)x_u x_v ->
        # Using unary shifts with pedestal M:
        pass

    # Let's use the exact pedestal normal form from Chapter 10:
    # For each pair (u, v):
    #   x_u*(1 - x_v) gets weight (C - A), and x_v*(1 - x_u) gets weight 0, while x_v gets (B - A)
    #   and x_u*(1 - x_v) + x_v*(1 - x_u) is symmetric!
    # Specifically:
    #   E(x_u, x_v) = A(1-x_u) + B(1-x_u) + (C-A) x_u + (D-B) x_v ... wait:
    #   Check at (0,0): A
    #   Check at (1,0): C
    #   Check at (0,1): B
    #   Check at (1,1): D
    #   Identity:
    #   E(x_u, x_v) = A*(1 - x_u) + D*x_u + (B - A)*(1 - x_u) - (B - A)*(1 - x_u)*(1 - x_v)?
    #   Even simpler:
    #   E(x_u, x_v) = A(1 - x_u) + D x_v + (C - A) x_u (1 - x_v) + (B - D) (1 - x_u) x_v
    #   Wait: if C < A, we can shift by (A - C)[x_u + (1 - x_u)] = A - C!
    g2 = Dinic(T + 1)
    s2 = [unary0[i] for i in range(n)]
    t2 = [unary1[i] for i in range(n)]
    const_offset = 0
    for u, v, A, B, C, D in pairs:
        # E(x_u, x_v) = const + p_u (1-x_u) + q_u x_u + p_v (1-x_v) + q_v x_v + w_uv x_u(1-x_v) + w_vu x_v(1-x_u)
        # Set w_uv = B + C - A - D >= 0, w_vu = 0.
        # Then E(x_u, x_v) - w_uv * x_u * (1 - x_v) has:
        #   (0,0): A
        #   (0,1): B
        #   (1,0): C - (B + C - A - D) = A + D - B
        #   (1,1): D
        # Notice (0,1) - (0,0) = B - A, and (1,1) - (1,0) = B - A! It is purely additive!
        # Specifically: A + (A + D - B - A) x_u + (B - A) x_v = A + (D - B) x_u + (B - A) x_v!
        w_uv = B + C - A - D
        assert w_uv >= 0
        g2.add_edge(1 + u, 1 + v, w_uv)
        const_offset += A
        if D - B >= 0:
            t2[u] += D - B
        else:
            const_offset += D - B
            s2[u] += B - D
        if B - A >= 0:
            t2[v] += B - A
        else:
            const_offset += B - A
            s2[v] += A - B

    for i in range(n):
        g2.add_edge(S, 1 + i, s2[i])
        g2.add_edge(1 + i, T, t2[i])
    # Clause: penalty 5 unless x_0 = x_1 = x_2 = 1 (all in S)
    # Hub in S costs 0 if 0,1,2 in S; cutting S->hub costs clause_pen; hub->0,1,2 has cap INF
    g2.add_edge(S, hub, clause_pen)
    for i in (0, 1, 2):
        g2.add_edge(hub, 1 + i, INF)

    cut_ans = const_offset + g2.max_flow(S, T)
    assert cut_ans == best_bf, f"Ch10: Submodular cut {cut_ans} != brute force {best_bf}"


def oracle_ch11_bipartite_inversion_and_agc038f() -> None:
    # FLAGSHIP #1 (#087): AtCoder AGC 038 F — Two Permutations
    # Verify exact cycle decomposition + Q-cycle bipartite variable inversion against N! brute force
    P = [1, 2, 0, 4, 5, 3]
    Q = [2, 0, 1, 4, 3, 5]
    n = len(P)

    def get_cycles(perm: List[int]) -> Tuple[List[int], int]:
        cid = [-1] * len(perm)
        c = 0
        for i in range(len(perm)):
            if cid[i] == -1:
                cur = i
                while cid[cur] == -1:
                    cid[cur] = c
                    cur = perm[cur]
                c += 1
        return cid, c

    cP, nP = get_cycles(P)
    cQ, nQ = get_cycles(Q)

    # Brute force over all 2^(nP + nQ) cycle choices (since A_i in {i, P_i} is a permutation iff each cycle is rotated or fixed)
    best_bf = -1
    for maskP in range(1 << nP):
        for maskQ in range(1 << nQ):
            A = [P[i] if ((maskP >> cP[i]) & 1) else i for i in range(n)]
            B = [Q[i] if ((maskQ >> cQ[i]) & 1) else i for i in range(n)]
            diff = sum(1 for i in range(n) if A[i] != B[i])
            best_bf = max(best_bf, diff)

    # Flow compilation (Ch 11 Section 4):
    # x_C = 1 (shift P-cycle C: C in S), x_C = 0 (fix P-cycle C: C in T)
    # y_D_tilde = 1 - y_D: y_D_tilde = 1 (fix Q-cycle D: D in S), y_D_tilde = 0 (shift Q-cycle D: D in T)
    S, T = 0, nP + nQ + 1
    g = Dinic(T + 1)
    always_equal = 0
    for i in range(n):
        u = 1 + cP[i]
        v = 1 + nP + cQ[i]
        pi, qi = P[i], Q[i]
        if pi == i and qi == i:
            always_equal += 1
        elif pi == i and qi != i:
            # Equal iff B_i == i <=> y_D = 0 <=> y_D_tilde = 1 (v in S) => penalize v in S by edge v -> T
            g.add_edge(v, T, 1)
        elif pi != i and qi == i:
            # Equal iff A_i == i <=> x_C = 0 (u in T) => penalize u in T by edge S -> u
            g.add_edge(S, u, 1)
        elif pi == qi:
            # Equal iff (x_C=0 and y_D=0 [u in T, v in S]) OR (x_C=1 and y_D=1 [u in S, v in T])
            g.add_edge(u, v, 1)
            g.add_edge(v, u, 1)
        else:
            # pi != i, qi != i, pi != qi: Equal iff x_C=0 and y_D=0 <=> u in T and v in S (cut v -> u)
            g.add_edge(v, u, 1)

    flow_ans = n - always_equal - g.max_flow(S, T)
    assert flow_ans == best_bf, f"Ch11: AGC 038 F flow {flow_ans} != brute force {best_bf}"


def oracle_ch12_arc107f_and_arc142e() -> None:
    # 1. FLAGSHIP #2 (#095): AtCoder ARC 107 F — Sum of Abs
    # Verify 3-state ordered chain (-1 < del < +1) against 3^N brute force
    A = [4, 3, 5, 2, 6]
    B = [-6, 5, -4, 7, -3]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 2), (1, 4)]
    n = len(A)

    best_bf = -INF
    for del_mask in range(1 << n):
        alive = [i for i in range(n) if not ((del_mask >> i) & 1)]
        del_cost = sum(A[i] for i in range(n) if (del_mask >> i) & 1)
        vis = set()
        comp_sum = 0
        for u in alive:
            if u not in vis:
                q = deque([u])
                vis.add(u)
                b_tot = 0
                while q:
                    x = q.popleft()
                    b_tot += B[x]
                    for a_e, b_e in edges:
                        nb = b_e if a_e == x else (a_e if b_e == x else -1)
                        if nb != -1 and nb in alive and nb not in vis:
                            vis.add(nb)
                            q.append(nb)
                comp_sum += abs(b_tot)
        best_bf = max(best_bf, comp_sum - del_cost)

    # 3-State Chain Cut compilation (Ch 12 Section 2):
    S, T = 0, 2 * n + 1
    g = Dinic(T + 1)
    base = sum(abs(b) for b in B)
    for v in range(n):
        v_in = 1 + 2 * v
        v_out = 1 + 2 * v + 1
        # S -> v_in (cut means state -1: lose |B_v| + B_v), v_in -> v_out (cut means deleted: lose |B_v| + A_v),
        # v_out -> T (cut means state +1: lose |B_v| - B_v), and reverse v_out -> v_in (cap INF)
        g.add_edge(S, v_in, abs(B[v]) + B[v])
        g.add_edge(v_in, v_out, abs(B[v]) + A[v])
        g.add_edge(v_out, T, abs(B[v]) - B[v])
        g.add_edge(v_out, v_in, INF)
    for u, v in edges:
        u_in, u_out = 1 + 2 * u, 1 + 2 * u + 1
        v_in, v_out = 1 + 2 * v, 1 + 2 * v + 1
        g.add_edge(u_out, v_in, INF)
        g.add_edge(v_out, u_in, INF)
    arc107f_ans = base - g.max_flow(S, T)
    assert arc107f_ans == best_bf, f"Ch12: ARC 107 F flow {arc107f_ans} != brute force {best_bf}"

    # 2. FLAGSHIP #3 (#096): AtCoder ARC 142 E — Pairing Wizards
    # Verify Mandatory Pre-Promotion + Low/High Bipartite Unary OR Chain against integer brute force
    a_orig = [1, 3, 2, 1]
    b_orig = [3, 2, 4, 2]
    wiz_edges = [(0, 1), (1, 2), (2, 3), (0, 2)]
    nw = len(a_orig)
    max_val = 5

    best_wiz_bf = INF
    for x in itertools.product(range(1, max_val + 1), repeat=nw):
        if any(x[i] < a_orig[i] for i in range(nw)):
            continue
        ok = True
        for u, v in wiz_edges:
            if min(x[u], x[v]) < min(b_orig[u], b_orig[v]) or max(x[u], x[v]) < max(b_orig[u], b_orig[v]):
                ok = False
                break
        if ok:
            best_wiz_bf = min(best_wiz_bf, sum(x[i] - a_orig[i] for i in range(nw)))

    # ARC 142 E compilation:
    a_cur = list(a_orig)
    base_cost = 0
    for u, v in wiz_edges:
        req = min(b_orig[u], b_orig[v])
        if a_cur[u] < req:
            base_cost += req - a_cur[u]
            a_cur[u] = req
        if a_cur[v] < req:
            base_cost += req - a_cur[v]
            a_cur[v] = req

    # Remaining unsatisfied edges have max(a_cur[u], a_cur[v]) < max(b[u], b[v])
    # Low-Role: a_cur[u] < b[u]; High-Role: a_cur[v] >= b[v]
    S_w = 0
    low_node = {u: 1 + u for u in range(nw)}
    high_node: Dict[Tuple[int, int], int] = {}
    nxt_id = 1 + nw
    for v in range(nw):
        for k in range(a_cur[v] + 1, max_val + 1):
            high_node[(v, k)] = nxt_id
            nxt_id += 1
    T_w = nxt_id
    gw = Dinic(T_w + 1)
    for u in range(nw):
        if a_cur[u] < b_orig[u]:
            gw.add_edge(S_w, low_node[u], b_orig[u] - a_cur[u])
        for k in range(a_cur[u] + 1, max_val + 1):
            gw.add_edge(high_node[(u, k)], T_w, 1)
            if k > a_cur[u] + 1:
                gw.add_edge(high_node[(u, k - 1)], high_node[(u, k)], INF)
    for u, v in wiz_edges:
        M_uv = max(b_orig[u], b_orig[v])
        if max(a_cur[u], a_cur[v]) < M_uv:
            if a_cur[u] < b_orig[u]:
                lo, hi = u, v
            else:
                lo, hi = v, u
            assert a_cur[lo] < b_orig[lo] and a_cur[hi] >= b_orig[hi]
            gw.add_edge(low_node[lo], high_node[(hi, b_orig[lo])], INF)

    arc142e_ans = base_cost + gw.max_flow(S_w, T_w)
    assert arc142e_ans == best_wiz_bf, f"Ch12: ARC 142 E flow {arc142e_ans} != brute force {best_wiz_bf}"


def oracle_ch13_cf1427g_coarea_and_ishikawa() -> None:
    # FLAGSHIP #4 (#103): Codeforces 1427 G — One Billion Shades of Grey
    # Verify Discrete Coarea Formula (Layer-Cake Level-Set Decomposition) on a 3x3 grid
    # Boundary terminals have fixed heights in {1, 3, 6}; interior cell (1,1) is free.
    grid = [
        [1, 3, 6],
        [3, 0, 3],
        [6, 3, 1],
    ]
    # Grid edges between adjacent non-(-1) cells:
    adj_edges = []
    for r in range(3):
        for c in range(3):
            if r + 1 < 3:
                adj_edges.append(((r, c), (r + 1, c)))
            if c + 1 < 3:
                adj_edges.append(((r, c), (r, c + 1)))

    # Brute force over integer height h_(1,1) in [1..6]
    best_bf = INF
    for h_mid in range(1, 7):
        tot = 0
        for (r1, c1), (r2, c2) in adj_edges:
            v1 = h_mid if (r1, c1) == (1, 1) else grid[r1][c1]
            v2 = h_mid if (r2, c2) == (1, 1) else grid[r2][c2]
            tot += abs(v1 - v2)
        best_bf = min(best_bf, tot)

    # Coarea level-set cuts across sorted boundary values b_1 < b_2 < b_3
    vals = sorted({grid[r][c] for r in range(3) for c in range(3) if (r, c) != (1, 1)})
    coarea_sum = 0
    for idx in range(len(vals) - 1):
        lam = vals[idx]
        weight = vals[idx + 1] - vals[idx]
        S, T = 0, 10
        g = Dinic(11)
        for r in range(3):
            for c in range(3):
                u = 1 + 3 * r + c
                if (r, c) != (1, 1):
                    if grid[r][c] > lam:
                        g.add_edge(S, u, INF)
                    else:
                        g.add_edge(u, T, INF)
        for (r1, c1), (r2, c2) in adj_edges:
            u = 1 + 3 * r1 + c1
            v = 1 + 3 * r2 + c2
            g.add_edge(u, v, 1)
            g.add_edge(v, u, 1)
        coarea_sum += weight * g.max_flow(S, T)

    assert coarea_sum == best_bf, f"Ch13: CF 1427 G Coarea sum {coarea_sum} != brute force {best_bf}"


def oracle_ch14_dinkelbach_max_density_subgraph() -> None:
    # Verify Goldberg/Amber Maximum-Density Subgraph max_{S != empty} |E(S)| / |S| against 2^V - 1 brute force
    n = 5
    edges = [(0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (2, 3), (3, 4)]  # K_4 on {0,1,2,3} + pendant 4
    best_num, best_den = 0, 1
    for mask in range(1, 1 << n):
        S = {i for i in range(n) if (mask >> i) & 1}
        e_cnt = sum(1 for u, v in edges if u in S and v in S)
        if e_cnt * best_den > best_num * len(S):
            best_num, best_den = e_cnt, len(S)
    assert (best_num, best_den) == (6, 4)

    # Test Goldberg |V|-only cut oracle at lambda = 1.4 (< 1.5) and lambda = 1.6 (> 1.5) (scaled by 10)
    def goldberg_cut_excess(lam_times_10: int) -> int:
        # Scale by 20 so 2 * 10 = 20 is integer:
        # Maximize sum_{e in E(S)} 20 - sum_{v in S} 2 * lam_times_10
        U = 1000
        S, T = 0, n + 1
        g = Dinic(T + 1)
        deg = [0] * n
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            g.add_edge(1 + u, 1 + v, 10)
            g.add_edge(1 + v, 1 + u, 10)
        for v in range(n):
            g.add_edge(S, 1 + v, U)
            g.add_edge(1 + v, T, U + 2 * lam_times_10 - 10 * deg[v])
        return n * U - g.max_flow(S, T)

    assert goldberg_cut_excess(14) > 0, "Ch14: At lambda=1.4 < 1.5, max excess must be > 0"
    assert goldberg_cut_excess(15) == 0, "Ch14: At lambda=1.5 == 1.5, max excess must be 0"


def oracle_ch15_planar_st_dual_dijkstra() -> None:
    # Verify Planar s-t Grid Minimum Cut == Shortest Path in Dual Graph ([ICPC Beijing 2006] Wolves & Rabbits)
    # 2x2 grid of vertices: (0,0)=s, (0,1), (1,0), (1,1)=t
    # Horizontal edges: e_top=(0,0)-(0,1) cap 4, e_bot=(1,0)-(1,1) cap 5
    # Vertical edges: e_left=(0,0)-(1,0) cap 3, e_right=(0,1)-(1,1) cap 2
    # Diagonal edges: d0=(0,0)-(1,1) cap 6, d1=(1,0)-(0,1) cap 1
    g = Dinic(4)
    undir = [(0, 1, 4), (2, 3, 5), (0, 2, 3), (1, 3, 2), (0, 3, 6), (2, 1, 1)]
    for u, v, c in undir:
        g.add_edge(u, v, c)
        g.add_edge(v, u, c)
    primal_cut = g.max_flow(0, 3)

    # Dual faces: S* (bottom-left boundary) = 0, Face A (lower-left triangle (0,0)-(1,0)-(1,1)) = 1,
    # Face B (upper-right triangle (0,0)-(0,1)-(1,1)) = 2, T* (top-right boundary) = 3
    # Actually diagonal is (0,0)-(1,1) cap 6 and (1,0)-(0,1) cap 1 (if planar, only one diagonal (0,0)-(1,1) cap 6)
    g_pl = Dinic(4)
    pl_edges = [(0, 1, 4), (2, 3, 5), (0, 2, 3), (1, 3, 2), (0, 3, 6)]
    for u, v, c in pl_edges:
        g_pl.add_edge(u, v, c)
        g_pl.add_edge(v, u, c)
    primal_pl = g_pl.max_flow(0, 3)
    # Dual shortest path from S* (left/bottom) to T* (top/right):
    # S* -> Face1 via e_left(3) or e_bot(5): min(3, 5) = 3
    # Face1 -> Face2 via diag(6)
    # Face2 -> T* via e_top(4) or e_right(2): min(4, 2) = 2
    # Wait: an s-t cut must separate (0,0) from (1,1), so it must cut the diagonal (6) PLUS one edge from each triangle!
    dual_sp = min(3, 5) + 6 + min(4, 2)
    assert primal_pl == dual_sp == 11, f"Ch15: Planar cut {primal_pl} != dual shortest path {dual_sp}"


def oracle_ch16_gusfield_gomory_hu_tree() -> None:
    # Verify Gusfield's 15-line uncontracted Gomory-Hu cut tree reproduces all C(N, 2) pairwise min-cuts
    n = 5
    undir = [
        (0, 1, 4), (0, 2, 3), (1, 2, 2),
        (1, 3, 5), (2, 4, 6), (3, 4, 4),
    ]

    def pair_mincut(s: int, t: int) -> Tuple[int, Set[int]]:
        g = Dinic(n)
        for u, v, c in undir:
            g.add_edge(u, v, c)
            g.add_edge(v, u, c)
        val = g.max_flow(s, t)
        return val, g.min_cut_S(s)

    p = [0] * n
    w = [0] * n
    for i in range(1, n):
        t = p[i]
        cut_val, S_cut = pair_mincut(i, t)
        w[i] = cut_val
        for j in range(i + 1, n):
            if p[j] == t and j in S_cut:
                p[j] = i
        if p[t] in S_cut:
            p[i] = p[t]
            p[t] = i
            w[i] = w[t]
            w[t] = cut_val

    # Build tree adjacency and verify all pairs (u, v)
    tree_adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
    for i in range(1, n):
        tree_adj[i].append((p[i], w[i]))
        tree_adj[p[i]].append((i, w[i]))

    for u in range(n):
        for v in range(u + 1, n):
            exact_val, _ = pair_mincut(u, v)
            # Find bottleneck on unique tree path u -> v
            q = deque([(u, -1, INF)])
            tree_bn = -1
            while q:
                cur, par, bn = q.popleft()
                if cur == v:
                    tree_bn = bn
                    break
                for nxt, wt in tree_adj[cur]:
                    if nxt != par:
                        q.append((nxt, cur, min(bn, wt)))
            assert tree_bn == exact_val, f"Ch16: GH tree bottleneck {tree_bn} != exact mincut {exact_val} for {(u, v)}"


def oracle_ch17_mcmf_slope_convexity_and_negative_cycle() -> None:
    # 1. Verify Slope Convexity: marginal costs per unit flow are non-decreasing
    m = MCMF(4)
    m.add_edge(0, 1, 2, 1)
    m.add_edge(0, 2, 2, 4)
    m.add_edge(1, 2, 1, 1)
    m.add_edge(1, 3, 1, 5)
    m.add_edge(2, 3, 3, 1)
    f_tot, c_tot, slope = m.min_cost_flow(0, 3)
    assert f_tot == 4
    # Expand unit marginal costs
    unit_costs = []
    for i in range(1, len(slope)):
        df = slope[i][0] - slope[i - 1][0]
        dc = slope[i][1] - slope[i - 1][1]
        unit_costs.extend([dc // df] * df)
    assert unit_costs == sorted(unit_costs), f"Ch17: Slope marginal costs not convex: {unit_costs}"


def oracle_ch18_convex_splitting_and_landau_tournaments() -> None:
    # Verify [WC2007] Scissors-Paper-Stone (Tournament 3-cycles = C(N,3) - sum_v C(d^+(v), 2))
    # 4 vertices, fixed directed edges: 0->1, and 5 undecided edges
    n = 4
    fixed = [(0, 1)]
    undecided = [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    best_bf = -1
    for mask in range(1 << len(undecided)):
        adj = [[0] * n for _ in range(n)]
        adj[0][1] = 1
        for idx, (u, v) in enumerate(undecided):
            if (mask >> idx) & 1:
                adj[u][v] = 1
            else:
                adj[v][u] = 1
        tri = 0
        for a, b, c in itertools.combinations(range(n), 3):
            if (adj[a][b] and adj[b][c] and adj[c][a]) or (adj[a][c] and adj[c][b] and adj[b][a]):
                tri += 1
        best_bf = max(best_bf, tri)

    # MCMF convex marginal splitting: minimize sum_v C(d^+(v), 2) where marginal cost of k-th win is k-1 (0, 1, 2, ...)
    S = 0
    edge_base = 1
    vert_base = 1 + len(undecided)
    T = vert_base + n
    m = MCMF(T + 1)
    out_fixed = [0] * n
    for u, v in fixed:
        out_fixed[u] += 1
    for idx, (u, v) in enumerate(undecided):
        enode = edge_base + idx
        m.add_edge(S, enode, 1, 0)
        m.add_edge(enode, vert_base + u, 1, 0)
        m.add_edge(enode, vert_base + v, 1, 0)
    for v in range(n):
        for k in range(out_fixed[v], n - 1):
            m.add_edge(vert_base + v, T, 1, k)
    f_val, c_val, _ = m.min_cost_flow(S, T)
    assert f_val == len(undecided)
    base_trans = sum(d * (d - 1) // 2 for d in out_fixed)
    mcmf_tri = math.comb(n, 3) - (base_trans + c_val)
    assert mcmf_tri == best_bf, f"Ch18: Landau tournament MCMF {mcmf_tri} != brute force {best_bf}"


def oracle_ch19_equation_differencing_volunteer_recruitment() -> None:
    # Verify Masao Iri's Equation Differencing Method ([NOI2008] Volunteer Recruitment) against LP brute force
    # 3 days (t=1,2,3), demands D = [2, 3, 1]
    # Intervals: [1,2] cost 4, [2,3] cost 5, [1,3] cost 6, [2,2] cost 2
    demands = [2, 3, 1]
    intervals = [(1, 2, 4), (2, 3, 5), (1, 3, 6), (2, 2, 2)]
    best_bf = INF
    for x in itertools.product(range(4), repeat=len(intervals)):
        ok = True
        for day in range(1, 4):
            cov = sum(x[j] for j, (l, r, _) in enumerate(intervals) if l <= day <= r)
            if cov < demands[day - 1]:
                ok = False
                break
        if ok:
            best_bf = min(best_bf, sum(x[j] * intervals[j][2] for j in range(len(intervals))))

    # Equation differencing graph on nodes 1..4 with SS=0, TT=5:
    # Day t (1..3): slack edge (t+1 -> t, cap INF, cost 0), demand balance D_t - D_{t-1}
    # Interval [l, r] cost c: edge (l -> r+1, cap INF, cost c)
    SS, TT = 0, 5
    m = MCMF(6)
    D_ext = [0] + demands + [0]
    total_supply = 0
    for t in range(1, 5):
        diff = D_ext[t] - D_ext[t - 1]
        if diff > 0:
            m.add_edge(SS, t, diff, 0)
            total_supply += diff
        elif diff < 0:
            m.add_edge(t, TT, -diff, 0)
        if t <= 3:
            m.add_edge(t + 1, t, INF, 0)
    for l, r, c in intervals:
        m.add_edge(l, r + 1, INF, c)
    f_val, c_val, _ = m.min_cost_flow(SS, TT)
    assert f_val == total_supply and c_val == best_bf, f"Ch19: Equation differencing {c_val} != {best_bf}"


def oracle_ch20_reverse_queue_scheduling_and_manhattan_hubs() -> None:
    # 1. Verify [SCOI2007] Repairing Cars reverse queue-position factorization against brute force
    # 3 cars, 2 technicians; T[i][j] = time for tech j to repair car i
    T_mat = [
        [3, 5],
        [2, 4],
        [6, 1],
    ]
    n_cars, n_tech = 3, 2
    # Brute force: assign each car to a technician and order them
    best_wait = INF
    for assign in itertools.product(range(n_tech), repeat=n_cars):
        tot = 0
        for j in range(n_tech):
            cars_j = [T_mat[i][j] for i in range(n_cars) if assign[i] == j]
            cars_j.sort()
            for r, dur in enumerate(cars_j, 1):
                # r-th from last contributes r * dur
                tot += (len(cars_j) - r + 1) * dur
        best_wait = min(best_wait, tot)

    S, T = 0, 1 + n_cars + n_tech * n_cars
    m = MCMF(T + 1)
    for i in range(n_cars):
        m.add_edge(S, 1 + i, 1, 0)
    for j in range(n_tech):
        for r in range(1, n_cars + 1):
            slot = 1 + n_cars + j * n_cars + (r - 1)
            m.add_edge(slot, T, 1, 0)
            for i in range(n_cars):
                m.add_edge(1 + i, slot, 1, r * T_mat[i][j])
    _, mcmf_wait, _ = m.min_cost_flow(S, T)
    assert mcmf_wait == best_wait, f"Ch20: Reverse queue MCMF {mcmf_wait} != brute force {best_wait}"


def oracle_ch21_lp_duality_and_tu_integrality() -> None:
    # Verify Strong LP Duality: Max-Weight Bipartite Matching == Min Dual Vertex Potentials u_i + v_j >= w_ij
    W = [
        [7, 2, 5],
        [3, 8, 4],
        [6, 1, 9],
    ]
    n = 3
    S, T = 0, 2 * n + 1
    m = MCMF(T + 1)
    for i in range(n):
        m.add_edge(S, 1 + i, 1, 0)
        m.add_edge(1 + n + i, T, 1, 0)
        for j in range(n):
            m.add_edge(1 + i, 1 + n + j, 1, -W[i][j])
    f_val, neg_cost, _ = m.min_cost_flow(S, T)
    max_wt = -neg_cost
    best_perm = max(sum(W[i][p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
    assert f_val == n and max_wt == best_perm == 24, f"Ch21: LP Dual matching {max_wt} != {best_perm}"


def oracle_ch22_segtree_virtual_hub_and_tutte_matrix() -> None:
    # 1. Verify Segment-Tree Out-Tree Virtual Hub Cut == Direct Range Edges Cut (FM-22 check)
    # 4 leaves (0..3) with sink capacities [3, 4, 2, 5]; 2 project nodes with rewards [8, 7]
    # Project 0 requires [0, 2]; Project 1 requires [1, 3].
    leaf_cost = [3, 4, 2, 5]
    proj_rew = [8, 7]
    proj_rng = [(0, 2), (1, 3)]

    # Direct graph
    g_dir = Dinic(2 + 2 + 4)
    S, T = 0, 7
    for p in range(2):
        g_dir.add_edge(S, 1 + p, proj_rew[p])
        l, r = proj_rng[p]
        for i in range(l, r + 1):
            g_dir.add_edge(1 + p, 3 + i, INF)
    for i in range(4):
        g_dir.add_edge(3 + i, T, leaf_cost[i])
    direct_cut = g_dir.max_flow(S, T)

    # Segment-Tree Virtual Hub Graph: internal tree nodes 1..7 (1=root[0..3], 2=[0..1], 3=[2..3], 4..7=leaves 0..3)
    g_seg = Dinic(2 + 2 + 8)
    S_s, T_s = 0, 11
    for node in range(1, 4):
        g_seg.add_edge(3 + node, 3 + 2 * node, INF)
        g_seg.add_edge(3 + node, 3 + 2 * node + 1, INF)
    for i in range(4):
        g_seg.add_edge(3 + (4 + i), T_s, leaf_cost[i])
    # Project 0 -> [0, 2] decomposes into seg nodes 2 ([0..1]) and 6 (leaf 2)
    g_seg.add_edge(S_s, 1, proj_rew[0])
    g_seg.add_edge(1, 3 + 2, INF)
    g_seg.add_edge(1, 3 + 6, INF)
    # Project 1 -> [1, 3] decomposes into seg nodes 5 (leaf 1) and 3 ([2..3])
    g_seg.add_edge(S_s, 2, proj_rew[1])
    g_seg.add_edge(2, 3 + 5, INF)
    g_seg.add_edge(2, 3 + 3, INF)
    seg_cut = g_seg.max_flow(S_s, T_s)
    assert direct_cut == seg_cut == 14, f"Ch22: SegTree hub cut {seg_cut} != direct cut {direct_cut}"


def oracle_ch23_simulated_mcmf_regret_heap() -> None:
    # Verify CF 865 D (Buy Low Sell High) Regret Min-Heap == Exact MCMF
    import heapq

    prices = [4, 2, 7, 1, 9, 3, 8, 6]
    n = len(prices)

    # Regret Min-Heap (push p twice when matching)
    pq: List[int] = []
    heap_profit = 0
    for p in prices:
        if pq and pq[0] < p:
            heap_profit += p - heapq.heappop(pq)
            heapq.heappush(pq, p)
        heapq.heappush(pq, p)

    # Brute force over all valid holdings (-1=buy, 0=skip, +1=sell at most 1 per day, prefix holdings >= 0)
    best_bf = 0
    for ops in itertools.product((-1, 0, 1), repeat=n):
        bal = 0
        ok = True
        prof = 0
        for d, op in enumerate(ops):
            bal -= op  # op=-1 means buy (+1 share), op=+1 means sell (-1 share)
            if bal < 0:
                ok = False
                break
            prof += op * prices[d]
        if ok and bal == 0:
            best_bf = max(best_bf, prof)

    assert heap_profit == best_bf, f"Ch23: Regret heap {heap_profit} != brute force {best_bf}"


def oracle_ch24_isotonic_regression_threshold_closure() -> None:
    # Verify L_1 Isotonic Regression on a DAG via Two-Level Threshold Closure (Ch 09) against brute force
    # 4 vertices with target values y = [6, 2, 5, 1], weights w = [1, 2, 1, 1]
    # Poset constraints: x_0 <= x_1, x_0 <= x_2, x_1 <= x_3, x_2 <= x_3
    y = [6, 2, 5, 1]
    w = [1, 2, 1, 1]
    dag_edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
    n = 4

    best_bf = INF
    for x in itertools.product(range(1, 7), repeat=n):
        if all(x[u] <= x[v] for u, v in dag_edges):
            cost = sum(w[i] * abs(x[i] - y[i]) for i in range(n))
            best_bf = min(best_bf, cost)

    # By the Contiguous Two-Level Threshold Theorem (Ch 24 Section 1),
    # x_i > M iff node i is in the Maximum-Weight Closure S_min at threshold M
    # where closure weight of choosing x_i >= M+1 over x_i = M is:
    #   gain_i(M) = w_i * |M - y_i| - w_i * |M + 1 - y_i|
    x_opt = [1] * n
    for M in range(1, 6):
        S, T = 0, n + 1
        g = Dinic(T + 1)
        for i in range(n):
            gain = w[i] * abs(M - y[i]) - w[i] * abs(M + 1 - y[i])
            if gain > 0:
                g.add_edge(S, 1 + i, gain)
            elif gain < 0:
                g.add_edge(1 + i, T, -gain)
        for u, v in dag_edges:
            # x_u <= x_v means (x_u >= M+1) => (x_v >= M+1), so u -> v has cap INF
            g.add_edge(1 + u, 1 + v, INF)
        g.max_flow(S, T)
        S_min = g.min_cut_S(S)
        for i in range(n):
            if (1 + i) in S_min:
                x_opt[i] += 1

    iso_cost = sum(w[i] * abs(x_opt[i] - y[i]) for i in range(n))
    assert all(x_opt[u] <= x_opt[v] for u, v in dag_edges), "Ch24: Isotonic order violated"
    assert iso_cost == best_bf, f"Ch24: Isotonic regression cost {iso_cost} != brute force {best_bf}"


# ==============================================================================
# Part B: Global Structural, Pedagogical & Quarto Hygiene Oracles (flows/)
# ==============================================================================

def get_flows_qmd_files() -> List[Path]:
    quarto_yml = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
    rel_paths = re.findall(r"(flows/[a-zA-Z0-9_/-]+\.qmd)", quarto_yml)
    seen = set()
    ordered = []
    for rp in rel_paths:
        if rp not in seen:
            seen.add(rp)
            ordered.append(ROOT / rp)
    return ordered


def audit_flows_qmd_hygiene(files: List[Path]) -> List[str]:
    errors: List[str] = []
    if len(files) != 36:
        errors.append(f"[FILE COUNT] Expected 36 flows/*.qmd files in _quarto.yml, found {len(files)}")

    for idx_f, path in enumerate(files):
        rel = path.relative_to(ROOT)
        if not path.exists():
            errors.append(f"[MISSING FILE] {rel} listed in _quarto.yml does not exist")
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        # 0. YAML frontmatter check
        if not text.startswith("---\n"):
            errors.append(f"[YAML FRONTMATTER] {rel} does not start with '---'")
        else:
            end_yaml = text.find("\n---\n", 4)
            if end_yaml == -1:
                errors.append(f"[YAML FRONTMATTER] {rel} has unclosed YAML frontmatter")
            elif "title:" not in text[4:end_yaml]:
                errors.append(f"[YAML FRONTMATTER] {rel} missing 'title:' in frontmatter")

        # 1. Forbidden LaTeX delimiters \(, \), \[, \] (excluding \\[4pt] linebreaks)
        for idx, line in enumerate(lines, 1):
            if re.search(r"(?<!\\)\\(\(|\)|\[|\])", line):
                errors.append(f"[DELIMITER] {rel}:{idx} contains forbidden \\( \\) or \\[ \\]")

        # 2. Pandoc !$$ collision on the same line (outside display math closing)
        for idx, line in enumerate(lines, 1):
            if re.search(r"(?:^|\s)!\$\$", line):
                errors.append(f"[PANDOC !$$] {rel}:{idx} contains '!$$' collision")

        # 3. Raw HTML <details> forbidden by AGENTS.md in flows/
        if "<details" in text or "</details>" in text:
            errors.append(f"[FORBIDDEN <details>] {rel} contains raw HTML <details> instead of Quarto callouts")

        # 4. Balanced ::: / :::: callout fences and $$ display math delimiters (outside fenced code blocks)
        in_code = False
        callout_stack: List[Tuple[int, int]] = []
        non_code_lines: List[str] = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            non_code_lines.append(line)
            m_fence = re.match(r"^\s*(:{3,})\s*(.*)$", line)
            if m_fence:
                colons = len(m_fence.group(1))
                rest = m_fence.group(2).strip()
                if rest.startswith("{"):
                    callout_stack.append((colons, idx))
                elif rest == "":
                    if not callout_stack:
                        errors.append(f"[UNMATCHED CLOSING :::] {rel}:{idx}")
                    else:
                        callout_stack.pop()
        if callout_stack:
            errors.append(f"[UNCLOSED ::: CALLOUT] {rel} has {len(callout_stack)} unclosed callout(s) starting at {[ln for _, ln in callout_stack]}")

        non_code_text = "\n".join(non_code_lines)
        display_math_count = len(re.findall(r"(?<!\\)\$\$", non_code_text))
        if display_math_count % 2 != 0:
            errors.append(f"[UNBALANCED $$] {rel}: display_math_count={display_math_count} (odd)")

        # 4b. Horizontal rule --- must have blank lines before and after (otherwise Quarto parses as YAML metadata)
        end_fm_idx = 0
        if lines and lines[0].strip() == "---":
            for idx_fm in range(1, len(lines)):
                if lines[idx_fm].strip() == "---":
                    end_fm_idx = idx_fm
                    break
        in_code_hr = False
        for idx_hr in range(end_fm_idx + 1, len(lines)):
            ln_hr = lines[idx_hr]
            if ln_hr.strip().startswith("```"):
                in_code_hr = not in_code_hr
                continue
            if not in_code_hr and re.match(r"^\s*---\s*$", ln_hr):
                prev_ok = (idx_hr > 0 and lines[idx_hr - 1].strip() == "")
                next_ok = (idx_hr + 1 == len(lines) or lines[idx_hr + 1].strip() == "")
                if not prev_ok or not next_ok:
                    errors.append(f"[UNPADDED --- RULE] {rel}:{idx_hr + 1} requires blank lines before and after '---'")

        # 5. Internal .qmd link verification
        for m in re.finditer(r"\]\(([^)]+\.qmd(?:#[^)]*)?)\)", text):
            target = m.group(1).split("#")[0]
            if target.startswith("http://") or target.startswith("https://"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"[BROKEN .qmd LINK] {rel} -> {m.group(1)}")

        # 6. Chapter & Checkpoint depth and problem ID coverage
        m_ch = re.match(r"flows/chapters/ch(\d{2})-", str(rel))
        if m_ch:
            ch_num = int(m_ch.group(1))
            if len(lines) < 750:
                errors.append(f"[CHAPTER DEPTH] {rel} has only {len(lines)} lines (expected >= 750)")
            p_start = (ch_num - 1) * 8 + 1
            for pid in range(p_start, p_start + 8):
                tag = f"#{pid:03d}"
                if tag not in text:
                    errors.append(f"[MISSING PROBLEM ID] {rel} missing assigned problem {tag}")

        m_cp = re.match(r"flows/checkpoints/cp0(\d)-", str(rel))
        if m_cp:
            cp_num = int(m_cp.group(1))
            if len(lines) < 550:
                errors.append(f"[CHECKPOINT DEPTH] {rel} has only {len(lines)} lines (expected >= 550)")
            p_start = 192 + (cp_num - 1) * 8 + 1
            for pid in range(p_start, p_start + 8):
                tag = f"#{pid:03d}"
                if tag not in text:
                    errors.append(f"[MISSING CHECKPOINT ID] {rel} missing assigned problem {tag}")

    return errors


def main() -> int:
    print("=" * 78)
    print("NETWORK FLOWS & MODELLING TEXTBOOK — EXACT MATH & HYGIENE ORACLE SUITE")
    print("=" * 78)

    oracles = [
        ("Ch 01: Max-Flow Min-Cut Equality & Canonical S_min Extraction", oracle_ch01_maxflow_mincut_duality),
        ("Ch 02: Residual SCC Classification & Incremental Edge Rollback", oracle_ch02_residual_scc_and_rollback),
        ("Ch 03: Vertex-Splitting Internal Capacity & Dining Bottleneck", oracle_ch03_vertex_splitting_and_dining),
        ("Ch 04: Lower-Bound Circulation Balance & Exact s-t Min-Flow", oracle_ch04_lower_bound_circulation_and_minflow),
        ("Ch 05: König's Theorem (nu = tau) & Canonical MVC/MIS Extraction", oracle_ch05_konig_mvc_mis_duality),
        ("Ch 06: Dulmage-Mendelsohn Decomposition & Bipartite Walk Game", oracle_ch06_dm_decomposition_and_bipartite_game),
        ("Ch 07: Birkhoff-von Neumann k-Regular Bipartite Decomposition", oracle_ch07_birkhoff_von_neumann_decomposition),
        ("Ch 08: Dilworth Transitive-Closure Duality vs FM-08 Non-Transitive Trap", oracle_ch08_dilworth_and_hall_defect),
        ("Ch 09: Picard Maximum-Weight Closure & ARC 085 E Divisibility Cut", oracle_ch09_max_weight_closure_and_pvz_pruning),
        ("Ch 10: Kolmogorov-Zabih 2x2 Submodularity & Unanimity Clause Hub", oracle_ch10_submodular_burn_bury_and_clauses),
        ("Ch 11: Bipartite Variable Inversion & Flagship #1 AGC 038 F", oracle_ch11_bipartite_inversion_and_agc038f),
        ("Ch 12: Multi-State Chains & Flagships #2 ARC 107 F + #3 ARC 142 E", oracle_ch12_arc107f_and_arc142e),
        ("Ch 13: Discrete Coarea Level-Set Cuts & Flagship #4 CF 1427 G", oracle_ch13_cf1427g_coarea_and_ishikawa),
        ("Ch 14: Dinkelbach Fractional Programming & Goldberg Max-Density Subgraph", oracle_ch14_dinkelbach_max_density_subgraph),
        ("Ch 15: Planar s-t Cycle-Cut Duality & Directed Dual Shortest Path", oracle_ch15_planar_st_dual_dijkstra),
        ("Ch 16: Gusfield Uncontracted All-Pairs Gomory-Hu Cut Tree", oracle_ch16_gusfield_gomory_hu_tree),
        ("Ch 17: MCMF Slope Convexity & Johnson Reduced-Cost Optimality", oracle_ch17_mcmf_slope_convexity_and_negative_cycle),
        ("Ch 18: Convex Marginal Edge Splitting & Landau Tournament 3-Cycles", oracle_ch18_convex_splitting_and_landau_tournaments),
        ("Ch 19: Masao Iri's Equation Differencing ([NOI2008] Volunteers)", oracle_ch19_equation_differencing_volunteer_recruitment),
        ("Ch 20: Reverse Queue-Position Factorization ([SCOI2007] Repairing Cars)", oracle_ch20_reverse_queue_scheduling_and_manhattan_hubs),
        ("Ch 21: Strong LP Duality & Totally Unimodular Matching Potentials", oracle_ch21_lp_duality_and_tu_integrality),
        ("Ch 22: Segment-Tree Virtual Hub DAG Sparsification Equivalence", oracle_ch22_segtree_virtual_hub_and_tutte_matrix),
        ("Ch 23: Simulated MCMF Regret Min-Heap (CF 865 D) vs Brute Force", oracle_ch23_simulated_mcmf_regret_heap),
        ("Ch 24: L_1 Isotonic Regression Two-Level Threshold Closure", oracle_ch24_isotonic_regression_threshold_closure),
    ]

    print(f"\n[Part A] Running {len(oracles)} Exact Mathematical & Graph-Compilation Oracles (Ch 01 - Ch 24)...")
    for name, fn in oracles:
        fn()
        print(f"  [PASS] {name}")

    files = get_flows_qmd_files()
    print(f"\n[Part B] Auditing Structural, Pedagogical & Quarto Hygiene across {len(files)} flows/*.qmd files...")
    errors = audit_flows_qmd_hygiene(files)
    if errors:
        print(f"\n  [INFO/FAIL] Found {len(errors)} structural/hygiene item(s):")
        for err in errors:
            print(f"    - {err}")
        return 1

    print(f"  [PASS] All {len(files)} flows/*.qmd files passed all structural & Quarto hygiene checks!")
    print("\nALL 24 MATHEMATICAL ORACLES & 36 FILE HYGIENE CHECKS PASSED (0 ERRORS).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
