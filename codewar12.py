def same_structure_as(original, other):

    # one is list and the other is not
    if isinstance(original, list) != isinstance(other, list):
        return False

    # if both are not lists -> structure matches
    if not isinstance(original, list):
        return True

    # lengths must match
    if len(original) != len(other):
        return False

    # recursively compare children
    return all(
        same_structure_as(x, y)
        for x, y in zip(original, other)
    )


print(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ]))   # False
print(same_structure_as([1, '[', ']'], [2, 'a', 'b']))     # True
print(same_structure_as([1, [1, 1]], [2, [3, 4]]))         # True
print(same_structure_as([1, [1, 1]], [2, 3]))              # False