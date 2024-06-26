# `pyloggermanager`

The 'pyloggermanager' package is a vital logging framework for Python applications, providing developers with essential
tools to streamline logging operations. Its primary function is to simplify the recording and organization of log
messages, including critical information, debugging messages, errors, and warnings. By offering a centralized interface
and robust functionalities, the package facilitates efficient monitoring and troubleshooting processes.

With its intuitive interface, the pyloggermanager package enables developers to seamlessly integrate logging mechanisms
into their applications. This allows for systematic recording and categorization of log entries based on severity
levels, enhancing readability and prioritization of issues. Moreover, the package offers flexibility in customizing
logging configurations to suit specific project requirements, including formatting, output destinations, and thread
safety.

Beyond technical capabilities, the pyloggermanager package contributes to the reliability and maintainability of Python
applications. It establishes consistent logging practices, simplifying collaboration, code reviews, and issue resolution
across development teams. Overall, the pyloggermanager package is an invaluable asset for developers aiming to implement
robust logging solutions, ensuring efficient and resilient application performance.

## Installation

Logger Manager can be installed using pip:

```bash
pip install pyloggermanager
```

## Usage

```python
import pyloggermanager

# Load configuration
pyloggermanager.load_config()

# Log a debug message
pyloggermanager.debug("This is a debug message.")

# Log an informational message
pyloggermanager.info("This is an informational message.")

# Log a warning message
pyloggermanager.warning("This is a warning message.")

# Log an error message
pyloggermanager.error("This is an error message.")

# Log a critical message
pyloggermanager.critical("This is a critical message.")

# Output
# 2024-03-22 23:37:21 :: INFO :: This is an informational message.
# 2024-03-22 23:37:21 :: WARNING :: This is a warning message.
# 2024-03-22 23:37:21 :: ERROR :: This is an error message.
# 2024-03-22 23:37:21 :: CRITICAL :: This is a critical message.
```

# Documentation

## `pyloggermanager`

#### Methods

- `load_config(file_name='default.log', file_mode='a', level=LogLevel.INFO, format_str=DEFAULT_FORMAT, date_format=DATE_FORMAT, stream=None, handlers=None, colorization=None, encoding='UTF-8')` -
  This function loads the logging configuration based on the provided parameters. It acquires a lock for thread safety,
  configures default handlers if no handlers are specified, configures the formatter and level for each handler, and
  adds the handlers to the root logger. Finally, it releases the lock.
- `disable(level=LogLevel.CRITICAL)` - This function disables logging up to the specified level.
- `critical(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with CRITICAL level.
- `debug(self, message: str, ignore_display: bool = True, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with DEBUG level.
- `error(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with ERROR level.
- `info(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with INFO level.
- `log(self, level: int, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message at the specified level.
- `warning(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with WARNING level.

### `CallerFrame`

The CallerFrame class represents caller details such as class name, file name, function name, module name, and path name
based on the caller's frame information. It provides a method to retrieve caller details from a given frame.

#### Properties

- `class_name`: Represents the name of the class where the function was called.
- `file_name`: Represents the name of the file from which the function was called.
- `function_name`: Represents the name of the function that called the method.
- `module_name`: Represents the name of the module where the function was called.
- `path_name`: Represents the path of the file from which the function was called.

#### Methods

- `__init__()`: Initializes the CallerFrame object with default attribute values.
- `get_caller_details(frame: FrameType) -> CallerFrame`: Retrieves caller details from the given frame.

#### Usage

````python
import pyloggermanager
import inspect


# Assume we have a function where we want to retrieve caller details
def some_function():
    caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())
    print("Caller Class:", caller_frame.class_name)
    print("Caller File:", caller_frame.file_name)
    print("Caller Function:", caller_frame.function_name)
    print("Caller Module:", caller_frame.module_name)
    print("Caller Path:", caller_frame.path_name)


# Now we call the function
some_function()

# Output
# Caller Class: Unknown Class
# Caller File: example
# Caller Function: test_function
# Caller Module: example
# Caller Path: /path/to/example.py
````

### `FileMode`

The FileMode class represents file modes supported by the Python open() function for reading, writing, and appending to
files. It provides methods to retrieve the default file mode, get the file mode mappings, check if a mode is valid, set
the default file mode, and get readable and writable modes.

#### Constants

- `READ`: Represents the read file mode.
- `READ_PLUS`: Represents the read/write file mode.
- `WRITE`: Represents the write file mode.
- `WRITE_PLUS`: Represents the read/write file mode.
- `EXCLUSIVE_CREATE`: Represents the exclusive creation file mode.
- `APPEND`: Represents the append file mode.
- `APPEND_PLUS`: Represents the read/append file mode.
- `BINARY`: Represents the binary file mode.
- `READ_BINARY`: Represents the read binary file mode.
- `READ_WRITE_BINARY`: Represents the read/write binary file mode.
- `TEXT`: Represents the text file mode.
- `UPDATE`: Represents the update file mode.

#### Methods

- `check_mode(mode: str) -> str`: Checks if the provided mode exists and returns the same value if it exists; otherwise,
  raises a ValueError.
- `get_default_mode() -> str`: Returns the default file mode.
- `get_file_mode(mode_str: str) -> str`: Returns the file mode string corresponding to the provided mode name.
- `get_file_modes() -> dict`: Returns a dictionary mapping file mode names to their corresponding strings.
- `get_readable_modes() -> dict`: Returns a dictionary of reading file modes and their corresponding strings.
- `get_writable_modes() -> dict`: Returns a dictionary of writable file modes and their corresponding strings.
- `is_valid_mode(mode: str) -> bool`: Checks if the provided mode string is a valid file mode.
- `set_default_mode(mode: str) -> None`: Sets the default file mode.

#### Usage

````python
# Import the FileMode class
import pyloggermanager

# Check if a mode is valid
mode = 'r'
if pyloggermanager.FileMode.is_valid_mode(mode):
    print(f"The mode '{mode}' is valid.")
else:
    print(f"The mode '{mode}' is invalid.")

# Get default mode
default_mode = pyloggermanager.FileMode.get_default_mode()
print(f"The default mode is: {default_mode}")

# Set default mode
new_default_mode = 'a'
pyloggermanager.FileMode.set_default_mode(new_default_mode)
print(f"New default mode set to: {new_default_mode}")

# Get readable modes
readable_modes = pyloggermanager.FileMode.get_readable_modes()
print("Readable modes:")
for mode_name, mode_str in readable_modes.items():
    print(f"- {mode_name}: {mode_str}")

# Get writable modes
writable_modes = pyloggermanager.FileMode.get_writable_modes()
print("Writable modes:")
for mode_name, mode_str in writable_modes.items():
    print(f"- {mode_name}: {mode_str}")

# Output
# The mode 'r' is valid.
# The default mode is: a
# New default mode set to: a
# Readable modes:
# - READ: r
# - READ_PLUS: r+
# - WRITE_PLUS: w+
# - APPEND_PLUS: a+
# Writable modes:
# - WRITE: w
# - WRITE_PLUS: w+
# - APPEND: a
# - APPEND_PLUS: a+
````

### `Lock`

The Lock class provides a simple interface to manage locks using the Python threading module. It allows acquiring,
creating, checking if a lock is locked, and releasing locks.

#### Methods

- `acquire(name: str, blocking: bool = True, timeout: float = -1) -> bool`: Acquires the lock with the given name.
- `create(name: str) -> None`: Creates a new lock with the given name.
- `generate_name(length: int = 10) -> str`: Generates a random name for a lock of specified length.
- `locked(name: str) -> bool`: Checks if the lock with the given name is currently locked.
- `release(name: str) -> None`: Releases the lock with the given name.

#### Usage

````python
# Import the Lock class
import pyloggermanager
import threading
import time


# Define a function to perform an action using a lock
def perform_action(lock_name):
    print(f"Thread {threading.current_thread().name} attempting to acquire lock {lock_name}")
    if pyloggermanager.Lock.acquire(lock_name, timeout=3):
        print(f"Thread {threading.current_thread().name} acquired lock {lock_name}")
        time.sleep(2)  # Simulating some action being performed
        pyloggermanager.Lock.release(lock_name)
        print(f"Thread {threading.current_thread().name} released lock {lock_name}")
    else:
        print(f"Thread {threading.current_thread().name} couldn't acquire lock {lock_name}")


# Create locks
lock1_name = pyloggermanager.Lock.generate_name()
lock2_name = pyloggermanager.Lock.generate_name()
pyloggermanager.Lock.create(lock1_name)
pyloggermanager.Lock.create(lock2_name)

# Spawn threads to perform actions using locks
thread1 = threading.Thread(target=perform_action, args=(lock1_name,))
thread2 = threading.Thread(target=perform_action, args=(lock2_name,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Output
# Thread Thread-1 (perform_action) attempting to acquire lock nzlggljagd
# Thread Thread-2 (perform_action) attempting to acquire lock mbsvxfocxdThread Thread-1 (perform_action) acquired lock nzlggljagd
# 
# Thread Thread-2 (perform_action) acquired lock mbsvxfocxd
# Thread Thread-1 (perform_action) released lock nzlggljagdThread Thread-2 (perform_action) released lock mbsvxfocxd
````

### `LogLevel`

The LogLevel class represents different log levels used in logging systems. It provides methods to check if a log level
is valid, get the default log level, get log level mappings, remove log levels, set the default log level, and set
custom log levels.

#### Constants

- `DEBUG`: Constant representing the debug log level (integer: 10)
- `INFO`: Constant representing the info log level (integer: 20)
- `WARNING`: Constant representing the warning log level (integer: 30)
- `ERROR`: Constant representing the error log level (integer: 40)
- `CRITICAL`: Constant representing the critical log level (integer: 50)

#### Methods

- `check_level(level: int) -> int`: Checks if the provided level exists and returns the same value if exists, else
  raises ValueError.
- `get_default_level() -> str`: Returns the default log level as a string.
- `get_level(level: int | str) -> str | int`: Returns the log level name if an integer level is provided, or returns the
  log level integer if a string level is provided.
- `get_levels() -> dict`: Returns a dictionary mapping log level integers to their corresponding names, sorted by level.
- `get_next_level(current_level: int) -> int | None`: Returns the next log level integer after the provided current
  level, or None if it is the highest level.
- `get_previous_level(current_level: int) -> int | None`: Returns the previous log level integer before the provided
  current level, or None if it is the lowest level.
- `is_valid_level(level: int | str) -> bool`: Checks if the provided log level (integer or string) is a valid log level.
- `remove_level(level: int | str) -> None`: Removes the log level mapping for the specified level.
- `set_default_level(level: int | str) -> None`: Sets the default log level based on the provided integer or string
  level.
- `set_level(level: int, level_name: str) -> None`: Sets a custom log level with the provided level integer and name.

#### Usage

````python
# Import the LogLevel class
import pyloggermanager

# Check if a log level is valid
print(pyloggermanager.LogLevel.is_valid_level(pyloggermanager.LogLevel.DEBUG))  # Output: True

# Get default log level
print(pyloggermanager.LogLevel.get_default_level())  # Output: INFO

# Get log level mappings
print(
    pyloggermanager.LogLevel.get_levels())  # Output: {10: 'DEBUG', 20: 'INFO', 30: 'WARNING', 40: 'ERROR', 50: 'CRITICAL'}

# Set default log level
pyloggermanager.LogLevel.set_default_level(pyloggermanager.LogLevel.WARNING)
print(pyloggermanager.LogLevel.get_default_level())  # Output: WARNING

# Set custom log level
pyloggermanager.LogLevel.set_level(15, 'CUSTOM')
print(pyloggermanager.LogLevel.get_level(15))  # Output: 'CUSTOM'

# Remove log level
pyloggermanager.LogLevel.remove_level('CUSTOM')
print(pyloggermanager.LogLevel.get_level(15))  # Output: 'Level 15'
````

### `Record`

The Record class represents a log record with various attributes such as message, logger name, level name, caller frame
information, execution information, stack information, and thread/process details. It provides methods to serialize the
record to a dictionary and JSON format.

#### Properties

- `time`: Property representing the timestamp of the log record.
- `message`: Property representing the log message.
- `logger_name`: Property representing the name of the logger.
- `level_number`: Property representing the numeric value of the log level.
- `level_name`: Property representing the name of the log level.
- `file_name`: Property representing the name of the file where the log occurred.
- `class_name`: Property representing the name of the class where the log occurred.
- `function_name`: Property representing the name of the function/method where the log occurred.
- `module_name`: Property representing the name of the module where the log occurred.
- `path_name`: Property representing the path of the file where the log occurred.
- `exec_info`: Property representing the execution information associated with the log record.
- `stack_info`: Property representing the stack information associated with the log record.
- `thread`: Property representing the thread ID associated with the log record.
- `thread_name`: Property representing the name of the thread associated with the log record.
- `process_id`: Property representing the process ID associated with the log record.

#### Methods

- `__init__(message: str, logger_name: str, level_number: int, caller_frame: CallerFrame, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: Optional[str] = None) -> None`:
  Constructs a new 'Record' object with the provided parameters.
- `json_serializer(obj: Any) -> Union[str, None]`: Static method to serialize objects to JSON format.
- `to_dict() -> dict`: Converts the 'Record' object to a dictionary.
- `to_json() -> str`: Converts the 'Record' object to JSON string.

#### Usage

````python
# Import the Record class
import inspect
import pyloggermanager

# Create a CallerFrame object (Assuming it's defined elsewhere)
caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())

# Create a new Record object
record = pyloggermanager.Record(
    message="An example log message",
    logger_name="example_logger",
    level_number=20,
    caller_frame=caller_frame,
    exec_info=(ValueError, ValueError("An example error occurred"), None),
    stack_info="Stack trace information"
)

# Access properties of the Record object
print(record.message)  # Output: An example log message
print(record.level_name)  # Output: INFO
print(record.file_name)  # Output: example

# Serialize the Record object to a dictionary
record_dict = record.to_dict()
print(record_dict)
# Output: {
#     'time': datetime.datetime(2024, 3, 22, 23, 41, 47, 604552),
#     'message': 'An example log message',
#     'logger_name': 'example_logger',
#     'level_name': 'INFO',
#     'level_number': 20,
#     'file_name': 'example',
#     'class_name': 'ExampleClass',
#     'function_name': 'example_function',
#     'module_name': 'example',
#     'path_name': 'example_path',
#     'exec_info': (<class 'ValueError', ValueError('An example error occurred'), None),
#     'stack_info': 'Stack trace information',
#     'thread': 12345,
#     'thread_name': 'MainThread',
#     'process_id': 67890 
# }

# Serialize the Record object to JSON format
json_string = record.to_json()
print(json_string)
# Output:
# {
#     "time": "2024-03-22T23:41:47.604552",
#     "message": "An example log message",
#     "logger_name": "example_logger",
#     "level_name": "INFO",
#     "level_number": 20,
#     "file_name": "example",
#     "class_name": "ExampleClass",
#     "function_name": "example_function",
#     "module_name": "example",
#     "path_name": "example_path",
#     "exec_info": [
#         "ValueError",
#         "An example error occurred",
#         null
#     ],
#     "stack_info": "Stack trace information",
#     "thread": 12345,
#     "thread_name": "MainThread",
#     "process_id": 67890
# }
````

### `Logger`

The Logger class represents a logger object with various attributes and methods for logging messages.

#### Properties

- `cache`: Gets or sets the cache dictionary.
- `disabled`: Indicates whether the logger is disabled or not.
- `handlers`: The list of handlers associated with the logger.
- `level`: The logging level of the logger.
- `lock_name`: Gets or sets the name of the lock used for thread safety.
- `manager`: The manager associated with the logger.
- `name`: The name of the logger.
- `parent`: The parent logger in the logger hierarchy.
- `root`: The root logger associated with the logger hierarchy.

#### Methods

- `__init__(self, name: str, level: int = LogLevel.INFO) -> None`: Initializes a new Logger object.
- `add_handler(self, handler: Handler) -> None`: Adds a handler to the logger's list of handlers after acquiring the
  lock.
- `call_handlers(self, record: Record, ignore_display: bool) -> None`: Calls the handlers associated with the logger.
- `critical(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with CRITICAL level.
- `debug(self, message: str, ignore_display: bool = True, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with DEBUG level.
- `error(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with ERROR level.
- `find_caller(self, stack_info: bool = False, stack_level: int = 1) -> Tuple[CallerFrame, str]`: Finds the caller frame
  and optionally collects stack information.
- `get_child(self, suffix: str) -> 'Logger'`: Get a child logger with the specified suffix.
- `get_effective_level(self) -> int`: Retrieves the effective log level for the logger.
- `handle(self, record: Record, ignore_display: bool) -> None`: Handles the given log record by calling its handlers if
  the logger is not disabled.
- `has_handlers(self) -> bool`: Checks if the logger or any of its ancestors have handlers.
- `info(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with INFO level.
- `is_enabled_for(self, level: int) -> bool`: Checks if logging is enabled for the specified log level.
- `log(self, level: int, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message at the specified level.
- `make_record(self, name: str, level: int, message: str, caller_frame: Optional[CallerFrame] = None, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: Optional[str] = None) -> Record`:
  Creates a Record object with specified attributes.
- `remove_handler(self, handler: Handler) -> None`: Removes a handler from the logger's list of handlers after acquiring
  the lock.
- `warning(self, message: str, ignore_display: bool = False, exec_info: Optional[Tuple[Type, BaseException, Optional[TracebackType]]] = None, stack_info: bool = False, stack_level: int = 1) -> None`:
  Logs a message with WARNING level.

#### Usage

````python
# Importing the necessary modules
import pyloggermanager
from pyloggermanager.handlers import ConsoleHandler

# Sample usage of the Logger class
# Creating a logger instance
logger = pyloggermanager.Logger("example_logger")

# Adding a handler
handler = ConsoleHandler()
logger.add_handler(handler)

# Logging messages
logger.info("This is an informational message.\n")
logger.error("An error occurred.")

# Removing the handler
logger.remove_handler(handler)

# Output
# 2024-03-22 23:45:14 :: INFO :: This is an informational message.
# 2024-03-22 23:45:14 :: ERROR :: An error occurred.
````

### `Manager`

The Manager class manages loggers and their settings within a logging hierarchy.

#### Properties

- `disable`: Gets or sets the level at which logging is disabled.
- `lock_name`: Gets or sets the name of the lock used for thread safety.
- `logger_class`: Gets or sets the logger class used for creating logger instances.
- `logger_dict`: Gets or sets the dictionary mapping logger names to their instances.
- `record_factory`: Gets or sets the factory used for creating log records.
- `root`: Gets or sets the root logger of the logging hierarchy.

#### Methods

- `__init__(self, root_node: Logger) -> None`: Initializes the Manager with a root logger.
- `clear_cache(self) -> None`: Clears the cache for all loggers and the root logger.
- `get_logger(self, name: str) -> Logger`: Retrieves a logger with the specified name. If the logger does not exist, it
  creates a new logger.
- `set_logger(self, logger: Logger) -> None`: Sets the logger class to be used for creating new loggers.

#### Usage

````python
# Importing the necessary modules
import pyloggermanager

# Create a root logger
root_logger = pyloggermanager.Logger("root")

# Create a manager with the root logger
manager = pyloggermanager.Manager(root_logger)

# Set the level at which logging is disabled
manager.disable = 20

# Get a logger named 'example_logger'
example_logger = manager.get_logger("example_logger")

# Set the logger class
manager.set_logger(example_logger)

# Clear the cache for all loggers and the root logger
manager.clear_cache()
````

### `Registry`

The Registry class serves as a registry to store and manage instances of the Logger class.

#### Properties

- `logger_map`: Gets or sets the dictionary mapping loggers to their associated values.

#### Methods

- `__init__(self, logger: Logger) -> None`: Initializes the Registry with a single logger.
- `append(self, logger: Logger) -> None`: Adds a new logger to the registry.

#### Usage

````python
# Importing the necessary modules
import pyloggermanager

# Create a logger
logger = pyloggermanager.Logger("example_logger")

# Create a registry with the logger
registry = pyloggermanager.Registry(logger)

# Append a new logger to the registry
new_logger = pyloggermanager.Logger("new_logger")
registry.append(new_logger)

# Get the logger map
logger_map = registry.logger_map
````

### `RootLogger`

The RootLogger class represents the root logger in a logging hierarchy. It inherits from the Logger class and
initializes itself with the name 'root' and the specified log level. The root logger serves as the ancestor of all other
loggers in the logging hierarchy.

#### Methods

- `__init__(self, level: int) -> None`: Constructs a new RootLogger object with the specified log level.

## `pyloggermanager.formatters`

The 'pyloggermanager.formatters' package provides classes for formatting log messages in various formats within the
logger manager framework. It includes implementations for formatting log messages as CSV (Comma-Separated Values),
JSON (JavaScript Object Notation), and the default text format.

Below listed formatter classes enable users to customize the appearance and structure of log messages according to their
requirements. By supporting different formats such as CSV and JSON, users have the flexibility to choose the most
suitable format for their logging needs, whether it's for human-readable output, structured data storage, or integration
with external systems.

Overall, the 'pyloggermanager.formatters' package enhances the logger manager framework by offering versatile formatting
options for log messages, catering to a wide range of logging use cases and preferences.

#### Constants

- `DEFAULT_FORMAT` (str): The default format string used for log message formatting.
- `CSV_FORMAT` (str): The format string used for CSV log message formatting.
- `JSON_FORMAT` (str): The format string used for JSON log message formatting.
- `DATE_FORMAT` (str): The default date format string used for log message formatting.

### `Formatter`

Base class for log record formatters. It allows customization of log message format. Subclasses must implement the
format method to customize log message formatting.

| Placeholder         | Description                                                                             |
|---------------------|-----------------------------------------------------------------------------------------|
| `%(time)s`          | The time at which the log record was created, formatted using `date_format`.            |
| `%(message)s`       | The message associated with the log record.                                             |
| `%(logger_name)s`   | The name of the logger.                                                                 |
| `%(level_name)s`    | The name of the logging level (e.g., INFO, WARNING).                                    |
| `%(level_number)d`  | The numeric value of the logging level.                                                 |
| `%(file_name)s`     | The name of the file from which the logging call was made.                              |
| `%(class_name)s`    | The name of the class containing the logging call.                                      |
| `%(function_name)s` | The name of the function/method containing the logging call.                            |
| `%(module_name)s`   | The name of the module containing the logging call.                                     |
| `%(path_name)s`     | The full pathname of the source file.                                                   |
| `%(exec_info)s`     | The formatted traceback information if an exception was raised during the logging call. |
| `%(stack_info)s`    | The stack information at the time of the logging call.                                  |
| `%(thread)d`        | The thread ID.                                                                          |
| `%(thread_name)s`   | The name of the thread.                                                                 |
| `%(process_id)d`    | The ID of the process.                                                                  |

#### Methods

- `__init__(format_str: str | dict = DEFAULT_FORMAT, date_format: str = DATE_FORMAT)`: Initializes the Formatter object.
- `format(record: 'Record') -> str`: Formats the log record into a string based on the provided record object.
- `format_time(value: time.struct_time, date_format: str) -> str`: Formats the provided time value into a string using
  the specified date format.
- `format_exception(exec_info: Optional[Tuple[Type[BaseException], BaseException, Optional[TracebackType]]] = None) -> str`:
  Formats the exception information into a string.

### `DefaultFormatter`

Custom formatter for log records. It allows customization of log record formatting using a specified format string.
Replaces tokens in the format string with corresponding values from the log record.

#### Methods

- `__init__(format_str: str = DEFAULT_FORMAT, date_format: str = DATE_FORMAT)`: Initializes a 'DefaultFormatter'
  instance with the specified format string.
- `format(record: 'Record') -> str`: Formats the given log record according to the format string.

#### Usage

````python
import inspect
import pyloggermanager
from pyloggermanager.formatters import DefaultFormatter

caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())

# Create a log record
record = pyloggermanager.Record(
    message="This is a log message",
    logger_name="example_logger",
    level_number=20,
    caller_frame=caller_frame,
    exec_info=None,
    stack_info=None
)

# Create a DefaultFormatter instance
formatter = DefaultFormatter()

# Format the log record
formatted_message = formatter.format(record)
print(formatted_message)

# Output: '2024-03-22 15:30:45 :: INFO :: This is a log message'
````

### `CSVFormatter`

Subclass of the 'Formatter' class for formatting log records in CSV format. It allows customization of the format string
used for formatting log records.

#### Methods

- `__init__(format_str: str = CSV_FORMAT, date_format: str = DATE_FORMAT)`: Initializes a 'CSVFormatter' object with the
  specified format string.
- `format(record: 'Record') -> str`: Formats the given log record into a CSV string based on the specified format
  string.

#### Usage

````python
import inspect
import pyloggermanager
from pyloggermanager.formatters import CSVFormatter

caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())

# Create a log record
record = pyloggermanager.Record(
    message="This is a log message",
    logger_name="example_logger",
    level_number=20,
    caller_frame=caller_frame,
    exec_info=None,
    stack_info=None
)

# Create a CSVFormatter instance
formatter = CSVFormatter()

# Format the log record as CSV
formatted_message = formatter.format(record)
print(formatted_message)

# Output: '2024-03-22 23:46:41,INFO,This is a log message'
````

### `JSONFormatter`

Subclass of the 'Formatter' class for formatting log records into JSON format. It provides methods to initialize the
formatter with a custom format string, format log records into JSON strings, and handle JSON decoding errors.

#### Methods

- `__init__(format_str: dict = None, date_format: str = DATE_FORMAT)`: Initializes the JSONFormatter object with a
  custom format string.
- `format(record: 'Record') -> str`: Formats the given log record into a JSON string.

#### Usage

````python
import inspect
import pyloggermanager
from pyloggermanager.formatters import JSONFormatter

caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())

# Create a log record
record = pyloggermanager.Record(
    message="This is a log message",
    logger_name="example_logger",
    level_number=20,
    caller_frame=caller_frame,
    exec_info=None,
    stack_info=None
)

# Create a JSONFormatter instance
formatter = JSONFormatter()

# Format the log record as JSON
formatted_message = formatter.format(record)
print(formatted_message)

# Output:
# {
#     "time": "2024-03-22 23:47:03",
#     "levelName": "INFO",
#     "message": "This is a log message"
# }
````

## `pyloggermanager.handlers`

The 'pyloggermanager.handlers' package provides classes responsible for handling log records generated within the logger
manager framework. It includes various handlers for processing log messages, directing them to different destinations,
and performing actions based on logging levels.

Below listed handler classes offer flexibility and customization options for managing log records within the logger
manager framework. They enable users to define how log messages are processed, where they are directed, and how they are
formatted, catering to various logging scenarios and deployment environments.

Overall, the 'pyloggermanager.handlers' package enhances the functionality of the logger manager framework by providing
a robust set of handlers for managing log records effectively and efficiently. Users can choose and configure handlers
based on their specific logging needs and infrastructure requirements.

### `Handler`

The Handler class is a base class for different log handlers used in logging systems. It provides methods and properties
to manage handler attributes such as name, log level, colorization, and formatter. Additionally, it includes methods to
acquire/release locks, close the handler, emit log records, format log records, flush buffered records, and retrieve a
list of all handlers.

#### Properties

- `colorization`: Gets or sets the colorization object for the handler.
- `formatter`: Gets or sets the formatter object for formatting log records.
- `level`: Gets or sets the log level for the handler.
- `name`: Gets or sets the name of the handler.

#### Methods

- `__init__(name: str = None, level: int = 20, colorization: pycolorecho.ColorMapper = None, formatter: Formatter = DefaultFormatter())` -
  Initializes the handler with optional attributes.
- `close()`: Closes the handler.
- `emit(record: 'Record', ignore_display: bool) -> None`: Abstract method to emit a log record.
- `format(record: 'Record') -> str`: Formats a log record using the handler's formatter.
- `flush()`: Flushes buffered records.
- `get_handlers() -> list[Any]`: Retrieves a list of all handlers.
- `handle(record: 'Record', ignore_display: bool) -> None`: Handles a log record.

#### Usage

````python
from pyloggermanager.formatters import Formatter
from pyloggermanager.handlers import Handler


# Create a custom formatter
class CustomFormatter(Formatter):
    def format(self, record):
        return f"[{record.level_name}] {record.message}"


# Create a handler with custom formatter
handler = Handler(formatter=CustomFormatter())
````

### `ConsoleHandler`

The ConsoleHandler class is a subclass of Handler representing a handler that writes log records to the console. It
provides methods to set and retrieve the stream used for logging, close the stream, emit log records, and flush the
stream.

#### Properties

- `stream`: Gets or sets the stream of the handler.

#### Methods

- `__init__(name: str = None, level: int = 20, colorization: pycolorecho.ColorMapper = None, formatter: Formatter = DefaultFormatter(), stream: Stream = TerminalStream())` -
  Initializes a ConsoleHandler instance with optional attributes
- `close()`: Closes the stream if it has a close method.
- `emit(record: 'Record', ignore_display: bool = True) -> None`: Emits the log record by formatting it, colorizing the
  message, and writing it to the stream.
- `flush()`: Flushes the stream if it has a flush method.

#### Usage

````python
import inspect
import pyloggermanager
from pyloggermanager.handlers import ConsoleHandler

# Create a console handler
console_handler = ConsoleHandler()

caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())

# Emit a log record
console_handler.emit(pyloggermanager.Record(
    message="This is a log message",
    logger_name='TestLogger',
    level_number=20,
    caller_frame=caller_frame
))

# Output
# 2024-03-22 23:47:35 :: INFO :: This is a log message
````

### `StreamHandler`

The StreamHandler class is a subclass of Handler representing a handler that emits log records to a stream. It provides
methods to set the log level, formatter, and stream, as well as to emit log records and flush the stream.

#### Properties

- `stream`: Gets or sets the stream of the handler.

#### Methods

- `__init__(name: str = None, level: int = 20, colorization: pycolorecho.ColorMapper = None, formatter: Formatter = DefaultFormatter(), stream: Stream = StdoutStream())` -
  Initializes a StreamHandler instance with optional attributes.
- `close()`: Closes the stream if it has a close method.
- `emit(record: 'Record', ignore_display: bool) -> None`: Emits a log record to the stream.
- `flush()`: Flushes the stream if it has a flush method.

#### Usage

````python
import inspect
import pyloggermanager
from pyloggermanager.handlers import StreamHandler

# Create a stream handler
stream_handler = StreamHandler()

caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())

# Emit a log record
stream_handler.emit(pyloggermanager.Record(
    message="This is a log message",
    logger_name='TestLogger',
    level_number=20,
    caller_frame=caller_frame
), ignore_display=True)

# Output
# 2024-03-22 23:48:13 :: INFO :: This is a log message
````

### `FileHandler`

The FileHandler class is a subclass of Handler responsible for handling log records by writing them to a file. It allows
customization of various parameters such as file name, file mode, encoding, etc.

#### Properties

- `encoding`: Gets or sets the encoding of the handler.
- `filemode`: Gets or sets the file mode for opening the file handler.
- `filename`: Gets or sets the file name of the handler.

#### Methods

- `__init__(name: str = None, level: int = 20, colorization: pycolorecho.ColorMapper = None, formatter: Formatter = DefaultFormatter(), file_name: str = 'default.log', file_mode: str = 'a', encoding: str = 'UTF-8')` -
  Initializes a FileHandler object with optional attributes.
- `close()`: Closes the file stream used for writing log records.
- `emit(record: 'Record', ignore_display: bool) -> None`: Emits a log record by writing it to the log file.
- `flush()`: Flushes the file stream used for writing log records.

#### Usage

````python
import inspect
import pyloggermanager
from pyloggermanager.handlers import FileHandler

# Create a file handler
file_handler = FileHandler(file_name='app.log', encoding='utf-8')

caller_frame = pyloggermanager.CallerFrame.get_caller_details(inspect.currentframe())

# Emit a log record
file_handler.emit(pyloggermanager.Record(
    message="This is a log message",
    logger_name='TestLogger',
    level_number=20,
    caller_frame=caller_frame
), ignore_display=False)

# Output
# 2024-03-22 23:48:30 :: INFO :: This is a log message
````

### `StderrHandler`

The StderrHandler class is a subclass of Handler responsible for handling log records by writing them to the standard
error stream (stderr).

#### Properties

- `stream`: Gets the standard error stream (stderr).

#### Methods

- `__init__(self, level: int = 30)` - Initializes a StderrHandler object with an optional log level.

## `pyloggermanager.streams`

The 'pyloggermanager.streams' package provides classes related to handling output streams for log records within the
logger manager framework. These classes define different types of streams that log messages can be directed to, allowing
for flexible and customizable logging behaviour.

Below listed stream classes offer versatility in directing log messages to different output channels, allowing users to
customize logging behavior based on their application's requirements and environment configuration. By supporting
various stream types, the logger manager framework enables users to control where log records are displayed or stored,
facilitating effective logging and troubleshooting processes.

Overall, the 'pyloggermanager.streams' package enhances the functionality of the logger manager framework by providing a
range of stream classes for directing log messages to different output channels. Users can leverage these classes to
tailor their logging setup to suit their specific needs and preferences, ensuring efficient management and processing of
log records.

### `Stream`

The Stream class is an abstract base class representing an output stream. It defines two abstract methods: write() and
flush(), which must be implemented by subclasses.

#### Methods

- `write(message: str) -> None`: Abstract method to write the given message to the stream.
- `flush() -> None`: Abstract method to flush the stream, ensuring all buffered data is written.

### `StdoutStream`

The StdoutStream class is a subclass of Stream representing a stream that writes messages to the standard output (
sys.stdout). It overrides the write and flush methods inherited from the Stream class.

#### Methods

- `write(message: str) -> None`: Writes the given message to the standard output (sys.stdout).
- `flush() -> None`: Flushes the output buffer of the standard output (sys.stdout), ensuring all buffered data is
  written.

#### Usage

````python
from pyloggermanager.streams import StdoutStream

# Create an instance of StdoutStream
stdout_stream = StdoutStream()

# Write a message to stdout
stdout_stream.write("This is a message to stdout\n")

# Flush stdout buffer
stdout_stream.flush()

# Output
# This is a message to stdout
````

### `StderrStream`

The StderrStream class is a subclass of Stream representing a stream for writing messages to the standard error (
sys.stderr) output. It overrides the write and flush methods inherited from the Stream class.

#### Methods

- `write(message: str) -> None`: Writes the provided message to the standard error (sys.stderr) output.
- `flush() -> None`: Flushes the standard error (sys.stderr) buffer.

#### Usage

````python
from pyloggermanager.streams import StderrStream

# Create an instance of StderrStream
stderr_stream = StderrStream()

# Write a message to stderr
stderr_stream.write("This is an error message to stderr\n")

# Flush stderr buffer
stderr_stream.flush()

# Output
# This is an error message to stderr
````

### `TerminalStream`

The TerminalStream class is a subclass of Stream representing a stream for writing messages to the terminal. It
overrides the write and flush methods inherited from the Stream class.

#### Methods

- `write(message: str) -> None`: Writes the provided message to the terminal.
- `flush() -> None`: Flushes the output buffer, but does nothing for the terminal stream since output is immediately
  displayed.

#### Usage

````python
from pyloggermanager.streams import TerminalStream

# Create an instance of TerminalStream
terminal_stream = TerminalStream()

# Write a message to the terminal
terminal_stream.write("This is a message to the terminal\n")

# Flush the terminal buffer (No operation required)
terminal_stream.flush()

# Output
# This is a message to the terminal
````

# Text Styles

For text colorization and styling, this package utilizes the `pycolorecho` package. You can find additional details
about its usage and features by following this
link: [pycolorecho](https://github.com/coldsofttech/pycolorecho/blob/main/README.md) package.

# License

Please refer to the [MIT license](LICENSE) within the project for more information.

# Contributing

We welcome contributions from the community! Whether you have ideas for new features, bug fixes, or enhancements, feel
free to open an issue or submit a pull request on [GitHub](https://github.com/coldsofttech/pyloggermanager).