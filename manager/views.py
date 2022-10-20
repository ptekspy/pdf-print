import io
import os
from .get_pdf.data import positions
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import FileResponse
from reportlab.pdfgen import canvas

from .get_pdf.contract_to_pdf_data import convert
from .get_pdf.print_to_pdf import generatePdf

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


def generate_canvas(buffer):
    # Create a new PDF with Reportlab
    dpi = 300
    mmwidth = 150
    mmheight = 105
    pixwidth = int(mmwidth / 25.4 * dpi)
    pixheight = int(mmheight / 25.4 * dpi)
    can = canvas.Canvas(buffer, pagesize=(pixwidth, pixheight))
    can.setFont('Helvetica', 7)
    return can


def index(request):
    data = convert(contract)
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; inline; filename="somefilename.pdf"'
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # p.drawImage('default.pdf', 0, 0)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    for key in positions.keys():
        p.drawString(positions[key]["x"], positions[key]["y"], f"{data[key]}")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    new_pdf = PdfFileReader(buffer)
    # Read your existing PDF
    output = PdfFileWriter()
    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    existing_pdf = PdfFileReader(open(os.path.join(os.path.abspath(os.path.dirname(__file__)),"default.pdf"), "rb"))
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    bytes_stream = io.BytesIO()
    # page.write(bytes_stream)
    return FileResponse(page, as_attachment=False, filename='hello.pdf')
