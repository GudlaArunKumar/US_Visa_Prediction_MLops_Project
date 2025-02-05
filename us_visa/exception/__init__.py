import os 
import sys  # sys package gives the error detail using exc_info() function


def error_message_detail(error, error_detail:sys):
    """
    Takes the error message and error detail and returns modified version 
    of error message to the user
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message



class USVisaException(Exception):

    def __init__(self, error_message, error_detail):
        """
        Initiates Exception class by passing 
        Error message paramter.

        Args:
            error_message: error message in string format
        """
        super().__init__(error_message) 

        self.error_message = error_message_detail(
           error_message, error_detail=error_detail 
        )

    def __str__(self):
        return self.error_message
        