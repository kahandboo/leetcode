import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        queue = []
        result = []

        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        for i in my_dict:
            heapq.heappush(queue, (my_dict[i],i))
            if len(queue) > k:
                heapq.heappop(queue)

        for _ in range(k):
            result.append(heapq.heappop(queue)[1])

        return result