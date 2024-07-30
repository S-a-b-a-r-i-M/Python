"""
 The pendulum library is a date and time manipulation library for Python that provides 
 a more intuitive and easier-to-use interface than the built-in datetime module
"""

'''
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


convert_datetime_to_utc_by_pendulum("2024-05-10 12:29:01.423329+05:30", "Asia/Kolkata")
'''


from datetime import datetime
import pytz
'''
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
'''

from dateutil import parser

def convert_date_to_timestamp(date: str | datetime):
    """
    Convert a date string or datetime object to a Unix timestamp.

    Args:
        date (str): The date to convert. Can be a either string format or datetime.
        Valid Inputs:
         - String representations of dates in various formats (e.g., "2023-10-26", "Oct 26, 2023", "2023/10/26", "10/26/2023")
         - String "present" (case-insensitive)
         - datetime objects

    Returns:
        float: The Unix timestamp, or -1.0 if conversion fails.
    """
    try:
        if isinstance(date, datetime):
            return date.timestamp()
        
        date = date.strip()
        if date.lower() == "present":
            date = datetime.now()
        else:
            date = parser.parse(date)

        return date.timestamp()
    except Exception as exp:
        return -1.0
        
def timestamp_to_readable_date(timestamp: float, format:str ="%Y-%m"):
    try:
        date = datetime.fromtimestamp(timestamp)
        return date.strftime(format)
    except Exception as exp:
        print("Error in timestamp_to_readable_date", exp)
        pass

timestamp = convert_date_to_timestamp("2024-04-01")
print(timestamp, timestamp_to_readable_date(timestamp))
timestamp = convert_date_to_timestamp("April 2024")
print(timestamp, timestamp_to_readable_date(timestamp))
# print('2023-10-26T12:34:56',convert_date_to_timestamp("2023-10-26T12:34:56"))
# print('April 2024',convert_date_to_timestamp("April 2024 "))
# print('Present',convert_date_to_timestamp("Present "))
# print('Jun 2021',convert_date_to_timestamp("Jun 2021"))
# print('July-2021',convert_date_to_timestamp('July-2021'))
# print("2023-10-26",convert_date_to_timestamp("2023-10-26"))
# print("10/26/2023",convert_date_to_timestamp("10/26/2023"))
# print("Oct 26, 2023",convert_date_to_timestamp("Oct 26, 2023"))
# print("datetime",convert_date_to_timestamp(datetime.now()))




