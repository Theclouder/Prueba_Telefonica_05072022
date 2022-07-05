from behave import *
from program.main import *

@when('I search {name} in the API and check if it is {result}')
def find_name(context, name, result):
    ret = setup("-n \"" + name + "\"")
    print('Returned: ' + ret)
    print('Correct: ' + result)
    if ret == result:
        context.name = name
        assert True
    else:
        assert False
    
@then('I get the lists which have this name: {name}')
def print_name(context, name):
    if context.name == name:
        assert True
    else:
        assert False