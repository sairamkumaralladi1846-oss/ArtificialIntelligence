def hello_b():
    print(__name__)

# hello_b()
if __name__ == '__main__':
    # this only runs if we run b.py directly
    # eg. by using 'python b.py'
    print('Hey this is b')