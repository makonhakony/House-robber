class Solution:
    def rob(self, nums) -> int:
        dp = [0] * len(nums)
        
        dp[0] = nums[0];
        if (len(nums) >1):
            dp[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
        
        return dp[-1]

class TestCase:
    pass

def main():
    print("hello")

if __name__ == "__main__":
    main()