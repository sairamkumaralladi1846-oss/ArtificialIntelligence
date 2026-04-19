from b import hello_b
from c import hello_c

def hello_a():
    print(__name__)

hello_a()
hello_b()
hello_c()