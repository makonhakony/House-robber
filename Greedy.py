import os
import time

def rob(nums) -> int:
    countDown = len(nums)/2
    res = 0
    while (countDown > 0):
        max = 0
        choose = 0
        for i in range(len(nums)):
            if (((i != 0 and nums[i-1] != -1) or i ==0) and ((i != len(nums) -1 and nums[i+1] != -1) or i == len(nums) -1)):
                if (max < nums[i]):
                    max = nums[i]
                    choose = i
        nums[choose] = -1
        countDown -= 1
        res += max

    return res

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