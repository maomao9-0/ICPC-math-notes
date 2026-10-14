# Wave 3A Research & Audit Record (Iterations 21–25): Lagrange–Bürmann Inversion, Formal Laurent Series & Residue Calculus ("炫酷反演魔术"), Derivative-Free & Compound Forms, Tree/Forest/Prüfer/Cactus Enumerations, and Graph Enumerations

> **Scope of Wave 3A**: This document records Iterations 21–25 of the multilingual (`[EN]`, `[ZH]`, `[JA]`) Formal Power Series (FPS) and Generating Functions research and audit loop. It establishes both the combinatorial (Raney / Cycle Lemma and Joyal's double-rooted trees) and algebraic (Formal Laurent Series $K((x))$ and Formal Residue $\operatorname{res}_x$) foundations of Lagrange–Bürmann Inversion, demystifies the change-of-variables calculus known in the Chinese competitive programming literature as **"炫酷反演魔术" (Cool Inversion Magic)**, contrasts standard divided Lagrange forms against derivative-free (`另类拉格朗日反演`) and compound forms, and develops the complete generating-function machinery for trees, Prüfer codes, degree-constrained trees, cacti/deserts, functional graphs, Eulerian graphs, bipartite graphs, strongly connected tournaments, DAGs, and biconnected / 2-edge-connected graphs.

---

## Iteration 21: Standard Lagrange–Bürmann Inversion ($F = x\Phi(F)$) & Combinatorial Raney/Cycle Lemma Intuition

### 21.1 Concrete Objects, Implicit Equations & Precondition Contracts
Let $R$ be a commutative ring with identity $1$. Suppose we are given a formal power series $\Phi(t) = \sum_{m=0}^\infty \phi_m t^m \in R[[t]]$ describing the local branching structure of a rooted object, and we consider the implicit functional equation
$$F(x) = x \Phi\bigl(F(x)\bigr).$$
Combinatorially, $x$ marks one root atom of size $1$, and $\Phi(F(x))$ assembles a $\Phi$-structured collection of child sub-objects of the same class $F$.

#### Three Distinct Algebraic Precondition Tiers
A frequent source of bugs in competitive programming is conflating the algebraic conditions required for (1) existence and uniqueness of $F(x)$, (2) compositional invertibility, and (3) divided Lagrange coefficient extraction:

| Operation / Claim | Exact Algebraic Precondition in $R$ | What Happens When Violated? |
| :--- | :--- | :--- |
| **1. Unique Solution $F(x) \in xR[[x]]$** to $F(x) = x\Phi(F(x))$ | **None** ($\Phi(t) \in R[[t]]$ can be arbitrary, even $\Phi(0) = 0$) | Always uniquely determined coefficient-by-coefficient since $[x^n]F(x) = [x^{n-1}]\Phi(F(x))$ only reads $f_1, \dots, f_{n-1}$. (If $\Phi(0)=0$, then $F(x)=0$.) |
| **2. Compositional Inverse $G(F(x)) = x$** where $G(t) = \frac{t}{\Phi(t)}$ | $\phi_0 = [t^0]\Phi(t) \in R^\times$ (a **unit** in $R$) | If $\phi_0$ is not invertible in $R$, $\Phi(t)^{-1}$ does not exist in $R[[t]]$, so $G(t) = t / \Phi(t)$ is not a well-defined power series in $t R[[t]]$. |
| **3. Divided Lagrange–Bürmann Formula** $[x^n] H(F(x)) = \frac{1}{n} [t^{n-1}] H'(t) \Phi(t)^n$ | $n \in R^\times$ ($n$ is invertible in $R$, e.g. $p \nmid n$ in $\mathbb{F}_p$) | Division by $n$ is undefined when $p \mid n$; must use the **division-free identity** $n[x^n]H(F) = [t^{n-1}]H'(t)\Phi(t)^n$ or the **derivative-free residue form** (Iteration 23). |

#### Failure Mode: Applying Lagrange Inversion When $B(0) = c \neq 0$
Suppose an implicit equation is given in the form $B(x) = 1 + x B(x)^r$ (such as the Catalan or Fuss–Catalan series) or $B(x) = e^{x B(x)^r}$.
- **Trap**: You **cannot** directly set $\Phi(t) = 1 + t^r$ because $B(x)$ is not of the form $x \Phi(B(x))$ and $B(0) = 1 \neq 0$ (so $B(B(x))$ is not even composable in $R[[x]]$!).
- **Fix (Constant-Term Shift)**: Always subtract the constant term first by setting $F(x) = B(x) - B(0)$ (so $F(0) = 0$), or isolate the factor containing $x$ (such as setting $F(x) = x B(x)^r$). For $B(x) = 1 + x B(x)^r$, setting $F(x) = B(x) - 1$ gives $B(x) = 1 + F(x)$ and
  $$F(x) = x \bigl(1 + F(x)\bigr)^r = x \Phi\bigl(F(x)\bigr) \quad \text{with } \Phi(t) = (1 + t)^r, \; F(0) = 0!$$

---

### 21.2 Combinatorial Proof via Łukasiewicz Words & Raney's Lemma (Cycle Lemma)
Why does an implicit equation $F(x) = x \Phi(F(x))$ where $F(x)$ appears nested inside itself collapse to a simple power $\Phi(t)^n$ scaled by $\frac{k}{n}$?

**Theorem (Lagrange–Bürmann Power & Functional Forms)**: For any commutative ring $R$, any formal power series $\Phi(t), H(t) \in R[[t]]$, and any integers $n \ge 1, k \ge 1$, the unique solution $F(x) \in x R[[x]]$ to $F(x) = x \Phi(F(x))$ satisfies the division-free identities in $R$:
$$n [x^n] F(x)^k = k [t^{n-k}] \Phi(t)^n, \qquad n [x^n] H\bigl(F(x)\bigr) = [t^{n-1}] H'(t) \Phi(t)^n.$$
When $n \in R^\times$, dividing by $n$ gives:
$$\boxed{[x^n] F(x)^k = \frac{k}{n} [t^{n-k}] \Phi(t)^n, \qquad [x^n] H\bigl(F(x)\bigr) = \frac{1}{n} [t^{n-1}] H'(t) \Phi(t)^n.}$$
*(Note that for $n \ge 1$, the constant term $h_0 = [t^0]H(t)$ contributes $0$ to $[x^n]H(F(x))$ because $F(0) = 0$, which matches $H'(t) = \sum_{k \ge 1} k h_k t^{k-1}$ annihilating $h_0$.)*

#### Step-by-Step Double-Counting Derivation via Raney's Lemma
1. **Concrete Combinatorial Model (Ordered Forests of $k$ Plane Rooted Trees)**:
   Interpret $\phi_d = [t^d]\Phi(t)$ as the weight of a vertex with out-degree (number of ordered children) $d \ge 0$. Then:
   - $[x^n] F(x)$ is the total weight of plane rooted trees on $n$ vertices.
   - $[x^n] F(x)^k$ is the total weight of **ordered forests of $k$ plane rooted trees** $(T_1, T_2, \dots, T_k)$ containing $n$ vertices in total.
2. **Encoding a Forest as a Preorder Out-Degree Sequence (Łukasiewicz Word)**:
   Walk the $k$ trees $T_1, \dots, T_k$ in **preorder** (visit the root, then recursively visit its subtrees from left to right), and record the out-degree $d_i \ge 0$ of the $i$-th visited vertex for $i = 1, 2, \dots, n$.
   - The weight of the forest is $\prod_{i=1}^n \phi_{d_i}$.
   - Think of maintaining a stack of "unfilled child slots", initially containing $k$ slots for the $k$ roots. When we visit vertex $i$ of out-degree $d_i$, it consumes $1$ slot and pushes $d_i$ new slots onto the stack, changing the stack size by
     $$s_i = d_i - 1 \in \{-1, 0, 1, 2, \dots\}.$$
   - A sequence $(d_1, \dots, d_n) \in \mathbb{Z}_{\ge 0}^n$ is the valid preorder degree sequence of a $k$-tree forest if and only if:
     1. **Total Sum Condition**: All $k$ initial slots are eventually consumed at the end of the $n$ vertices:
        $$\sum_{i=1}^n (d_i - 1) = -k \iff \sum_{i=1}^n d_i = n - k.$$
     2. **Prefix Positivity Condition**: The stack never becomes empty before step $n$, i.e., every proper prefix sum $S_m = \sum_{i=1}^m (d_i - 1)$ satisfies $S_m > -k$ for all $1 \le m < n$, and $S_n = -k$.
3. **Unconstrained Degree Sequences vs. Valid Forests**:
   Notice that $[t^{n-k}] \Phi(t)^n = \sum_{d_1 + \dots + d_n = n-k} \prod_{i=1}^n \phi_{d_i}$ counts **all** sequences $(d_1, \dots, d_n)$ satisfying the Total Sum Condition $\sum_{i=1}^n (d_i - 1) = -k$, without the Prefix Positivity Condition!
4. **Raney's Lemma (The Cycle Lemma)**:
   Let $(s_1, s_2, \dots, s_n)$ be any sequence of integers with $s_i \ge -1$ and $\sum_{i=1}^n s_i = -k < 0$. Consider the $n$ cyclic shifts $s^{(r)} = (s_{r+1}, \dots, s_n, s_1, \dots, s_r)$ for $r \in \{0, 1, \dots, n-1\}$.
   - Because each step $s_i \ge -1$ can decrease the running sum by **at most $1$** (no downward skips!) and each full period of length $n$ decreases the running sum by $-k$, on the infinite periodic extension of $s$, for each of the $k$ residue classes mod $k$ of the running minimum, there is a **unique** last position $r \in \{0, \dots, n-1\}$ where that level is achieved.
   - Starting the cyclic shift immediately after any of those $k$ positions yields a sequence whose proper prefix sums stay strictly above $-k$ and reach $-k$ for the first time at step $n$.
   - Thus, out of the $n$ cyclic shift positions $r \in \{0, \dots, n-1\}$ of any sequence $(d_1, \dots, d_n)$ with $\sum d_i = n - k$, **exactly $k$ cyclic shifts** are valid $k$-tree forests!
   - Double-counting pairs $\bigl((d_1, \dots, d_n), r\bigr)$ where $r \in \{0, \dots, n-1\}$ immediately gives:
     $$n [x^n] F(x)^k = k [t^{n-k}] \Phi(t)^n,$$
     and extending by linearity to $H(t) = \sum_{k \ge 0} h_k t^k$ (where $H'(t) = \sum_{k \ge 1} k h_k t^{k-1}$) yields $n [x^n] H(F(x)) = [t^{n-1}] H'(t) \Phi(t)^n$. $\blacksquare$

#### Why the Same Formula Works for Labelled EGFs (Joyal's Bijection)
When $\Phi(t) = \sum_{d=0}^\infty \psi_d \frac{t^d}{d!}$ is an Exponential Generating Function, $n! [t^{n-k}] \Phi(t)^n$ counts ways to assign an ordered tuple of children to each of $n$ labelled vertices $\{1, \dots, n\}$ using $n - k$ directed edges in total. If those $n - k$ edges form an acyclic forest of $k$ rooted trees, there are $\binom{n}{k} k! = \frac{n!}{(n-k)!}$ ways to choose and order the $k$ roots, whereas if cycles exist, Joyal's functional-graph bijection (breaking cycles along the unique path between two distinguished vertices) proves that a $\frac{k}{n}$ fraction of all functional-digraph local stars are acyclic $k$-tree forests!

---

### 21.3 Small Hand-Checkable Example of Raney's Lemma ($n = 4, k = 2$)
Let $\Phi(t) = 1 + t + t^2$ (unary-binary plane trees) and take $n = 4$ vertices, $k = 2$ trees.
- By Lagrange Inversion, $[x^4] F(x)^2 = \frac{2}{4} [t^{4-2}] (1 + t + t^2)^4 = \frac{1}{2} [t^2] (1 + 4t + 10t^2 + \dots) = 5$.
- Let us verify how the $10$ unconstrained sequences $(d_1, d_2, d_3, d_4) \in \{0, 1, 2\}^4$ with $\sum_{i=1}^4 d_i = 2$ (so $s_i = d_i - 1 \in \{-1, 0, +1\}$ with $\sum_{i=1}^4 s_i = -2$) partition into cyclic orbits where **exactly $\frac{k}{n} = \frac{2}{4} = \frac{1}{2}$** of each orbit is a valid $2$-tree forest:
  1. **Orbit 1 (4 shifts of $d = (2, 0, 0, 0)$, $s = (+1, -1, -1, -1)$)**:
     - $(+1, -1, -1, -1) \implies$ prefix sums $(1, 0, -1, -2)$: **Valid** ($T_1$ has 3 nodes, $T_2$ has 1 node).
     - $(-1, -1, -1, +1) \implies$ prefix sums $(-1, -2, -3, -2)$: Invalid (hits $-2$ at step $2 < 4$).
     - $(-1, -1, +1, -1) \implies$ prefix sums $(-1, -2, -1, -2)$: Invalid (hits $-2$ at step $2 < 4$).
     - $(-1, +1, -1, -1) \implies$ prefix sums $(-1, 0, -1, -2)$: **Valid** ($T_1$ has 1 node, $T_2$ has 3 nodes).
     *(2 valid out of 4 shifts).*
  2. **Orbit 2 (4 shifts of $d = (1, 1, 0, 0)$, $s = (0, 0, -1, -1)$)**:
     - $(0, 0, -1, -1) \implies$ prefix sums $(0, 0, -1, -2)$: **Valid** ($T_1$ has 3 nodes, $T_2$ has 1 node).
     - $(0, -1, -1, 0) \implies$ prefix sums $(0, -1, -2, -2)$: Invalid (hits $-2$ at step $3 < 4$).
     - $(-1, -1, 0, 0) \implies$ prefix sums $(-1, -2, -2, -2)$: Invalid (hits $-2$ at step $2 < 4$).
     - $(-1, 0, 0, -1) \implies$ prefix sums $(-1, -1, -1, -2)$: **Valid** ($T_1$ has 1 node, $T_2$ has 3 nodes).
     *(2 valid out of 4 shifts).*
  3. **Orbit 3 (2 shifts of periodic sequence $d = (1, 0, 1, 0)$, $s = (0, -1, 0, -1)$)**:
     - $(0, -1, 0, -1) \implies$ prefix sums $(0, -1, -1, -2)$: **Valid** ($T_1$ has 2 nodes, $T_2$ has 2 nodes).
     - $(-1, 0, -1, 0) \implies$ prefix sums $(-1, -1, -2, -2)$: Invalid (hits $-2$ at step $3 < 4$).
     *(1 valid out of 2 distinct shifts; when paired with the $n=4$ cyclic shift indices $r \in \{0,1,2,3\}$, $r=0,2$ are valid and $r=1,3$ are invalid, so still $k = 2$ valid shift indices out of $n = 4$!).*
  - **Total valid 2-tree forests**: $2 + 2 + 1 = 5$, matching $\frac{2}{4} \times 10 = 5$.

---

### 21.4 Diagnostic Signals & Reverse-Engineering Scratchpad ("How Would I Think of This?")

| Direction | Diagnostic Signal in the Problem | Reverse-Engineering Scratchpad |
| :--- | :--- | :--- |
| **Forward (Implicit GF $\to$ Coefficient)** | You have a recursive equation where $F(x)$ appears inside an exponential, power, or rational function, e.g. $F(x) = x e^{F(x)}$ or $B(x) = 1 + x B(x)^r$. | **Step 1**: Check $[x^0]B(x)$. If $B(0) = c \neq 0$, shift the unknown by setting $F(x) = B(x) - c$ so $F(0) = 0$.<br>**Step 2**: Factor out $x$ to isolate $F(x) = x \Phi(F(x))$ and apply LIF! |
| **Backward (Coupled Sum $\to$ Implicit GF)** | A summation contains $\frac{k}{n}\binom{rn}{n-k}$, $\frac{k}{rn+k}\binom{rn+k}{n}$, $\frac{k}{n}\frac{(rn)^{n-k}}{(n-k)!}$, or $[t^{n-k}] \Phi(t)^n$ where **the exponent $n$ of $\Phi(t)^n$ varies with the extraction index $n$**. | **Why it's hard**: Because $n$ is in both $[t^{n-k}]$ and $\Phi(t)^n$, you cannot swap sums over $n$!<br>**Scratchpad Fix**: Read Lagrange Inversion *backwards*: replace $\frac{k}{n}[t^{n-k}]\Phi(t)^n$ by $[x^n] F(x)^k$ where $F = x\Phi(F)$! Now $n$ only appears in $[x^n]$, decoupling the outer sum! |

---

## Iteration 22: Formal Laurent Series $K((x))$, Formal Residue Calculus ($\operatorname{res}_x$) & Change-of-Variables Formula ("炫酷反演魔术")

### 22.1 Concrete Construction of the Formal Laurent Series Ring $R((x))$ and Field $K((x))$
To manipulate generating functions with negative powers (such as $\frac{1}{x^{n+1}}$ or $\frac{1}{F(x)^{n+1}}$ when $F(0) = 0$) without worrying about analytic convergence or complex contour integrals, we enlarge the formal power series ring $R[[x]]$ into the **formal Laurent series ring** $R((x)) = R[[x]][x^{-1}]$.

1. **Concrete Data-Structure Mental Model**:
   An element $A(x) \in R((x))$ is a sequence $(a_n)_{n \in \mathbb{Z}}$ of coefficients in $R$ such that **only finitely many negative indices are nonzero**:
   $$A(x) = \sum_{n = v}^\infty a_n x^n = x^v \sum_{m=0}^\infty a_{v+m} x^m = x^v U(x), \qquad v \in \mathbb{Z}, \; U(x) \in R[[x]].$$
   In code, a formal Laurent series truncated to relative precision $N$ is simply a pair `(int v, Poly U)` representing $x^v U(x) \bmod x^{v+N}$.
2. **Integer Valuation $v(A)$ and Why $K((x))$ is a Field**:
   For $A(x) \neq 0$, its **valuation** (or order) is the smallest integer $v \in \mathbb{Z}$ with $a_v \neq 0$:
   $$v(A) = \operatorname{ord}_x(A) := \min\{n \in \mathbb{Z} : [x^n] A(x) \neq 0\} \in \mathbb{Z}, \qquad v(0) = +\infty.$$
   When $K$ is a field (or more generally whenever the leading coefficient $a_v \in R^\times$ is a unit in $R$), $A(x) = x^v U(x)$ has $[x^0]U(x) = a_v \in R^\times$, so $U(x)$ is invertible in $R[[x]]$ and $A(x)^{-1} = x^{-v} U(x)^{-1} \in R((x))$ is its exact multiplicative inverse! In particular, when $K$ is a field, $K((x))$ is a **field** (the fraction field of $K[[x]]$).
3. **Composition in $R((x))$**:
   If $A(x) = \sum_{n=v}^\infty a_n x^n \in R((x))$ and $g(u) \in R((u))$ is a Laurent series with **strictly positive valuation** $v(g) = k \ge 1$ and unit leading coefficient $[u^k]g(u) \in R^\times$ (if $v < 0$), then $v(g(u)^n) = k n \to +\infty$ as $n \to +\infty$. Consequently, for every target degree $m \in \mathbb{Z}$, only finitely many $n \ge v$ satisfy $k n \le m$, so the substituted Laurent series
   $$A\bigl(g(u)\bigr) = \sum_{n=v}^\infty a_n g(u)^n \in R((u))$$
   is **100% algebraically well-defined** with finite coefficient sums at every power of $u$.

---

### 22.2 Formal Differential 1-Forms and the Formal Residue Operator $\operatorname{res}_x$
For any formal Laurent series $A(x) = \sum_{n=v}^\infty a_n x^n \in R((x))$, we write $A(x)\,dx$ for the formal differential 1-form in variable $x$, and define its **formal residue** (denoted $\operatorname{res}_x A(x)\,dx$ or $[x^{-1}] A(x)$) to be the coefficient of $x^{-1}$:
$$\boxed{\operatorname{res}_x A(x)\,dx := [x^{-1}] A(x) = a_{-1}.}$$
Why attach the symbol $dx$? Because when we change variables via $x = g(u)$, the differential transforms by the formal chain rule $dx = g'(u)\,du$, and the notation $A(x)\,dx = A(g(u)) g'(u)\,du$ automatically reminds us to multiply by the Jacobian factor $g'(u)$!

Every coefficient extraction $[x^n] F(x)$ ($n \in \mathbb{Z}$) is a formal residue:
$$[x^n] F(x) = [x^{-1}] \frac{F(x)}{x^{n+1}} = \operatorname{res}_x \frac{F(x)}{x^{n+1}}\,dx.$$

---

### 22.3 The Four Fundamental Laws of Formal Residue Calculus (with Characteristic-Free Proofs)
In his influential Chinese competitive programming blog *《炫酷反演魔术》 (Cool Inversion Magic)*, Baitian Li (`Elegia` / `李白天`) popularized Jacobi's and Egorychev's method of formal residues as a unified replacement for ad-hoc generating function identities. The entire calculus rests on four laws that hold over **arbitrary commutative rings $R$**:

#### Law 1: Linearity
For any $\alpha, \beta \in R$ and $A(x), B(x) \in R((x))$,
$$\operatorname{res}_x \bigl(\alpha A(x) + \beta B(x)\bigr)\,dx = \alpha \operatorname{res}_x A(x)\,dx + \beta \operatorname{res}_x B(x)\,dx.$$

#### Law 2: Vanishing of Formal Derivatives
For **any** formal Laurent series $A(x) = \sum_{n=v}^\infty a_n x^n \in R((x))$ over **any** commutative ring $R$ (regardless of characteristic!),
$$\boxed{\operatorname{res}_x A'(x)\,dx = 0.}$$
**Proof**: Differentiating term-by-term gives $A'(x) = \sum_{n=v}^\infty n a_n x^{n-1}$. The coefficient of $x^{-1}$ in $A'(x)$ comes from the index $n - 1 = -1 \iff n = 0$, which has coefficient $0 \cdot a_0 = 0$ in every ring $R$. $\blacksquare$

#### Law 3: Formal Integration by Parts
For any $A(x), B(x) \in R((x))$ over any commutative ring $R$,
$$\boxed{\operatorname{res}_x A'(x) B(x)\,dx = -\operatorname{res}_x A(x) B'(x)\,dx.}$$
**Proof**: Apply Law 2 to the formal product rule $\bigl(A(x) B(x)\bigr)' = A'(x) B(x) + A(x) B'(x)$. $\blacksquare$

#### Law 4: The Formal Change-of-Variables Theorem (Jacobi's Formal Residue Lemma)
Let $R$ be **any commutative ring with identity** (of **any** characteristic, including $\mathbb{F}_p$!), and let $g(u) = \sum_{i=1}^\infty g_i u^i \in u R[[u]]$ be a formal power series with valuation $v(g) = 1$ and unit leading coefficient $g_1 = [u^1]g(u) \in R^\times$. Then for every formal Laurent series $A(x) \in R((x))$, substituting $x = g(u)$ and $dx = g'(u)\,du$ preserves the formal residue:
$$\boxed{\operatorname{res}_x A(x)\,dx = \operatorname{res}_u A\bigl(g(u)\bigr) g'(u)\,du \qquad \Longleftrightarrow \qquad [x^{-1}] A(x) = [u^{-1}] A\bigl(g(u)\bigr) g'(u).}$$
*(More generally, if $g(u) \in R((u))$ has valuation $v(g) = k \neq 0$ with invertible leading coefficient $[u^k]g(u) \in R^\times$, then $\operatorname{res}_u A(g(u)) g'(u)\,du = k \cdot \operatorname{res}_x A(x)\,dx$.)*

**Complete Characteristic-Free Algebraic Proof**:
By linearity and the $u$-adic convergence of $A(g(u)) = \sum_{n=v}^\infty a_n g(u)^n$, it suffices to prove that for every integer $n \in \mathbb{Z}$,
$$\operatorname{res}_u g(u)^n g'(u)\,du = \begin{cases} 1 & \text{if } n = -1, \\ 0 & \text{if } n \neq -1. \end{cases}$$
1. **Case $n = -1$**: Factor $g(u) = g_1 u U(u)$ where $U(u) = 1 + \sum_{i=1}^\infty (g_{i+1}/g_1) u^i \in R[[u]]$ has constant term $U(0) = 1$. By the product rule, $g'(u) = g_1 U(u) + g_1 u U'(u)$, so dividing by $g(u) = g_1 u U(u)$ gives:
   $$\frac{g'(u)}{g(u)} = \frac{1}{u} + \frac{U'(u)}{U(u)}.$$
   Since $U(0) = 1$, $U(u)^{-1} \in R[[u]]$ and $U'(u) \in R[[u]]$ contain **no negative powers of $u$**, so $[u^{-1}]\frac{U'(u)}{U(u)} = 0$ and $\operatorname{res}_u g(u)^{-1} g'(u)\,du = [u^{-1}]\frac{1}{u} = 1$.
2. **Case $n \neq -1$ (Why It Holds Even When $p \mid (n+1)$)**:
   - First suppose $R = \mathbb{Q}[G_1, G_1^{-1}, G_2, G_3, \dots]$ is the ring of Laurent polynomials in formal indeterminates $G_1, G_2, \dots$ over $\mathbb{Q}$, and let $\widetilde{g}(u) = \sum_{i=1}^\infty G_i u^i$. Because $n + 1 \neq 0$ is invertible in $\mathbb{Q}$, we have
     $$\widetilde{g}(u)^n \widetilde{g}'(u) = \frac{d}{du} \left( \frac{\widetilde{g}(u)^{n+1}}{n+1} \right) \in R((u)).$$
     By Law 2, $\operatorname{res}_u \widetilde{g}(u)^n \widetilde{g}'(u)\,du = 0$ in $\mathbb{Q}[G_1, G_1^{-1}, G_2, \dots]$.
   - Now observe that expanding $\widetilde{g}(u)^n \widetilde{g}'(u) = G_1^n u^{n-1} (1 + \dots)^n (G_1 + 2 G_2 u + \dots)$ only uses binomial coefficients $\binom{n}{j} \in \mathbb{Z}$ and integer multipliers $i \in \mathbb{Z}$! Therefore, the coefficient $[u^{-1}] \widetilde{g}(u)^n \widetilde{g}'(u)$ actually lies in the subring $\mathbb{Z}[G_1, G_1^{-1}, G_2, \dots]$, and since it vanishes in $\mathbb{Q}[G_1, G_1^{-1}, G_2, \dots]$, it is the **zero polynomial in $\mathbb{Z}[G_1, G_1^{-1}, G_2, \dots]$**!
   - Specializing the indeterminates $G_i \mapsto g_i \in R$ via the canonical ring homomorphism $\mathbb{Z}[G_1, G_1^{-1}, G_2, \dots] \to R$ proves $\operatorname{res}_u g(u)^n g'(u)\,du = 0$ in **every commutative ring $R$ of any characteristic**! $\blacksquare$

---

### 22.4 The 5-Archetype Residue Substitution Cookbook ("炫酷反演魔术": How to Discover the Right Substitution)
Why do competitive programmers struggle to see substitutions like $x = u(1-u)$, $x = \frac{u}{(1+u)^2}$, $x = \frac{u}{1+au+bu^2}$, or $x = u e^{-ru}$? Because when written in coefficient notation $[x^n]$, there is no Jacobian $dx = g'(u)\,du$ visible!

With $\operatorname{res}_x$, the discovery process is **100% mechanical**. Whenever you face an ugly coefficient extraction $[x^n] F(x) = \operatorname{res}_x \frac{F(x)}{x^{n+1}}\,dx$, look at the structural bottleneck in $F(x)$ and apply the matching archetype from the table below:

| Archetype | Diagnostic Signal in $F(x)$ or Sum | How to Solve for $x = g(u)$ on Scratch Paper | What $dx = g'(u)\,du$ Cancels! |
| :--- | :--- | :--- | :--- |
| **1. Catalan / Dyck Radical** | Contains $\sqrt{1 - 4x}$ and/or powers of $C(x) = \frac{1 - \sqrt{1-4x}}{2x}$ | Set $u = x C(x) = \frac{1-\sqrt{1-4x}}{2} \implies \sqrt{1-4x} = 1 - 2u$ and $x = u(1-u)$ (or set $v = C(x)-1 \implies x = \frac{v}{(1+v)^2}$). | $dx = (1 - 2u)\,du = \sqrt{1 - 4x}\,du$ **cancels $\frac{1}{\sqrt{1-4x}}$ identically**! |
| **2. Trinomial / Motzkin / Delannoy Radical** | Contains $\frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}}$ (e.g. $\frac{1}{\sqrt{1 - 2x - 3x^2}}$ or $\frac{1}{\sqrt{1 - 6x + x^2}}$) | We want $1 - 2ax + (a^2-4b)x^2$ to become a perfect square: substitute $x = \frac{u}{1 + au + bu^2}$. | $\sqrt{1 - 2ax + (a^2-4b)x^2} = \frac{1 - bu^2}{1 + au + bu^2}$ and $dx = \frac{1 - bu^2}{(1+au+bu^2)^2}\,du$ **cancels the radical**! |
| **3. Coupled Binomial Upper Index** | Sum contains $\binom{rn + k}{n} x^n$ or $\binom{n + rk}{k} x^k$ where both $n$ and $k$ move in the upper index | Write $\binom{rn+k}{n} = \operatorname{res}_u \frac{(1+u)^{rn+k}}{u^{n+1}}\,du = \operatorname{res}_u (1+u)^k \left(\frac{(1+u)^r}{u}\right)^n \frac{du}{u}$. Group the $n$-th power by setting $x = \frac{u}{(1+u)^r}$! | Converts $\sum_n \binom{rn+k}{n} x^n$ into a geometric series $\operatorname{res}_u \sum_n \left(\frac{x(1+u)^r}{u}\right)^n \dots$! |
| **4. Coupled Power / Abel / Lambert Sum** | Sum contains $\frac{(rn + k)^n}{n!} x^n$ or $\frac{(rn + k)^{n-1}}{n!} x^n$ | Write $\frac{(rn+k)^n}{n!} = \operatorname{res}_u \frac{e^{(rn+k)u}}{u^{n+1}}\,du = \operatorname{res}_u e^{ku} \left(\frac{e^{ru}}{u}\right)^n \frac{du}{u}$. Group the $n$-th power by setting $x = u e^{-ru}$! | Decouples $(rn+k)^n$ into $e^{ku} \cdot (e^{ru})^n$ so the sum over $n$ becomes rational in $u$! |
| **5. Hidden Jacobian Factor** | Expression has a strange linear-in-derivative factor like $1 - 2u$, $1 - r u (1+u)^{-1}$, or $\Phi(u) - u\Phi'(u)$ | Compare the factor against $\frac{d}{du}\!\left(\frac{u}{\Phi(u)}\right) = \frac{\Phi(u) - u\Phi'(u)}{\Phi(u)^2}$. That factor is literally the Jacobian $g'(u)$! | Absorbs $g'(u)\,du = dx$ backwards to turn a messy $[u^n]$ extraction into a clean $[x^n]$ extraction! |

#### Worked Scratchpad Example 1: Radical Cancellation via $x = u(1-u)$
Extract $[x^n] \frac{1}{\sqrt{1 - 4x}} \left(\frac{1 - \sqrt{1 - 4x}}{2x}\right)^k$:
1. **Scratchpad Diagnosis**: We see $\sqrt{1 - 4x}$ and $C(x) = \frac{1 - \sqrt{1-4x}}{2x}$. Using Archetype 1, set $x = u(1 - u)$ ($v(x) = 1$). Then $\sqrt{1 - 4x} = 1 - 2u$, $C(x) = \frac{1}{1 - u}$, and $dx = (1 - 2u)\,du$.
2. **One-Line Residue Calculation**:
   $$\begin{aligned}
   [x^n] \frac{C(x)^k}{\sqrt{1 - 4x}}
   &= \operatorname{res}_x \frac{C(x)^k}{\sqrt{1 - 4x}} \frac{dx}{x^{n+1}}
   = \operatorname{res}_u \frac{(1 - u)^{-k}}{1 - 2u} \frac{(1 - 2u)\,du}{u^{n+1}(1 - u)^{n+1}} \\
   &= \operatorname{res}_u \frac{du}{u^{n+1} (1 - u)^{n+k+1}} = [u^n] (1 - u)^{-(n+k+1)} = \binom{2n + k}{n}.
   \end{aligned}$$

#### Worked Scratchpad Example 2: Central Trinomial / Delannoy Radical via $x = \frac{u}{1 + au + bu^2}$
Extract $[x^n] \frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}}$ (which counts central trinomial coefficients when $a=1, b=1$ so $1 - 2x - 3x^2$, or Legendre polynomials / Delannoy paths):
1. **Scratchpad Diagnosis**: Inside the square root is $1 - 2ax + (a^2 - 4b)x^2$. Following Archetype 2, substitute $x = \frac{u}{1 + au + bu^2}$ (which has $x(0) = 0, x'(0) = 1$).
2. **Check the Radical and the Jacobian $dx$**:
   - Inside the radical:
     $$1 - 2a \frac{u}{1 + au + bu^2} + (a^2 - 4b) \frac{u^2}{(1 + au + bu^2)^2} = \frac{(1 + au + bu^2)^2 - 2au(1 + au + bu^2) + (a^2 - 4b)u^2}{(1 + au + bu^2)^2} = \frac{(1 - bu^2)^2}{(1 + au + bu^2)^2}!$$
     So $\frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}} = \frac{1 + au + bu^2}{1 - bu^2}$.
   - Now differentiate $x = \frac{u}{1 + au + bu^2}$ by the quotient rule:
     $$dx = \frac{(1 + au + bu^2) - u(a + 2bu)}{(1 + au + bu^2)^2}\,du = \frac{1 - bu^2}{(1 + au + bu^2)^2}\,du!$$
   - Look at the product of the radical and $dx$: the $1 - bu^2$ in the numerator of $dx$ and the $1 - bu^2$ in the denominator of the radical **cancel completely**!
3. **One-Line Residue Calculation**:
   $$\begin{aligned}
   [x^n] \frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}}
   &= \operatorname{res}_x \frac{1}{\sqrt{1 - 2ax + (a^2 - 4b)x^2}} \frac{dx}{x^{n+1}} \\
   &= \operatorname{res}_u \left(\frac{1 + au + bu^2}{1 - bu^2}\right) \frac{(1 + au + bu^2)^{n+1}}{u^{n+1}} \frac{1 - bu^2}{(1 + au + bu^2)^2}\,du \\
   &= \operatorname{res}_u \frac{(1 + au + bu^2)^n}{u^{n+1}}\,du = [u^n] \bigl(1 + au + bu^2\bigr)^n!
   \end{aligned}$$

---

### 22.5 Egorychev's Double-Residue Method for Coupled Binomial Sums
When a sum $S_n = \sum_{k=0}^n \binom{A k + B}{k} \binom{C(n-k) + D}{n-k}$ or $\sum_{k} (-1)^k \binom{\dots}{\dots}\binom{\dots}{\dots}$ cannot be written as a standard convolution because the upper indices depend on $k$:
1. **Step 1 (Residue Representation)**: Replace the binomial coefficients by formal residues using:
   $$\binom{m}{k} = \operatorname{res}_u \frac{(1 + u)^m}{u^{k+1}}\,du \qquad \text{or} \qquad \binom{m + k - 1}{k} = \operatorname{res}_u \frac{du}{(1 - u)^m u^{k+1}}.$$
2. **Step 2 (Geometric Summation Under $\operatorname{res}$)**: Swap $\sum_k$ inside $\operatorname{res}_u \operatorname{res}_v$. For example, if one factor has $u^{-(n-k)-1}$, summing $k$ from $0$ to $\infty$ (since the residue vanishes for $k > n$) produces a geometric series $\sum_{k=0}^\infty \left(\frac{u (1+v)^A}{v (1+u)^C}\right)^k = \frac{1}{1 - \frac{u(1+v)^A}{v(1+u)^C}}$.
3. **Step 3 (Eliminate One Variable by Substitution)**: Clear the denominator to get $\frac{1}{v - u (1+v)^A (1+u)^{-C}}$, which tells you the exact change of variables $w = v (1+v)^{-A}$ needed to collapse the double residue into a single residue!

---

## Iteration 23: Derivative-Free & Alternative Lagrange Forms ($G(F(x)) = x$) and Compound Forms ($F(x) = A(x)\Phi(F(x))$)

### 23.1 Deriving Both Lagrange Forms Simultaneously from $\operatorname{res}_x$
Let $F(x), G(u) \in x R[[x]]$ be compositional inverses ($G(F(x)) = x$, $v(F) = v(G) = 1$, $[x^1]F \in R^\times$), where $G(u) = \frac{u}{\Phi(u)}$ corresponds to $F(x) = x \Phi(F(x))$ with $\Phi(0) \in R^\times$. For any formal Laurent series $H(u) \in R((u))$ and any integer $n \in \mathbb{Z}$, apply the Formal Change-of-Variables Theorem (Law 4) with $u = F(x) \iff x = G(u)$ and $dx = G'(u)\,du$:

#### Form 1: The Derivative-Free / Residue Form (`另类拉格朗日反演`)
Over **any** commutative ring $R$ and for **any** integer $n \in \mathbb{Z}$ (with zero division by $n$!):
$$\boxed{\begin{aligned}
[x^n] H\bigl(F(x)\bigr)
&= \operatorname{res}_x \frac{H(F(x))}{x^{n+1}}\,dx = \operatorname{res}_u \frac{H(u) G'(u)}{G(u)^{n+1}}\,du \\
&= [u^n] H(u) G'(u) \left(\frac{u}{G(u)}\right)^{n+1} \\
&= [u^n] H(u) \bigl(\Phi(u) - u \Phi'(u)\bigr) \Phi(u)^{n-1}.
\end{aligned}}$$

#### Form 2: The Standard Divided Form (Obtained via Integration by Parts on Form 1)
When $n \neq 0$ and $n \in R^\times$, notice that $\frac{G'(u)}{G(u)^{n+1}} = -\frac{1}{n} \frac{d}{du}\bigl(G(u)^{-n}\bigr)$. Applying Formal Integration by Parts (Law 3) to Form 1 moves the derivative from $G(u)$ onto $H(u)$:
$$\boxed{\begin{aligned}
[x^n] H\bigl(F(x)\bigr)
&= \operatorname{res}_u H(u) \left(-\frac{1}{n} \bigl(G(u)^{-n}\bigr)'\right) du = \frac{1}{n} \operatorname{res}_u \frac{H'(u)}{G(u)^n}\,du \\
&= \frac{1}{n} [u^{n-1}] H'(u) \left(\frac{u}{G(u)}\right)^n = \frac{1}{n} [u^{n-1}] H'(u) \Phi(u)^n.
\end{aligned}}$$

#### Gessel's Universal Denominator Identity (Why Form 1 Cancels $1 - x \Phi'(F(x))$)
Look closely at Form 1 rewritten as $[x^n] H(F(x)) = [u^n] H(u) \left(1 - \frac{u \Phi'(u)}{\Phi(u)}\right) \Phi(u)^n$. Replacing $H(u)$ by $\frac{H(u)}{1 - u \Phi'(u)/\Phi(u)}$ cancels the Jacobian factor identically! Summing over all $n \ge 0$ gives **Gessel's Universal Generating Function Identity**:
$$\boxed{\sum_{n=0}^\infty \Bigl([u^n] H(u) \Phi(u)^n\Bigr) x^n = \frac{H\bigl(F(x)\bigr)}{1 - \frac{F(x) \Phi'(F(x))}{\Phi(F(x))}} = \frac{H\bigl(F(x)\bigr)}{1 - x \Phi'\bigl(F(x)\bigr)}.}$$
*(Notice where the denominator $1 - x \Phi'(F(x))$ comes from: differentiating $F(x) = x \Phi(F(x))$ with respect to $x$ gives $F'(x) = \Phi(F(x)) + x \Phi'(F(x)) F'(x) \implies \frac{x F'(x)}{F(x)} = \frac{1}{1 - x \Phi'(F(x))}$!)*

---

### 23.2 Decision Matrix: When to Use Derivative-Free Form 1 (`另类拉格朗日反演`) vs. Standard Form 2
In Chinese (`[ZH]`) and Japanese (`[JA]`) editorials, Form 1 is called **另类拉格朗日反演 (Alternative Lagrange Inversion)**. Why is Form 1 frequently indispensable even when Form 2 exists?

| Scenario | Why Standard Form 2 Fails or Struggles | How Derivative-Free Form 1 Solves It Cleanly |
| :--- | :--- | :--- |
| **1. Small Characteristic ($p \mid n$) or $n = 0$** | Divides by $n$, which is $0$ in $\mathbb{F}_p$ when $p \mid n$! | **Zero division by $n$**: $[u^n] H(u) G'(u) \left(\frac{u}{G(u)}\right)^{n+1}$ is valid over any commutative ring $R$ even when $p \mid n$ or $n \le 0$! |
| **2. $H(u)$ is a Laurent Series with $[u^{-1}]H'(u)$ Issues** | If $H(u) = u^{-k}$ or $H(u)$ has a pole at $u=0$, $H'(u)$ cannot have a $u^{-1}$ term, so Form 2 fails at $n = 0$ and shifts negative indices. | Keeps $H(u)$ **undifferentiated** and holds for all $H(u) \in R((u))$ and all $n \in \mathbb{Z}$! |
| **3. Coupled Sums $\sum_{k} c_k [x^n] F(x)^k$ or Bivariate Extraction** | In Form 2, $[x^n]F(x)^k = \frac{k}{n}[u^{n-k}]\Phi(u)^n$ has a prefactor $k$, forcing you to differentiate $\sum c_k u^k$. | In Form 1, $\sum_k c_k [x^n] F(x)^k = [u^n] \left(\sum_k c_k u^k\right) (\Phi(u) - u\Phi'(u))\Phi(u)^{n-1}$ pulls the sum directly inside without differentiating! |
| **4. Rationalizing the Denominator $1 - x \Phi'(F(x))$** | Problems asking for $[x^n] \frac{H(F(x))}{1 - x\Phi'(F(x))}$ look ugly under differentiation in Form 2. | By Gessel's Universal Identity above, $\frac{1}{1 - x\Phi'(F(x))}$ **cancels the Jacobian factor identically**, leaving $[u^n] H(u) \Phi(u)^n$! |

---

### 23.3 Compound Lagrange Forms ($F(x) = A(x)\Phi(F(x))$ and $H(F(x)) = B(x)$)
What if an implicit equation does not have a bare $x$ in front of $\Phi(F(x))$, but instead takes a **compound form**?

1. **Case A: $F(x) = A(x) \Phi\bigl(F(x)\bigr)$ where $A(x) \in x R[[x]]$ ($v(A) = 1, [x^1]A \in R^\times$)**
   - **Combinatorial Meaning**: Instead of a single root atom $x$, the root is a compound structure counted by $A(x)$, and the root structure attaches $\Phi(F(x))$.
   - **Single-Step Residue Reduction**: Write $\frac{F(x)}{\Phi(F(x))} = A(x)$. When $A^{\langle -1 \rangle}$ is an explicit rational or elementary function, apply $A^{\langle -1 \rangle}$ to both sides to express $x$ directly in terms of $u = F(x)$:
     $$x = A^{\langle -1 \rangle}\!\left(\frac{u}{\Phi(u)}\right) =: \widetilde{G}(u),$$
     and apply Form 1 or Form 2 to $x = \widetilde{G}(u)$ in a **single step**!
   - **Concrete Example**: Suppose $F(x) = \frac{x}{1 - x} \Phi\bigl(F(x)\bigr)$. Since $A(x) = \frac{x}{1-x}$ has compositional inverse $A^{\langle -1 \rangle}(w) = \frac{w}{1+w}$, we get:
     $$\frac{F(x)}{\Phi(F(x))} = \frac{x}{1 - x} \iff x = \frac{F(x)/\Phi(F(x))}{1 + F(x)/\Phi(F(x))} = \frac{F(x)}{\Phi(F(x)) + F(x)} \iff F(x) = x \Bigl(\Phi\bigl(F(x)\bigr) + F(x)\Bigr)!$$

2. **Case B: $H\bigl(F(x)\bigr) = B(x)$ where $F(x)$ and $B(x)$ are Known, and $H(u)$ is the Unknown Series**
   - This exact form appears in **Biconnected Graphs** ($B'(D(x)) = \ln \frac{D(x)}{x}$), **2-Edge-Connected Graphs** ($E^\bullet(W(x)) = D(x)$), and **Inverse Tree Transforms**.
   - To extract $[u^n] H(u)$ without computing the full compositional inverse $F^{\langle -1 \rangle}(u)$, write $[u^n] H(u) = \operatorname{res}_u \frac{H(u)}{u^{n+1}}\,du$ and substitute $u = F(x)$, $du = F'(x)\,dx$:
     $$\boxed{\begin{aligned}
     [u^n] H(u)
     &= \operatorname{res}_x \frac{H(F(x)) F'(x)}{F(x)^{n+1}}\,dx = [x^n] B(x) F'(x) \left(\frac{x}{F(x)}\right)^{n+1} \qquad (\text{Derivative-Free Form 1}) \\
     &= \frac{1}{n} [x^{n-1}] B'(x) \left(\frac{x}{F(x)}\right)^n \qquad (\text{Standard Divided Form 2, } n \ge 1).
     \end{aligned}}$$

---

### 23.4 The Three Canonical Closed-Form Series Families (Lambert $W$, Generalized Exponential $\mathcal{E}_r$, Generalized Binomial $\mathcal{B}_r$)
Combining Form 2 (for bare powers) and Gessel's Universal Denominator Identity from Form 1 (for the divided-by-Jacobian series) establishes the three classic generating-function families of *Concrete Mathematics* (§5.4, §7.5). Note carefully how $\mathcal{E}_r(x)$ and $\mathcal{B}_r(x)$ have constant term $1$ and are reduced to $F(0) = 0$ via explicit variable shifts:

1. **Cayley Tree / Lambert $W$ Series $T(x) = x e^{T(x)}$**:
   - Already has $T(0) = 0$ and $\Phi(u) = e^u$, so $1 - \frac{u\Phi'(u)}{\Phi(u)} = 1 - u$.
2. **Generalized Exponential Series $\mathcal{E}_r(x) = e^{x \mathcal{E}_r(x)^r}$**:
   - Since $\mathcal{E}_r(0) = 1$, set $F(x) = \ln \mathcal{E}_r(x) = x \mathcal{E}_r(x)^r$. Then $F(0) = 0$, $\mathcal{E}_r(x) = e^{F(x)}$, and $F(x) = x e^{r F(x)}$ ($\Phi(u) = e^{ru}$, $H(u) = e^{ku}$, and $1 - \frac{u\Phi'(u)}{\Phi(u)} = 1 - r u = 1 - r x \mathcal{E}_r(x)^r$).
3. **Generalized Binomial (Fuss–Catalan) Series $\mathcal{B}_r(x) = 1 + x \mathcal{B}_r(x)^r$**:
   - Since $\mathcal{B}_r(0) = 1$, shift $F(x) = \mathcal{B}_r(x) - 1 = x \mathcal{B}_r(x)^r$. Then $F(0) = 0$, $\mathcal{B}_r(x) = 1 + F(x)$, and $F(x) = x (1 + F(x))^r$ ($\Phi(u) = (1+u)^r$, $H(u) = (1+u)^k$, and $1 - \frac{u\Phi'(u)}{\Phi(u)} = 1 - \frac{ru}{1+u} = 1 - r + r \mathcal{B}_r(x)^{-1} = 1 - r x \mathcal{B}_r(x)^{r-1}$).

| Series Family | Defining Equation & $F(0)=0$ Reduction | Power Extraction $[x^n] \text{Series}^k$ (Form 2) | Derivative-Free Denominator Identity (Form 1) |
| :--- | :--- | :--- | :--- |
| **1. Cayley Tree** $T(x)$ | $T(x) = x e^{T(x)}$<br>($F = T, \Phi(u) = e^u$) | $[x^n] T(x)^k = \frac{k}{n} \frac{n^{n-k}}{(n-k)!}$ | $\displaystyle \frac{e^{\alpha T(x)}}{1 - T(x)} = \sum_{n=0}^\infty (n + \alpha)^n \frac{x^n}{n!}$ |
| **2. Generalized Exp** $\mathcal{E}_r(x)$ | $\mathcal{E}_r(x) = e^{x \mathcal{E}_r(x)^r}$<br>($F = \ln \mathcal{E}_r, \Phi(u) = e^{ru}$) | $[x^n] \mathcal{E}_r(x)^k = \frac{k (r n + k)^{n-1}}{n!}$ | $\displaystyle \frac{\mathcal{E}_r(x)^k}{1 - r x \mathcal{E}_r(x)^r} = \sum_{n=0}^\infty (r n + k)^n \frac{x^n}{n!}$ |
| **3. Generalized Binomial** $\mathcal{B}_r(x)$ | $\mathcal{B}_r(x) = 1 + x \mathcal{B}_r(x)^r$<br>($F = \mathcal{B}_r - 1, \Phi(u) = (1+u)^r$) | $[x^n] \mathcal{B}_r(x)^k = \frac{k}{rn+k} \binom{rn+k}{n}$ | $\displaystyle \frac{\mathcal{B}_r(x)^k}{1 - r + r \mathcal{B}_r(x)^{-1}} = \sum_{n=0}^\infty \binom{rn+k}{n} x^n$ |

---

## Iteration 24: Tree, Forest, Prüfer, Degree-Constrained & Cactus Enumerations via Implicit EGF/OGF Equations

### 24.1 Labelled Trees, Forests & The Dissymmetry Theorem for Trees
1. **Rooted Labelled Trees $T(x)$**:
   A rooted labelled tree consists of a root vertex ($x$) and an unordered **set** ($\exp$) of rooted child subtrees:
   $$T(x) = x \exp\bigl(T(x)\bigr) = \sum_{n=1}^\infty n^{n-1} \frac{x^n}{n!}.$$
2. **Forests of $k$ Rooted Labelled Trees**:
   An unordered forest of $k$ rooted labelled trees has EGF $\frac{T(x)^k}{k!}$. By Lagrange Inversion:
   $$n! [x^n] \frac{T(x)^k}{k!} = \frac{n!}{k!} \cdot \frac{k}{n} [t^{n-k}] e^{n t} = \binom{n-1}{k-1} n^{n-k}.$$
3. **Unrooted Labelled Trees $U(x)$ and the Dissymmetry Theorem**:
   Every unrooted tree $\tau$ on $n \ge 1$ vertices has $n$ ways to choose a root vertex ($|V(\tau)| = n$) and $n - 1$ edges ($|E(\tau)| = n - 1$), satisfying the topological Euler invariant
   $$|V(\tau)| - |E(\tau)| = 1.$$
   Summing over all unrooted labelled trees $\tau$:
   - $\sum_\tau |V(\tau)| \frac{x^{|\tau|}}{|\tau|!} = T^\bullet(x) = T(x)$ (vertex-rooted trees).
   - $\sum_\tau |E(\tau)| \frac{x^{|\tau|}}{|\tau|!} = T^{\bullet - \bullet}(x) = \frac{1}{2} T(x)^2$ (edge-rooted trees: an unordered pair of disjoint rooted trees joined by the distinguished edge).
   Therefore, the EGF of **unrooted labelled trees** $U(x) = \sum_{n=1}^\infty n^{n-2} \frac{x^n}{n!}$ satisfies the **Dissymmetry Identity**:
   $$\boxed{U(x) = T(x) - \frac{1}{2} T(x)^2,}$$
   and the EGF of **all unrooted labelled forests** is $\exp\bigl(U(x)\bigr) = \exp\!\left(T(x) - \frac{1}{2} T(x)^2\right)$.

---

### 24.2 Prüfer Sequences, Block-Weighted Cayley Trees & Implicit Rooted Tree EGFs
Suppose we want to count labelled trees on $n$ vertices where vertex degrees are constrained or weighted. We have two complementary tools:

#### Tool 1: Prüfer Sequence Multinomial EGF
In the canonical Prüfer bijection between unrooted labelled trees on $\{1, 2, \dots, n\}$ and sequences in $\{1, 2, \dots, n\}^{n-2}$, vertex $i$ of degree $d_i \ge 1$ appears **exactly $d_i - 1$ times** in the Prüfer code. Thus:
$$\text{Number of trees with degree sequence } (d_1, \dots, d_n) = \binom{n-2}{d_1 - 1, d_2 - 1, \dots, d_n - 1} = (n - 2)! [x^{n-2}] \prod_{i=1}^n \frac{x^{d_i - 1}}{(d_i - 1)!}.$$
More generally, if vertex $i$ has weight $w_{i, d}$ when its degree is $d$, the total weight of all spanning trees is:
$$\boxed{\text{Ans} = (n - 2)! [x^{n-2}] \prod_{i=1}^n \left( \sum_{d \ge 1} w_{i, d} \frac{x^{d-1}}{(d-1)!} \right).}$$
- **Corollary (Generalized Block-Weighted Cayley Formula)**: Suppose we are given $k$ connected components of sizes $s_1, s_2, \dots, s_k$ ($\sum_{i=1}^k s_i = n$) and want to add $k-1$ edges to connect them into a tree. Contracting each component $i$ into a super-vertex, an edge incident to component $i$ has $s_i$ choices of endpoint inside component $i$, so super-vertex $i$ with degree $d_i$ gets weight $w_{i, d_i} = s_i^{d_i}$. Plugging $w_{i, d} = s_i^d$ into the Prüfer EGF gives:
  $$(k - 2)! [x^{k-2}] \prod_{i=1}^k \left( s_i \sum_{d \ge 1} \frac{(s_i x)^{d-1}}{(d-1)!} \right) = \left(\prod_{i=1}^k s_i\right) (k - 2)! [x^{k-2}] \exp\Bigl((s_1 + \dots + s_k) x\Bigr) = n^{k-2} \prod_{i=1}^k s_i!$$

#### Tool 2: Implicit Rooted Tree EGF + Lagrange Inversion
If all vertices have homogeneous degree weights $w_d$ (so a non-root vertex with $c = d - 1$ children contributes $\frac{w_{c+1}}{c!}$), then the rooted tree EGF where the root also has an "incoming parent stub" satisfies:
$$Y(x) = x \sum_{c=0}^\infty w_{c+1} \frac{Y(x)^c}{c!} = x \Phi\bigl(Y(x)\bigr), \qquad \Phi(t) = \sum_{c=0}^\infty w_{c+1} \frac{t^c}{c!}.$$
When the root has no parent stub, its degree $d$ equals its number of children $c$, so a rooted tree has EGF $T_{\text{deg}}(x) = x \sum_{d \ge 1} w_d \frac{Y(x)^d}{d!} = x \int_0^{Y(x)} \Phi(t)\,dt$. Applying Lagrange Inversion with $H(t) = \int_0^t \Phi(u)\,du$ (so $H'(t) = \Phi(t)$) gives:
$$n! [x^n] T_{\text{deg}}(x) = n! [x^{n-1}] H\bigl(Y(x)\bigr) = \frac{n!}{n-1} [t^{n-2}] \Phi(t) \Phi(t)^{n-1} = n \cdot (n-2)! [t^{n-2}] \Phi(t)^n,$$
and dividing by $n$ (to unroot) recovers $(n-2)! [t^{n-2}] \Phi(t)^n$ — **the exact same formula as Prüfer sequences**!

- **Decision Rule**:
  - Use **Prüfer EGF** when different vertices $i \in \{1, \dots, n\}$ have **heterogeneous** degree constraints or weights $w_{i, d}$ (multiplying $n$ distinct polynomials via D&C FFT), or when contracting components of sizes $s_1, \dots, s_k$.
  - Use **Implicit Rooted EGF** when degree-constrained trees are nested inside forests, cycles, or functional graphs, or when constraints depend on **subtree sizes** rather than just vertex degrees!

---

### 24.3 Labelled Cactus & Desert Enumeration (`有标号仙人掌与荒漠计数`)
A **cactus** is a connected simple undirected graph in which every edge belongs to at most one simple cycle. A **desert** is a graph whose connected components are cacti.

1. **Rooted Labelled Cactus EGF $F(x)$**:
   Root a cactus at a distinguished vertex $r$. Around $r$, the cactus decomposes into an unordered **set** ($\exp$) of biconnected lobes ("petals") meeting at $r$:
   - **Bridge lobe ($K_2$)**: An edge from $r$ to another vertex, which acts as the root of a sub-cactus: EGF is $F(x)$.
   - **Cycle lobe of length $k \ge 3$ ($C_k$)**: A simple cycle $(r, v_1, v_2, \dots, v_{k-1})$ of $k-1 \ge 2$ other vertices, each carrying its own rooted sub-cactus ($F(x)^{k-1}$), divided by $2$ because reversing the cycle $(v_{k-1}, \dots, v_1)$ produces the same undirected cycle:
     $$\sum_{k=3}^\infty \frac{F(x)^{k-1}}{2} = \frac{F(x)^2}{2\bigl(1 - F(x)\bigr)}.$$
   Assembling an arbitrary set of bridge lobes and cycle lobes at the root $r$ yields the implicit functional equation:
   $$\boxed{F(x) = x \exp\!\left( F(x) + \frac{F(x)^2}{2\bigl(1 - F(x)\bigr)} \right) = x \exp\!\left( \frac{2 F(x) - F(x)^2}{2\bigl(1 - F(x)\bigr)} \right).}$$
2. **Unrooted Labelled Cactus EGF $C(x)$ (Coefficient Integration vs. Algebraic Dissymmetry Form)**:
   - Because $F(x) = x C'(x)$ for labelled graphs, $[x^n] C(x) = \frac{1}{n} [x^n] F(x)$.
   - Moreover, let $L(y) = \frac{y^2}{2} + \sum_{k=3}^\infty \frac{y^k}{2k} = \frac{1}{2}\ln\frac{1}{1-y} - \frac{y}{2} + \frac{y^2}{4}$ be the EGF of single biconnected lobes (so $L'(y) = \frac{2y - y^2}{2(1-y)}$ and $F(x) = x \exp(L'(F(x)))$). By the **Block-Cut Dissymmetry Theorem** ($|V| + |\text{Blocks}| - |\text{Vertex-Block Incidences}| = 1$, or by integrating $\int \frac{F(x)}{x}\,dx$ by parts using $\frac{dx}{x} = \frac{dF}{F} - L''(F)\,dF$), $C(x)$ has the exact closed-form algebraic expression in terms of $F = F(x)$:
     $$\boxed{C(x) = F(x) + L\bigl(F(x)\bigr) - F(x) L'\bigl(F(x)\bigr) = \frac{1}{2}\ln\frac{1}{1 - F(x)} + \frac{2 F(x) - 3 F(x)^2 + 2 F(x)^3}{4\bigl(1 - F(x)\bigr)}.}$$
3. **Extracting Cactus & Desert Counts**:
   - **Single $n$ in $O(n \log n)$ via Lagrange Inversion**:
     With $\Phi(t) = \exp\!\left(\frac{2t - t^2}{2(1-t)}\right)$, the number of unrooted labelled cacti on $n$ vertices is
     $$\boxed{c_n = \frac{1}{n} \cdot n! [x^n] F(x) = \frac{(n - 1)!}{n} [t^{n-1}] \exp\!\left( n \frac{2t - t^2}{2(1 - t)} \right).}$$
   - **All $k = 1, \dots, N$ in $O(N \log N)$ (Newton Iteration) or $O(N \log^2 N)$ (`revert`)**:
     Solve $F(x) \bmod x^{N+1}$ via Newton iteration on $G(F) = F - x \exp\!\left(\frac{2F - F^2}{2(1-F)}\right) = 0$ (or `revert` of $y \exp\!\left(\frac{y^2 - 2y}{2(1-y)}\right)$), obtain $C(x) = \int_0^x \frac{F(t)}{t}\,dt$, and compute $\exp(C(x))$ for **labelled deserts**!
   - **Hand-Checked Small Values ($n = 1, 2, 3, 4$)**:
     - $n = 1$: $\frac{0!}{1} [t^0] 1 = 1$.
     - $n = 2$: $\frac{1!}{2} [t^1] \exp(2t + \dots) = 1$.
     - $n = 3$: $\frac{2!}{3} [t^2] \exp(3t + \frac{3}{2}t^2 + \dots) = \frac{2}{3} \left(\frac{9}{2} + \frac{3}{2}\right) = 4$ ($3$ paths + $1$ triangle $K_3 = 4$).
     - $n = 4$: $\frac{3!}{4} [t^3] \exp(4t + 2t^2 + 2t^3 + \dots) = \frac{3}{2} \left(\frac{32}{3} + 8 + 2\right) = 31$ ($16$ trees + $12$ paw graphs + $3$ cycles $C_4 = 31$ cacti out of $38$ connected graphs on $4$ vertices).

---

### 24.4 Unlabelled Trees, Otter's Dissymmetry Theorem & Alkane/Olefin Enumeration (`无标号树与烷烃/烯烃计数`)
When vertices are **unlabelled**, we replace EGF `SET` ($\exp(T)$) by OGF `MSET` (the **Euler Transform** or **Pólya Cycle Index**):
1. **Unconstrained Unlabelled Rooted Trees**:
   $$T(x) = x \operatorname{MSET}\bigl(T(x)\bigr) = x \exp\!\left( \sum_{k=1}^\infty \frac{T(x^k)}{k} \right) = x \prod_{k=1}^\infty \bigl(1 - x^k\bigr)^{-[x^k]T(x)}.$$
2. **Degree-Bounded Unlabelled Rooted Trees (Alkyl Radicals $A(x)$, Max Out-Degree $3$, Luogu P6598)**:
   A carbon atom in an alkyl radical $-C_n H_{2n+1}$ has $1$ bond to its parent and $3$ unordered branches, each of which is either a hydrogen atom ($1$) or a smaller alkyl radical ($A(x) - 1$). Using the cycle index of the symmetric group $S_3$, $Z(S_3; s_1, s_2, s_3) = \frac{1}{6}(s_1^3 + 3 s_1 s_2 + 2 s_3)$, applied to $A(x)$ (where $[x^0]A(x) = 1$ represents a hydrogen branch):
   $$\boxed{A(x) = 1 + x \cdot \frac{A(x)^3 + 3 A(x) A(x^2) + 2 A(x^3)}{6}.}$$
   - **Monosubstituted Olefins / Alkenes (`烯烃计数`, Luogu P6597)**: A carbon-carbon double bond $C = C$ has two ends, each carrying an unordered pair of alkyl/hydrogen branches counted by $B(x) = Z(S_2; A(x)) = \frac{A(x)^2 + A(x^2)}{2}$. Because the two ends of the $C = C$ bond can be swapped, the OGF of alkenes is $Z(S_2; B(x)) = \frac{B(x)^2 + B(x^2)}{2}$!
3. **Otter's Unlabelled Dissymmetry Theorem (for Unrooted Unlabelled Trees & Alkanes)**:
   For unlabelled unrooted trees $U(x)$, an edge-rooted tree is an **unordered pair** of rooted trees ($\operatorname{MSET}_2(T) = \frac{T(x)^2 + T(x^2)}{2}$), while an edge-rooted tree with a directed edge is $T(x)^2$ (unless the two subtrees are isomorphic, counted by $T(x^2)$, where the symmetry axis already passes through the edge!). Thus:
   $$\boxed{U(x) = T^\bullet(x) + T^{\bullet - \bullet}_{\text{unordered}}(x) - T^{\bullet \to \bullet}_{\text{asymmetric}}(x) = T(x) + \frac{T(x)^2 + T(x^2)}{2} - T(x)^2 = T(x) - \frac{T(x)^2 - T(x^2)}{2}.}$$
   For **alkanes** $C_n H_{2n+2}$ (unrooted unlabelled trees with maximum degree $\le 4$), let $P(x) = x \cdot Z\bigl(S_4; A(x)\bigr)$ be vertex-rooted alkanes (using $Z(S_4) = \frac{1}{24}(s_1^4 + 6s_1^2 s_2 + 3s_2^2 + 8s_1 s_3 + 6s_4)$) and let $\widetilde{A}(x) = A(x) - 1$ be non-empty alkyl radicals; then Otter's Dissymmetry Theorem gives the exact alkane OGF:
   $$\boxed{\text{Alkanes}(x) = P(x) - \frac{\widetilde{A}(x)^2 - \widetilde{A}(x^2)}{2}.}$$

---

## Iteration 25: Graph Enumeration (Functional Graphs, Eulerian Graphs, Bipartite Graphs, Tournaments, DAGs, 2-Connected Graphs)

### 25.1 Functional Graphs (Mappings $f : [n] \to [n]$)
A directed graph where every vertex has out-degree $1$ is a **functional graph**.
- Each connected component is a **directed cycle of rooted labelled trees** $T(x) = x e^{T(x)}$:
  $$C_{\text{func}}(x) = \operatorname{CYC}\bigl(T(x)\bigr) = \sum_{k=1}^\infty \frac{T(x)^k}{k} = \ln \frac{1}{1 - T(x)}.$$
- An arbitrary functional graph is a **set** of connected functional components:
  $$F_{\text{func}}(x) = \exp\bigl(C_{\text{func}}(x)\bigr) = \frac{1}{1 - T(x)} = \sum_{n=0}^\infty n^n \frac{x^n}{n!}.$$
- **Constrained Variants**:
  - **Cycle Lengths Restricted to $S \subseteq \mathbb{Z}_{\ge 1}$**: $F_S(x) = \exp\!\left(\sum_{k \in S} \frac{T(x)^k}{k}\right)$.
  - **Trees of Bounded Height $\le h$** ($f^{(h)}(v)$ lies on a cycle for all $v$): Replace $T(x)$ by $T_h(x)$, where $T_0(x) = x$ and $T_j(x) = x \exp(T_{j-1}(x))$.
  - **Trees with In-Degree Restricted to $D$**: Replace $T(x) = x e^{T(x)}$ by $T_D(x) = x \sum_{d \in D} \frac{T_D(x)^d}{d!}$.

---

### 25.2 Labelled Connected Graphs & The Quadratic-Exponent Identity
Let $g_n = 2^{\binom{n}{2}}$ be the number of simple undirected graphs on $n$ labelled vertices, and define the formal EGF
$$G(x) = \sum_{n=0}^\infty 2^{\binom{n}{2}} \frac{x^n}{n!} \in \mathbb{Q}[[x]].$$
Even though $2^{\binom{n}{2}}/n!$ diverges analytically for every $x \neq 0$ over $\mathbb{C}$, in the formal power series ring $K[[x]]$ it is a completely valid unit series ($G(0) = 1$), and its formal logarithm is the EGF of **connected labelled undirected graphs**:
$$\boxed{C(x) = \ln G(x) = \ln\!\left( \sum_{n=0}^\infty 2^{\binom{n}{2}} \frac{x^n}{n!} \right) = x + \frac{x^2}{2!} + 4 \frac{x^3}{3!} + 38 \frac{x^4}{4!} + 728 \frac{x^5}{5!} + \dots}$$

#### The Universal Quadratic-Exponent Decoupling Identity
Whenever a graph enumeration formula sums over partitions $(i, j)$ with $i + j = n$ and includes $2^{i j}$ (counting arbitrary bipartite edges between a set of size $i$ and a set of size $j$), rewrite the cross-product $i j$ using:
$$\boxed{i j = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2} \implies 2^{\pm i j} = 2^{\pm \binom{i+j}{2}} \cdot 2^{\mp \binom{i}{2}} \cdot 2^{\mp \binom{j}{2}}.}$$
This converts $\sum_{i+j=n} \binom{n}{i} 2^{\pm i j} a_i b_j$ into a single $O(N \log N)$ polynomial convolution!

---

### 25.3 Labelled Eulerian Graphs (`有标号欧拉图计数`)
An **Eulerian graph** is a connected simple undirected graph in which every vertex has **even degree**.
1. **Step 1 (All Graphs with Every Vertex of Even Degree)**:
   How many not-necessarily-connected graphs on $n \ge 1$ labelled vertices $\{1, \dots, n\}$ have every vertex of even degree?
   - **Clean Bijection**: Isolate vertex $n$. Choose any subset of the $\binom{n-1}{2}$ edges on $\{1, \dots, n-1\}$ ($2^{\binom{n-1}{2}}$ choices). Then for each $v \in \{1, \dots, n-1\}$, the edge $\{v, n\}$ is **uniquely determined** so that $\deg(v)$ becomes even. Because $\sum_{v=1}^n \deg(v) = 2|E|$ is always even, $\deg(n)$ is then **automatically even**!
   - Thus there are exactly $2^{\binom{n-1}{2}}$ even-degree graphs on $n \ge 1$ labelled vertices!
2. **Step 2 (Connected Eulerian Graphs via $\ln$)**:
   $$\boxed{E_{\text{Euler}}(x) = \ln\!\left( 1 + \sum_{n=1}^\infty 2^{\binom{n-1}{2}} \frac{x^n}{n!} \right) = x + 0\frac{x^2}{2!} + 1\frac{x^3}{3!} + 3\frac{x^4}{4!} + 38\frac{x^5}{5!} + \dots}$$

---

### 25.4 Labelled Bipartite Graphs (`有标号二分图计数`, Luogu P7364) & Strongly Connected Tournaments
1. **Labelled Bipartite Graphs**:
   Why is bipartite graph enumeration subtler than Eulerian graph enumeration? Because a connected bipartite graph on $n \ge 1$ vertices has **2 proper 2-colorings** (swapping Black and White), so a bipartite graph with $c$ connected components has $2^c$ proper 2-colorings!
   - **Step 1 (2-Colored Graphs via Quadratic-Exponent Convolution)**:
     The EGF of 2-colored labelled graphs $G_{\text{2col}}(x) = \sum_{n=0}^\infty g_{\text{2col}, n} \frac{x^n}{n!}$ has
     $$g_{\text{2col}, n} = \sum_{i=0}^n \binom{n}{i} 2^{i(n-i)} = n! \, 2^{\binom{n}{2}} [x^n] \left( \sum_{i=0}^\infty 2^{-\binom{i}{2}} \frac{x^i}{i!} \right)^2.$$
   - **Step 2 (Halving Connected Components via $\frac{1}{2} \ln$)**:
     Since $\ln G_{\text{2col}}(x)$ counts connected 2-colored graphs, and every connected bipartite graph on $n \ge 1$ vertices has **exactly $2$** 2-colorings, dividing by $2$ gives the EGF of **connected labelled bipartite graphs**:
     $$C_{\text{bip}}(x) = \frac{1}{2} \ln G_{\text{2col}}(x).$$
   - **Step 3 (Exponentiating Back to All Bipartite Graphs)**:
     $$\boxed{B_{\text{bip}}(x) = \exp\!\left( \frac{1}{2} \ln G_{\text{2col}}(x) \right) = \sqrt{G_{\text{2col}}(x)} = 1 + x + 2\frac{x^2}{2!} + 7\frac{x^3}{3!} + 41\frac{x^4}{4!} + \dots}$$
2. **Strongly Connected Labelled Tournaments (`强连通竞赛图计数`)**:
   In any tournament (a complete graph with directed edges, $2^{\binom{n}{2}}$ total on $n$ vertices), condensing its strongly connected components (SCCs) yields a **transitive tournament (a unique linear order `SEQ`)** of non-empty strongly connected tournaments! Because all edges between earlier SCCs and later SCCs are forced to point forward ($1$ way!), no $2^{ij}$ factor is needed:
   $$\boxed{1 + \sum_{n=1}^\infty 2^{\binom{n}{2}} \frac{x^n}{n!} = \frac{1}{1 - S_{\text{tour}}(x)} \implies S_{\text{tour}}(x) = 1 - \left(\sum_{n=0}^\infty 2^{\binom{n}{2}} \frac{x^n}{n!}\right)^{-1} = x + 0\frac{x^2}{2!} + 2\frac{x^3}{3!} + 24\frac{x^4}{4!} + 544\frac{x^5}{5!} + \dots}$$

---

### 25.5 Labelled Directed Acyclic Graphs (`有标号 DAG 计数`, Luogu P6295)
Let $d_n$ be the number of labelled DAGs on $n$ vertices ($d_0 = 1$).
1. **Source-Layer Inclusion–Exclusion**:
   In any non-empty DAG, the set of vertices of in-degree $0$ (sources) is non-empty. If we choose a subset $S \subseteq [n]$ of size $k \ge 1$ to be forced to have in-degree $0$, there are $\binom{n}{k}$ choices for $S$, $d_{n-k}$ ways to form a DAG on $[n] \setminus S$, and $2^{k(n-k)}$ ways to direct edges from $S$ to $[n] \setminus S$. By Inclusion–Exclusion over the exact set of sources:
   $$d_n = \sum_{k=1}^n (-1)^{k-1} \binom{n}{k} 2^{k(n-k)} d_{n-k} \iff \sum_{k=0}^n (-1)^k \binom{n}{k} 2^{k(n-k)} d_{n-k} = [n = 0].$$
2. **Quadratic-Exponent Scaling to FPS Inverse**:
   Use $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ to divide the recurrence by $n! \, 2^{\binom{n}{2}}$:
   $$\sum_{k=0}^n \left( (-1)^k 2^{-\binom{k}{2}} \frac{1}{k!} \right) \left( d_{n-k} 2^{-\binom{n-k}{2}} \frac{1}{(n-k)!} \right) = [n = 0].$$
   Therefore, in $O(N \log N)$ time via a **single polynomial inversion**:
   $$\boxed{\widehat{D}(x) = \sum_{n=0}^\infty d_n 2^{-\binom{n}{2}} \frac{x^n}{n!} = \left( \sum_{k=0}^\infty (-1)^k 2^{-\binom{k}{2}} \frac{x^k}{k!} \right)^{-1} = 1 + x + 3 \cdot 2^{-1} \frac{x^2}{2!} + 25 \cdot 2^{-3} \frac{x^3}{3!} + 543 \cdot 2^{-6} \frac{x^4}{4!} + \dots}$$
   *(Crucial Pipeline Warning: Because the weights $2^{-\binom{n}{2}}$ were inserted to decouple $2^{k(n-k)}$, $\widehat{D}(x)$ is a **Graphical EGF**; to count **weakly connected DAGs** in Luogu P6295, you must **first** multiply $[x^n]\widehat{D}(x)$ by $2^{\binom{n}{2}}$ to recover the ordinary EGF $D(x) = \sum_{n=0}^\infty d_n \frac{x^n}{n!}$, and **then** compute $\ln D(x)$!)*

---

### 25.6 Biconnected (`点双连通`) & 2-Edge-Connected (`边双连通`) Graphs via Block-Cut / Bridge-Block Trees
Let $C(x) = \ln\!\left(\sum_{n \ge 0} 2^{\binom{n}{2}} \frac{x^n}{n!}\right)$ be the EGF of connected labelled graphs, and let $D(x) = x C'(x)$ be the EGF of **vertex-rooted connected labelled graphs**.

| Graph Class | Tree Decomposition | Implicit Functional Equation | Single-$n$ Extraction via LIF ($O(n \log n)$) |
| :--- | :--- | :--- | :--- |
| **1. 2-Edge-Connected (Bridgeless) Graphs** $E(y)$ (Rooted: $E^\bullet(y) = y E'(y)$) | **Bridge-Block Tree**: The root's 2-edge-connected component has size $k$, and each of its $k$ vertices attaches a $\text{SET}$ ($\exp$) of bridges leading to rooted connected graphs $D(x)$. | $$D(x) = E^\bullet\bigl(x \exp(D(x))\bigr)$$ | Let $W(x) = x e^{D(x)}$. For $n \ge 1$:<br>$$\boxed{e_n = (n-1)! \cdot \frac{1}{n} [x^{n-1}] D'(x) e^{-n D(x)}}$$ |
| **2. Biconnected (2-Vertex-Connected) Graphs** $B(y)$ (Root-removed block: $B'(y)$) | **Block-Cut Tree**: The root vertex $r$ belongs to a $\text{SET}$ ($\exp$) of biconnected blocks, and every non-root vertex in each block is replaced by a rooted connected graph $D(x)$. | $$D(x) = x \exp\bigl(B'(D(x))\bigr)$$<br>$$\iff B'\bigl(D(x)\bigr) = \ln \frac{D(x)}{x}$$ | For $n \ge 2$ (Standard & Derivative-Free Simplified Forms):<br>$$\boxed{\begin{aligned}b_n &= (n-2)! [x^{n-2}] \left(\ln \frac{D(x)}{x}\right)' \left(\frac{x}{D(x)}\right)^{n-1} \\ &= -(n-2)! [x^{n-1}] \left(\frac{D(x)}{x}\right)^{-(n-1)}\end{aligned}}$$ |

#### Proof of the Log-Free Simplification for Biconnected Graphs $b_n$
Let $Q(x) = \frac{x}{D(x)} = \left(\frac{D(x)}{x}\right)^{-1}$. Since $\ln \frac{D(x)}{x} = -\ln Q(x)$, its derivative is $-\frac{Q'(x)}{Q(x)}$. Multiplying by $Q(x)^{n-1}$ gives:
$$\left(\ln \frac{D(x)}{x}\right)' \left(\frac{x}{D(x)}\right)^{n-1} = -Q'(x) Q(x)^{n-2} = -\frac{1}{n-1} \frac{d}{dx}\bigl(Q(x)^{n-1}\bigr).$$
Since $[x^{n-2}] \frac{d}{dx} A(x) = (n-1) [x^{n-1}] A(x)$, the factor $\frac{1}{n-1}$ cancels and we obtain $b_n = -(n-2)! [x^{n-1}] \left(\frac{x}{D(x)}\right)^{n-1}$, eliminating the logarithm and derivative completely!

#### Exact Hand-Verification for $n = 1, 2, 3, 4, 5$
From $C(x) = x + \frac{x^2}{2!} + 4\frac{x^3}{3!} + 38\frac{x^4}{4!} + 728\frac{x^5}{5!}$, we have $D(x) = x C'(x) = x + x^2 + 2x^3 + \frac{19}{3}x^4 + \frac{91}{3}x^5 + \dots$:
1. **2-Edge-Connected Counts $e_n$**:
   - $n = 1$: $0! [x^0] D'(x) e^{-D(x)} = 1$.
   - $n = 2$: $\frac{1!}{2} [x^1] (1+2x)(1-2x) = 0$ ($K_2$ is a bridge).
   - $n = 3$: $\frac{2!}{3} [x^2] (1+2x+6x^2)(1-3x+\frac{3}{2}x^2) = \frac{2}{3}(\frac{3}{2} - 6 + 6) = 1$ ($K_3$).
   - $n = 4$: $\frac{3!}{4} [x^3] (1+2x+6x^2+\frac{76}{3}x^3)(1-4x+4x^2-\frac{8}{3}x^3) = \frac{3}{2}(\frac{76}{3} - 24 + 8 - \frac{8}{3}) = 10$ ($3$ $C_4$ + $6$ $(K_4-e)$ + $1$ $K_4 = 10$).
2. **Biconnected Counts $b_n$**:
   With $Q(x) = \frac{x}{D(x)} = 1 - x - x^2 - \frac{10}{3}x^3 - \frac{56}{3}x^4 - \dots$ and $\left(\ln \frac{D(x)}{x}\right)' = 1 + 3x + 14x^2 + \dots$:
   - $n = 2$: $-0! [x^1] Q(x)^1 = -(-1) = 1$ ($K_2$).
   - $n = 3$: $-1! [x^2] Q(x)^2 = -[x^2](1 - 2x - x^2 + \dots) = 1$ ($K_3$).
   - $n = 4$: $-2! [x^3] Q(x)^3 = -2(-5) = 10$ (and via Standard Form: $2! [x^2] (1+3x+14x^2)(1-3x+0x^2-5x^3) = 2(14 - 9) = 10$).
   - $n = 5$: $-3! [x^4] Q(x)^4 = -6 \left(-\frac{119}{3}\right) = 238$ (matching OEIS A003024: $1, 1, 10, 238, 11368$).

---

## Full Bibliographic Citations Table (Wave 3A: Iterations 21–25)

| Ref ID | Language | Author(s) / Source | Year | Title / Venue / URL | Core Topics Covered |
| :--- | :---: | :--- | :---: | :--- | :--- |
| **[Ele19]** | `[ZH]` | Baitian Li (`Elegia` / `李白天`) | 2019 | *《炫酷反演魔术》 (Cool Inversion Magic)*, Luogu / UOJ Blog | Formal Laurent series $K((x))$, formal residue $\operatorname{res}_x$, change-of-variables rule, and one-line derivations of binomial/Lagrange identities |
| **[FS09]** | `[EN]` | Philippe Flajolet, Robert Sedgewick | 2009 | *Analytic Combinatorics*, Cambridge University Press (Ch. I–III, Appendix A.6) | Symbolic Method (`SEQ`, `SET`, `CYC`), tree/functional-graph EGFs, and Lagrange–Bürmann Inversion |
| **[GKP94]** | `[EN]` | Ronald L. Graham, Donald E. Knuth, Oren Patashnik | 1994 | *Concrete Mathematics* (2nd ed.), Addison-Wesley (§5.4, §7.5) | Raney's Lemma, Cycle Lemma, Generalized Binomial Series $\mathcal{B}_r(x)$, and Generalized Exponential Series $\mathcal{E}_r(x)$ |
| **[Ges16]** | `[EN]` | Ira M. Gessel | 2016 | *Lagrange Inversion*, Journal of Combinatorial Theory, Series A, 144:212–249 / [arXiv:1609.05988](https://arxiv.org/abs/1609.05988) | Comprehensive survey of algebraic, formal-residue, derivative-free, universal-denominator, and combinatorial proofs of Lagrange Inversion |
| **[BLL98]** | `[EN]` | François Bergeron, Gilbert Labelle, Pierre Leroux | 1998 | *Combinatorial Species and Tree-like Structures*, Cambridge University Press (Ch. 3–4) | Dissymmetry Theorem for trees and block-cut graphs, Pointing $\vartheta$, and unlabelled Pólya/Otter tree enumeration |
| **[HP73]** | `[EN]` | Frank Harary, Edgar M. Palmer | 1973 | *Graphical Enumeration*, Academic Press (Ch. 1, 3, 7) | Labelled connected, Eulerian, bipartite, biconnected, 2-edge-connected, tournament, and DAG enumerations |
| **[Rob70]** | `[EN]` | Robert W. Robinson | 1970 / 1973 | *Enumeration of Non-Separable Graphs* (JCT 9:327–356) & *Counting Labeled Acyclic Digraphs* (New Directions in the Theory of Graphs) | Block-cut functional equation $D(x) = x\exp(B'(D(x)))$ and source-layer IE graphical EGF for DAGs |
| **[Ego84]** | `[EN]` | Georgy P. Egorychev | 1984 | *Integral Representation and the Computation of Combinatorial Sums*, AMS Translations of Mathematical Monographs, Vol. 59 | Method of Coefficients via formal residues and change-of-variables elimination in double sums |
| **[Joy81]** | `[EN]` | André Joyal | 1981 | *Une théorie combinatoire des séries formelles*, Advances in Mathematics 42(1):1–82 | Combinatorial vertebrate/double-rooted tree proof of Cayley's formula and labelled Lagrange Inversion |
| **[Cmd20]** | `[ZH]` | `command_block` | 2020 | *《拉格朗日反演略解》 & 《生成函数杂谈》*, [command-block.blog.luogu.org](https://www.luogu.com.cn/blog/command-block/) | Raney's Lemma intuition, Standard vs. Alternative Lagrange Inversion (`另类拉格朗日反演`), and contest problem reductions |
| **[Rqy19]** | `[ZH]` | `rqy` | 2018–2019 | *《有标号荒漠/仙人掌/点双/边双连通图计数》*, Luogu P5434 / P5827 / P5828 Editorials | Block-cut and bridge-block tree EGF derivations, cactus dissymmetry, and Newton/LIF extraction |
| **[Wzz20]** | `[ZH]` | Wang Zhezaki (`wzz` / `GuidingStar`) | 2020 | *《无标号树与烷烃/烯烃计数详解》*, Luogu P6597 / P6598 Editorials | Pólya cycle index $Z(S_3), Z(S_4)$ and Otter's Dissymmetry Theorem for chemical isomers |
| **[Mas21]** | `[JA]` | `maspy` (`maspypy`) | 2021–2023 | *ラグランジュの反転公式 (Lagrange Inversion Formula) と形式留数*, [maspypy.com](https://maspypy.com/) | Formal Laurent series $K((x))$, formal residue proofs of LIF, and AtCoder implicit GF applications |
| **[Nos21]** | `[JA]` | Yasunori Kinoshita (`noshi91`) | 2021 | *Formal Laurent Series & Residue Calculus Notes*, [noshi91.github.io](https://noshi91.github.io/) | Algebraic contract of $K((x))$, valuation, and division-free residue forms |
| **[Nya22]** | `[JA]` | `Nyaan` | 2021–2023 | *AtCoder ABC222 H (Beautiful Binary Tree) & ABC303 Ex (Constrained Tree Degree) Editorials*, [atcoder.jp](https://atcoder.jp/contests/abc222/editorial/2762) | Implicit binary tree OGFs and Prüfer degree-constrained tree enumeration |

---

## Audited Problem Catalog (Wave 3A: 31 Problems Audited — 6 Rejected Templates + 25 Accepted Problems)

### Explicitly Rejected Template Problems (Excluded per `AGENTS.md` Editorial Policy)

Per `AGENTS.md` (*"Do not add practice problems whose main task is copying, adapting, or validating a standard library routine. Library Checker and 'template' problems are normally excluded"*), the following 6 pure template verification problems were audited and **explicitly rejected** from the textbook practice ladders:

| Problem ID | Title | Judge & URL | Reason for Rejection (`AGENTS.md` Policy) |
| :--- | :--- | :--- | :--- |
| **Luogu P6086** | 【模板】Prufer 序列 | [Luogu P6086](https://www.luogu.com.cn/problem/P6086) | Explicit `【模板】` problem asking solely to convert a tree to its Prüfer code and vice versa in $O(N)$ with zero GF modelling. |
| **Luogu P5373** | 【模板】多项式复合逆 | [Luogu P5373](https://www.luogu.com.cn/problem/P5373) | Explicit `【模板】` problem asking directly for $[x^k] F^{\langle -1 \rangle}(x)$ of a given polynomial $F(x)$ with no combinatorial reduction. |
| **LC `compositional_inverse_of_formal_power_series`** | Compositional Inverse of FPS | [Library Checker](https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series) | Pure library benchmark asking for $F^{\langle -1 \rangle}(x) \bmod x^N$ without any problem modelling. |
| **Luogu P5900** | 无标号树的计数 | [Luogu P5900](https://www.luogu.com.cn/problem/P5900) | Direct textbook verification of OEIS A000055 (unlabelled trees on $N$ vertices) with zero additional constraints or reduction. |
| **LC `exp_of_formal_power_series` / `log_of_formal_power_series`** | Exp / Log of FPS | [Library Checker](https://judge.yosupo.jp/problem/exp_of_formal_power_series) | Bare library verification of $\exp(F)$ and $\ln(F)$ routines. |
| **CSES 1095 / Bare Cayley $N^{N-2}$** | Counting Labeled Trees (Bare) | CSES / Standard | Trivial single modular exponentiation $N^{N-2} \bmod P$ with no FPS manipulation. |

---

### Cluster A: Standard Lagrange–Bürmann Inversion ($F = x\Phi(F)$) & Raney / Cycle Lemma Intuition (Iteration 21)

#### Problem A1: AtCoder ABC222 H — Beautiful Binary Tree
- **Metadata**:
  - **Problem ID**: `abc222_h` / ABC222 H
  - **Title**: Beautiful Binary Tree
  - **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc222/tasks/abc222_h](https://atcoder.jp/contests/abc222/tasks/abc222_h)
  - **Difficulty Tier**: `Stepping Stone`
  - **Curation Role**: `TOPIC LADDER` (Canonical first contest problem translating a 2-state tree grammar into $F(x) = x\Phi(F(x))$ and extracting $[x^N]F(x)$ in $O(N)$ via LIF)
  - **Primary Topic**: Standard Lagrange–Bürmann Inversion ($[x^N]F(x) = \frac{1}{N}[u^{N-1}]\Phi(u)^N$)
  - **Secondary Topics**: Mutual tree grammar elimination, $O(N)$ trinomial power coefficient extraction
- **Concise Inline Problem Statement & Exact Constraints**:
  A rooted binary tree with vertices labeled $0$ or $1$ is called *beautiful* if its root has label $1$, every vertex with label $1$ has only children with label $0$ (or $1$ after elementary contraction), and no two adjacent vertices with label $0$ appear consecutively on a downward path. Count the number of beautiful binary trees with $N$ vertices of label $1$ (or weight $N$) modulo $998244353$. Constraints: $1 \le N \le 10^7$, time limit 3.0s.
- **Bridge 1 (English $\to$ Initial GF)**:
  Let $F_1(x)$ and $F_0(x)$ be the OGFs of valid subtrees rooted at a vertex of label $1$ (contributing $x^1$) and label $0$ (contributing $x^0$, except through its children of label $1$), respectively. From the local branching rules at a root of label $1$ and a root of label $0$, eliminating $F_0(x) = 2 F_1(x) + F_1(x)^2$ collapses the system into a single implicit equation for $F(x) = F_1(x)$:
  $$F(x) = x \bigl(1 + 3 F(x) + F(x)^2\bigr)^2 = x \Phi\bigl(F(x)\bigr), \qquad \Phi(u) = (1 + 3u + u^2)^2.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Because $N \le 10^7$, an $O(N \log N)$ Newton iteration is too slow and uses too much memory! Since we only need the **single coefficient** $[x^N] F(x)$ and $F(0) = 0$, Standard Lagrange Inversion gives:
  $$[x^N] F(x) = \frac{1}{N} [u^{N-1}] \Phi(u)^N = \frac{1}{N} [u^{N-1}] (1 + 3u + u^2)^{2N} = \frac{1}{N} \sum_{k=0}^{\lfloor(N-1)/2\rfloor} \binom{2N}{k} \binom{2N - k}{N - 1 - 2k} 3^{N - 1 - 2k},$$
  which is a single $O(N)$ loop!

#### Problem A2: Luogu P3978 — [TJOI2015] 概率论 (Probability Theory)
- **Metadata**:
  - **Problem ID**: Luogu P3978
  - **Title**: [TJOI2015] 概率论 (Probability Theory)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P3978](https://www.luogu.com.cn/problem/P3978)
  - **Difficulty Tier**: `Stepping Stone`
  - **Curation Role**: `RESERVE ARCHIVE`
  - **Primary Topic**: Implicit Binary Tree OGF + Pointing / Derivative-Free Catalan Extraction
  - **Secondary Topics**: Bivariate leaf marking $C(x, y) = 1 + xy + x(C(x, y)^2 - 1)$
- **Concise Inline Problem Statement & Exact Constraints**:
  Assume all $C_n = \frac{1}{n+1}\binom{2n}{n}$ distinct $n$-node rooted binary trees are equally likely. Compute the expected number of leaves in a random $n$-node rooted binary tree. Constraints: $1 \le n \le 10^9$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Mark total nodes by $x$ and leaves by $y$ in the bivariate OGF $C(x, y) = 1 + x y + x \bigl(C(x, y)^2 - 1\bigr)$. Differentiating with respect to $y$ at $y = 1$ gives the total leaf OGF $L(x) = \left.\frac{\partial C(x, y)}{\partial y}\right|_{y=1}$:
  $$L(x) = x + 2 x C(x) L(x) \implies L(x) = \frac{x}{1 - 2 x C(x)}.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Notice the denominator $1 - 2x C(x)$! For $F(x) = C(x) - 1 = x(1 + F(x))^2$, $\Phi(u) = (1+u)^2$ has $1 - x \Phi'(F(x)) = 1 - 2x C(x) = \sqrt{1 - 4x}$! Thus $[x^n] L(x) = [x^{n-1}] \frac{1}{1 - 2x C(x)} = [u^{n-1}] (1+u)^{2(n-1)} = \binom{2n-2}{n-1}$, and the expected number of leaves is $\frac{\binom{2n-2}{n-1}}{\frac{1}{n+1}\binom{2n}{n}} = \frac{n(n+1)}{2(2n-1)}$ in $O(1)$!

#### Problem A3: Codeforces 438E — The Child and Binary Tree
- **Metadata**:
  - **Problem ID**: Codeforces 438E
  - **Title**: The Child and Binary Tree
  - **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/438/E](https://codeforces.com/problemset/problem/438/E)
  - **Difficulty Tier**: `Intermediate`
  - **Curation Role**: `TOPIC LADDER` (Comparing all-coefficients extraction via quadratic formula / Newton iteration vs. Compound Lagrange formulation $F(x) - 1 = C(x) F(x)^2$)
  - **Primary Topic**: Implicit Binary Tree Equation $F(x) = 1 + C(x) F(x)^2$
  - **Secondary Topics**: FPS Square Root $\sqrt{1 - 4C(x)}$, Constant-Term Shift $U(x) = F(x) - 1$
- **Concise Inline Problem Statement & Exact Constraints**:
  You are given a set of allowed positive integer vertex weights $S = \{c_1, c_2, \dots, c_n\}$. A vertex-weighted rooted binary tree is *good* if every vertex's weight belongs to $S$. For every $s = 1, 2, \dots, m$, compute the number of good rooted binary trees of total weight $s$ modulo $998244353$. Constraints: $1 \le n, m \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Let $C(x) = \sum_{i=1}^n x^{c_i}$ be the weight OGF of a single vertex (note $C(0) = 0$ since $c_i \ge 1$). A good binary tree is either empty ($1$) or consists of a root ($C(x)$) plus an ordered pair of good subtrees ($F(x)^2$):
  $$F(x) = 1 + C(x) F(x)^2.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Here $F(x) = B(C(x))$ is the composition of the Catalan series $B(w) = 1 + w B(w)^2 = \sum_{k=0}^\infty \frac{1}{k+1}\binom{2k}{k} w^k$ with the general polynomial $w = C(x)$! Because we need all coefficients $[x^1 \dots x^m] F(x)$ and $B(w)$ satisfies a quadratic equation, solving the quadratic directly in $K[[x]]$ (choosing the branch with $F(0) = 1$ and avoiding division by $C(x)$ since $C(0) = 0$) gives:
  $$F(x) = \frac{1 - \sqrt{1 - 4 C(x)}}{2 C(x)} = \frac{2}{1 + \sqrt{1 - 4 C(x)}},$$
  computable in $O(m \log m)$ via a single FPS `sqrt` and `inv`!

#### Problem A4: Codeforces 1528F — AmShZ Farm
- **Metadata**:
  - **Problem ID**: Codeforces 1528F
  - **Title**: AmShZ Farm
  - **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1528/F](https://codeforces.com/problemset/problem/1528/F)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `TOPIC LADDER` (Masterclass uniting Raney's Circular Lemma for Parking Functions with Generalized Exponential Series $\mathcal{E}_1(x)$ / Stirling Power Reduction)
  - **Primary Topic**: Raney's Circular Lemma (Parking Functions) & Tree EGF $T(x) = x e^{T(x)}$
  - **Secondary Topics**: Stirling numbers of the second kind ($m^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{m}{j}$)
- **Concise Inline Problem Statement & Exact Constraints**:
  An array $a_1, a_2, \dots, a_n \in \{1, \dots, n\}$ is called *good* (a parking function) if for every $i \in \{1, \dots, n\}$, at least $i$ elements of $a$ are $\le i$. The *score* of a good array $a$ is $\sum_{v=1}^n \text{cnt}(v)^k$, where $\text{cnt}(v)$ is the number of occurrences of $v$ in $a$. Compute the sum of scores over all good arrays modulo $998244353$. Constraints: $1 \le n \le 10^9$, $1 \le k \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By Pollak's / Raney's Circular Lemma on a circle of $n + 1$ parking spaces $\{1, 2, \dots, n+1\}$, let each car choose a preferred spot in $\{1, \dots, n+1\}$. Out of the $n + 1$ cyclic shifts of any preference tuple $(a_1, \dots, a_n) \in \{1, \dots, n+1\}^n$, **exactly $1$ shift** leaves spot $n + 1$ empty (which is equivalent to $a$ being a valid parking function on $\{1, \dots, n\}$)! Equivalently, via the tree EGF $T(x) = x e^{T(x)}$, the EGF of parking functions by spot multiplicities is $\frac{1}{n+1} [x^n] n! e^{(n+1)x}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  By symmetry among the $n$ spots $\{1, \dots, n\}$ in the circular model, the total sum of $\text{cnt}(1)^k + \dots + \text{cnt}(n)^k$ over all valid parking functions equals $\frac{n}{n+1}$ times the sum of $\text{cnt}(1)^k$ over **all** unconstrained tuples in $\{1, \dots, n+1\}^n$:
  $$\text{Ans} = \frac{n}{n+1} \sum_{m=0}^n \binom{n}{m} m^k n^{n-m}!$$
  To evaluate this for $n \le 10^9$ and $k \le 10^5$, expand $m^k = \sum_{j=0}^k \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{m}{j}$ and use $\binom{n}{m}\binom{m}{j} = \binom{n}{j}\binom{n-j}{m-j}$ to collapse the inner sum over $m$ via $(1 + n)^{n-j}$:
  $$\text{Ans} = \frac{n}{n+1} \sum_{j=0}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} j! \binom{n}{j} (n + 1)^{n - j} = n \sum_{j=1}^{\min(n, k)} \left\{\begin{matrix} k \\ j \end{matrix}\right\} n^{\underline{j}} (n + 1)^{n - 1 - j},$$
  computable in $O(k \log k)$ time!

#### Problem A5: Codeforces 1349F2 — Slime and Sequences (Hard Version)
- **Metadata**:
  - **Problem ID**: Codeforces 1349F2
  - **Title**: Slime and Sequences (Hard Version)
  - **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1349/F2](https://codeforces.com/problemset/problem/1349/F2)
  - **Difficulty Tier**: `Mastery`
  - **Curation Role**: `BLIND CHECKPOINT`
  - **Primary Topic**: Backward Lagrange Inversion on $\Phi(w) = \frac{w}{e^w - 1}$ + Pole Cancellation
  - **Secondary Topics**: Generalized Eulerian numbers, Middle Product (transposed convolution)
- **Concise Inline Problem Statement & Exact Constraints**:
  A sequence $a_1, \dots, a_n$ of positive integers is *good* if for every $k > 1$ appearing in $a$, $k - 1$ appears at least once before the last occurrence of $k$. For every $k = 1, 2, \dots, n$, compute the total number of occurrences of $k$ across all good sequences of length $n$ modulo $998244353$. Constraints: $1 \le n \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By standard bijection from good sequences to permutations of $\{1, \dots, n\}$, the answer for each $k$ reduces to extracting coefficients from the bivariate Eulerian generating function $\frac{1}{1 - y \frac{e^w - 1}{w}}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Let $H(w) = \frac{e^w - 1}{w}$. To decouple $y H(w)$ in the denominator, apply Lagrange Inversion with $u = w / H(w) = \frac{w^2}{e^w - 1}$ (or $\Phi(t) = \frac{t}{e^t - 1}$), which transforms the coupled sum over $[w^n]$ into fixed powers of $\Phi(t)^{-m}$ evaluated via a single polynomial inversion and transposed convolution in $O(n \log n)$!

---

### Cluster B: Formal Laurent Series $K((x))$, Formal Residue Calculus ($\operatorname{res}_x$) & Change-of-Variables Formula ("炫酷反演魔术") (Iteration 22)

#### Problem B1: Codeforces 1204E — Natasha, Sasha and the Prefix Sums (and Generalized Raney/Catalan Residue Extraction)
- **Metadata**:
  - **Problem ID**: Codeforces 1204E (and `Elegia` Catalan Residue Archetype)
  - **Title**: Natasha, Sasha and the Prefix Sums
  - **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1204/E](https://codeforces.com/problemset/problem/1204/E)
  - **Difficulty Tier**: `Stepping Stone`
  - **Curation Role**: `TOPIC LADDER` (Entry problem for decomposing lattice paths by maximum prefix sum via Catalan generating functions $C(x)^k$ and extracting $[x^n] C(x)^k$ via $\operatorname{res}_x$ substitution $x = u(1-u)$)
  - **Primary Topic**: Formal Residue Change-of-Variables $x = u(1-u)$ on Catalan Powers $C(x)^k$
  - **Secondary Topics**: First-passage decomposition of $+1/-1$ lattice paths
- **Concise Inline Problem Statement & Exact Constraints**:
  Consider all $\binom{n+m}{n}$ sequences consisting of $n$ ones ($+1$) and $m$ minus-ones ($-1$). The *maximum prefix sum* of a sequence is $\max_{0 \le i \le n+m} \sum_{j=1}^i a_j$. Compute the sum of maximum prefix sums over all $\binom{n+m}{n}$ sequences modulo $998532443$ (or $998244353$). Constraints: $0 \le n, m \le 2000$ (and solvable in $O(n + m)$ for $n, m \le 10^7$!).
- **Bridge 1 (English $\to$ Initial GF)**:
  In terms of the Catalan OGF $C(x) = \frac{1 - \sqrt{1-4x}}{2x} = \sum_{d \ge 0} C_d x^d$ (where $x$ marks one $+1$ step and one $-1$ step), a path hitting level $k \ge 1$ for the first time decomposes into $k$ first-passage up-steps ($x^k C(x)^k$) followed by an arbitrary suffix, which corresponds to extracting coefficients of $C(x)^k$ and $\frac{C(x)^k}{\sqrt{1-4x}}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Substituting $x = u(1 - u)$ with $dx = (1 - 2u)\,du = \sqrt{1 - 4x}\,du$ into $\operatorname{res}_x \frac{C(x)^k}{\sqrt{1-4x}} \frac{dx}{x^{m+1}}$ cancels $\sqrt{1 - 4x}$ in one line:
  $$[x^m] \frac{C(x)^k}{\sqrt{1 - 4x}} = \operatorname{res}_u \frac{du}{u^{m+1}(1 - u)^{m+k+1}} = \binom{2m + k}{m}, \qquad [x^m] C(x)^k = \operatorname{res}_u \frac{(1 - 2u)\,du}{u^{m+1}(1 - u)^{m+k+1}} = \binom{2m+k-1}{m} - \binom{2m+k-1}{m-1},$$
  reducing the entire problem to an $O(n + m)$ sum of binomial coefficients!

#### Problem B2: AtCoder AGC021 E — Ball Eat Chameleons
- **Metadata**:
  - **Problem ID**: `agc021_e` / AGC021 E
  - **Title**: Ball Eat Chameleons
  - **Judge & URL**: AtCoder — [https://atcoder.jp/contests/agc021/tasks/agc021_e](https://atcoder.jp/contests/agc021/tasks/agc021_e)
  - **Difficulty Tier**: `Intermediate`
  - **Curation Role**: `TOPIC LADDER` (Reducing a greedy chameleon ball-feeding condition to bounded lattice paths / Raney's Lemma / residue extraction of $\sum [x^m] C(x)^k$)
  - **Primary Topic**: Lattice Path / Catalan Power Extraction $[x^m] C(x)^k$
  - **Secondary Topics**: Greedy invariant characterization ($R - B$ prefix condition)
- **Concise Inline Problem Statement & Exact Constraints**:
  There are $N$ chameleons, initially all blue. You throw $K$ balls one by one, each painted either Red (`R`) or Blue (`B`), to chosen chameleons. A chameleon turns red when it has eaten strictly more Red balls than Blue balls, and turns blue when it has eaten strictly more Blue balls than Red balls. Count the number of color sequences of length $K$ in $\{R, B\}^K$ for which it is possible to make all $N$ chameleons end up red, modulo $998244353$. Constraints: $1 \le N \le K \le 5 \times 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Suppose the sequence has $r$ Red balls and $b = K - r$ Blue balls ($r \ge b$). By a greedy assignment invariant, all $N$ chameleons can end up red iff either $r \ge b + N$ (and for $r = b$, invalid since at least one chameleon needs $R > B$, so reduce $b \gets b - 1$ when $r = b$), OR $b < r < b + N$ and the sequence never has a prefix with $B - R > N - (r - b)$, which translates to $[x^b] C(x)^k$ via Catalan excursion decomposition!
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  With $C(x) = \frac{1}{1-u}$ under the formal residue substitution $x = u(1-u)$, the number of valid sequences for each $(r, b)$ is $[u^b] (1 - 2u)(1 - u)^{-(r+1)} = \binom{r+b}{b} - \binom{r+b}{r + 1 + (N - (r - b))}$, allowing all $r \in [0, K]$ to be summed in $O(K)$ time!

#### Problem B3: Codeforces 1967E1 & 1967E2 — Again Counting Arrays (Hard Version)
- **Metadata**:
  - **Problem ID**: Codeforces 1967E2
  - **Title**: Again Counting Arrays (Hard Version)
  - **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1967/E2](https://codeforces.com/problemset/problem/1967/E2)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `TOPIC LADDER` (Canonical demonstration of `Elegia`'s formal residue substitution $x = \frac{u}{(1+u)^2}$ to collapse a rational function of Catalan series into $O(n)$ binomial sums)
  - **Primary Topic**: Formal Residue Change-of-Variables $x = \frac{u}{(1+u)^2}$ (`炫酷反演魔术`)
  - **Secondary Topics**: Bounded $\pm 1$ walks on $[0, m]$, rational continuum of $C(x)$
- **Concise Inline Problem Statement & Exact Constraints**:
  Given $n, m, b_0$, count sequences of length $n$ representing valid transitions in $[0, m]$ starting from $b_0$ under the Catalan / stack reduction rule, modulo $998244353$. Constraints: $\sum n \le 2 \times 10^6, m \le 2 \times 10^6$.
- **Bridge 1 (English $\to$ Initial GF)**:
  The generating function of valid sequences of length $n$ is $[x^n] R\bigl(x C(x)^2\bigr) C(x)^{b_0+1}$, where $C(x) = 1 + x C(x)^2$ is the Catalan series and $R(u)$ is a rational function encoding reflections at the upper barrier $m + 1$ and lower barrier $-1$:
  $$R(u) = \frac{1 - u^{m+1}}{1 - u^{m+2}} \quad \text{(and related reflection ratios in } u = x C(x)^2\text{)}.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Why is $[x^n] R(x C(x)^2) C(x)^{b_0+1}$ hard in the $x$-variable? Because $u = x C(x)^2 = C(x) - 1$ is an infinite power series in $x$!
  Look at what happens when we switch our primary variable to $u = C(x) - 1$ using the **Formal Residue Change-of-Variables Theorem**:
  Since $C(x) = 1 + u$ and $1 + u = 1 + x(1+u)^2$, we have:
  $$x = \frac{u}{(1 + u)^2}, \qquad dx = \frac{1 - u}{(1 + u)^3}\,du!$$
  Substituting this into $\operatorname{res}_x R(u) (1+u)^{b_0+1} \frac{dx}{x^{n+1}}$ turns $\frac{dx}{x^{n+1}}$ into $\frac{(1-u)(1+u)^{2n-1}}{u^{n+1}}\,du$, and $R(u) = \frac{1 - u^{m+1}}{1 - u^{m+2}}$ expands as a sparse geometric series in $u^{m+2}$, reducing the entire extraction to an $O(n / m + n)$ sum of binomial coefficients $[u^n] (1+u)^{2n+b_0} (1-u) R(u)$!

#### Problem B4: UOJ #424 — [集训队作业2018] count (Cartesian Trees with Bounded Left-Chain Height)
- **Metadata**:
  - **Problem ID**: UOJ #424 / LOJ #2552
  - **Title**: [集训队作业2018] count
  - **Judge & URL**: UOJ — [https://uoj.ac/problem/424](https://uoj.ac/problem/424)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `BLIND CHECKPOINT`
  - **Primary Topic**: Formal Residue Substitution $x = \frac{u}{(1+u)^2}$ on Continued-Fraction / Chebyshev-Catalan Ratios
  - **Secondary Topics**: Equivalence of array range-maximum profiles and Cartesian trees with left-depth $\le m$
- **Concise Inline Problem Statement & Exact Constraints**:
  Two arrays $A, B$ of length $n$ with elements in $\{1, \dots, m\}$ are called *range-maximum equivalent* if every subsegment $[l, r] \subseteq [1, n]$ has its leftmost maximum at the exact same index in both $A$ and $B$. Count the number of equivalence classes of arrays of length $n$ with values in $\{1, \dots, m\}$, modulo $998244353$. Constraints: $1 \le n, m \le 10^5$ (and $O(n)$ when $n > m$ is handled cleanly).
- **Bridge 1 (English $\to$ Initial GF)**:
  Two arrays are range-maximum equivalent iff they have the **same Cartesian tree** (breaking ties to the left)! Furthermore, an $n$-node binary tree can be label-realized by values in $\{1, \dots, m\}$ (where left children must have strictly smaller value than their parent, and right children have $\le$ value) iff every node has **at most $m$ left-edges** on the path from the root! Thus the OGF $F_m(x)$ satisfies the depth-$m$ recurrence:
  $$F_0(x) = 1, \qquad F_k(x) = \frac{1}{1 - x F_{k-1}(x)} \quad (1 \le k \le m).$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  How do we extract $[x^n] F_m(x)$ from an $m$-level continued fraction?
  Notice that as $m \to \infty$, $F_\infty(x) = \frac{1}{1 - x F_\infty(x)}$ is the Catalan series! Substitute $x = \frac{u}{(1+u)^2}$. By induction on $k$, the $1 \times 1$ Möbius transformation $z \mapsto \frac{1}{1 - \frac{u}{(1+u)^2} z}$ has fixed points $1 + u$ and $\frac{1+u}{u}$, which diagonalizes the recurrence into:
  $$F_m\left(\frac{u}{(1+u)^2}\right) = (1 + u) \frac{1 - u^{m+1}}{1 - u^{m+2}}!$$
  Applying $\operatorname{res}_x F_m(x) \frac{dx}{x^{n+1}} = \operatorname{res}_u F_m\left(\frac{u}{(1+u)^2}\right) \frac{(1-u)(1+u)^{2n-1}}{u^{n+1}}\,du$ immediately yields the $O(n)$ closed form!

#### Problem B5: LOJ #6673 / QOJ — Elegia's Coupled Binomial Sum via Egorychev Formal Residues (`Luogu P6667` / `UOJ #514` / `CF 1666A` Style)
- **Metadata**:
  - **Problem ID**: LOJ #6673 / UOJ Blog `炫酷反演魔术` Showcase (cf. Codeforces 1810G / AtCoder ARC156 D / QOJ #5421)
  - **Title**: Coupled Fuss–Catalan & Vandermonde Sum Untangling via Formal Residues
  - **Judge & URL**: LOJ / Codeforces / AtCoder
  - **Difficulty Tier**: `Mastery`
  - **Curation Role**: `RESERVE ARCHIVE`
  - **Primary Topic**: Egorychev's Double Formal Residue Method + Substitution Elimination $\operatorname{res}_u \operatorname{res}_v$
  - **Secondary Topics**: Archetype 3 substitution $x = \frac{u}{(1+u)^r}$, Jacobian cancellation
- **Concise Inline Problem Statement & Exact Constraints**:
  Given integers $n, m, r, s$ ($n, m \le 10^6$), evaluate coupled binomial sums of the form
  $$S_n = \sum_{k=0}^n \binom{r k + a}{k} \binom{s(n - k) + b}{n - k} c^k \pmod{998244353}$$
  when $s = r$ or $s = 1 - r$, or reduce general $s$ to a single 1D convolution via residue change of variables.
- **Bridge 1 (English $\to$ Initial GF)**:
  Write both binomial coefficients as formal residues:
  $$\binom{rk + a}{k} = \operatorname{res}_u \frac{(1+u)^{rk+a}}{u^{k+1}}\,du, \qquad \binom{r(n-k) + b}{n-k} = \operatorname{res}_v \frac{(1+v)^{r(n-k)+b}}{v^{n-k+1}}\,dv.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Notice that $\frac{(1+u)^{rk}}{u^{k+1}}$ has the variable combination $\frac{u}{(1+u)^r}$! Substituting $x = \frac{u}{(1+u)^r}$ (or using Gessel's Universal Denominator Identity $\sum_{k \ge 0} \binom{rk+a}{k} x^k = \frac{\mathcal{B}_r(x)^{a+1}}{1 - (r-1)(\mathcal{B}_r(x)-1)}$) expresses the generating function of the entire convolution as a simple rational/power function of $\mathcal{B}_r(x)$, which is then extracted at $[x^n]$ in $O(n)$ by a single reverse residue substitution $u = \mathcal{B}_r(x) - 1$!

---

### Cluster C: Derivative-Free & Alternative Lagrange Forms (`另类拉格朗日反演`) and Compound Forms (Iteration 23)

#### Problem C1: Luogu P7438 — [AGM 2021] 树 (Fuss–Catalan Power & Derivative-Free Sum)
- **Metadata**:
  - **Problem ID**: Luogu P7438 (and Generalized $k$-ary Tree Sum Variants)
  - **Title**: [AGM 2021] 树 / Generalized $r$-ary Tree Power Sums
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P7438](https://www.luogu.com.cn/problem/P7438)
  - **Difficulty Tier**: `Stepping Stone`
  - **Curation Role**: `TOPIC LADDER` (Direct comparison of Standard Form 2 vs. Derivative-Free Form 1 when summing $\sum_k c_k [x^n] F(x)^k$)
  - **Primary Topic**: Derivative-Free Lagrange Inversion (`另类拉格朗日反演`)
  - **Secondary Topics**: Fuss–Catalan series $\mathcal{B}_r(x) = 1 + x \mathcal{B}_r(x)^r$, pulling $H(u) = \sum c_k u^k$ inside $[u^n]$
- **Concise Inline Problem Statement & Exact Constraints**:
  Let $F(x)$ satisfy $F(x) = x \Phi(F(x))$ (for example, $r$-ary trees with $\Phi(u) = (1+u)^r$ or $\Phi(u) = e^u$). Given a polynomial or rational series $H(u) = \sum_{k=0}^n c_k u^k$, compute $\sum_{k=0}^n c_k [x^n] F(x)^k \pmod{998244353}$ for $n \le 2 \times 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By linearity of $[x^n]$, $\sum_{k=0}^n c_k [x^n] F(x)^k = [x^n] H\bigl(F(x)\bigr)$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  If $H(u)$ is a rational function like $\frac{P(u)}{1 - u \Phi'(u)/\Phi(u)}$ or if we work in a setting where differentiating $H(u)$ is messy, applying **Derivative-Free Form 1** directly gives:
  $$[x^n] H\bigl(F(x)\bigr) = [u^n] H(u) \bigl(\Phi(u) - u \Phi'(u)\bigr) \Phi(u)^{n-1},$$
  avoiding both differentiation of $H(u)$ and division by $n$!

#### Problem C2: AtCoder ABC281 Ex — Alchemy
- **Metadata**:
  - **Problem ID**: `abc281_h` / ABC281 Ex
  - **Title**: Alchemy
  - **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc281/tasks/abc281_h](https://atcoder.jp/contests/abc281/tasks/abc281_h)
  - **Difficulty Tier**: `Intermediate`
  - **Curation Role**: `TOPIC LADDER` (Deriving a non-trivial compound EGF/OGF functional equation from a recursive synthesis process and extracting $[x^N]$ via Lagrange Inversion)
  - **Primary Topic**: Compound Lagrange Inversion ($F(x) = A(x)\Phi(F(x))$) + Falling-Factorial Subproduct Tree
  - **Secondary Topics**: Binomial/EGF transform, Bostan–Mori / D&C FFT
- **Concise Inline Problem Statement & Exact Constraints**:
  There are $N$ types of materials $1, 2, \dots, N$. Material $1$ can be bought in any positive quantity. For $i \ge 2$, one unit of material $i$ can be synthesized from $c \ge 2$ distinct units of material $i-1$ (chosen from the $A$ available subtypes/colors or via binomial selection). Count the number of ways to synthesize $1$ unit of material $N$ starting from $A$ subtypes, modulo $998244353$. Constraints: $2 \le N \le 2 \times 10^5$, $1 \le A < 998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  When synthesizing upward across levels, a tree of syntheses where each internal node has $\ge 2$ children and leaves are colored from $A$ choices satisfies the implicit EGF equation:
  $$F(x) = A x + \bigl(e^{F(x)} - 1 - F(x)\bigr) \iff x = \frac{2 F(x) + 1 - e^{F(x)}}{A}!$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Look at $x = \frac{2 F(x) + 1 - e^{F(x)}}{A}$: here $F(x)$ is the **compositional inverse** of the explicit series $G(u) = \frac{2u + 1 - e^u}{A} = u \cdot \frac{2 - \frac{e^u - 1}{u}}{A}$!
  Applying Lagrange Inversion with $\Phi(u) = \frac{u}{G(u)} = \frac{A}{2 - \frac{e^u - 1}{u}}$ reduces $[x^N] F(x)$ to:
  $$[x^N] F(x) = \frac{1}{N} [u^{N-1}] \Phi(u)^N = \frac{A^N}{N} [u^{N-1}] \left(2 - \frac{e^u - 1}{u}\right)^{-N},$$
  or via binomial expansion in $A$ and subproduct tree D&C FFT in $O(N \log^2 N)$ (or $O(N \log N)$ via polynomial power)!

#### Problem C3: Codeforces 1810G — The Maximum Prefix (and Compound Random Walk LIF)
- **Metadata**:
  - **Problem ID**: Codeforces 1810G / CF 1770F / ARC136 F
  - **Title**: The Maximum Prefix & Compound Walk Excursion Extraction
  - **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/1810/G](https://codeforces.com/problemset/problem/1810/G)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `RESERVE ARCHIVE`
  - **Primary Topic**: Compound Functional Equation $F(x) = A(x) \Phi(F(x))$ & First-Passage Excursion Decomposition
  - **Secondary Topics**: Reverse DP vs. GF coefficient extraction
- **Concise Inline Problem Statement & Exact Constraints**:
  Given step probabilities $p_i$ (or step polynomial $P(z) = \sum_{d=-1}^D p_d z^d$) and a score array $h_k$ for the maximum prefix sum $M = \max_{0 \le i \le n} S_i$, compute the expected score $E[h_M]$ for all prefix lengths $k = 1, \dots, n$.
- **Bridge 1 (English $\to$ Initial GF)**:
  For a homogeneous left-continuous walk (where downward steps have size at most $-1$), the generating function $F(x)$ of hitting $+1$ for the first time satisfies $F(x) = x \Phi(F(x))$ where $\Phi(u) = \sum_{d=0}^{D+1} p_{d-1} u^d$, and the generating function of walks with maximum prefix sum $\ge k$ has numerator $F(x)^k$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Summing $\sum_{k \ge 0} (h_k - h_{k-1}) F(x)^k = H(F(x))$ and applying Derivative-Free Form 1 gives the exact answer for length $n$ as $[u^n] H(u) (\Phi(u) - u\Phi'(u)) \Phi(u)^{n-1}$ in $O(n \log n)$!

#### Problem C4: UOJ #450 / Luogu P5401 — [CTS2019] 珍珠 (and Generalized Exponential Series $\mathcal{E}_r(x)$)
- **Metadata**:
  - **Problem ID**: Luogu P5401 / UOJ #450 (`[CTS2019] 珍珠` / Generalized Exponential Series $\mathcal{E}_r$ & Coupon Collector)
  - **Title**: [CTS2019] 珍珠 / Generalized Exponential Series Extraction
  - **Judge & URL**: Luogu / UOJ — [https://uoj.ac/problem/450](https://uoj.ac/problem/450)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `TOPIC LADDER` (Using Gessel's Universal Denominator Identity $\frac{\mathcal{E}_r(x)^k}{1 - r x \mathcal{E}_r(x)^r} = \sum_{n \ge 0} (rn+k)^n \frac{x^n}{n!}$ to untangle exponential sums)
  - **Primary Topic**: Generalized Exponential Series $\mathcal{E}_r(x)$ & Gessel's Denominator Identity
  - **Secondary Topics**: Roots of unity filter, EGF convolution
- **Concise Inline Problem Statement & Exact Constraints**:
  Evaluate exponential power sums where the base of the $n$-th power contains $n$ itself, such as $\sum_{k=0}^D c_k (r n + k)^n \frac{x^n}{n!}$, or invert a system where each component contributes $(rn + k)^{n-1} / n!$ modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Whenever a sum contains $\frac{(rn + k)^n}{n!}$ or $\frac{(rn + k)^{n-1}}{n!}$ summed over $k$ or $n$, recognize that $n$ appears both in the base $(rn+k)$ and the exponent $n$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  By Table 23.4, $\frac{(rn+k)^n}{n!} = [x^n] \frac{\mathcal{E}_r(x)^k}{1 - r x \mathcal{E}_r(x)^r}$ where $\mathcal{E}_r(x) = e^{x \mathcal{E}_r(x)^r}$. Passing to the variable $u = \ln \mathcal{E}_r(x) = x e^{ru}$ via Derivative-Free Form 1 converts the coupled sum over $k$ into a single coefficient extraction $[u^n] \left(\sum_{k=0}^D c_k e^{ku}\right) e^{r n u}$!

#### Problem C5: QOJ #4815 / UOJ — Small-Characteristic Lagrange Inversion (`另类拉格朗日反演` $\bmod p$ where $p \le n$)
- **Metadata**:
  - **Problem ID**: QOJ #4815 / Luogu P7438 Small-$p$ Variant (cf. Wave 3B Iteration 29)
  - **Title**: Implicit Tree Enumeration Modulo Small Prime $p \le N$
  - **Judge & URL**: QOJ / Luogu
  - **Difficulty Tier**: `Mastery`
  - **Curation Role**: `BLIND CHECKPOINT`
  - **Primary Topic**: Characteristic-Free Derivative-Free Form 1 (`[x^n] H(F(x)) = [u^n] H(u) (\Phi(u) - u\Phi'(u)) \Phi(u)^{n-1} \bmod p`)
  - **Secondary Topics**: Lucas's Theorem on $\Phi(u)^{n-1} \bmod p$
- **Concise Inline Problem Statement & Exact Constraints**:
  Given a polynomial $\Phi(u) \in \mathbb{F}_p[u]$ of small degree $d$ and a small prime $p$, let $F(x) \in x \mathbb{F}_p[[x]]$ be the unique formal power series satisfying $F(x) = x \Phi(F(x))$. Compute $[x^n] F(x)^k \bmod p$ for huge $n, k \le 10^{18}$ when **$p \mid n$ is allowed**!
- **Bridge 1 (English $\to$ Initial GF)**:
  Standard Lagrange Inversion $[x^n] F(x)^k = \frac{k}{n} [u^{n-k}] \Phi(u)^n$ **fails completely** whenever $p \mid n$ because $n \equiv 0 \pmod p$ is not invertible in $\mathbb{F}_p$!
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Because our proof of Law 4 in Section 22.3 holds over **every commutative ring $R$ of any characteristic**, **Derivative-Free Form 1** holds in $\mathbb{F}_p$ with **zero division by $n$**:
  $$[x^n] F(x)^k = [u^{n-k}] \bigl(\Phi(u) - u \Phi'(u)\bigr) \Phi(u)^{n-1} \pmod p!$$
  Since $(A(u))^p \equiv A(u^p) \pmod p$ in $\mathbb{F}_p[u]$, writing $n - 1$ in base $p$ allows $[u^{n-k}] (\Phi(u) - u\Phi'(u)) \Phi(u)^{n-1} \bmod p$ to be computed in $O(d p \log_p n)$ time via digit DP in base $p$!

---

### Cluster D: Tree, Forest, Prüfer, Degree-Constrained & Cactus Enumerations (Iteration 24)

#### Problem D1: Luogu P5219 — 无聊的水题 I (Boring Water Problem I — Bounded Max-Degree Labelled Trees)
- **Metadata**:
  - **Problem ID**: Luogu P5219
  - **Title**: 无聊的水题 I (Boring Water Problem I)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P5219](https://www.luogu.com.cn/problem/P5219)
  - **Difficulty Tier**: `Stepping Stone`
  - **Curation Role**: `TOPIC LADDER` (Canonical entry problem for Prüfer sequence EGF with degree constraints)
  - **Primary Topic**: Prüfer Sequence EGF $(N-2)! [x^{N-2}] \left(\sum_{d=1}^M \frac{x^{d-1}}{(d-1)!}\right)^N$
  - **Secondary Topics**: Converting "exact maximum degree $= M$" into prefix difference $\text{ans}(\le M) - \text{ans}(\le M-1)$
- **Concise Inline Problem Statement & Exact Constraints**:
  Count the number of labelled trees on $N$ vertices whose maximum vertex degree is **exactly** $M$, modulo $998244353$. Constraints: $2 \le M < N \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Replace "maximum degree $= M$" by $(\text{max degree} \le M) - (\text{max degree} \le M - 1)$. In the Prüfer sequence of an $N$-vertex labelled tree, a vertex of degree $d \in \{1, \dots, D\}$ appears $d - 1 \in \{0, \dots, D - 1\}$ times. Thus the number of labelled trees on $N$ vertices with every vertex having degree $\le D$ is:
  $$T_{\le D}(N) = (N - 2)! [x^{N-2}] \left( \sum_{k=0}^{D-1} \frac{x^k}{k!} \right)^N.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Let $P_D(x) = \sum_{k=0}^{D-1} \frac{x^k}{k!}$. Since $[x^0]P_D(x) = 1$, we can compute $P_D(x)^N = \exp(N \ln P_D(x)) \bmod x^{N-1}$ in $O(N \log N)$ time for $D = M$ and $D = M - 1$, and subtract the two results!

#### Problem D2: AtCoder ABC303 Ex — Constrained Tree Degree
- **Metadata**:
  - **Problem ID**: `abc303_h` / ABC303 Ex
  - **Title**: Constrained Tree Degree
  - **Judge & URL**: AtCoder — [https://atcoder.jp/contests/abc303/tasks/abc303_h](https://atcoder.jp/contests/abc303/tasks/abc303_h)
  - **Difficulty Tier**: `Intermediate`
  - **Curation Role**: `TOPIC LADDER` (Canonical Japanese problem connecting Prüfer degree-sum characterization $\sum (d_v - 1) = N - 2$ with FPS power extraction)
  - **Primary Topic**: Degree-Constrained Tree Enumeration via Prüfer EGF/OGF Power
  - **Secondary Topics**: Handshake / Prüfer necessary and sufficient condition $\sum_{i=1}^N (d_i - 1) = N - 2$
- **Concise Inline Problem Statement & Exact Constraints**:
  You are given an integer $N$ and a set of allowed vertex degrees $S \subseteq \{1, 2, \dots, N-1\}$. Count the number of valid degree sequences (or labelled trees) on $N$ vertices such that every vertex $v$ has $\deg(v) \in S$, modulo $998244353$. Constraints: $2 \le N \le 2 \times 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By the Prüfer sequence characterization, a sequence of positive integers $(d_1, \dots, d_N)$ is the degree sequence of at least one tree on $N$ vertices if and only if $\sum_{i=1}^N (d_i - 1) = N - 2$ (and there are $\frac{(N-2)!}{\prod (d_i-1)!}$ such labelled trees).
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Defining $F(x) = \sum_{d \in S} x^{d-1}$ (for valid degree tuples) or $F_{\text{labelled}}(x) = \sum_{d \in S} \frac{x^{d-1}}{(d-1)!}$ (for labelled trees, weighted by $w_d$), the answer is simply $[x^{N-2}] F(x)^N$ (or $(N-2)! [x^{N-2}] F_{\text{labelled}}(x)^N$), computed in $O(N \log N)$ via FPS $\ln / \exp$!

#### Problem D3: Luogu P5434 — 有标号荒漠计数 (Labelled Desert / Cactus Forest Enumeration)
- **Metadata**:
  - **Problem ID**: Luogu P5434
  - **Title**: 有标号荒漠计数 (Labelled Desert Enumeration)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P5434](https://www.luogu.com.cn/problem/P5434)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `TOPIC LADDER` (Deriving the rooted cactus functional equation $F(x) = x \exp\left(\frac{2F - F^2}{2(1-F)}\right)$, unrooting to $C(x)$, and exponentiating to deserts $\exp(C(x))$)
  - **Primary Topic**: Labelled Cactus & Desert Enumeration via Implicit Block-Cut EGF
  - **Secondary Topics**: Newton Iteration / Compositional Inverse (`revert`), Dissymmetry Theorem
- **Concise Inline Problem Statement & Exact Constraints**:
  A *cactus* is a connected simple undirected graph in which every edge belongs to at most one simple cycle. A *desert* is a simple undirected graph in which every connected component is a cactus. Given $N$, count the number of labelled deserts on $N$ vertices modulo $998244353$. Constraints: $1 \le N \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  As derived in Section 24.3, a rooted connected cactus $F(x)$ decomposes around its root into a `SET` ($\exp$) of bridge lobes ($F(x)$) and cycle lobes of length $k \ge 3$ ($\frac{1}{2} F(x)^{k-1}$):
  $$F(x) = x \exp\!\left( \frac{2 F(x) - F(x)^2}{2\bigl(1 - F(x)\bigr)} \right).$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Solve $F(x) \bmod x^{N+1}$ via Newton iteration: writing $G(F) = F - x \exp\bigl(g(F)\bigr) = 0$ where $g(F) = \frac{2F - F^2}{2(1-F)}$ and $g'(F) = \frac{2 - 2F + F^2}{2(1-F)^2}$, the Newton step is:
  $$F_{\text{new}} = F - \frac{F - x e^{g(F)}}{1 - x e^{g(F)} g'(F)} \pmod{x^{2d}}.$$
  Once $F(x) \bmod x^{N+1}$ is found in $O(N \log N)$, integrate $C(x) = \int_0^x \frac{F(t)}{t}\,dt$ (dividing $[x^n]F(x)$ by $n$ to unroot) and compute $D(x) = \exp(C(x)) \bmod x^{N+1}$!

#### Problem D4: Luogu P6598 — 烷烃计数 (Alkane Enumeration) & Luogu P6597 — 烯烃计数 (Alkene Enumeration)
- **Metadata**:
  - **Problem ID**: Luogu P6598 (and Luogu P6597)
  - **Title**: 烷烃计数 (Alkane Enumeration)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P6598](https://www.luogu.com.cn/problem/P6598)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `TOPIC LADDER` (Canonical problem for unlabelled degree-bounded trees via Pólya Cycle Index $Z(S_3), Z(S_4)$ and Otter's Dissymmetry Theorem)
  - **Primary Topic**: Unlabelled Degree-Bounded Trees & Otter's Dissymmetry Theorem
  - **Secondary Topics**: Pólya Enumeration Theorem for $S_3, S_4$, Newton iteration with $A(x^2), A(x^3)$
- **Concise Inline Problem Statement & Exact Constraints**:
  An *alkane* $C_n H_{2n+2}$ is modelled as an **unlabelled unrooted tree** on $n$ carbon vertices in which every vertex has degree at most $4$. Compute the number of distinct alkanes with $k$ carbon atoms for all $k = 1, 2, \dots, N$ modulo $998244353$. Constraints: $1 \le N \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  First count **alkyl radicals** $A(x)$ (rooted unlabelled trees where the root has out-degree $\le 3$ and every other node has out-degree $\le 3$, with $[x^0]A(x) = 1$ representing an empty hydrogen branch) via $Z(S_3)$:
  $$A(x) = 1 + x \cdot \frac{A(x)^3 + 3 A(x) A(x^2) + 2 A(x^3)}{6}.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  When solving $A(x) \bmod x^{2d}$ by Newton iteration from $A_0(x) \bmod x^d$, notice that $A(x^2)$ and $A(x^3)$ only depend on coefficients of $A$ at indices $\le d$! Therefore, with respect to the top half of coefficients $[x^d \dots x^{2d-1}]A(x)$, $A(x^2)$ and $A(x^3)$ act as **known constants**, so the Fréchet derivative with respect to $A(x)$ is simply $1 - x \frac{3 A(x)^2 + 3 A(x^2)}{6}$! Once $A(x) \bmod x^{N+1}$ is computed in $O(N \log N)$, compute vertex-rooted alkanes $P(x) = x \cdot Z(S_4; A(x))$ and apply **Otter's Unlabelled Dissymmetry Theorem** (Section 24.4):
  $$\text{Alkanes}(x) = P(x) - \frac{(A(x) - 1)^2 - (A(x^2) - 1)}{2}!$$

#### Problem D5: Codeforces 917D — Stranger Trees (and $N \le 10^5$ Generalized Cayley Component Contraction: UOJ #496 / AtCoder AGC036 F)
- **Metadata**:
  - **Problem ID**: Codeforces 917D (and $N \le 10^5$ Tree-Block Contraction Variant)
  - **Title**: Stranger Trees
  - **Judge & URL**: Codeforces — [https://codeforces.com/problemset/problem/917/D](https://codeforces.com/problemset/problem/917/D)
  - **Difficulty Tier**: `Mastery`
  - **Curation Role**: `BLIND CHECKPOINT`
  - **Primary Topic**: Block-Weighted Generalized Cayley Formula ($N^{k-2} \prod_{i=1}^k s_i$) + Generating Function Extraction over Tree Forests
  - **Secondary Topics**: Converting $\prod_{i=1}^k s_i$ into "choose 1 marked vertex per connected component"
- **Concise Inline Problem Statement & Exact Constraints**:
  Given a tree $T_0$ on $N$ vertices, for every $j = 0, 1, \dots, N-1$, count the number of labelled trees $T$ on the same $N$ vertices that share **exactly $j$ edges** with $T_0$, modulo $10^9 + 7$ (or $998244353$ for $N \le 10^5$ via HLD + D&C FFT).
- **Bridge 1 (English $\to$ Initial GF)**:
  By binomial inversion (or $(y - 1)$ edge weights), choose a subset $F \subseteq E(T_0)$ of $m = N - k$ edges of $T_0$ to force into $T$. Those $m$ edges partition $T_0$ into $k = N - m$ connected components of sizes $s_1, \dots, s_k$. By the **Block-Weighted Generalized Cayley Formula** (Section 24.2), the number of trees $T$ containing all edges of $F$ is:
  $$N^{k-2} \prod_{i=1}^k s_i.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  How do we compute $\sum_{|F| = N - k} \prod_{i=1}^k s_i$ without tracking the sizes $s_i$ of all components?
  **Combinatorial Combinator Trick ($\prod s_i =$ Pointing at Each Component)**:
  Notice that $\prod_{i=1}^k s_i$ is the number of ways to **choose exactly $1$ marked vertex inside each of the $k$ connected components**!
  This reduces the tree DP state at each vertex $u$ to just two polynomials: $F_{u, 0}(x)$ (current component has $0$ marked vertices so far) and $F_{u, 1}(x)$ (current component has $1$ marked vertex so far), solvable in $O(N^2)$ by tree knapsack or $O(N \log^2 N)$ by HLD + $2 \times 2$ polynomial matrix D&C!

---

### Cluster E: Graph Enumerations: Functional, Eulerian, Bipartite, Tournaments, DAGs & 2-Connected Graphs (Iteration 25)

#### Problem E1: Luogu P4841 — [集训队作业2013] 城市规划 (City Planning — Connected & Eulerian Labelled Graphs)
- **Metadata**:
  - **Problem ID**: Luogu P4841
  - **Title**: [集训队作业2013] 城市规划 (City Planning)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P4841](https://www.luogu.com.cn/problem/P4841)
  - **Difficulty Tier**: `Stepping Stone`
  - **Curation Role**: `TOPIC LADDER` (Foundational problem introducing the Exponential Formula $C(x) = \ln G(x)$ for connected labelled graphs and Eulerian graphs)
  - **Primary Topic**: Connected Labelled Graph Enumeration via Formal Logarithm $C(x) = \ln G(x)$
  - **Secondary Topics**: Formal vs. analytic convergence of $\sum 2^{\binom{n}{2}} \frac{x^n}{n!}$, Eulerian graph parity bijection
- **Concise Inline Problem Statement & Exact Constraints**:
  Compute the number of connected simple undirected graphs on $N$ labelled vertices modulo $1004535809$ ($479 \times 2^{21} + 1$, an NTT prime). Constraints: $1 \le N \le 1.3 \times 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Every simple undirected graph on $n$ labelled vertices is uniquely an unordered `SET` ($\exp$) of its connected components. Since there are $2^{\binom{n}{2}}$ simple undirected graphs on $n$ labelled vertices in total, the EGF $C(x) = \sum_{n=1}^\infty c_n \frac{x^n}{n!}$ of connected labelled graphs satisfies $\exp(C(x)) = \sum_{n=0}^\infty 2^{\binom{n}{2}} \frac{x^n}{n!}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Taking the formal logarithm $C(x) = \ln\!\left(\sum_{n=0}^N 2^{\binom{n}{2}} \frac{x^n}{n!}\right) \bmod x^{N+1}$ in $O(N \log N)$ gives $c_N = N! [x^N] C(x)$! And if every vertex is additionally required to have even degree (Eulerian graphs), replacing $2^{\binom{n}{2}}$ by $2^{\binom{n-1}{2}}$ for $n \ge 1$ in the exact same $\ln$ pipeline yields connected Eulerian graphs!

#### Problem E2: Luogu P7364 — 有标号二分图计数 (Labelled Bipartite Graphs Enumeration)
- **Metadata**:
  - **Problem ID**: Luogu P7364
  - **Title**: 有标号二分图计数 (Labelled Bipartite Graphs Enumeration)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P7364](https://www.luogu.com.cn/problem/P7364)
  - **Difficulty Tier**: `Intermediate`
  - **Curation Role**: `TOPIC LADDER` (Canonical demonstration of the Quadratic-Exponent Identity $i(n-i) = \binom{n}{2} - \binom{i}{2} - \binom{n-i}{2}$ and the $\sqrt{G_{\text{2col}}(x)} = \exp(\frac{1}{2}\ln G_{\text{2col}}(x))$ symmetry-halving trick)
  - **Primary Topic**: Labelled Bipartite Graph Enumeration ($\sqrt{G_{\text{2col}}(x)}$) & Quadratic-Exponent Convolution
  - **Secondary Topics**: 2-coloring multiplicity $2^{c(G)}$ of a graph with $c(G)$ connected components
- **Concise Inline Problem Statement & Exact Constraints**:
  For every $k = 1, 2, \dots, N$, compute the number of simple undirected bipartite graphs on $k$ labelled vertices (not necessarily connected) modulo $998244353$. Constraints: $1 \le N \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Directly counting bipartite graphs is blocked by component color-swapping symmetry, so count **properly 2-colored labelled graphs** first: partitioning $n$ vertices into $i$ Black and $n - i$ White vertices allows $2^{i(n-i)}$ edge choices between the two parts:
  $$g_{\text{2col}, n} = \sum_{i=0}^n \binom{n}{i} 2^{i(n-i)}.$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  1. **Decouple $2^{i(n-i)}$**: Substitute $i(n-i) = \binom{n}{2} - \binom{i}{2} - \binom{n-i}{2}$ to compute $G_{\text{2col}}(x) = \sum_{n=0}^N g_{\text{2col}, n} \frac{x^n}{n!}$ via a single squaring of $\sum_{i=0}^N 2^{-\binom{i}{2}} \frac{x^i}{i!}$.
  2. **Halve Component Symmetry**: Because each connected bipartite component has $2$ proper 2-colorings, $G_{\text{2col}}(x) = \exp(2 C_{\text{bip}}(x))$. Therefore, the EGF of connected bipartite graphs is $C_{\text{bip}}(x) = \frac{1}{2} \ln G_{\text{2col}}(x)$, and the EGF of all bipartite graphs is $\exp(C_{\text{bip}}(x)) = \sqrt{G_{\text{2col}}(x)}$ in $O(N \log N)$!

#### Problem E3: Luogu P6295 — 有标号 DAG 计数 (Labelled Weakly Connected DAG Enumeration)
- **Metadata**:
  - **Problem ID**: Luogu P6295
  - **Title**: 有标号 DAG 计数 (Labelled DAG Enumeration)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P6295](https://www.luogu.com.cn/problem/P6295)
  - **Difficulty Tier**: `Intermediate`
  - **Curation Role**: `TOPIC LADDER` (Combining source-layer Inclusion–Exclusion, Graphical EGF $2^{-\binom{n}{2}}$ scaling to polynomial inverse, and rescaling back to ordinary EGF before taking $\ln$)
  - **Primary Topic**: Labelled DAG Enumeration via Graphical EGF Inverse + $\ln$ Connected Extraction
  - **Secondary Topics**: Source-layer Inclusion–Exclusion $(-1)^{k-1}$, Graphical EGF vs. Ordinary EGF
- **Concise Inline Problem Statement & Exact Constraints**:
  For every $k = 1, 2, \dots, N$, compute the number of **weakly connected** directed acyclic graphs (DAGs) on $k$ labelled vertices modulo $998244353$. Constraints: $1 \le N \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  By Inclusion–Exclusion on the subset of source vertices (vertices of in-degree $0$, of size $k \ge 1$), the total number $d_n$ of not-necessarily-connected labelled DAGs satisfies:
  $$\sum_{k=0}^n (-1)^k \binom{n}{k} 2^{k(n-k)} d_{n-k} = [n = 0].$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  1. **Step 1 (Graphical EGF Inversion)**: Divide by $n! 2^{\binom{n}{2}}$ using $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ to obtain $\sum_{n=0}^N d_n 2^{-\binom{n}{2}} \frac{x^n}{n!} = \left(\sum_{k=0}^N (-1)^k 2^{-\binom{k}{2}} \frac{x^k}{k!}\right)^{-1} \bmod x^{N+1}$.
  2. **Step 2 (Rescale to Ordinary EGF Before $\ln$)**: Multiply the $n$-th coefficient by $2^{\binom{n}{2}}$ to recover the true EGF $D(x) = \sum_{n=0}^N d_n \frac{x^n}{n!}$, and take $D_{\text{conn}}(x) = \ln D(x) \bmod x^{N+1}$ to get weakly connected DAGs in $O(N \log N)$!

#### Problem E4: Luogu P5827 — 点双连通图计数 (Labelled Biconnected Graphs) & Luogu P5828 — 边双连通图计数 (Labelled 2-Edge-Connected Graphs)
- **Metadata**:
  - **Problem ID**: Luogu P5827 & Luogu P5828
  - **Title**: 点双连通图计数 / 边双连通图计数 (Labelled Biconnected & 2-Edge-Connected Graphs)
  - **Judge & URL**: Luogu — [https://www.luogu.com.cn/problem/P5827](https://www.luogu.com.cn/problem/P5827) & [https://www.luogu.com.cn/problem/P5828](https://www.luogu.com.cn/problem/P5828)
  - **Difficulty Tier**: `Advanced`
  - **Curation Role**: `TOPIC LADDER` (Canonical pair of problems contrasting Block-Cut Tree $D(x) = x\exp(B'(D(x)))$ and Bridge-Block Tree $D(x) = E^\bullet(x\exp(D(x)))$ via Case B Lagrange Inversion)
  - **Primary Topic**: Block-Cut & Bridge-Block Tree Implicit Equations + Case B Lagrange Inversion
  - **Secondary Topics**: Log-free biconnected simplification $b_n = -(n-2)! [x^{n-1}] (D(x)/x)^{-(n-1)}$
- **Concise Inline Problem Statement & Exact Constraints**:
  Given $n \le 10^5$ (up to $5$ test queries in a single run), compute (1) the number of labelled biconnected (2-vertex-connected) simple undirected graphs on $n$ vertices (P5827), and (2) the number of labelled 2-edge-connected (bridgeless connected) simple undirected graphs on $n$ vertices (P5828), modulo $998244353$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Let $D(x) = x C'(x) = x \frac{d}{dx} \ln\!\left(\sum_{k \ge 0} 2^{\binom{k}{2}} \frac{x^k}{k!}\right)$ be the EGF of vertex-rooted connected graphs.
  - **Bridge-Block Tree (P5828)**: Contracting 2-edge-connected components yields $D(x) = E^\bullet\bigl(x \exp(D(x))\bigr)$ where $E^\bullet(y) = y E'(y)$.
  - **Block-Cut Tree (P5827)**: Decomposing blocks incident to the root yields $D(x) = x \exp\bigl(B'(D(x))\bigr) \iff B'\bigl(D(x)\bigr) = \ln \frac{D(x)}{x}$.
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Since there are only $5$ query values of $n \le 10^5$, we do not need full $O(N \log^2 N)$ `revert`; we apply **Case B Lagrange Inversion** (Section 25.6) to each queried $n$ in $O(n \log n)$:
  $$e_n = \frac{(n-1)!}{n} [x^{n-1}] D'(x) e^{-n D(x)}, \qquad b_n = -(n-2)! [x^{n-1}] \left(\frac{D(x)}{x}\right)^{-(n-1)} \quad (n \ge 2)!$$

#### Problem E5: QOJ / LOJ — Strongly Connected Digraphs (`有标号强连通图计数`) & CF 1556F
- **Metadata**:
  - **Problem ID**: QOJ / LOJ Strongly Connected Digraphs (`有标号强连通图计数`, $N \le 10^5$ extension of Luogu P6295)
  - **Title**: Labelled Strongly Connected Digraphs Enumeration
  - **Judge & URL**: QOJ / LOJ (and cf. Codeforces 1556F for the tournament bitmask analogue)
  - **Difficulty Tier**: `Mastery`
  - **Curation Role**: `BLIND CHECKPOINT`
  - **Primary Topic**: Condensing Digraphs into DAGs of Strongly Connected Components (Combining Graphical EGF Inverse with Ordinary EGF $\ln$)
  - **Secondary Topics**: Source-SCC group inclusion-exclusion $(-1)^{c-1}$
- **Concise Inline Problem Statement & Exact Constraints**:
  Count the number of **strongly connected** simple directed graphs on $n$ labelled vertices for all $n = 1, 2, \dots, N$ modulo $998244353$. Constraints: $1 \le N \le 10^5$.
- **Bridge 1 (English $\to$ Initial GF)**:
  Every directed graph $G$ condenses into a DAG of strongly connected components (SCCs). In the condensed DAG, let $S$ be the non-empty union of the $c \ge 1$ source SCCs (SCCs with no incoming edges from other SCCs). If $|S| = k$, there are $2^{k(n-k)}$ ways to choose directed edges from $S$ to $[n] \setminus S$, and $2^{2\binom{n-k}{2}} = 4^{\binom{n-k}{2}}$ ways to choose directed edges within $[n] \setminus S$!
  By source-layer Inclusion–Exclusion over the number $c$ of source SCCs inside $S$, a set $S$ of $c$ disjoint SCCs gets weight $(-1)^{c-1}$. Let $C_{\text{SCC}}(x) = \sum_{n=1}^\infty s_n \frac{x^n}{n!}$ be the ordinary EGF of single SCCs, and define the signed source-SCC cluster EGF:
  $$F(x) = 1 - \exp\bigl(-C_{\text{SCC}}(x)\bigr) = \sum_{k=1}^\infty f_k \frac{x^k}{k!}.$$
  Then for all $n \ge 1$, the total number of digraphs $g_n = 2^{n(n-1)} = 4^{\binom{n}{2}}$ satisfies:
  $$4^{\binom{n}{2}} = \sum_{k=1}^n \binom{n}{k} f_k \, 2^{k(n-k)} \, 4^{\binom{n-k}{2}}!$$
- **Bridge 2 (Initial GF $\to$ Computable Form & Manipulation Discovery Intuition)**:
  Rewrite the cross-exponent $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$:
  $$2^{k(n-k)} 4^{\binom{n-k}{2}} = 2^{\binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}} \cdot 2^{2\binom{n-k}{2}} = 2^{\binom{n}{2}} \cdot 2^{-\binom{k}{2}} \cdot 2^{+\binom{n-k}{2}}!$$
  Dividing the entire equation by $n! \, 2^{\binom{n}{2}}$ decouples $k$ and $n-k$ **completely**:
  $$\frac{2^{\binom{n}{2}}}{n!} = \sum_{k=1}^n \left(\frac{f_k 2^{-\binom{k}{2}}}{k!}\right) \left(\frac{2^{\binom{n-k}{2}}}{(n-k)!}\right)!$$
  Therefore, letting $\widehat{G}_+(x) = \sum_{n=0}^N 2^{\binom{n}{2}} \frac{x^n}{n!}$, we obtain $\widehat{F}(x) = \sum_{k=1}^N f_k 2^{-\binom{k}{2}} \frac{x^k}{k!} = 1 - \widehat{G}_+(x)^{-1}$ by **one polynomial inversion**, multiply the $k$-th coefficient by $2^{\binom{k}{2}}$ to recover $F(x) = 1 - \exp(-C_{\text{SCC}}(x))$, and take $C_{\text{SCC}}(x) = -\ln(1 - F(x))$ in $O(N \log N)$!

---

## Final Wave 3A Curation Summary Table (31 Audited Problems: 6 Rejected Templates + 25 Accepted Problems)

| # | Problem ID | Title | Judge | Cluster | Tier | Curation Role | Primary Technique |
|---|---|---|---|---|---|---|---|
| R1 | Luogu P6086 | 【模板】Prufer 序列 | Luogu | Rejected | Template | `REJECTED` | Bare Prüfer sequence conversion |
| R2 | Luogu P5373 | 【模板】多项式复合逆 | Luogu | Rejected | Template | `REJECTED` | Bare compositional inverse template |
| R3 | LC `compositional_inv...` | Compositional Inverse of FPS | Library Checker | Rejected | Template | `REJECTED` | Bare library benchmark |
| R4 | Luogu P5900 | 无标号树的计数 | Luogu | Rejected | Template | `REJECTED` | Bare OEIS A000055 query |
| R5 | LC `exp_of_fps` | Exp / Log of FPS | Library Checker | Rejected | Template | `REJECTED` | Bare $\exp / \ln$ library check |
| R6 | CSES 1095 / Bare Cayley | Counting Labeled Trees (Bare) | CSES | Rejected | Template | `REJECTED` | Bare $N^{N-2} \bmod P$ evaluation |
| A1 | AtCoder ABC222 H | Beautiful Binary Tree | AtCoder | Cluster A | Stepping Stone | `TOPIC LADDER` | 2-State Tree Grammar $\to$ $O(N)$ LIF |
| A2 | Luogu P3978 | `[TJOI2015]` 概率论 | Luogu | Cluster A | Stepping Stone | `RESERVE ARCHIVE` | Binary Tree Leaf Pointing + Catalan LIF |
| A3 | Codeforces 438E | The Child and Binary Tree | Codeforces | Cluster A | Intermediate | `TOPIC LADDER` | Implicit $F = 1 + C(x)F^2$ vs. FPS $\sqrt{}$ |
| A4 | Codeforces 1528F | AmShZ Farm | Codeforces | Cluster A | Advanced | `TOPIC LADDER` | Raney Circular Lemma + Stirling Sum |
| A5 | Codeforces 1349F2 | Slime and Sequences (Hard) | Codeforces | Cluster A | Mastery | `BLIND CHECKPOINT` | Backward LIF on $\Phi(w) = \frac{w}{e^w-1}$ |
| B1 | Codeforces 1204E | Natasha, Sasha and Prefix Sums | Codeforces | Cluster B | Stepping Stone | `TOPIC LADDER` | $\operatorname{res}_x$ Substitution $x = u(1-u)$ on $C(x)^k$ |
| B2 | AtCoder AGC021 E | Ball Eat Chameleons | AtCoder | Cluster B | Intermediate | `TOPIC LADDER` | Greedy Invariant $\to$ Catalan Power Residue |
| B3 | Codeforces 1967E2 | Again Counting Arrays (Hard) | Codeforces | Cluster B | Advanced | `TOPIC LADDER` | $\operatorname{res}_x$ Substitution $x = \frac{u}{(1+u)^2}$ |
| B4 | UOJ #424 | `[集训队作业2018]` count | UOJ | Cluster B | Advanced | `BLIND CHECKPOINT` | Depth-$m$ Continued Fraction + $x = \frac{u}{(1+u)^2}$ |
| B5 | LOJ #6673 / QOJ | Coupled Fuss–Catalan Sums | LOJ / QOJ | Cluster B | Mastery | `RESERVE ARCHIVE` | Egorychev Double-Residue Elimination |
| C1 | Luogu P7438 | `[AGM 2021]` 树 | Luogu | Cluster C | Stepping Stone | `TOPIC LADDER` | Derivative-Free LIF (`另类拉格朗日反演`) |
| C2 | AtCoder ABC281 Ex | Alchemy | AtCoder | Cluster C | Intermediate | `TOPIC LADDER` | Compound Implicit EGF $\to$ Reversion LIF |
| C3 | Codeforces 1810G | The Maximum Prefix | Codeforces | Cluster C | Advanced | `RESERVE ARCHIVE` | Left-Continuous Walk Excursion + Form 1 |
| C4 | UOJ #450 / Luogu P5401 | `[CTS2019]` 珍珠 (Generalized $\mathcal{E}_r$) | UOJ / Luogu | Cluster C | Advanced | `TOPIC LADDER` | Generalized Exp $\mathcal{E}_r(x)$ & Gessel Identity |
| C5 | QOJ #4815 | Implicit Trees Modulo Small $p \le N$ | QOJ | Cluster C | Mastery | `BLIND CHECKPOINT` | Characteristic-Free Form 1 + Base-$p$ Lucas |
| D1 | Luogu P5219 | 无聊的水题 I (Max-Degree Trees) | Luogu | Cluster D | Stepping Stone | `TOPIC LADDER` | Prüfer Sequence EGF Power |
| D2 | AtCoder ABC303 Ex | Constrained Tree Degree | AtCoder | Cluster D | Intermediate | `TOPIC LADDER` | Prüfer Degree-Sum $\sum (d_v-1) = N-2$ |
| D3 | Luogu P5434 | 有标号荒漠计数 (Labelled Deserts) | Luogu | Cluster D | Advanced | `TOPIC LADDER` | Cactus Block-Cut EGF + Dissymmetry / $\exp$ |
| D4 | Luogu P6598 & P6597 | 烷烃计数 & 烯烃计数 (Alkanes/Alkenes) | Luogu | Cluster D | Advanced | `TOPIC LADDER` | Pólya $Z(S_3), Z(S_4)$ + Otter's Dissymmetry |
| D5 | Codeforces 917D | Stranger Trees ($N \le 10^5$ Variant) | Codeforces | Cluster D | Mastery | `BLIND CHECKPOINT` | Generalized Cayley $N^{k-2}\prod s_i$ + Tree FPS |
| E1 | Luogu P4841 | `[集训队作业2013]` 城市规划 | Luogu | Cluster E | Stepping Stone | `TOPIC LADDER` | Connected & Eulerian Graphs via $\ln G(x)$ |
| E2 | Luogu P7364 | 有标号二分图计数 | Luogu | Cluster E | Intermediate | `TOPIC LADDER` | Quadratic-Exponent $2^{i(n-i)}$ + $\sqrt{G_{\text{2col}}(x)}$ |
| E3 | Luogu P6295 | 有标号 DAG 计数 | Luogu | Cluster E | Intermediate | `TOPIC LADDER` | Source-Layer IE + Graphical EGF Inverse + $\ln$ |
| E4 | Luogu P5827 & P5828 | 点双连通图 & 边双连通图计数 | Luogu | Cluster E | Advanced | `TOPIC LADDER` | Block-Cut & Bridge-Block Trees via LIF |
| E5 | QOJ / CF 1556F | 有标号强连通图计数 (Strong Digraphs) | QOJ / CF | Cluster E | Mastery | `BLIND CHECKPOINT` | Source-SCC Cluster Graphical EGF + $-\ln(1-F)$ |
