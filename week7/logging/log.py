import logging

logger = logging.getLogger("log.py")
#Configure the logger system short operand, anything that needs to be added in one config
logging.basicConfig(filename="d.log", level=logger.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#alternative method this does everything separately

#set level
logger.setLevel(logging.DEBUG)
#create a file handler to save log to file
file_handler = logging.FileHandler("log_file.log", encoding="utf-8")
#create a handler to stream to terminal
stream_handler = logging.StreamHandler()
#set log format
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
#set format for every handler 
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
#add the handlers to this logger instance
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# Generate some logs
logger.debug("This is a debug message.")
logger.info("System has started successfully.")
logger.warning("API response is slower than usual.")
logger.error("Failed to save user data to the database.")
logger.critical("Server is out of memory. Shutting down.")


def say_hello():
    try:
        name = int(input("name: "))
        logger.info("user input a name")
    
        print("hello" + name)
        return
    except ValueError:
        logger.exception("invalid input")
        print("invalid input")
        return
    
say_hello()