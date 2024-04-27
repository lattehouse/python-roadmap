# raise 
# assert
# try...except
# try...except...expect
# try...except...else
# try...except...finally
# custom exception
# https://docs.python.org/zh-cn/3/tutorial/errors.html
number = 1
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)

assert (number < 5), f"The number should not exceed 5. ({number=})"
print(number)

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

try:
    linux_interaction()
except:
    pass
    print("Linux function wasn't executed.")