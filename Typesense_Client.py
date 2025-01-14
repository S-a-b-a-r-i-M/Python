import os
import json
from typing import Any
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

    @property
    def client(self) -> Client:
        return self.typesense_client


typesense_client = TypesenseClient().client

def delete_collection(collection_name):
    print("collecction deleted", collection_name)
    return typesense_client.collections[collection_name].delete()


def create_country_schema():
        schema = {
            "name": "countries",
            "fields": [
                {
                    "facet":False,
                    "index":True,
                    "name":"name",
                    "optional":False,
                    "sort":False,
                    "type":"string"
                },
                {
                    "facet":False,
                    "index":True,
                    "name":"location",
                    "optional":False,
                    "sort":True,
                    "type":"geopoint"
                },
                {
                    "facet":False,
                    "index":True,
                    "name":"type",
                    "optional":False,
                    "sort":False,
                    "type":"string"
                },
                {
                    "facet":False,
                    "index":True,
                    "name":"country_name",
                    "optional":True,
                    "sort":False,
                    "type":"string"
                },
                {
                    "facet":False,
                    "index":True,
                    "name":"state_name",
                    "optional":True,
                    "sort":False,
                    "type":"string"
                },
                {
                    "facet":False,
                    "index":True,
                    "name":"phone_code",
                    "optional":True,
                    "sort":False,
                    "type": "int32"
                },
                {
                    "facet":False,
                    "index":True,
                    "name":"iso2",
                    "optional":False,
                    "sort":False,
                    "type":"string"
                },
                {
                    "facet":False,
                    "index":True,
                    "name":"emoji",
                    "optional":False,
                    "sort":False,
                    "type":"string"
                }
            ],
            "enable_nested_fields": False,
        }
        res = typesense_client.collections.create(schema)
        return res


def get_candidate_fields() -> list[dict[str, Any]]:
    return [
        {
            "name": "id",  # primary key - candidate id
            "type": "string",
        },
        {"name": "name", "type": "string"},
        {
            "name": "skills",
            "type": "string[]",
        },
        {
            "name": "phone",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "email",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "total_experience",
            "type": "float",
        },
        {
            "name": "location",
            "type": "geopoint",
            "optional": True,
        },
        {
            "name": "source",
            "type": "string[]",
        },
        {
            "name": "social_links",
            "type": "string[]",
        },
        {
            "name": "resume",
            "type": "string",
            "optional": True,
        },
        {
            "name": "headline",
            "type": "string",
            "optional": True,
        },
        {
            "name": "work_type",
            "type": "string",
            "optional": True,
        },
        {
            "name": "updated_at",
            "type": "int64",
        },
        # experiences
        {
            "name": "experiences.designation",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "experiences.company",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "experiences.location",
            "type": "geopoint[]",
            "optional": True,
        },
        {
            "name": "experiences.location_name",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "experiences.start_date",
            "type": "string[]",
            "index": False,
            "sortable": True,
            "optional": True,
        },
        {
            "name": "experiences.end_date",
            "type": "string[]",
            "index": False,
            "sortable": True,
            "optional": True,
        },
        # educations
        {
            "name": "educations.degree",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "educations.college",
            "type": "string[]",
            "optional": True,
        },
        {
            "name": "educations.grad_year",
            "type": "int64[]",
            "optional": True,
            "sortable": True,
        },
        {
            "name": "embedding",
            "type": "float[]",
            "embed": {
                "from": [
                    "skills",
                    "experiences.designation",
                    "educations.degree",
                ],
                "model_config": {
                    "model_name": "openai/text-embedding-3-small",
                    "api_key": f"{os.getenv('OPENAI_API_KEY')}",
                },
            },
        },
    ]


def create_candidate_collection(schema_name: str):
    fields = get_candidate_fields()
    fields.append({ "name": "status", "type": "bool" })
    schema = {
        "name": f"{schema_name}",
        "enable_nested_fields": True,
        "fields": fields,
        "default_sorting_field": "updated_at",
    }
    return typesense_client.collections.create(schema)


def create_jd_collection(schema_name):
    schema = {
        "name": schema_name,
        "enable_nested_fields": True,
        "fields": [
            {
                "name": "id",  # candidate_id + jd_id
                "type": "string",
            },
            {
                "name": "jd_id",
                "type": "string",
                "index": True,
            },
            {
                "name": "status",
                "type": "string",
                "index": False,
                "sortable": True,
            },
            {
                "name": "stage",
                "type": "string",
            },
            {
                "name": "ranking_score",
                "type": "float",
                "sortable": True,
            },
            {
                "name": "is_ranked",
                "type": "bool",
                "sortable": True,
            },
            {
                "name": "candidate",
                "type": "string",
                "reference": "candidate1.id",
                "optional": True,
            }
        ],
    }
    return typesense_client.collections.create(schema)


def create_marketplace_collection() :
        schema_name = "marketplace"
        fields = get_candidate_fields()
        # add additional fields for marketplace candidates(employees)
        fields.extend(
            [
                {
                    "name": "company_id",
                    "type": "int32",
                },
                {
                    "name": "visibility",
                    "type": "string",
                },
                {
                    "name": "current_status",
                    "type": "string",
                },
            ]
        )
        schema = {
            "name": f"{schema_name}",
            "enable_nested_fields": True,
            "fields": fields,
            "default_sorting_field": "updated_at",
        }
        return typesense_client.collections.create(schema)


def create_document(collection_name, document):
    return typesense_client.collections[collection_name].documents.create(document)


def convert_json_to_jsonl():
    # open copuntries json file 
    data = []
    id=1
    with open("/home/new/PROGRAMMING_GROUND/Python/contries.json", "r") as f:
        contetnt = f.read()

    data_list = json.loads(contetnt)

    # write into jsonl file
    with open("/home/new/PROGRAMMING_GROUND/Python/contries2.jsonl", "w") as f:
        for data in data_list:
            flattened = {
                "country_name": data["name"],
                "iso2": data["iso2"],
                "phone_code": data["phone_code"],
                "emoji": data["emoji"],
            }
            for state in data["states"]:
                flattened["state_name"] = state["name"]
                for city in state["cities"]:
                    flattened["id"] = str(id)
                    flattened["name"] = city["name"]
                    flattened["location"] = [float(city["latitude"]), float(city["longitude"])]
                    flattened["type"] = "city"
                    id += 1
                    f.write(json.dumps(flattened) + "\n")


def retrive_all_collection():
    """
    Retrieves a list of all collections from the Typesense server.

    Returns:
        List of dict: A list of dictionaries, each representing a collection.
    """
    return typesense_client.collections.retrieve()


def retrieve_collection(collection_name):
    """
    Retrieves information about a specified collection from the Typesense server.

    Args:
        collection_name (str): The name of the collection to retrieve.

    Returns:
        dict: A dictionary containing details about the specified collection.
    """
    return typesense_client.collections[collection_name].retrieve()


def fetch_all_data(collection_name):
    """
    Fetches all data from the specified Typesense collection.

    Args:
        collection_name (str): The name of the collection to fetch data from.

    Returns:
        list: A list of dictionaries representing the data in the collection.
    """
    datas = []
    is_data_present = True
    i = 1
    while is_data_present:
        search_parameters = {
            "q": "*",		
            "query_by": "",
            "page": i,
            "per_page": 250,	
            "include_fields": "*",
            "exclude_fields": "embedding",		
        }
        data = typesense_client.collections[collection_name].documents.search(search_parameters)			
        is_data_present = bool(len(data["hits"]))
        datas.extend([i["document"] for i in data["hits"]])
        i += 1
            
    print("old data", len(datas), datas[0])


def fetch_all_data_from_jd_collection(collection_name, jd_id):
    datas = []
    search_parameters = {
        "q": "*",
        # Note: Reference searching is not working
        # "query_by": "$marketplace(name),$marketplace(email),$marketplace(phone),$marketplace(skills)",
        "filter_by": f"jd_id:={jd_id} && is_ranked:=true",
        "include_fields": "$marketplace(*),$candidate1(*)",
        "page": 1,
        "per_page": 10,
        "prefix": False,
        "exclude_fields": "$marketplace(embedding),$candidate1(embedding)",
        "sort_by": "ranking_score:desc"
    }
    data = typesense_client.collections[collection_name].documents.search(search_parameters)			
    datas.extend([i["document"] for i in data["hits"]])

    print("data", len(datas), datas)


def import_jsonl_file_to_collection(collection_name):
    """
    Imports data from a JSONL file into a specified Typesense collection.

    Args:
        collection_name (str): The name of the Typesense collection to import data into.

    Returns:
        dict: A response from the Typesense server indicating the result of the import operation.
    """
    res = None
    with open("jd_mappping.jsonl") as jsonl:
        res = typesense_client.collections[collection_name].documents.import_(
             jsonl.read().encode('utf-8'), {"action": "create"}
        )

    return res

# id : '4258862608352808960' in market place
# id : 1000 in jd0 collection

# create_document(
#     collection_name="marketplace",
#     document={
#     "work_type": "Full Time",
#     "company_id": 1,
#     "id": "4258862608352808960",
#     "educations": [
#         {
#         "college": "Unisinos University",
#         "degree": "Specialization",
#         "grad_year": 2021
#         }
#     ],
#     "email": [],
#     "experiences": [
#         {
#         "company": "Meta",
#         "designation": "Senior Oracle Developer",
#         "end_date": "2025-01-01",
#         "start_date": "2021-06-01"
#         }
#     ],
#     "headline": "Software Engineering Specialist | Oracle APEX Cloud Developer Certified Professional | Oracle PL/SQL Developer",
#     "location": [
#         -29.01417,
#         -53.734236
#     ],
#     "name": "Raul Welter",
#     "phone": [],
#     "resume": "",
#     "skills": [
#         "Snyk",
#         "ERP (Planejamento de recursos empresariais)",
#         "C#",
#         "Agile & Waterfall Methodologies",
#         "Unified Modeling Language (UML)"
#     ],
#     "social_links": [
#         "https://www.linkedin.com/in/raulwelter"
#     ],
#     "source": [
#         "LINKEDIN"
#     ],
#     "total_experience": 13.33,
#     "updated_at": 1736383198,
#     "visibility": "public",
#     "current_status": "active"
#     }
# )

# create_document(
#     collection_name="jd0",
#     document={
#         'id': '1001', 
#         'is_ranked': True, 
#         'jd_id': '4253550266886918144', 
#         'marketplace': None, 
#         'ranking_score': 15.4, 
#         'stage': 'SOURCED', 
#         'status': 'QUALIFIED',
#         'candidate': '4258862607581057024'
#     }
# )
