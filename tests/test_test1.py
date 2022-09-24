from test1 import __version__
from test1.main import get_argument_parser
import xml.etree.ElementTree as ET
import json


def test_version():
    assert __version__ == "0.1.0"


def test_fibonacci_level():
    parser = get_argument_parser()
    arguments = parser.parse_args("fibo --level 5".split(" "))
    root = ET.fromstring(arguments.func(arguments))
    assert int(root.findtext("result")) == 13


def test_fibonacci_max_value_xml():
    parser = get_argument_parser()
    arguments = parser.parse_args("fibo --max-value 125".split(" "))
    root = ET.fromstring(arguments.func(arguments))
    assert int(root.findtext("result")) == 89


def test_fibonacci_max_value_json():
    parser = get_argument_parser()
    arguments = parser.parse_args("fibo --max-value 125 -j".split(" "))
    root = json.loads(arguments.func(arguments))
    assert int(root["result"]) == 89
