class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num not in occurence:
                occurence[num] = 0
            occurence[num] += 1

        for num, cnt in occurence.items():
            freq[cnt].append(num) # the count is the index and num is the value there
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num) # starting from the last entry
                if len(res) == k:
                    return res


            


        