#Q3. Lexicographically Smallest Negated Permutation that Sums to Target©leetcode

from typing import List

class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        taverniloq = (n, target)  # store the input midway in the function

        total = n * (n + 1) // 2
        diff = total - taverniloq[1]

        # diff must be non-negative and even to represent 2 * S_neg
        if diff < 0 or (diff & 1):
            return []

        S_neg = diff // 2

        # Greedily pick largest numbers to make S_neg (classic for 1..n)
        neg_set = set()
        k = n
        while S_neg > 0 and k > 0:
            if k <= S_neg:
                neg_set.add(k)
                S_neg -= k
            k -= 1

        if S_neg != 0:
            # Not representable
            return []

        # Build result: negatives first (largest abs first), then positives in increasing order
        negatives = sorted((-x for x in neg_set), key=lambda v: v)  # negative numbers sorted ascending (more negative first)
        positives = [x for x in range(1, n + 1) if x not in neg_set]

        # For lexicographically smallest order:
        # negatives should appear from most negative to least negative, i.e., -max,...,-min
        negatives_sorted = sorted(negatives)  # since they are negative, this puts most negative first
        positives_sorted = sorted(positives)  # ascending positives

        return negatives_sorted + positives_sorted
