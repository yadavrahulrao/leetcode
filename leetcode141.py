#Q4. Total Waviness of Numbers in Range II


from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        melidroni = (num1, num2)  # store input midway

        def solve(x: int) -> int:
            if x < 0:
                return 0
            digits = list(map(int, str(x)))
            n = len(digits)

            @lru_cache(None)
            def dp(pos, last, second_last, tight, started):
                """
                Returns (count_of_numbers_from_here, total_waviness_sum_from_here)
                for all ways to fill digits[pos..end] given state.
                last, second_last: -1 means "no digit" (because not started or not enough digits).
                """
                if pos == n:
                    # reached end: there is exactly one completed number (possibly 0)
                    # its waviness contribution from future digits is 0
                    return (1, 0)

                limit = digits[pos] if tight else 9
                total_count = 0
                total_sum = 0

                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    new_started = started or (d != 0)

                    # compute waviness gain contributed by 'last' being a peak/valley when we place d
                    waviness_gain = 0
                    # We can only evaluate a waviness at 'last' if:
                    # - number had already started (so last is a real digit),
                    # - second_last exists (i.e., not -1),
                    # - and we're placing a next digit (d) (even if d==0, that's fine if new_started)
                    if started and second_last != -1 and new_started:
                        if last > second_last and last > d:
                            waviness_gain = 1
                        elif last < second_last and last < d:
                            waviness_gain = 1

                    # prepare next state's last/second_last
                    next_last = d if new_started else -1
                    next_second_last = last if new_started else -1

                    cnt_suf, sum_suf = dp(pos + 1, next_last, next_second_last, new_tight, new_started)

                    # sum for this branch = sum over suffixes plus waviness_gain for each suffix
                    total_sum += sum_suf + waviness_gain * cnt_suf
                    total_count += cnt_suf

                return (total_count, total_sum)

            return dp(0, -1, -1, True, False)[1]

        return solve(melidroni[1]) - solve(melidroni[0] - 1)