import logging

logging.basicConfig(filename='test.log',level=logging.INFO)
logging.info("This is my first log")
l=[1,2,3,4,5,6,7,8,9]
for i in l:
    if i==2:
        logging.info(i)


# Different level of logs from top to bottom or highest priority to lowest priority 'Critical > Error > Warning > Info > Debug' and they can be ranked as '50 > 40 > 30 > 20 > 10' 
# Now what are these rankings and where are they used? So there are the rankings or the levels as in if I log INFO level of log I can't log anything in debug so if 20 is being used then logs would be created for 20 and above as in for INFO and above say for warning error and critical and nothing would be logged for Debug even if we try to. FOR EX CHECK THE BELOW CODE

logging.warning('This goes for warning')
logging.debug('This goes for debug')

# Now whenever you'll execute the code you'll see warning is logged but debug has been skipped which is because in the line no. 3 we have set the level as INFO which is everything above the INFO level is being logged

logging.shutdown()

