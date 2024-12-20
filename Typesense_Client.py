import os
from dotenv import load_dotenv

import typesense
from typesense import Client

load_dotenv()

class TypesenseClient:
    """
    A class representing a Typesense client.

    This class provides methods to interact with the Typesense search engine.
    It initializes a Typesense client with the specified host, port, and API key.

    Methods:
        client() -> typesense.Client:
            Returns the Typesense client object.
    """

    def __init__(self):
        self.typesense_client = typesense.Client(
            {
                "nodes": [
                    {
                        "host": os.getenv("TYPESENSE_HOST"),
                        "port": os.getenv("TYPESENSE_PORT"),
                        "protocol": "https",
                    }
                ],
                "api_key": os.getenv("TYPESENSE_API_KEY"),
                "connection_timeout_seconds": 300,
            }
        )

    def client(self) -> Client:
        return self.typesense_client


typesense_client = TypesenseClient().client()

datas = []
is_data_present = True
i = 1
while is_data_present:
        search_parameters = {
            "q": "*",		
            "query_by": "",
            "page": i,
            "per_page": 250,	
            "include_fields": "*"		
        }
        data = typesense_client.collections["jd1"].documents.search(search_parameters)			
        is_data_present = bool(len(data))
        datas.extend([i["document"] for i in data["hits"]])
        i += 1
        
print("old data", len(datas), datas[0])