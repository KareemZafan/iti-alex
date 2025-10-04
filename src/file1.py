impot pytest

def add(a,b):
 return a + b
 
def mul(a,b):
 return a * b
 
 
def div(a,b):
 if b == 0: 
  return None
 else 
  return a /b 


# todo write tests for the previous functions
 
def test_mul():
 assert mul(2, 40) == 80


def test_div():
 assert div(20, 4) == 5

def test_add():
 assert add(2, 40) == 42