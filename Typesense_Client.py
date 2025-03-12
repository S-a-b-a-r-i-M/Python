import os
import json
from typing import Any
from dotenv import load_dotenv

import requests
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
                        "protocol": "http",
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


def create_employee_request_collection():
    schema ={
        "name": "employee_request",
        "fields": [
            {
                "name": "id",  # same as postgres table id int string
                "type": "string",
            },
            {
                "name": "jd_id",
                "type": "string",
                "index": False,
            },
            {
                "name": "marketplace",
                "type": "string",
                "reference": "marketplace.id",
            },
            {
                "name": "requesting_user_id",
                "type": "int64",
                "index": True,
            },
            {
                "name": "requesting_company_id",
                "type": "int32",
                "index": True,
            },
            {
                "name": "requesting_company_name",
                "type": "string",
                "index": True,
            },
            {
                "name": "source_company_id",
                "type": "int32",
                "index": True,
            },
            {
                "name": "status", # request status [PENDING, REJECTED, APPROVED]
                "type": "string",
                "index": True,
                "sortable": True,
            },
            {
                "name": "updated_at",
                "type": "int64",
            },
            {
                "name": "created_at",
                "type": "int64",
            },
        ]
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
            },
            {
                "name": "marketplace",
                "type": "string",
                "reference": "marketplace.id",
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
                    "name": "company_name",
                    "type": "string",
                },
                {
                    "name": "visibility",
                    "type": "string",
                },
                {
                    "name": "current_status",
                    "type": "string",
                },
                # request details
                {
                    "name": "requests.jd_id",
                    "type": "string[]",
                    "optional": True,
                },
                {
                    "name": "requests.status",
                    "type": "string[]",
                    "optional": True,
                }
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


def create_country_json_file():
    response = requests.get("https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/json/countries%2Bstates%2Bcities.json")
    with open("/home/new/PROGRAMMING_GROUND/Python/contries.json", "w") as f:
        f.write(response.text)

def convert_json_to_jsonl():
    # open copuntries json file 
    data = []
    id=1
    with open("/home/new/PROGRAMMING_GROUND/Python/contries.json", "r") as f:
        contetnt = f.read()

    data_list = json.loads(contetnt)

    # write into jsonl file
    with open("/home/new/PROGRAMMING_GROUND/Python/contries.jsonl", "w") as f:
        for data in data_list:
            flattened = {
                "country_name": data["name"],
                "iso2": data["iso2"],
                "phone_code": data["phonecode"],
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
    print("fetching.....")
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
            "filter_by": "id:=4258862608352808960",
            "page": i,
            "per_page": 250,	
            "include_fields": "*",
            "exclude_fields": "embedding",		
        }
        data = typesense_client.collections[collection_name].documents.search(search_parameters)			
        is_data_present = bool(len(data["hits"]))
        datas.extend([i["document"] for i in data["hits"]])
        i += 1

    print("found data:", len(datas), datas[0])

def fetch_all_data_from_jd_collection(collection_name, jd_id):
    datas = []
    search = "Ashok" # employee name or requesting company name
    search_query = f"&& $marketplace(name:{search}) || $candidate1(name:{search})" if search else ""
    search_parameters = {
        "q": "*",
        # "filter_by": f"jd_id:={jd_id} && stage:={"sourced"} {search_query}",
        "include_fields": "$marketplace(*),$candidate1(*)",
        "page": 1,
        "per_page": 10,
        "prefix": False,
        "exclude_fields": "$marketplace(embedding),$candidate1(embedding)",
        "sort_by": "ranking_score:desc"
    }
    data = typesense_client.collections[collection_name].documents.search(search_parameters)			
    datas.extend([i["document"] for i in data["hits"]])

    print("data", len(datas), datas[0])


def fetch_all_data_from_employee_request():
    datas = []
    search = "John" # employee name or requesting company name
    search_query = f"$marketplace(name:{search}) || requesting_company_name:{search}"
    search_parameters = {
        "q": "*",
        # Note: Reference query_by searching is not working
        # "filter_by": f"source_company_id:={1} && status:={'PENDING'} && ({search_query})",
        "include_fields": "$marketplace(*)",
        "page": 1,
        "per_page": 10,
        "prefix": False,
        "exclude_fields": "$marketplace(embedding)",
        "sort_by": "created_at:desc"
    }
    data = typesense_client.collections["employee_request"].documents.search(search_parameters)			
    datas.extend([i["document"] for i in data["hits"]])

    print("data", len(datas), datas)


def import_jsonl_file_to_collection(collection_name, file_name):
    """
    Imports data from a JSONL file into a specified Typesense collection.

    Args:
        collection_name (str): The name of the Typesense collection to import data into.

    Returns:
        dict: A response from the Typesense server indicating the result of the import operation.
    """
    res = None
    with open(file_name) as jsonl:
        res = typesense_client.collections[collection_name].documents.import_(
             jsonl.read().encode('utf-8'), {"action": "create"}
        )

    return res

# id : '4258862608352808960' in market place
# id : 1000 in jd0 collection

# create_document(
#     collection_name="marketplace",
#     document={
#     "work_type": "Full_Time",
#     "company_id": 99,
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
#     "total_experience": 13.00,
#     "updated_at": 1736383198,
#     "visibility": "PUBLIC",
#     "current_status": "ACTIVE",
#     "requests":[
#         {
#             "company_id": 1,
#             "status": "PENDING"
#         }
#     ]
#     }
# )

# create_document(
#     collection_name="jd0",
#     document={
#         'id': '1001', 
#         'is_ranked': True, 
#         'jd_id': '4253550266886918144', 
#         'marketplace': None, 
#         'ranking_score': 15.0, 
#         'stage': 'SOURCED', 
#         'status': 'QUALIFIED',
#         'candidate': '4258862607581057024'
#     }
# )

# create_document(
#     collection_name="jd0",
#     document={
#         'id': '1002', 
#         'is_ranked': True, 
#         'jd_id': '4253550266886918144', 
#         'marketplace': '4295020289387925504', 
#         'ranking_score': 15.4, 
#         'stage': 'SOURCED', 
#         'status': 'QUALIFIED',
#         'candidate': None
#     }
# )

# create_document(
#     collection_name="employee_request",
#     document={
#         'id': '1', 
#         'jd_id': '4243205049994448896', 
#         'marketplace': '4283336314311413760', 
#         'requesting_user_id': 3912326645730512897, 
#         'requesting_company_id': 2, 
#         'requesting_company_name': "Test Company",
#         'source_company_id': 1,
#         'updated_at': int(datetime.now().timestamp()),
#         'created_at': int(datetime.now().timestamp()),
#         'status': 'PENDING',
#     }
# )

# request_ids = ['1', '2']
# data = {"status": "APPROVED", "updated_at": int(datetime.now().timestamp())}
# filter_by = f"id:[{",".join(request_ids)}]"
# update_count = typesense_client.collections["employee_request"].documents.update(
#     data, {"filter_by": {filter_by}}
# ).get("num_updated", 0)

# print(update_count)
# fetch_all_data_from_employee_request()

def bulk_update_or_create_marketplace_candidates_requests(data_list: list[dict[str, Any]]) -> int:
    """
    updates: list of dicts with keys 'id', 'jd_id', 'status'
    returns: number of successful updates
    """
    update_requests = []
    data_dict = {
        str(data["id"]): data
        for data in data_list
    }
    typesense_data = typesense_client.collections["marketplace"].documents.search({
        "q":  "*",
        "filter_by": f"id:[{",".join(data_dict.keys())}]",
        "per_page": len(data_dict),
    })
    # extract only the actual data
    documents: list[dict[str, Any]] = [i["document"] for i in typesense_data["hits"]]
    for doc in documents:
        update_data = data_dict[doc["id"]]
        requests: list = doc.get("requests", [])
        for request in requests:
            # If exists update
            if update_data["jd_id"]==request["jd_id"]:
                request["status"] = update_data["status"]
                break
        else: # Add new
            requests.append({
                "jd_id": update_data["jd_id"],
                "status": update_data["status"]
            })
        update_requests.append({
            "id": doc["id"],
            "requests": requests
        })

    result: list = typesense_client.collections["marketplace"].documents.import_(
        update_requests, {"action": "emplace"}
    )

    return len(result)


convert_json_to_jsonl()