from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from contract_to_pdf_data import convert
from data import positions
from django.conf import settings

def generatePdf(data):
    buffer = io.BytesIO()
    # Create a new PDF with Reportlab
    dpi = 300
    mmwidth = 150
    mmheight = 105
    pixwidth = int(mmwidth / 25.4 * dpi)
    pixheight = int(mmheight / 25.4 * dpi)
    can = canvas.Canvas(buffer, pagesize=(pixwidth, pixheight))
    can.setFont('Helvetica', 7)
    for key in positions.keys():
        can.drawString(positions[key]["x"], positions[key]["y"], f"{data[key]}")
        
    can.showPage()
    can.save()

    # Move to the beginning of the StringIO buffer
    buffer.seek(0)
    new_pdf = PdfFileReader(buffer)
    # Read your existing PDF
    existing_pdf = PdfFileReader(open("default.pdf", "rb"))
    output = PdfFileWriter()
    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # Finally, write "output" to a real file
    settings.configure()
    url = os.path.join(settings.BASE_DIR, settings.STATIC_ROOT, 'data', f'{data["formNumber"]}.pdf')
    outputStream = open(url, "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ == "__main__":
    contract = {
        "formNumber": "A1",
        "toBePaid": 500,
        "toBePaidTwo": 0,
        "toBePaidThree": 0,
        "storeToBeCheckedInExpected": "A",
        "storeToBeCheckedInActual": "A",
        "storeRentedFrom": "A",
        "formTime": "12:41",
        "formDate": "12/10/2022",
        "inDate": "19/10/2022",
        "inTime": "15:41",
        "outDate": "12/10/2022",
        "outTime": "12:42",
        "driver": {
            "firstNames": "Stephen James",
            "lastName": "Johnson",
            "contNo": "14564242345",
            "placeOfBirth": "England",
            "dateOfBirth": "17/02/1993",
            "addresses": [
                {
                    "addressType": "H",
                    "lineOne": "44 Summerset Street",
                    "lineTwo": "Bradford",
                    "lineThree": "England",
                    "lineFour": "BD4 8DG",
                },
                {
                    "addressType": "B",
                    "lineOne": "123 Parade Street",
                    "lineTwo": "Bradford",
                    "telephone": "01274567857"
                }
            ],
            "licenses": [
                {
                    "licenseType": "L1",
                    "licenseNumber": "1232343",
                    "licenseCountry": "England",
                    "dateIssued": "18-12-2018"
                },
                {
                    "licenseType": "L2",
                    "licenseNumber": "rfgdbdnhfgn",
                    "licenseCountry": "England",
                    "dateIssued": "18-12-2018"
                },
                {
                    "licenseType": "PA",
                    "licenseNumber": "76576575",
                    "licenseCountry": "England",
                    "dateIssued": "18-12-2018"
                }
            ]
        },
        "secondaryDriver": {
            "firstNames": "Sally Sarah",
            "lastName": "Johnson",
        },
        "car": {
            "carModel": "Ford Mondeo",
            "carLicense": "LA12 9NH",
            "carOwner": "Internal",
            "carGroup": "A",
            "carCharge": "J",
            "carTarrif": "L",
        }
    }
    data = convert(contract)
    generatePdf(data)