"""fibonacci module

This module contains the implementation of the Fibonacci class

"""


def _fibo(level, max, verbose=False):
    """the fibonacci calculation function

    Calculates the fibonacci series according to its input parameters

    Examples:
        >>> _fibo(5, -1)
        13

    :param level: How many steps does fibo function needs to take.
    :param max: Maximum value to reach
    :param verbose: Verbose output
    :return: the fibonacci number
    """
    result1 = 1
    result2 = 1
    while True:
        if level != -1 and level == 0:
            return result2
        if max != -1 and result2 > max:
            return result1
        result2 = result1 + result2
        result1 = result2 - result1
        level -= 1


def _output_error_xml(value, error_msg):
    """show error message in xml

    :param value: Error code
    :param error_msg: descriptive error message
    :return:
    """
    return "<fibonacci><result>{}</result><error-msg>{}</error-msg></fibonacci>".format(
        value, error_msg
    )


def _output_error_json(value, error_msg):
    """show error message in json

    :param value: Error code
    :param error_msg: descriptive error message
    :return:
    """
    return '{{"result":{},"error-msg>":"{}"}}'.format(value, error_msg)


def _output_value_xml(value):
    """show result in xml

    :param value: Fibonacci result
    :return:
    """
    return "<fibonacci><result>{}</result></fibonacci>".format(value)


def _output_value_json(value):
    """show result in json

    :param value: Fibonacci result
    :return:
    """
    return '{{"result":{}}}'.format(value)


def _output(json_format, value, error_msg=None):
    """output result

    According to the parameters the output will be an XML or JSON result.

    :param json_format: True/False to show JSON otherwise it is XML.
    :param value: value of Fibonacci or error code when error_msg is present
    :param error_msg: a descriptive error message
    :return: string with XML or JSON
    """
    if error_msg:
        return (
            _output_error_json(value, error_msg)
            if json_format
            else _output_error_xml(value, error_msg)
        )
    return _output_value_json(value) if json_format else _output_value_xml(value)


class Fibonacci:
    """Fibonacci class

    Fibonacci class contains the business logic for the fibonacci commandline tool

    """

    def _process(self, args):
        """calculate the Fibonacci number

        This process will validate the arguments, calulate Fibonacci number and return
        the result in the requested format.

        :param args: arguments initialized in the constructor will be injected.
        :return: Returns a XML or JSON string
        """
        if args.level == -1 and args.max_value == -1:
            return _output(
                args.json,
                -1,
                error_msg="Missing arguments, 'level' or 'max-value' is obligatory",
            )
        result = _fibo(args.level, args.max_value, args.verbose)
        return _output(args.json, result)

    def __init__(self, parent_parser):
        """constructor

        Initializes the Fibonacci class where we add the necessary arguments to parse by
        the argument parser

        :param parent_parser: parent argument parser of test1 application.
        """
        subparser = parent_parser.add_parser("fibo")
        subparser.add_argument(
            "-l",
            "--level",
            type=int,
            default=-1,
            help="Number steps for Fibonacci to take",
        )
        subparser.add_argument(
            "-m",
            "--max-value",
            type=int,
            default=-1,
            help="Run steps for Fibonacci as long as its less then 'max-value'",
        )
        subparser.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            help="Verbose output, prints each step of Fibonacci series!",
        )
        subparser.add_argument(
            "-j",
            "--json",
            action="store_true",
            help="Return json result",
        )
        subparser.add_argument(
            "-x",
            "--xml",
            action="store_true",
            help="Return xml result",
        )
        subparser.set_defaults(func=self._process)
