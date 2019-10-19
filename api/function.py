__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."


class Function:
    """
    Class Function.
    This function class is used to define common function used in whole
    application.
    """

    def error_response(self, data, msg=''):
        """
        Function error_response
        This function is used to pass error message and error details.
        :param data:
            A data that contains error data.
        :param msg:
            A msg that contains message string.

        :return:
            Return error message and error details.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        return {'success': False, 'error': True, 'details': data, 'message':
            msg}

    def success_response(self, data, msg=''):
        """
        Function success_response
        This function is used to pass success message and success details.

        :param data:
            A data that contains data.
        :param msg:
            A msg that contains message string.
        :param pagination:
            A pagination that contains pagination data.

        :return:
            Return error message and success details.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        return {'success': True, 'error': False, 'details': data, 'message':
            msg}