
def print_message(name):
    print "Hello, {}\n{}".format(name, message)


def main():
    global message
    message = "Welcome to this test"
    print_message("Babis")

if __name__ == "main()":
    main()
