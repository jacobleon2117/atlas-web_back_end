#!/usr/bin/env python3
"""
logger filtering module
"""

import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ('phone', 'name', 'ssn', 'password', 'email')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
        Redact personal information from the provided string.
    """
    for field in fields:
        pattern = r"" + re.escape(field) + r"=.*?"+re.escape(separator)
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """
        Custom logging formatter that redacts specified fields in log messages
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            Format the log record with redacted fields.
        """
        log = filter_datum(self.FIELDS,
                           self.REDACTION,
                           record.getMessage(),
                           self.SEPARATOR)
        record.msg = log
        return logging.Formatter(self.FORMAT).format(record)


def get_logger() -> logging.Logger:
    """
        Create and configure a logger instance with RedactingFormatter.
    """
    hdlr = logging.StreamHandler()
    hdlr.setFormatter(RedactingFormatter(PII_FIELDS))
    user_data = logging.getLogger('user_data')
    user_data.setLevel(logging.INFO)
    user_data.addHandler(hdlr)
    user_data.propagate = False
    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
        Establish a connection to the MySQL database.
    """
    usr = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    pw = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    hst = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    connection = mysql.connector.connect(
        user=usr,
        password=pw,
        host=hst,
        database=db_name
    )
    return connection


def main():
    """
        Retrieves all user records from the 'users' table
        in the database and logs the data with sensitive
        PII fields redacted.
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        nm = f"name={row[0]}; "
        em = f"email={row[1]}; "
        ph = f"phone={row[2]}; "
        sn = f"ssn={row[3]}; "
        pw = f"password={row[4]}; "
        ip = f"ip={row[5]}; "
        ll = f"last_login={row[6]}; "
        ua = f"user_agent={row[7]}"
        message = f"{nm}{em}{ph}{sn}{pw}{ip}{ll}{ua}"
        log_record = logging.LogRecord(logger,
                                       logging.INFO,
                                       None,
                                       None,
                                       message,
                                       None,
                                       None)
        logger.info(log_record.msg)


if __name__ == '__main__':
    main()
