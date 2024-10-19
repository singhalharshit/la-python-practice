import logging

logging.basicConfig(filename='test3.log', level= logging.INFO, format='%(name)s %(asctime)s %(levelname)s %(message)s')



def divide(a,b):
    logging.info('The values entered by the user are %s and %s', a,b)
    try:
        logging.info('Entered into function')
        div =a/b
        logging.info('We have completed the division with the value %s', div)
        return div
    except Exception as e:
        logging.exception(e)


divide(12,0)

# This is a basic program which explain what happens in production grade of code and how logging can help a lot. You can take as a example where we check the polaris logs in which we search for error