#!/usr/bin/env python
#

# Imports
from __future__ import print_function
import argparse
import logging
import datetime
import sys
from collections import namedtuple

# Logging initialization
LOG = logging.getLogger('script-name')
LOG_FORMAT = (
    '%(asctime)-15s '
    '(%(levelname).1s) '
    '%(threadName)s:%(module)s.%(funcName)s:%(lineno)d - '
    '%(message)s'
)
LOG_LEVEL = logging.DEBUG

# Argument container
Args = namedtuple('Args', [
    'numbers',
    'thing',
    'do_it',
])

def main():
    args = parse_cli_args()
    set_up_logging()

    LOG.info('hi!')
    LOG.info('numbers: {}'.format(args.numbers))
    LOG.info('thing: {}'.format(args.thing))
    LOG.info('do it: {}'.format(args.do_it))

    return


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Do the business.")
    # Positional arguments
    parser.add_argument(
        'numbers', metavar='NUM', type=int, nargs='+',
        help="The number of things."
    )
    # Optional argument with values
    parser.add_argument(
        '--thing-opt', metavar="THING", type=str, default="beep",
        help="Optionally, set the thing to a value. (Defaults to 'beep')"
    )
    # Optional flag
    parser.add_argument(
        '--do-it', action='store_true',
        help="Optionally, do it.  Otherwise don't do it."
    )
    # Version
    parser.add_argument(
        '--version', action='version',
        version='Throwaway Script v9.2.7rc5 2003 Enterprise Edition',
        help="Print program version and exit."
    )

    parsed_args = parser.parse_args()

    args = Args(
        numbers=parsed_args.numbers,
        thing=parsed_args.thing_opt,
        do_it=parsed_args.do_it,
    )

    return args


def set_up_logging():
    """
    Initialize logging.  Must be called before LOG is used.
    """
    LOG.setLevel(LOG_LEVEL)
    stdout = logging.StreamHandler(sys.stdout)
    LOG.addHandler(stdout)
    stdout.setFormatter(LOGFormatter(LOG_FORMAT))
    return


class LOGFormatter(logging.Formatter):
    """
    Log line formatter used by LOG.
    """
    converter = datetime.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        timestamp = self.converter(record.created)

        if datefmt:
            s = timestamp.stftime(Datefmt)
        else:
            # TODO add timezone
            s = timestamp.strftime(
                "%Y-%m-%d %H:%M:%S.{msecs:03.0f}".format(msecs=record.msecs)
            )

        return s


if __name__ == "__main__":
    main()
