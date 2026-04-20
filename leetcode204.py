#134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
          total_tank += gas[i] - cost[i]
          current_tank += gas[i] - cost[i]

          if current_tank < 0 :
            start = i + 1
            current_tank = 0
        
        return start if total_tank >= 0 else -1