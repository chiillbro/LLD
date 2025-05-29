import module_singleton as logger_singleton

def do_something_and_log():
    logger_singleton.log_message("Log from utils.do_something_and_log")