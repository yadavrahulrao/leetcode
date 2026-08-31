#457. Circular Array Loop


class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            direction = nums[i] > 0

            slow = i
            fast = i

            while True:
                # Next step must have the same direction
                next_slow = next_index(slow)
                if (nums[next_slow] > 0) != direction:
                    break

                # Fast pointer: first step
                next_fast = next_index(fast)
                if (nums[next_fast] > 0) != direction:
                    break

                # Fast pointer: second step
                next_fast = next_index(next_fast)
                if (nums[next_fast] > 0) != direction:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    # One-element cycle is not valid
                    if slow == next_index(slow):
                        break
                    return True

        return False
