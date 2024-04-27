from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import io
import datetime
import base64


def generate_customer_agreement(signer_name, signer_address, poc_name, poc_designation):
    start_date = datetime.date.today()
    end_date = datetime.timedelta(weeks=3) + start_date

    agreement_text = f"""This Agreement is entered into by and between<b> Hire10x.ai (Mahadev Technologies LLC)</b> with its
    principal office at <b>#10167 W Avenida Del Rey, Peoria, AZ 85383</b>, (“referred as Company”) and
    <b>{signer_name}, {signer_address}</b> ("referred as Partner").<br/>
    This Agreement is valid for a period of <b>3 weeks</b> (“Term”) effective from {start_date} (start date)
    till {end_date} (end date)..<br/>
    Hire10x software license is given to the partner. The software application is intended to speedup the
    hiring/recruitment process facilitating the end-to-end hiring process from sourcing to interview until
    selection.<br/>
    The Partner will be given 50 phone credits + 50 email credits per license included in the current pricing
    model. Top Ups need to be purchased for additional phone/email credits. Company will provide
    support throughout the duration of 3 weeks.<br/>
    Any party can terminate this agreement by giving 7 days of advanced notice. Contract renewal with
    new terms may happen post the expiration of the current contract based on the interest of the partner.
    Product pricing will be discussed and agreed upon by call/email from Hire10x and the same will be
    disclosed in the renewed contract.<br/>
    This Agreement expresses the complete understanding of the parties with respect to the subject
    matter and supersedes all prior proposals, agreements, and representations. This Agreement and each
    party's obligations shall be binding on the representatives, assigns, and successors of such party.<br/>
    Each party has signed this Agreement through its authorized representative below.<br/><br/>
    For Mahadev Technologies LLC        {10 * '&nbsp'}     For {signer_name}
    Name: Thangalapalli Shivanand       {10 * '&nbsp'}     Customer Name: {poc_name}
    Designation: Director               {27 * '&nbsp'}     Designation: {poc_designation}"""

    return agreement_content_as_pdf_in_memory(signer_name, agreement_text)


def generate_customer_agreement_pdf(company_name, agreement_text, replacements):
    # Create a PDF file
    pdf_file_path = ("/home/hire10x/Progrmming practice/PycharmProjects/Practice_and_Learning_python"
                     "/Customer_Agreement_{}.pdf".format(company_name.split(' ')[0]))
    pdf_canvas = SimpleDocTemplate(pdf_file_path, pagesize=letter, topMargin=0)

    # Styles for different elements in the PDF
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading1"]
    body_style = styles["BodyText"]
    body_style.leading = 9

    # Content to be added to the PDF
    content = []

    # Signature Image
    signature_image = Image("/home/hire10x/Progrmming practice/PycharmProjects/Practice_and_Learning_python/agreement"
                            "-header.png", width=600, height=175)
    content.append(signature_image)
    content.append(Spacer(1, 10))

    # Title
    title_text = "<u>Partnership Agreement</u>"
    content.append(Paragraph(title_text, title_style))
    content.append(Spacer(1, 10))

    # Agreement Text Replacements
    for key, val in replacements.items():
        agreement_text = agreement_text.replace(key, val)

    agreement_text = agreement_text.replace('\n', '<br/><br/>')
    agreement_text = agreement_text.replace('<new_line>', '<br/>')
    agreement_paragraph = Paragraph(agreement_text, body_style)
    content.append(agreement_paragraph)
    content.append(Spacer(1, 10))

    # Build PDF document
    pdf_canvas.build(content)
    print(f"PDF generated successfully: {pdf_file_path}")
    with open(pdf_file_path, "rb") as file:
        content_bytes = file.read()

    base64_file_content = base64.b64encode(content_bytes).decode("ascii")
    return base64_file_content


def agreement_content_as_pdf_in_memory(company_name, agreement_text):
    # Create an in-memory file-like object
    pdf_bytes_io = io.BytesIO()

    # Styles for different elements in the PDF
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading1"]
    body_style = styles["BodyText"]
    body_style.leading = 9

    # Content to be added to the PDF
    content = []

    # Signature Image
    signature_image = Image("/home/hire10x/Progrmming practice/PycharmProjects/Practice_and_Learning_python/agreement"
                            "-header.png", width=600, height=175)
    content.append(signature_image)
    content.append(Spacer(1, 10))

    # Title
    title_text = "<u>Partnership Agreement</u>"
    content.append(Paragraph(title_text, title_style))
    content.append(Spacer(1, 10))

    agreement_text = agreement_text.replace('\n', '<br/><br/>')
    agreement_text = agreement_text.replace('<new_line>', '<br/>')
    agreement_paragraph = Paragraph(agreement_text, body_style)
    content.append(agreement_paragraph)
    content.append(Spacer(1, 10))

    # Build PDF document in-memory
    pdf_canvas = SimpleDocTemplate(pdf_bytes_io, pagesize=letter, topMargin=0)
    pdf_canvas.build(content)

    # Get content bytes from in-memory file-like object
    content_bytes = pdf_bytes_io.getvalue()

    # Return base64 encoding if needed
    base64_file_content = base64.b64encode(content_bytes).decode("ascii")
    return base64_file_content


if __name__ == '__main__':
    print(generate_customer_agreement("signer_name", "signer_address", "poc_name", "poc_designation"))
