class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        indices = [0]*len(primes)
        while len(ugly) < n:
            candidate = []
            for i in range(len(primes)):
                value = ugly[indices[i]] * primes[i]
                candidate.append(value)
            next = min(candidate)
            ugly.append(next)
            for i in range(len(primes)):
                if candidate[i] == next:
                    indices[i] += 1
        return ugly[n-1]
