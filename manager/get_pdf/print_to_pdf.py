from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from .data import positions

def generatePdf(data, buffer, canvas, root):
    for key in positions.keys():
        canvas.drawString(positions[key]["x"], positions[key]["y"], f"{data[key]}")
        
    canvas.showPage()
    canvas.save()

    # Move to the beginning of the StringIO buffer
    buffer.seek(0)
    # return buffer
    new_pdf = PdfFileReader(buffer)
    # Read your existing PDF
    existing_pdf = PdfFileReader(open(f"{os.path.abspath(os.path.dirname(__file__))}/default.pdf", "rb"))
    output = PdfFileWriter()
    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # Finally, write "output" to a real file
    url = os.path.join(root, 'data', f'{data["formNumber"]}.pdf')
    print(url)
    outputStream = open(url, "wb")
    output.write(outputStream)
    outputStream.close()
    return outputStream
    

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
    # data = convert(contract)
    # generatePdf(data)