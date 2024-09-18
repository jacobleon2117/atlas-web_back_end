#!/usr/bin/env python3
"""
    Filtered Logger - module
"""

import logging
import re


def filter_datum(fields, redaction, message, separator):
    pattern = f'({"|".join(map(re.escape, fields))}){re.escape(separator)}'
    return re.sub(pattern, f'{redaction}{separator}', message)

class RedactingFormatter(logging.Formatter):
    """
        Redacting Formatter class
    """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__()
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)
