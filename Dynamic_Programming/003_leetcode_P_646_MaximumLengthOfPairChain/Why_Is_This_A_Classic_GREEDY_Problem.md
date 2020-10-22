We now prove that the smallest "end" value is indeed a valid greedy choice.

1. Considering an output, `G = {g_1 , g_2 , . . . , g_k }` that this **greedy choice** results in vs. an **optimal choice**, `T = {t_1 , t_2 , . . . , t_m }`.
    
    1.1. Suppose the start of a pair is `s(·)`, and the end is `f(·)`.
    
    1.2. We assume, without any loss of generality, that the pairs in the two sets are ordered by the end value.
    
    1.3. We know, for the sets `G` and `T`, `m >= k`. Our objective is to prove that k = m.

2. Claim I - ___For every i = 1, . . . , k, f(gi) <= f(ti)___
    
    2.1. Proof by induction on `i`. For the base case, consider `i = 1`. The greedy choice is to pick a meeting with the earliest finish time. This guarantees that `f(g_1) <= f(t_1)`.

    2.2. For the step, assume that the assertion is true for `i = 1, . . . , p-1`. For `i = p`, we know that `f(g_p-1) <= f(t_p-1) <= s(t_p)`. Thus, the meeting `t_p` does not conﬂict with `g_p - 1`, and therefore, is available to be chosen after `g_p - 1` is chosen.

    2.3. Thus, `f(g_p) <= f(t_p)` because we choose the meeting with the earliest finish time.

3. Claim II - ___k = m___
    
    3.1. Assume otherwise, for the purpose of contradiction, and that `m > k`.
    
    3.2. Then, there exists a pair `t_k+1` in the set `T`. But, `f(g_k) <= f(t_k)` by `I`.
    
    3.3. Thus, the meeting `t_k+1` does not conflict with `t_k`, and therefore does not conflict with `g_k`, and is available to be chosen after `g_k` is chosen, which contradicts the claim that no more meetings are left that can be chosen after `g_k` is chosen.