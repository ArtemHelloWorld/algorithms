from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        time O(NlogN)
        memory O(N)
        """
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        return sorted(counter, key=lambda word: (-counter[word], word))[:k]


import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        time O(KlogN)
        memory O(N)
        """
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        heap = [(-counter[word], word) for word in counter]
        heapq.heapify(heap)  # O(N)
        return [heapq.heappop(heap)[1] for _ in range(k)]  # O(KLogN)
