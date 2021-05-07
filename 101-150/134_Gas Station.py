from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remainGas = 0
        n = len(gas)
        start = -1
        startGas = 0

        for i in range(n):
            remainGas += gas[i] - cost[i]
            if start == -1 and gas[i] - cost[i] >= 0:
                start = i
                startGas = gas[i] - cost[i]
            elif start != -1:
                startGas += gas[i] - cost[i]
                if startGas < 0:
                    start = -1
        if remainGas < 0:
            return -1
        return start

    def run(self):
        print(self.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
        print(self.canCompleteCircuit([2, 3, 4], [3, 4, 3]))

        print(self.canCompleteCircuit(
            [2, 0, 1, 2, 3, 4, 0], [0, 1, 0, 0, 0, 0, 11]))


foo = Solution()
foo.run()
