# This entire file acts as the singleton

_log_messages = []
_initialized = False


def initialize_logger(config):
    global _initialized

    if not _initialized:
        print(f"Initializing logger with config: {config}")
        _initialized = True

    else:
        print("Logger already initialized")



def log_message(message):
    if not _initialized:
        initialize_logger({"default_level": "INFO"})
        print("Logger was not initialized, using defaults.")
    
    _log_messages.append(message)

    print(f"LOG: {message}")


def get_all_logs():
    return _log_messages



# You define your state (e.g., _log_messages) and functions at the module level.
# When you import logger_singleton, you get access to these
# Every past of your application that imports logger_singleton gets the same module object and thus shares the same state and functions.