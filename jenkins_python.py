
def print_message(name):
    print "In staging mode"
    print "Hello, {}\n{}".format(name, message)


def main():
    global message
    message = "Welcome to this test"
    print_message("Babis")

if __name__ == "__main__":
    main()
