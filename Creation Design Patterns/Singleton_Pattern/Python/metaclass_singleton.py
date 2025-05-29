class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            print(f"Creating new instance via Metaclass for {cls.__name__}")
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] =instance
        else:
            print(f"Returning existing instance via Metaclass for {cls.__name__}")

        return cls._instances[cls]
    


class Logger(metaclass=SingletonMeta):
    def __init__(self, name="DefaultLogger"):
        print(f"Logger {name} __init__ called")
        self.name = name
        self.messages = []
    

    def log(self, message):
        self.messages.append(message)
        print(f"[{self.name}] LOG: {message}")


class ConfigManager(metaclass=SingletonMeta):
    def __init__(self, config_file="settings.ini"):
        print(f"ConfigManager using {config_file} __init__ called")
        self.settings = {"db_host": "localhost", "port": 5432} # load from file
    

    def get_setting(self, key):
        return self.settings[key]




# ----- Usage ------

logger1 = Logger("AppLogger")
logger1.log("Application Started.")

logger2 = Logger("AnotherLoggerAttempt") # Will get the same "AppLogger" instance

logger2.log("Another log.") # Logged by "AppLogger" instance
print(f"logger1 is logger2: {logger1 is logger2}") # True
print(f"Logger1 name: {logger1.name}, Logger2 name: {logger2.name}") # logger1 name: AppLogger, Logger2 name: AppLogger


config1 = ConfigManager("prod.ini")

print(f"DB HOST from config1: {config1.get_setting('db_host')}")

config2 = ConfigManager("dev.ini")
print(f"DB HOST from config2: {config2.get_setting('db_host')}")
print(f"config1 is config2: {config1 is config2}") # True

print(f"Singleton instances created: {SingletonMeta._instances}")



# The metaclass SingletonMeta overrides the __call__ method. When you try to instantiate Logger() or ConfigManager(), it's actually SingletonMeta.__call__ that gets executed.

# It maintains a dictionary _instances mapping classes to their single instance
 
 # This ensures __init__ of Logger or ConfigManager is truly called only once.