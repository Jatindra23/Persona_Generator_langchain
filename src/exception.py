import sys
import os
import traceback


def error_message_detail(error, error_detail=sys):
    """
    Return the error message with the filename and line number.
    """
    exc_type, exc_obj, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        filename = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occurred in file [{0}] at line [{1}]: {2}".format(
            filename, exc_tb.tb_lineno, str(error)
        )
    else:
        error_message = str(error)

    return error_message



class PersonaException(Exception):

    def __init__(self, error_message, error_detail: sys):

        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
