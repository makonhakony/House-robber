import os
import time

mem = [] 
def rob(nums) -> int:
    n = len(nums)
    global mem 
    mem = [None]* len(nums)
    return dp(nums, n-1)

def dp(nums: list[int], i) -> int:
    global mem
    if (i == 0):
        mem[0] = nums[0]
        return mem[0]
    
    if (i > 0):
        if i == 1:
            if mem[1] == None:
                mem[1] = nums[1]
            return mem[1]
            
        if (mem[i] == None):
            mem[i] = max(int(dp(nums, i-1)), int(dp(nums,i-2)) + int(nums[i]))
            
        return mem[i]

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
    # TODO: start timer
    start = time.perf_counter_ns()
    for test in testCase:
        result = rob(test.input)
        print("for",test.name,"the value is",result)

    # TODO: stop timer
    end = time.perf_counter_ns()

    print("total runtime",end - start,"ns")



if __name__ == "__main__":
    main()