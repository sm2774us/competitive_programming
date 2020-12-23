"""
Notes:

This is an example method of comparing 2 arrays at any rotation,
where there may be multiple matching values.

The typical 'best' case is a single loop to find the minimums,
if theres only one - then this is a simple operation.
Otherwise we need to find the lowest minimum from both arrays before comparing.

Further Optimizations:
- Avoid modulo entirely (using multiple loops, making it more verbose)
- Depending on use case, caller may want to compare sorted arrays,
  (to avoid more extensive checks),
"""


def normalize_rotation_index(ls, v_min_other=None):
    """ Return the index or -1 (when the minimum is above `v_min_other`) """

    if len(ls) <= 1:
        return 0

    def compare_rotations(i_a, i_b):
        """ Return True when i_a is smaller.
            Note: unless there are large duplicate sections of identical values,
            this loop will exit early on.
        """
        for offset in range(1, len(ls)):
            v_a = ls[(i_a + offset) % len(ls)]
            v_b = ls[(i_b + offset) % len(ls)]
            if v_a < v_b:
                return True
            elif v_a > v_b:
                return False
        return False

    v_min = ls[0]
    i_best_first = 0
    i_best_last = 0
    i_best_total = 1
    for i in range(1, len(ls)):
        v = ls[i]
        if v_min > v:
            v_min = v
            i_best_first = i
            i_best_last = i
            i_best_total = 1
        elif v_min == v:
            i_best_last = i
            i_best_total += 1

    # all values match
    if i_best_total == len(ls):
        return 0

    # exit early if we're not matching another lists minimum
    if v_min_other is not None:
        if v_min != v_min_other:
            return -1
    # simple case, only one minimum
    if i_best_first == i_best_last:
        return i_best_first

    # otherwise find the minimum with the lowest values compared to all others.
    # start looking after the first we've found
    i_best = i_best_first
    for i in range(i_best_first + 1, i_best_last + 1):
        if (ls[i] == v_min) and (ls[i - 1] != v_min):
            if compare_rotations(i, i_best):
                i_best = i

    return i_best


def compare_circular_lists(ls_a, ls_b):
    # sanity checks
    if len(ls_a) != len(ls_b):
        return False
    if len(ls_a) <= 1:
        return ls_a == ls_b

    index_a = normalize_rotation_index(ls_a)
    index_b = normalize_rotation_index(ls_b, ls_a[index_a])

    if index_b == -1:
        return False

    if index_a == index_b:
        return ls_a == ls_b

    # cancel out 'index_a'
    index_b = index_b - index_a
    if index_b < 0:
        index_b += len(ls_a)
    index_a = 0  # ignore it

    # compare rotated lists
    for i in range(len(ls_a)):
        if ls_a[i] != ls_b[(index_b + i) % len(ls_b)]:
            return False
    return True


assert compare_circular_lists([0, 9, -1, 2, -1], [-1, 2, -1, 0, 9]) == True
assert compare_circular_lists([2, 9, -1, 0, -1], [-1, 2, -1, 0, 9]) == False
assert (
    compare_circular_lists(["Hello" "Circular", "World"], ["World", "Hello" "Circular"])
    == True
)
assert (
    compare_circular_lists(["Hello" "Circular", "World"], ["Circular", "Hello" "World"])
    == False
)

# -------------------
# Extra Sanity Checks


def normalize_rotation(ls):
    index = normalize_rotation_index(ls)
    if index != 0:
        return ls[index:] + ls[:index]
    return ls[:]


def normalize_rotation_simple(ls):
    if ls:
        return min((ls[i:] + ls[:i] for i in range(len(ls))))
    return ls[:]


def compare_circular_lists_simple(ls_a, ls_b):
    return normalize_rotation_simple(ls_a) == normalize_rotation_simple(ls_b)


test_data = [
    (7, 1, 1, 1, 2, 3, 4, 3, 2, 1),
    (9, 2, 0, 0, 9),
    (546, 54, 1, 88, 5, 5, 5, 5, 0, 1, 1, 4),
    (),
    (0,),
    (0, 0),
    (0, 0, 0),
    (0, 0, 0, -1),
    ("Hello", "Circle", "World"),
    ("Hello", "Hello", "There"),
    ("", "", "There"),
]

for ls in test_data:
    ofs = len(ls) // 2
    ls_ofs = ls[ofs:] + ls[:ofs]
    assert compare_circular_lists(ls, ls_ofs) == compare_circular_lists_simple(
        ls, ls_ofs
    )

    ofs = 1
    ls_ofs = ls[ofs:] + ls[:ofs]
    assert compare_circular_lists(ls, ls_ofs) == compare_circular_lists_simple(
        ls, ls_ofs
    )

    ofs = len(ls) - 2
    ls_ofs = ls[ofs:] + ls[:ofs]
    assert compare_circular_lists(ls, ls_ofs) == compare_circular_lists_simple(
        ls, ls_ofs
    )

    a = normalize_rotation(ls)
    b = normalize_rotation_simple(ls)
    assert a == b
