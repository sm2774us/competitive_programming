#!/usr/bin/env python3

''' Test speeds of various ways of counting inversions in a list

    The inversion count is a measure of how sorted an array is.
    A pair of items in a are inverted if i < j but a[j] > a[i]

    See https://stackoverflow.com/questions/337664/counting-inversions-in-an-array

    This program contains code by the following authors:
    mkso
    Niklas B
    B. M.
    Tim Babych
    python
    Zhe Hu
    prasadvk
    noman pouigt
    PM 2Ring

    Timing and verification code by PM 2Ring
    Collated 2017.12.16
    Updated 2017.12.21
'''

from timeit import Timer
from random import seed, randrange
from bisect import bisect, insort_left

seed('A random seed string')

# Merge sort version by mkso
def count_inversion_mkso(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = len(lst) // 2
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# Using a Binary Indexed Tree, aka a Fenwick tree, by Niklas B.
def count_inversions_NiklasB(a):
    res = 0
    counts = [0] * (len(a) + 1)
    rank = {v: i for i, v in enumerate(sorted(a), 1)}
    for x in reversed(a):
        i = rank[x] - 1
        while i:
            res += counts[i]
            i -= i & -i
        i = rank[x]
        while i <= len(a):
            counts[i] += 1
            i += i & -i
    return res

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# Merge sort version by B.M
# Modified by PM 2Ring to deal with the global counter
bm_count = 0

def merge_count_BM(seq):
    global bm_count
    bm_count = 0
    sort_bm(seq)
    return bm_count

def merge_bm(l1,l2):
    global bm_count
    l = []
    while l1 and l2:
        if l1[-1] <= l2[-1]:
            l.append(l2.pop())
        else:
            l.append(l1.pop())
            bm_count += len(l2)
    l.reverse()
    return l1 + l2 + l

def sort_bm(l):
    t = len(l) // 2
    return merge_bm(sort_bm(l[:t]), sort_bm(l[t:])) if t > 0 else l

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# Bisection based method by Tim Babych
def solution_TimBabych(A):
    sorted_left = []
    res = 0
    for i in range(1, len(A)):
        insort_left(sorted_left, A[i-1])
        # i is also the length of sorted_left
        res += (i - bisect(sorted_left, A[i]))
    return res

# Slightly faster, except for very small lists
def solutionE_TimBabych(A):
    res = 0
    sorted_left = []
    for i, u in enumerate(A):
        # i is also the length of sorted_left
        res += (i - bisect(sorted_left, u))
        insort_left(sorted_left, u)
    return res

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# Bisection based method by "python"
def solution_python(A):
    B = list(A)
    B.sort()
    inversion_count = 0
    for i in range(len(A)):
        j = binarySearch_python(B, A[i])
        while B[j] == B[j - 1]:
            if j < 1:
                break
            j -= 1
        inversion_count += j
        B.pop(j)
    return inversion_count

def binarySearch_python(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# Merge sort version by Zhe Hu
def inv_cnt_ZheHu(a):
    _, count = inv_cnt(a.copy())
    return count

def inv_cnt(a):
    n = len(a)
    if n==1:
        return a, 0
    left = a[0:n//2] # should be smaller
    left, cnt1 = inv_cnt(left)
    right = a[n//2:] # should be larger
    right, cnt2 = inv_cnt(right)

    cnt = 0
    i_left = i_right = i_a = 0
    while i_a < n:
        if (i_right>=len(right)) or (i_left < len(left)
            and left[i_left] <= right[i_right]):
            a[i_a] = left[i_left]
            i_left += 1
        else:
            a[i_a] = right[i_right]
            i_right += 1
            if i_left < len(left):
                cnt += len(left) - i_left
        i_a += 1
    return (a, cnt1 + cnt2 + cnt)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# Merge sort version by noman pouigt
# From https://stackoverflow.com/q/47830098
def reversePairs_nomanpouigt(nums):
    def merge(left, right):
        if not left or not right:
            return (0, left + right)
        #if everything in left is less than right
        if left[len(left)-1] < right[0]:
            return (0, left + right)
        else:
            left_idx, right_idx, count = 0, 0, 0
            merged_output = []

            # check for condition before we merge it
            while left_idx < len(left) and right_idx < len(right):
                #if left[left_idx] > 2 * right[right_idx]:
                if left[left_idx] > right[right_idx]:
                    count += len(left) - left_idx
                    right_idx += 1
                else:
                    left_idx += 1

            #merging the sorted list
            left_idx, right_idx = 0, 0
            while left_idx < len(left) and right_idx < len(right):
                if left[left_idx] > right[right_idx]:
                    merged_output += [right[right_idx]]
                    right_idx += 1
                else:
                    merged_output += [left[left_idx]]
                    left_idx += 1
            if left_idx == len(left):
                merged_output += right[right_idx:]
            else:
                merged_output += left[left_idx:]
        return (count, merged_output)

    def partition(nums):
        count = 0
        if len(nums) == 1 or not nums:
            return (0, nums)
        pivot = len(nums)//2
        left_count, l = partition(nums[:pivot])
        right_count, r = partition(nums[pivot:])
        temp_count, temp_list = merge(l, r)
        return (temp_count + left_count + right_count, temp_list)
    return partition(nums)[0]

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# PM 2Ring
def merge_PM2R(seq):
    seq, count = merge_sort_count_PM2R(seq)
    return count

def merge_sort_count_PM2R(seq):
    mid = len(seq) // 2
    if mid == 0:
        return seq, 0
    left, left_total = merge_sort_count_PM2R(seq[:mid])
    right, right_total = merge_sort_count_PM2R(seq[mid:])
    total = left_total + right_total
    result = []
    i = j = 0
    left_len, right_len = len(left), len(right)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            total += left_len - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, total

def rank_sum_PM2R(a):
    total = 0
    counts = [0] * len(a)
    rank = {v: i for i, v in enumerate(sorted(a))}
    for u in reversed(a):
        i = rank[u]
        total += sum(counts[:i])
        counts[i] += 1
    return total

# Fenwick tree functions adapted from C code on Wikipedia
def fen_sum(tree, i):
    ''' Return the sum of the first i elements, 0 through i-1 '''
    total = 0
    while i:
        total += tree[i-1]
        i -= i & -i
    return total

def fen_add(tree, delta, i):
    ''' Add delta to element i and thus
        to fen_sum(tree, j) for all j > i
    '''
    size = len(tree)
    while i < size:
        tree[i] += delta
        i += (i+1) & -(i+1)

def fenwick_PM2R(a):
    total = 0
    counts = [0] * len(a)
    rank = {v: i for i, v in enumerate(sorted(a))}
    for u in reversed(a):
        i = rank[u]
        total += fen_sum(counts, i)
        fen_add(counts, 1, i)
    return total

def fenwick_inline_PM2R(a):
    total = 0
    size = len(a)
    counts = [0] * size
    rank = {v: i for i, v in enumerate(sorted(a))}
    for u in reversed(a):
        i = rank[u]
        j = i + 1
        while i:
            total += counts[i]
            i -= i & -i
        while j < size:
            counts[j] += 1
            j += j & -j
    return total

def bruteforce_loops_PM2R(a):
    total = 0
    for i in range(1, len(a)):
        u = a[i]
        for j in range(i):
            if a[j] > u:
                total += 1
    return total

def bruteforce_sum_PM2R(a):
    return sum(1 for i in range(1, len(a)) for j in range(i) if a[j] > a[i])

# Using binary tree counting, derived from C++ code (?) by prasadvk
# https://stackoverflow.com/a/16056139
def ltree_count_PM2R(a):
    total, root = 0, None
    for u in a:
        # Store data in a list-based tree structure
        # [data, count, left_child, right_child]
        p = [u, 0, None, None]
        if root is None:
            root = p
            continue
        q = root
        while True:
            if p[0] < q[0]:
                total += 1 + q[1]
                child = 2
            else:
                q[1] += 1
                child = 3
            if q[child]:
                q = q[child]
            else:
                q[child] = p
                break
    return total

# Counting based on radix sort, recursive version
def radix_partition_rec(a, L):
    if len(a) < 2:
        return 0
    if len(a) == 2:
        return a[1] < a[0]
    left, right = [], []
    count = 0
    for u in a:
        if u & L:
            right.append(u)
        else:
            count += len(right)
            left.append(u)
    L >>= 1
    if L:
        count += radix_partition_rec(left, L) + radix_partition_rec(right, L)
    return count

# The following functions determine swaps using a permutation of
# range(len(a)) that has the same inversion count as `a`. We can create
# this permutation with `sorted(range(len(a)), key=lambda k: a[k])`
# but `sorted(range(len(a)), key=a.__getitem__)` is a little faster.

# Counting based on radix sort, iterative version
def radix_partition_iter(seq, L):
    count = 0
    parts = [seq]
    while L and parts:
        newparts = []
        for a in parts:
            if len(a) < 2:
                continue
            if len(a) == 2:
                count += a[1] < a[0]
                continue
            left, right = [], []
            for u in a:
                if u & L:
                    right.append(u)
                else:
                    count += len(right)
                    left.append(u)
            if left:
                newparts.append(left)
            if right:
                newparts.append(right)
        parts = newparts
        L >>= 1
    return count

def perm_radixR_PM2R(a):
    size = len(a)
    b = sorted(range(size), key=a.__getitem__)
    n = size.bit_length() - 1
    return radix_partition_rec(b, 1 << n)

def perm_radixI_PM2R(a):
    size = len(a)
    b = sorted(range(size), key=a.__getitem__)
    n = size.bit_length() - 1
    return radix_partition_iter(b, 1 << n)

# Plain sum of the counts of the permutation
def perm_sum_PM2R(a):
    total = 0
    size = len(a)
    counts = [0] * size
    for i in reversed(sorted(range(size), key=a.__getitem__)):
        total += sum(counts[:i])
        counts[i] = 1
    return total

# Fenwick sum of the counts of the permutation
def perm_fenwick_PM2R(a):
    total = 0
    size = len(a)
    counts = [0] * size
    for i in reversed(sorted(range(size), key=a.__getitem__)):
        j = i + 1
        while i:
            total += counts[i]
            i -= i & -i
        while j < size:
            counts[j] += 1
            j += j & -j
    return total

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# All the inversion-counting functions
funcs = (
    solution_TimBabych,
    solutionE_TimBabych,
    solution_python,
    count_inversion_mkso,
    count_inversions_NiklasB,
    merge_count_BM,
    inv_cnt_ZheHu,
    reversePairs_nomanpouigt,
    fenwick_PM2R,
    fenwick_inline_PM2R,
    merge_PM2R,
    rank_sum_PM2R,
    bruteforce_loops_PM2R,
    bruteforce_sum_PM2R,
    ltree_count_PM2R,
    perm_radixR_PM2R,
    perm_radixI_PM2R,
    perm_sum_PM2R,
    perm_fenwick_PM2R,
)

def time_test(seq, loops, verify=False):
    orig = seq
    timings = []
    for func in funcs:
        seq = orig.copy()
        value = func(seq) if verify else None
        t = Timer(lambda: func(seq))
        result = sorted(t.repeat(3, loops))
        timings.append((result, func.__name__, value))
        assert seq==orig, 'Sequence altered by {}!'.format(func.__name__)
    first = timings[0][-1]
    timings.sort()
    for result, name, value in timings:
        result = ', '.join([format(u, '.5f') for u in result])
        print('{:24} : {}'.format(name, result))

    if verify:
        # Check that all results are identical
        bad = ['%s: %d' % (name, value)
            for _, name, value in timings if value != first]
        if bad:
            print('ERROR. Value: {}, bad: {}'.format(first, ', '.join(bad)))
        else:
            print('Value: {}'.format(first))
    print()

#Run the tests
size, loops = 5, 1 << 12
verify = True
for _ in range(7):
    hi = size // 2
    print('Size = {}, hi = {}, {} loops'.format(size, hi, loops))
    seq = [randrange(hi) for _ in range(size)]
    time_test(seq, loops, verify)
    loops >>= 1
    size <<= 1

#size, loops = 640, 8
#verify = False
#for _ in range(5):
    #hi = size // 2
    #print('Size = {}, hi = {}, {} loops'.format(size, hi, loops))
    #seq = [randrange(hi) for _ in range(size)]
    #time_test(seq, loops, verify)
    #size <<= 1

#size, loops = 163840, 4
#verify = False
#for _ in range(3):
    #hi = size // 2
    #print('Size = {}, hi = {}, {} loops'.format(size, hi, loops))
    #seq = [randrange(hi) for _ in range(size)]
    #time_test(seq, loops, verify)
    #size <<= 1