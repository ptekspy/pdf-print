def ifIs(value):
    if value:
        return value
    return ""

def convert(contract):
    driver = contract["driver"]
    secondaryDriver = contract["secondaryDriver"]
    homeAddress = [x for x in driver["addresses"] if x["addressType"] == 'H']
    if len(homeAddress) > 0:
        homeAddress = homeAddress[0]
    else:
        raise Exception("No Home Address")
    businessAddress = [x for x in driver["addresses"] if x["addressType"] == 'B']
    if len(businessAddress) > 0:
        businessAddress = businessAddress[0]
    
    l1 = [x for x in driver["licenses"] if x["licenseType"] == 'L1']
    if len(l1) > 0:
        l1 = l1[0]
    print(l1)
    l2 = [x for x in driver["licenses"] if x["licenseType"] == 'L2']
    if len(l2) > 0:
        l2 = l2[0]
    pa = [x for x in driver["licenses"] if x["licenseType"] == 'PA']
    if len(pa) > 0:
        pa = pa[0]
    car = contract["car"]
    data = {
        "formNumber": contract["formNumber"],
        "toBePaid": contract["toBePaid"],
        "toBePaidTwo": contract["toBePaidTwo"],
        "toBePaidThree": contract["toBePaidThree"],
        "firstNames": driver["firstNames"],
        "lastName": driver["lastName"],
        "addressLineOne": homeAddress["lineOne"],
        "addressLineTwo": homeAddress["lineTwo"],
        "addressLineThree": homeAddress["lineThree"],
        "addressLineFour": homeAddress["lineFour"],
        "contNo": driver["contNo"],
        "businessOne": businessAddress["lineOne"],
        "businessTwo": businessAddress["lineTwo"],
        "businessTelephone": businessAddress["telephone"],
        "licenseOneNumber": l1["licenseNumber"],
        "licenseOneCountry": l1["licenseCountry"],
        "licenseOneDate": l1["dateIssued"],
        "passportNumber": pa["licenseNumber"],
        "passportCountry": pa["licenseCountry"],
        "passportDate": pa["dateIssued"],
        "licenseTwoNumber": l2["licenseNumber"],
        "licenseTwoCountry": l2["licenseCountry"],
        "licenseTwoDate": l2["dateIssued"],
        "placeOfBirth": driver["placeOfBirth"],
        "dateOfBirth": driver["dateOfBirth"],
        "secondaryDriver": f'{secondaryDriver["firstNames"]} {secondaryDriver["lastName"]}' if secondaryDriver else "",
        "storeToBeCheckedInExpected": contract["storeToBeCheckedInExpected"],
        "storeToBeCheckedInActual": contract["storeToBeCheckedInActual"],
        "storeRentedFrom": contract["storeRentedFrom"],
        "carModel": car["carModel"],
        "carLicense": car["carLicense"],
        "carOwner": car["carOwner"],
        "carGroup": car["carGroup"],
        "carCharge": car["carCharge"],
        "carTarrif": car["carTarrif"],
        "formTime": contract["formTime"],
        "formDate": contract["formDate"],
        "inDate": contract["inDate"],
        "inTime": contract["inTime"],
        "outDate": contract["outDate"],
        "outTime": contract["outTime"]
    }
    return data

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
    convert(contract)