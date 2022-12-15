import os
import time

def rob(nums) -> int:
    dp = [0] * len(nums)
    
    dp[0] = nums[0];
    if (len(nums) >1):
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])

    return dp[-1]

path = "testcase"
class TestCase:
    name = ""
    input = []

    def __init__(self,file) -> None:
        # TODO: read file
        file_path = f"{file}"
        self.name = file
        with open(file_path, 'r') as f:
            self.input = list(map(int,f.read().split(",")))


def main():
    print("hello")

    os.chdir(path)

    testCase = []
    # TODO: take testcase from folder
    for file in os.listdir():
        if file.endswith(".txt"):
            testCase.append(TestCase(file))
    
    runtime = []
    for test in testCase:
        # TODO: start timer
        start = time.perf_counter_ns()

        result = rob(test.input)

        # TODO: stop timer
        end = time.perf_counter_ns()

        print("for",test.name,"the value is",result)
        print(test.name,"took",end-start,"ns\n")
        runtime.append(end-start)
    
    total_runtime= 0
    for each in runtime:
        total_runtime += each
    print("total runtime",total_runtime,"ns")



if __name__ == "__main__":
    main()