'''PyLog
--------
Author: Fabrizio Traina (Fabrizio927)
email:  fabrizio.traina@hotmail.it
GitHub: https://github.com/Fabrizio927/PyLog
Version: 1.0

License
-------
THE BEERWARE LICENSE (Revision 42):
Fabrizio Traina <fabrizio.traina@hotmail.it> wrote this code. As long as you 
retain this notice, you can do whatever you want with this stuff. If we meet 
some day, and you think this stuff is worth it, you can buy me a beer in 
return. Cheers!
'''

import logging
import time
from logging.handlers import RotatingFileHandler


def log_handler(log_file='app.log',
                log_level='INFO',
                logger_name='App Logger',
                use_utc=False,
                separator=' - ',
                terminal_output=False,
                backup_count=10,
                mega_byte_split=100,
                date_format='%Y-%m-%d %H:%M:%S') -> logging.Logger:
    """
    Configures and returns a logger with options for file logging, terminal
    output, and log file rotation.

    Parameters:
        log_file (str): The name of the log file. Default is 'app.log'.
        log_level (str): The logging level to be set for the logger. It can be
            either 'DEBUG' or 'INFO'. Default is 'INFO'.
        logger_name (str): The name of the logger. Default is 'App Logger'.
        use_utc (bool): Whether to use UTC time zone for log timestamps.
            Default is False.
        separator (str): The separator to use between different parts of the
            log message. Default is ' - '.
        terminal_output (bool): Whether to enable output to the terminal.
            Default is False.
        backup_count (int): The number of backup log files to keep when
            rotating log files. Default is 10.
        mega_byte_split (int): The size (in megabytes) at which to split log
            files. Default is 100.
        date_format (str): The format string for log timestamps. Default is
            '%Y-%m-%d %H:%M:%S'.

    Returns:
        logging.Logger: A configured logger object.

    Example:
        # Configure logger to log to 'my_app.log', enable terminal output,
            use UTC time zone for log timestamps, and use a custom separator
        logger = log_handler(log_file='my_app.log', log_level='INFO',
                             use_utc=True, terminal_output=True,
                             separator=' | ')
        logger.info('This is an info message')
    """

    # Configure logging formatter
    message_format = '%(asctime)s' + separator + \
                     '%(levelname)s' + separator + \
                     '%(message)s'
    log_formatter = logging.Formatter(message_format, datefmt=date_format)

    # File handler
    file_size = 1024 * 1024 * mega_byte_split
    file_handler = RotatingFileHandler(log_file,
                                       maxBytes=file_size,
                                       backupCount=backup_count)
    file_handler.setFormatter(log_formatter)

    # Configure logger
    logger = logging.getLogger(logger_name)
    if log_level.upper() == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logger.addHandler(file_handler)

    if terminal_output:
        # Stream handler (for terminal output)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)
        logger.addHandler(stream_handler)

    if use_utc:
        logging.Formatter.converter = time.gmtime

    return logger
