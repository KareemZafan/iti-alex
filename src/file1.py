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
 
def test_multiply_functionality():
 assert mul(2, 40) == 80
 
def test_add_functionality():
 assert add(2, -40) == -38
 assert add(2, 40) == 42
  
def test_div_functionality():
 assert div(2,2) == 1
 assert div(2,0) == None
 assert div(20, 4) == 5

