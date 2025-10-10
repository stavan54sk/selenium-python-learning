def setup_module(module):
    print("Module setup - once per module")

def teardown_module(module):
    print("Module teardown - once per module")

def setup_function(module):
    print("Function setup - once per function")

def teardown_function(module):
    print("Function teardown - once per function")

def test_login():
   print("MyHook Login Test")

def test_home():
   print("MyHook Home Test")

def test_order():
   print("MyHook Order Test")

def test_summary():
   print("MyHook Summary Test")