# PyLog

**PyLog** is a configurable logging utility for Python, designed for 
flexibility and ease of use. It enables you to log messages to a file with 
rotation, customize log message formatting, output logs to the terminal, and 
use UTC timestamps.

## Features

- **Log Rotation**: Automatically splits log files when they reach a specified 
size.
- **Terminal Output**: Optionally logs messages to the terminal alongside the 
log file.
- **Custom Formatting**: Fully customizable log message format, including 
separators and timestamp formatting.
- **UTC Support**: Optionally formats log timestamps in UTC.
- **Backup Logs**: Maintains a specified number of backup log files.

## Usage

### Import and Configure the Logger

```python
from pylog import log_handler

# Configure logger
logger = log_handler(
    log_file='app.log',           # Log file name
    log_level='INFO',             # Logging level: 'DEBUG' or 'INFO'
    logger_name='PyLog Logger',   # Name of the logger
    use_utc=True,                 # Use UTC timestamps
    separator=' | ',              # Separator for log messages
    terminal_output=True,         # Output logs to the terminal
    backup_count=5,               # Keep 5 backup log files
    megabyte_split=50,            # Split log file at 50MB
    date_format='%Y-%m-%d %H:%M:%S' # Timestamp format
)

# Log a message
logger.info('This is an informational message.')
```

### Output Example

A typical log message might look like this:

```
2024-12-06 12:34:56 | INFO | This is an informational message.
```

## Parameters

| Parameter       | Description                                                                 | Default                |
|------------------|-----------------------------------------------------------------------------|------------------------|
| `log_file`      | Name of the log file.                                                      | `'app.log'`            |
| `log_level`     | Logging level (`'DEBUG'` or `'INFO'`).                                      | `'INFO'`               |
| `logger_name`   | Name of the logger.                                                        | `'PyLog Logger'`       |
| `use_utc`       | Whether to use UTC timestamps.                                             | `False`                |
| `separator`     | Separator between log message components.                                  | `' - '`                |
| `terminal_output` | Whether to output logs to the terminal.                                  | `False`                |
| `backup_count`  | Number of backup log files to keep.                                         | `10`                   |
| `megabyte_split` | Log file size in MB before splitting.                                      | `100`                  |
| `date_format`   | Timestamp format for log messages.                                         | `'%Y-%m-%d %H:%M:%S'`  |

## Requirements

- Python 3.6 or later

## Installation

Clone the repository and import the script into your project:

```
git clone https://github.com/Fabrizio927/PyLog.git
```

Then, import and use it as shown in the examples.

## License

**PyLog** is licensed under the Beerware License (Revision 42):

```
THE BEERWARE LICENSE (Revision 42):
Fabrizio Traina <fabrizio.traina@hotmail.it> wrote this code. As long as you 
retain this notice, you can do whatever you want with this stuff. If we meet 
some day, and you think this stuff is worth it, you can buy me a beer in 
return. Cheers!
```

---

## Author


[Fabrizio Traina](https://github.com/Fabrizio927) 
📧 fabrizio.traina@hotmail.it  


---

Happy Logging with **PyLog**! 🍻

