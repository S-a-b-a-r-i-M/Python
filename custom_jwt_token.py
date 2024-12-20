
import jwt


class ServerToServerAuth:
    def generate_token(unique_id = "hire10x"):
        data = {"unique_id": unique_id}
        jwt_token = jwt.encode(
            data,
            "Y1mVowT+Kq/Npd3nladzuWEPiuL5QZKV4JMM23WWHUpR47lvja872ERlp43jDak8",
            algorithm="HS256",
        )

        return jwt_token


    # def authenticate(token):
    #         auth_header = request.META.get("HTTP_AUTHORIZATION")
    #         if not auth_header:
    #             logger.exception("No auth token provided")
    #             raise NoAuthToken("No auth token provided")
    #             print("No auth token provided")

    #         id_token = token.split(" ").pop()
    #         try:
    #             decoded = jwt.decode(
    #                 id_token,
    #                 "Y1mVowT+Kq/Npd3nladzuWEPiuL5QZKV4JMM23WWHUpR47lvja872ERlp43jDak8",
    #                 algorithms="HS256",
    #             )
    #         except Exception as e:
    #             print(id_token)
    #             logger.exception("Invalid auth token")
    #             raise InvalidAuthToken("Invalid auth token")

    #         unique_id = decoded.get("unique_id")
    #         print(unique_id)
    

# headers = {
#             "Authorization": f"Bearer {token}",
#             "Content-Type": "application/json",
#         }

def generate_token(unique_id: str = "hire10x") -> str:
    data = {"unique_id": unique_id}
    return jwt.encode(
        payload=data,
        key="Y1mVowT+Kq/Npd3nladzuWEPiuL5QZKV4JMM23WWHUpR47lvja872ERlp43jDak8",
        algorithm="HS256",
    )

print(generate_token())