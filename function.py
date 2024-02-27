def greeting(name):
    """please say hello"""
    print(f"hello, {name.title()}")

greeting('woody')
# information on the method
help(greeting)
# see its docstring
print(greeting.__doc__)

def pizza(*args):
    print(len(args), "ingredients are ready for you, which are :", args)

pizza('cheese','bacon','mushroom')

def toy_profile(name, owner, **args):
    args['name']=name
    args['owner']=owner
    return args

my_toy = toy_profile('woody','andy',color='yellow',age=30)
print(my_toy) #unordered
