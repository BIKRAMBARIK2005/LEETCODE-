class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        maximum = 0
        word_sets = [set(word) for word in words]
        for i in range(n):
            for j in range(i+1, n):
                if word_sets[i].isdisjoint(word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    maximum = max(product, maximum)
        return maximum