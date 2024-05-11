from pydantic import BaseModel

class PersonModel(BaseModel):
    name: str
    age: int 
    education: str = None
    profession: str = None

    def __str__(self):
        return f"{self.name}  {self.age} : {self.education} -> {self.profession}"

if __name__ == '__main__':
    person_dict = {
        "name": "sabari",
        "age": 21,
        "education": "BSc.CS",
        "profession": "Software Developer"
    }

    person = PersonModel(**person_dict)
    print(person)