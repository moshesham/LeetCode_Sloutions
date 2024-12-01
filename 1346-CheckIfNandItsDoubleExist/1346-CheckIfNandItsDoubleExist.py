class Solution:
    def check(self, arr):
        store = defaultdict(int)
        for val in arr:
            if store[val * 2]:
                return True
            store[val] = 1
        return False

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        if self.check(arr):
            return True
            
        arr.reverse()
        return self.check(arr)