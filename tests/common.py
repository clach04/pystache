# coding: utf-8

"""
Provides test-related code that can be used by all tests.

"""

import os

import examples


DATA_DIR = 'tests/data'
EXAMPLES_DIR = os.path.dirname(examples.__file__)


def get_data_path(file_name):
    return os.path.join(DATA_DIR, file_name)


class AssertStringMixin:

    """A unittest.TestCase mixin to check string equality."""

    def assertString(self, actual, expected, format=None):
        """
        Assert that the given strings are equal and have the same type.

        Arguments:

          format: a format string containing a single conversion specifier %s.
            Defaults to "%s".

        """
        if format is None:
            format = "%s"

        # Show both friendly and literal versions.
        details = """String mismatch: %%s\


        Expected: \"""%s\"""
        Actual:   \"""%s\"""

        Expected: %s
        Actual:   %s""" % (expected, actual, repr(expected), repr(actual))

        def make_message(reason):
            description = details % reason
            return format % description

        self.assertEqual(actual, expected, make_message("different characters"))

        reason = "types different: %s != %s (actual)" % (repr(type(expected)), repr(type(actual)))
        self.assertEqual(type(expected), type(actual), make_message(reason))


class AssertIsMixin:

    """A unittest.TestCase mixin adding assertIs()."""

    # unittest.assertIs() is not available until Python 2.7:
    #   http://docs.python.org/library/unittest.html#unittest.TestCase.assertIsNone
    def assertIs(self, first, second):
        self.assertTrue(first is second, msg="%s is not %s" % (repr(first), repr(second)))
