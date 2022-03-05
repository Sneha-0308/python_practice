def dec(func):
    def nowexec():
        print("Executing now")
        func()
        print("Executed")
    return nowexec


@dec
def greeting():
    print("Hello")


greeting()