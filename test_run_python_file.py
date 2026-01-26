from functions.run_python_file import run_python_file

def test():
    result = run_python_file("calculator", "main.py") # (should print the calculator's usage instructions)
    print(result)
    result = run_python_file("calculator", "main.py", ["3 + 5"]) # (should run the calculator... which gives a kinda nasty rendered result)
    print(result)
    result = run_python_file("calculator", "tests.py") # (should run the calculator's tests successfully)
    print(result)
    result = run_python_file("calculator", "../main.py") # (this should return an error)
    print(result)
    result = run_python_file("calculator", "nonexistent.py") # (this should return an error)
    print(result)
    result = run_python_file("calculator", "lorem.txt") # (this should return an error)
    print(result)


if __name__ == "__main__":
    test()