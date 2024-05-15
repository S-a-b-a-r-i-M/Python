"""
 The pendulum library is a date and time manipulation library for Python that provides 
 a more intuitive and easier-to-use interface than the built-in datetime module
"""

import pendulum


def convert_datetime_to_utc_by_pendulum(datetime_str: str, local_tz:str):
    """
    Convert a datetime string in the local timezone to UTC
    Args:
        datetime_str(str) : Datetime string (ex: 2024-05-10 12:29:01.423329+05:30)
        local_tz(str) : Local timezone (ex: Asia/Kolkata)
    """
    local_dt = pendulum.parse(datetime_str, tz=local_tz)
    # print(type(local_dt), local_dt)

    utc_dt = local_dt.in_tz(pendulum.timezone("UTC"))
    print(local_dt, utc_dt)


# convert_datetime_to_utc_by_pendulum("2024-05-10 12:29:01.423329+05:30", "Asia/Kolkata")


from datetime import datetime
import pytz

def convert_datetime_to_utc(datetime_str: str):
    """
    Convert a datetime string in the local timezone to UTC
    Args:
        datetime_str(str) : Datetime string (ex: 2024-05-10 12:29:01.423329+05:30)
    """
    # Convert the datetime string to a datetime object with the local timezone
    local_dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f%z")

    utc_dt = local_dt.astimezone(pytz.timezone("UTC"))
    print(local_dt, utc_dt)


convert_datetime_to_utc("2024-05-10 12:29:01.423329+05:30", "Asia/Kolkata")