from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel, Field
import json


# model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash-8b",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     google_api_key="" # at .env
# ) 
# system_prompt = "Your task is to extract the data from the user text. Donot make up anything any information.If any field is not available return empty string"
# prompt = [SystemMessage(content=system_prompt)]

# class JdData(BaseModel):
#     years_of_experience: str = Field(description="Years of experience required for the job.")
#     location: str = Field(description="The job location. If remote just say `remote`")
#     skills: str = Field(description="The skills required for the job,exactly as mentioned in the text by user itself.This can be a larger text also depending upon user text.")
#     company_name: str = Field(description="The name of the company as mentioned in the text.")
#     visa_type: str =Field(description="The type of work visa , ex: l2, h4, C2C, w2, gc, H1, opt, cpt,etc ")
#     job_role: str =Field(description="Job designation/job role/job title.")

# def get_structured_data(text: str) -> JdData:
#     structured_model= model.with_structured_output(JdData)
#     list_of_text = [text[i:i+2000] for i in range(0, len(text), 2000)]
#     for i,chunk in enumerate(list_of_text):
#         struct_data=structured_model.invoke(prompt + [HumanMessage(content=chunk if i==0 else str(struct_data)+chunk)])  # noqa: F821
#     return struct_data 



class JdData(BaseModel):
    years_of_experience: str = Field(description="Years of experience required for the job.")
    location: str = Field(description="The job location. If remote just say `remote`")
    skills: str = Field(
        description="""The skills required for the job,exactly as mentioned in the text by user
        itself.This can be a larger text also depending upon user text."""
    )
    company_name: str = Field(description="The name of the company as mentioned in the text.")
    visa_type: str =Field(description="The type of work visa , ex: l2, h4, C2C, w2, H1, opt, etc ")
    job_role: str =Field(description="Job designation/job role/job title.")

# @singleton
class AIHelper:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-8b",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            google_api_key=""
        )

    def get_structured_jd_data(self, text: str) -> JdData:
        structured_model= self.model.with_structured_output(JdData)
        chunk_size = 2000
        list_of_text = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        prompt = self.get_prompt_for_structured_jd()

        for i,chunk in enumerate(list_of_text):
            struct_data = structured_model.invoke(
                prompt + [HumanMessage(content=chunk if i==0 else str(struct_data)+chunk)]  # noqa: RUF005, F821
            )

        return struct_data

    def get_prompt_for_structured_jd(self):
        system_prompt = """Your task is to extract the jd data from the user text.
        Donot make up anything any information.If any field is not available return empty string"""
        return [SystemMessage(content=system_prompt)]


jd_data = AIHelper().get_structured_jd_data("""We are looking for a skilled and dedicated Java Backend Developer to join our growing engineering team. The ideal candidate will have a minimum of 2 years of experience working with Java in a backend-focused role and a passion for building scalable, high-performance applications.
Key Responsibilities
Design, develop, and maintain high-quality Java-based backend services and APIs.
Collaborate with frontend developers, product managers, and other stakeholders to deliver innovative features and solutions.
Write clean, efficient, and maintainable code following best practices and coding standards.
Implement RESTful APIs and work with JSON/XML data formats.
Optimize application performance, scalability, and reliability.
Participate in code reviews, debugging, and troubleshooting to ensure code quality.
Integrate backend services with various data sources and third-party systems.
Work with databases, including schema design, query optimization, and data migration.
Maintain and improve application security, ensuring compliance with security best practices.
Qualifications
Minimum 2 years of experience in Java development, with a strong focus on backend development.
Solid understanding of Object-Oriented Programming (OOP) and Design Patterns.
Hands-on experience with Spring Framework (Spring Boot, Spring MVC, Spring Data).
Knowledge of RESTful APIs and experience with API design and implementation.
Proficiency with relational databases (e.g., MySQL, PostgreSQL) and familiarity with ORM frameworks (e.g., Hibernate).
Experience working with version control systems, preferably Git.
Strong debugging and troubleshooting skills.
Familiarity with Agile development methodologies and tools (e.g., JIRA, Confluence).
Nice to Have
Experience with microservices architecture and containerization tools (e.g., Docker, Kubernetes).
Familiarity with message brokers (e.g., RabbitMQ, Kafka).
Exposure to cloud platforms such as AWS, Azure, or GCP.
Knowledge of NoSQL databases (e.g., MongoDB, Redis).
Experience with CI/CD tools like Jenkins or GitLab CI.
What We Offer
Competitive salary and benefits package.
Opportunity to work on challenging and exciting projects.
Career growth and development opportunities within a dynamic and innovative environment.
Collaborative and inclusive work culture.""")

print(jd_data, type(jd_data))

# with open(f"jd_data.jsonl", "a") as file:
#       file.write(json.dumps(jd_data.model_dump()))
#       file.write("\n")

'''
# Core packages
pip install langchain
pip install langchain-google-genai  # For Google's Generative AI integration
pip install google-generativeai     # Required for Google AI backend
pip install pydantic               # For BaseModel and Field'''