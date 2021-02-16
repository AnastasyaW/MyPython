class HomePageData:

    # this is a dictionary data that will send to the test
    # - home page
    test_homePage_data = [
        {
            "firstName": "Rahul",
            "email": "Shetty@mail.here",
            "password": "PassHere",
            "gender": "Male",
        },
        {
            "firstName": "Alina",
            "email": "emailhere@mail.here",
            "password": "PassTwo",
            "gender": "Female",
        },
    ]

    @staticmethod
    def getTestDataExcell(test_case_name):
        dict = {}
        file = openpyxl.load_workbook("C:\\Users\\atcin\\Documents\\PythonDemo.xlxs")
        sheet = file.active
        for i in range(1, sheet.max_row + 1):
            if sheet.cell(row=i, colum=1).value == "testcase2":
                for x in range(2, sheet.max_column + 1):
                    # here we add the value into the dictionary
                    dict[sheet.cell(row=1, column=x).value] = sheet.cell(
                        row=i, column=x
                    ).value
        return [dict]
