import os
import time

def rob(nums, i) -> int:
    
    if (i < len(nums)):
        return max( rob(nums, i+1) , nums[i] + rob(nums, i+2))
    else:
        return 0

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

        result = rob(test.input, 0)

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