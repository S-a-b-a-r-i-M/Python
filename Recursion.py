#FACTORIAL
'''
def factorial(num):
    if num<=1:
        return 1
    fact=num * factorial(num-1)
    return fact

num=int(input("enter the number:"))
print(factorial(num))
'''

# BUILDING TEAM STRUCTURE
from typing import Any


all_team = [
    {
        "id": 1,
        "name": "Shivanand",
        "subordinate": [2, 3]
    },
    {
        "id": 2,
        "name": "Rina",
        "subordinate": []
    },
    {
        "id": 3,
        "name": "Shudipto",
        "subordinate": [4, 6]
    },
    {
        "id": 4,
        "name": "Sabari",
        "subordinate": [5]
    },
    {
        "id": 5,
        "name": "Arasu",
        "subordinate": []
    },
    {
        "id": 6,
        "name": "Tamil",
        "subordinate": []
    },
]


def build_teams(users):
    # Construct all_team_dict
    users_dict = { user["id"] : user for user in users }
    
    def _build_teams(lead_id):
        if lead_id not in users_dict:
            raise KeyError(f"Given {lead_id} is not present in users_dict")
        
        leader = users_dict[lead_id].copy()
        team = []
        for subordinate_id in leader.get("subordinate", []):
            team.append(_build_teams(subordinate_id))

        leader["team"] = team
        return leader

    return _build_teams(1) # call the function with lead id


# Helper function to print team structure
def print_team_structure(team: dict[str, Any], level: int = 0) -> None:
    """
    Prints the team structure in a hierarchical format.
    
    Args:
        team: Team dictionary with nested structure
        level: Current indentation level (default: 0)
    """
    indent = "  " * level
    print(f"{indent}|\n{indent}-->: {team.get('name', f'User {team['id']}')}")
    
    for member in team["team"]:
        print_team_structure(member, level + 1)


print_team_structure(build_teams(all_team))
