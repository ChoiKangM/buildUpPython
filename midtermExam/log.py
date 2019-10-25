import logging

logging.basicConfig(filename='logging.log',format='%(asctime)s %(message)s') # datefmt=' %m %d %I:%M:%S %Y'
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
