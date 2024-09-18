#!/usr/bin/env python3
"""
    Filtered Logger - module
"""

import re
from typing import List
import logging
import os
import mysql.connector


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

def get_db() -> mysql.connector.connection.MySQLConnection:

    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    connection = mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )

    return connection

def main() -> None:
    """
        Retrieves all rows from the 'users'
        table and displays each row with PII fields redacted.
    """
    connection = get_db()

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        logger = get_logger()

        for row in rows:
            log_message = '; '.join(f"{key}={value}" for key, value in row.items())
            logger.info(log_message)
    finally:
        connection.close()

if __name__ == "__main__":
    main()
