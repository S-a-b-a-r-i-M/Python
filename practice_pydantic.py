from datetime import datetime
from enum import StrEnum
import hashlib
from typing import Any

import orjson
from pydantic import BaseModel, ConfigDict, Field, computed_field, field_validator, model_validator

'''
class ChannelTypes(StrEnum):
    JD = "jd"
    AI = "ai"
    BASIC = "basic"
    ACTIVITY = "activity"
    CANDIDATE = "candidate"
    COMMUNICATION = "communication"
    LINKEDIN_ALERT = "linkedin_alert"


class WSChannels(StrEnum):
    WS_BASIC = "ws_basic"
    WS_ADD_TO_JD = "ws_add_to_jd"


class MessageModel(BaseModel):
    # Candidate details
    candidate_id: int | None = None
    candidate_name: str | None = None

    @model_validator(mode="before")
    def validate_values(cls, values: dict[str, Any]):
        return values


class ActivityData(BaseModel):
    """
    Model containing necessary activity (single or bulk) activity information.
    These messages are not sent as a notifacation to frontend.
    """

    candidate_ids: list[int] | None = None

    @model_validator(mode="before")
    def validate_values(cls, values: dict[str, Any]):
        return values


class SubscribedNotifyModel(BaseModel):
    channel: ChannelTypes | WSChannels
    data: MessageModel | ActivityData

    @model_validator(mode="before")
    def validate_values(cls, values: dict[str, Any]):
        if isinstance(values["channel"], bytes):
            values["channel"] = values["channel"].decode("utf-8")

        if not values.get("data", False):
            raise ValueError("Data cannot be empty to send a notification")

        data = values["data"]
        if isinstance(values["data"], bytes):
            data_js = data.decode("utf-8")
            data = orjson.loads(data_js)

            try:
                channel = values["channel"].lower()
                if channel == ChannelTypes.ACTIVITY:
                    values["data"] = ActivityData(**data, notification_type=ChannelTypes.ACTIVITY)
                else:
                    values["data"] = MessageModel(
                        **data, notification_type=ChannelTypes[channel.upper()]
                    )

            except Exception as exp:
                print(f"schema.py -> Invalid data: {data} exp: {exp}")
        print("data from subscribed notify model", values)
        return values
    
    @model_validator(mode="after")
    def validate_values_after(cls, values: dict[str, Any]):
        return values

SubscribedNotifyModel(**{'channel': b'activity', 'data': b'{"jd_id": 1}'})
'''


#######################################################################################
"""
def unique_id(name, account_url, company_id):  # FIXME: Add the proper unique id
    return hashlib.md5(
        f"{name}/{account_url},{company_id}".encode(),
        usedforsecurity=False,
    ).hexdigest()

print(unique_id("sabari", "", 1))
print(unique_id("sabari", "fsdfasfsdf123", 1))
print(unique_id("sabari", "", 1))
print(unique_id("sabari", "fsdfasfsdf123", 1))
"""

class EducationModel(BaseModel):
    degree: str | None = Field(None, max_length=255)
    college_name: str | None = Field(None, max_length=255)
    grad_year: int | None = Field(None, description="graduation year")
    from_date: datetime | None = None
    to_date: datetime | None = None

    @computed_field(return_type=str)
    def unique_id(self):
        return hashlib.md5(
            f"{self.college_name}:{self.degree}/{self.grad_year}".encode(),
            usedforsecurity=False,
        ).hexdigest()

    @field_validator("from_date", "to_date", mode="before")
    def validate_dates(cls, v):
        try:
            if v and isinstance(v, str):
                v = datetime.strptime(v, "%d-%b-%Y")
        except ValueError:
            print(f"Invalid date format - {v}")
            raise ValueError(f"Invalid date format - {v}. valid format example 01-Jan-2020")

        return v

    # model config
    model_config = ConfigDict(extra="allow")

EducationModel(
    degree="Bachelor of Technology (B.Tech.)",
    college_name="Dr. A.P.J. Abdul Kalam Technical University",
    grad_year=2014,
    from_date="01-Jan-2014",
    to_date="01-Jan-2018",
)