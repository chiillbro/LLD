import module_singleton as my_logger
from utils import do_something_and_log


my_logger.initialize_logger({"level": "DEBUG", "file": "app.log"})
my_logger.log_message("Application Started.")
my_logger.log_message("User performed an action.")

do_something_and_log()

print(my_logger.get_all_logs())
