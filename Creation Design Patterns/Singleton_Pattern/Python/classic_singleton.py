# ** Classic Implementation (using class variable and __new__) ** #
# This is often shown as a direct translation from languages from Java/C++ 


class SingletonClassic:
    _instance = None # A class variable that holds the single instance.

    # __new__(cls, *args, **kwargs): This special method is responsible for creating and returning a new instance of a class. We override it
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Creating new instance (classic)")
            cls._instance =  super(SingletonClassic, cls).__new__(cls) # optional to include SingletonClassic and cls in the call to super, Python usually infers this automatically

        else:
            print("Returning existing instance (classic)")
        
        return cls._instance


    def __init__(self, data=None):
        # This will be called every time SingletonClassic is invoked,
        # even if __new__ returns an existing instance.
        # So, be careful with re-initialization logic here.
        # A common pattern is to initialize only if it's the first time
        if not hasattr(self, 'initialized'): # check if already initialized
            print(f"Initializing instance with data: {data}")
            self.data = data
            self. initialized = True
        
        else:
            print(f'Instance already initialized. Current data: {self.data}')



# ------ Usage ------
s1 = SingletonClassic("Initial data")
print(f"s1 data: {s1.data}")
print(f"s1 id: {id(s1)}")



s2 = SingletonClassic("New data Attempt") # Try to create/get another instance

print(f"s2 data: {s2.data}") # Will show "Initial data" because __init__ logic prevents re-init
print(f"s2 id: {id(s2)}")

print(f"Are s1 and s2 the same object? {id(s1) == id(s2)}") 

s1.data = "Modified data"
print(f"s2 data after s1 modification: {s2.data}")