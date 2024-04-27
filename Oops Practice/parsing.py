from typing import Dict

from jinja2 import Template
import re

# Your HTML content string with Jinja variables
html_content = ("<p><br></p><p><span style=\"color: rgb(34, 34, 34);font-size: small\">Hi {{NAME}},"
                "</span></p><p>​</p><p><span style=\"color: rgb(34, 34, 34);font-size: small\">We found your profile"
                "suitable for {{ROLE}} at Global Enterprise,&nbsp;</span>a&nbsp;dubai based consumer&nbsp;electronics "
                "product company&nbsp;<br></p><p><span style=\"color: rgb(34, 34, 34);font-size: small\">JD -{{"
                "jd_link}}</span><span style=\"color: rgb(34, 34, 34);font-size: small\">&nbsp;Pls let me know your "
                "Thank you</span></p><p>​</p><p><br></p>")

# Context data with values for Jinja variables
context = {
    'NAME': 'John Doe',
    'ROLE': 'Software Engineer',
    'JD_LINK': 'https://example.com/jd',
}


def template_parser(content: str, template_values: Dict):
    # Create a Jinja template object
    template = Template(content)
    # Render the template with the context data
    rendered_content = template.render(template_values)

    return rendered_content


#########################################################################################################

class CandidateTable:
    def __init__(self):
        self.name = "george"


class JD:
    def __init__(self):
        self.uuid = "fnf89ahybsia8"
        self.designation = "manager"
        self.company_name = "10xscale"


def get_defaults_values(
        cv: CandidateTable, jd: JD, form_link: str, tags: Dict | None
):
    link = f"https://jobapply.web.app/?uuid={jd.uuid}"
    di = {
        "NAME": cv.name,
        "CANDIDATE": cv.name,
        "DESIGNATION": jd.designation,
        "ROLE": jd.designation,
        "POSITION": jd.designation,
        "FROM": f'<a href="{link}">FROM</a>',
        "COMPANY": jd.company_name,
        "COMPANY NAME": jd.company_name,
        "JD_LINK": f'<a href="{link}">Check JD</a>',
        "name": cv.name,
        "candidate": cv.name,
        "designation": jd.designation,
        "role": jd.designation,
        "position": jd.designation,
        "from": f'<a href="{link}">FROM</a>',
        "company": jd.company_name,
        "company name": jd.company_name,
        "jd_link": f'<a href="{link}">Check JD</a>',
    }

    for key, value in tags.items():
        di[key] = value

    return di


def preprocessing():
    subject = "<h1>Invitation for Aptitude Test - {{COMPANY NAME}}</h1>"
    content = ("<p><br></p><p><span style=\"color: rgb(34, 34, 34);font-size: small\">Hi {{NAME}},"
               "</span></p><p>​</p><p><span style=\"color: rgb(34, 34, 34);font-size: small\">We found your profile "
               "suitable for {{ROLE}} at Global Enterprise,&nbsp;</span>a&nbsp;dubai based consumer&nbsp;electronics "
               "product company&nbsp;<br></p><p><span style=\"color: rgb(34, 34, 34);font-size: small\">JD -{{"
               "JD_LINK}}</span><span style=\"color: rgb(34, 34, 34);font-size: small\">&nbsp;Pls let me know your "
               "CTC, ECTC, and Notice Period, if interested</span></p><p><span style=\"color: rgb(34, 34, "
               "34);font-size: small\"><br></span></p><p><span style=\"color: rgb(34, 34, 34);font-size: "
               "small\">Thank you</span></p><p>​</p><p><br></p>")
    form_link = ""
    custom_email = None
    tags = {'NAME': 'sabari'}

    default_tag_values = get_defaults_values(CandidateTable(), JD(), form_link, tags)
    subject = template_parser(subject, default_tag_values)
    if not custom_email:
        content = template_parser(content, default_tag_values)
    else:
        content = custom_email

    return subject, content


preprocessing()
