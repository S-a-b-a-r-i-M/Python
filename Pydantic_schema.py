
from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field, field_validator, model_validator
import json
from enum import IntEnum, StrEnum
"""
class ChannelsInt(IntEnum):
    EMAIL = 1
    SMS = 2
    WHATS_APP = 3
    WHATS_APP_BUSINESS = 4
    LINKEDIN_CONNECT = 5
    LINKEDIN_MESSAGE = 6
    LINKEDIN_INMAIL = 7


class ChannelsStr(StrEnum):
    EMAIL = "EMAIL"
    SMS = "SMS"
    WHATS_APP = "WHATS_APP"
    WHATS_APP_BUSINESS = "WHATS_APP_BUSINESS"
    LINKEDIN_CONNECT = "LINKEDIN_CONNECT"
    LINKEDIN_MESSAGE = "LINKEDIN_MESSAGE"
    LINKEDIN_INMAIL = "LINKEDIN_INMAIL"


class SendChatSchema(BaseModel):
    channel: ChannelsStr = Field(
        ...,
        description="Whatsapp, email, sms or linkedin",
        example=" | ".join(ChannelsStr._member_names_)
    )
    chat: str = Field(..., description="body of the message or email")
    # mail details
    to_email: Optional[str] = Field(None)
    # whatsapp and sms details
    phone: Optional[str] = Field(None)

    @model_validator(mode="before")
    def validate_values(cls, values: dict[str, Any]) -> dict[str, Any]:
        channel = values.get("channel", "").upper()
        if channel not in ChannelsStr._member_names_:
            raise ValueError(f"Channel must be provided. values - ${ChannelsStr.__member_names_}")

        if channel == ChannelsStr.EMAIL and not values.get("to_email"):
            # TODO: add validation for email
            raise ValueError("to_email cannot be empty or null")

        if channel in (ChannelsStr.SMS, ChannelsStr.WHATS_APP) and not values.get("phone"):
            # TODO: add validation for email
            raise ValueError("phone must be provided")
        
        return values

    @field_validator("channel")
    def validate_channel(cls, v):
        v = v.upper()
        if v not in ChannelsStr._member_names_:
            raise ValueError(f"Invalid channel: {v}")
        # transform str value to int value to store in db
        return ChannelsInt[v].value
    

print(SendChatSchema(channel="WHATS_APP", chat="hello", phone="1234567890"))
"""
"""
class SubMessageSchema(BaseModel):
  type: str
  pattern: str | None = None
  channel: str
  data: str
  
  @model_validator(mode="before")
  def validate_bytes(cls, values: dict[str, Any]):
    if values.get("channel", "") and isinstance(values["channel"], bytes):
        values["channel"] = values["channel"].decode("utf-8")

    if values.get("data", "") and isinstance(values["data"], bytes):
        values["data"] = values["data"].decode("utf-8")

    return values
    
    


  
data = {'type': 'message', 
 'pattern': None, 
 'channel': b'jd', 
 'data': b'{"name":"connection sucessful","Author":"sabari","channel":"jd"}'
 }

data = SubMessageSchema(**data)
print(data)
"""

class ChannelTypeStr(StrEnum):
    JD = "jd"
    AI = "ai"
    USER = "user"
    USER_SETTING = "user_setting"
    RANKING = "ranking"
    CANDIDATE = "candidate"
    WHATSAPP = "whatsapp"
    SMS = "sms"
    EMAIL = "email"
    BASIC = "basic"

class BaseNotifyDataModel(BaseModel):
    title: str
    message: str = Field(..., description="message can be string or dict(json string)")
    user_id: str =  Field(..., description="the user id of who will receive the notification")
    date_time: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    notification_type: ChannelTypeStr = Field(..., description="channel type", alias="channel")

    @model_validator(mode="before")
    def validate_values(cls, values: dict[str, Any]):
        if isinstance(values["date_time"], datetime):
            values["date_time"] = values["date_time"].strftime("%Y-%m-%dT%H:%M:%S")

        if not isinstance(values["user_id"], str):
            values["user_id"] = str(values["user_id"])

        if not isinstance(values["message"], str):
            try:
                values["message"] = json.dumps(values["message"])
            except Exception as e:
                print(f"Error occurred while dumps the message {e}")


        print("values", values)
        return values
    
data  = BaseNotifyDataModel(**{'title': 'Ranking failed', 'message': 'Try after sometime', 'user_id': '6', 'date_time': '2024-10-02T05:28:43.808312', 'channel': 'basic'})
