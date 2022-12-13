import os
import time

def rob(nums) -> int:
    pass

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