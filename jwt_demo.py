from pathlib import Path
import jwt 

########################################
# JWT AUTH CREDES
########################################
# JWT_SECRET_KEY="Y1mVowT+Kq/Npd3nladzuWEPiuL5QZKV4JMM23WWHUpR47lvja872ERlp43jDak8"
# JWT_ALGORITHM="HS256"
# JWT_IDENTIFIER="server"

# def create_unique_token(data: dict) -> str:
#     return jwt.encode(
#         payload=data,
#         key=JWT_SECRET_KEY,
#         algorithm=JWT_ALGORITHM
#     )
    
# def decode_unique_token(token: str):
#     return jwt.decode(
#         jwt=token,
#         key=JWT_SECRET_KEY,
#         algorithms=[JWT_ALGORITHM]
#     )

# token = create_unique_token({"username": "sabari"})
# print(token)
# print(decode_unique_token(token))


import os


template_folder = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "templates"
)

print(template_folder,"\n" ,os.path.dirname(__file__))
print( Path(__file__).parent / 'templates')