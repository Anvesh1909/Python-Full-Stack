import logging

logging.basicConfig(filename="data.txt",level=logging.DEBUG)
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")



# for removing duplicate

import logging

logging.basicConfig(filename="data.txt",level=logging.DEBUG,filemode="w")
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")




'''
- CRITICAL --> 50
- ERROR    --> 40
- WARNING  --> 30
- INFO     --> 20
- DEBUG    --> 10
- NOTSET   --> 0
'''

# by give ing number as a level
import logging

logging.basicConfig(filename="data.txt",level=10,filemode="w")
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")



# without level by default
import logging

logging.basicConfig(filename="data.txt",filemode="w")
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")






# only critical information
import logging

logging.basicConfig(filename="data.txt",level=logging.WARNING,filemode="w")
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")





# to log inside the console
import logging

logging.basicConfig(format="%(levelname)s",level=logging.DEBUG)
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")


# display message
import logging

logging.basicConfig(format="%(message)s",level=logging.DEBUG)
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")




# display time
import logging

logging.basicConfig(format="%(asctime)s",level=logging.DEBUG)
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")




import logging

logging.basicConfig(format="%(asctime)s",level=logging.DEBUG, datefmt="%I:%M:%s %d:%m:%y %p")
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")



import logging

logging.basicConfig(format="%(asctime)s:%(message)s:%(levelname)s",level=logging.DEBUG, datefmt="%I:%M:%S %d:%m:%Y %p")
print("Hello world!")

logging.critical("Critical information")
logging.error("Errorinformation")
logging.warning("Warning information")
logging.info("Info information")
logging.debug("Debug information")











import logging
logging.basicConfig(filename="data2.txt",level=logging.DEBUG,format="%(levelname)s:%(message)s:%(asctime)s",datefmt="%I:%M:%S %d:%m:%Y %p",filemode="w")

try:
    10//0
except ZeroDivisionError as e:
    print(e)
    logging.exception(e)
    
    
    
    
    



import logging
logging.basicConfig(filename="data2.txt",level=logging.DEBUG,format="%(levelname)s:%(message)s:%(asctime)s",datefmt="%I:%M:%S %d:%m:%Y %p",filemode="w")

a = int(input("Enter a value: "))
while True:
    try:
        print()
        op = input("enter - + / // * **: ")
        b = int(input("Enter a value: "))
        a = eval(f"{a}{op}{b}")
        print(a)
    except Exception as e:
        print(e)
        logging.exception(e)
        
        
        
        
        

