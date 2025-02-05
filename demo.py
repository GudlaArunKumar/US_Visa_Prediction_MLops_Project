from us_visa.exception import USVisaException 
import sys 


try:
    a = 5 / 0 
except Exception as e:
    raise USVisaException(e, sys)
