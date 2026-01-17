"Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]"

from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    return [x for x, _ in freq.most_common(k)]
