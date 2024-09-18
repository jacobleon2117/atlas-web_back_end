#!/usr/bin/env python3
"""
    Filtered Logger - module
"""

import re
from typing import List
import logging


PII_FIELDS = (
    'email',
    'ssn',
    'password',
    'address',
    'phone_number'
)


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
        Redact specified fields in a
        log message with a given redaction string.
    """
    pattern = '|'.join(
        [f'{field}=[^{separator}]*' for field in fields]
    )

    return re.sub(
        pattern,
        lambda m: m.group(0).split('=')[0] + '=' + redaction,
        message
    )


class RedactingFormatter(logging.Formatter):
    """
        Custom logging formatter that
        redacts specified fields in log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
            Initialize the RedactingFormatter
            with the specified fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            Format the log record by redacting specified fields.
        """
        log = filter_datum(
            self.fields,
            self.REDACTION,
            record.getMessage(),
            self.SEPARATOR
        )
        record.msg = log
        return super().format(record)

def get_logger() -> logging.Logger:
    """
        Initializes and returns a logger instance configured to redact sensitive information
    """
    logger = logging.getLogger('user_data')

    if logger.level == logging.NOTSET:
        logger.setLevel(logging.INFO)

    if not any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers):
        stream_handler = logging.StreamHandler()

        formatter = RedactingFormatter(fields=PII_FIELDS)
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)

    logger.propagate = False
    
    return logger
