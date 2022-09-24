class Fibonacci:
    def _fibo(self, level, max, verbose=False):
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

    def _output_error_xml(self, value, error_msg):
        return "<fibonacci><result>{}</result><error-msg>{}</error-msg></fibonacci>".format(
            value, error_msg
        )

    def _output_error_json(self, value, error_msg):
        return '{{"result":{},"error-msg>":"{}"}}'.format(value, error_msg)

    def _output_value_xml(self, value):
        return "<fibonacci><result>{}</result></fibonacci>".format(value)

    def _output_value_json(self, value):
        return '{{"result":{}}}'.format(value)

    def _output(self, json_format, value, error_msg=None):
        if error_msg:
            return (
                self._output_error_json(value, error_msg)
                if json_format
                else self._output_error_xml(value, error_msg)
            )
        return (
            self._output_value_json(value)
            if json_format
            else self._output_value_xml(value)
        )

    def process(self, args):
        if args.level == -1 and args.max_value == -1:
            return self._output(
                args.json,
                -1,
                error_msg="Missing arguments, 'level' or 'max-value' is obligatory",
            )
        result = self._fibo(args.level, args.max_value, args.verbose)
        return self._output(args.json, result)

    def __init__(self, parent_parser):
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
        subparser.set_defaults(func=self.process)
