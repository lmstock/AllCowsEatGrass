import logging
import time

t = time.time()
tfile = "aceg_logs\\" + str(t) + ".log"


logger = logging.getLogger('aceg')
logger.setLevel(logging.INFO)

# create file handler which logs even debug messages
# fh = logging.FileHandler(tfile)
# fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter2)
# fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
# logger.addHandler(fh)

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')