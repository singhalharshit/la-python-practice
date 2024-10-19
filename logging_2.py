import logging

logging.basicConfig(filename='test2.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logging.info('This is my log with timestamp')

# The above code was for including timestamp while logging
