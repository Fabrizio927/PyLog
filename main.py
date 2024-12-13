#!/usr/bin/env python3

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

from pylog.pylog import log_handler

def main():
    logger = log_handler(log_file='app.log',
                         log_level='DEBUG',
                         logger_name='App Logger',
                         use_utc=True,
                         separator=' - ',
                         terminal_output=False,
                         backup_count=10,
                         mega_byte_split=100,
                         date_format='%Y-%m-%d %H:%M:%S')
    
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

if __name__ == '__main__':
    main()
