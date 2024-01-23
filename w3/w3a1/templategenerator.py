moreletters = input()

while True:
    if moreletters == "Yes":

        offer_type = input()
        firstname = input()

        if len(firstname) > 10 or len(firstname) < 2:
            print("Input error")
            quit()

        lastname = input()
        if len(lastname) > 10 or len(lastname) < 2:
            print("Input error")
            quit()

        jobtitle = input()
        if len(jobtitle) < 10:
            print("Input error")
            quit()

        if offer_type == "Job Offer":

            yearlysalary = input()

            salary_float = yearlysalary.replace('.', '')

            salary_float = salary_float.replace(',', '.')

            salary_float = float(salary_float)

            if salary_float <= 20000.00:
                print("Input error")
                quit()
            if salary_float >= 80000.00:
                print("Input error")
                quit()

            startdate = input()

            year, month, day = map(int, startdate.split('-'))
            if year not in {2021, 2022}:
                print("Input error")
                quit()
            if not (1 <= month <= 12 and 1 <= day <= 31):
                print("Input error")
                quit()

            if len(jobtitle) < 10:
                print("Input error")
                quit()

            print(f""" Here is the final letter to send:
Dear {firstname} {lastname},
After careful evaluation of your application for the position of {jobtitle},
we are glad to offer you the job. Your salary will be {yearlysalary} euro annually.
Your start date will be on {startdate}. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
            """)

            moreletters = input()

            if moreletters == "No":
                exit()
            else:
                exit()

        elif offer_type == "Rejection":
            feedbackadd = input()
            if feedbackadd == "No":
                print(f"""Here is the final letter to send:
Dear {firstname} {lastname},
After careful evaluation of your application for the position of {jobtitle},
at this moment we have decided to proceed with another candidate.
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
                """)

                if moreletters == "No":
                    exit()
                else:
                    exit()

            elif feedbackadd == "Yes":
                feedback = input()

                print(f""" Here is the final letter to send:
Dear {firstname} {lastname},
After careful evaluation of your application for the position of {jobtitle},
at this moment we have decided to proceed with another candidate.
Here we would like to provide you our feedback about the interview.
{feedback}
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
                """)

                if moreletters == "No":
                    exit()
                else:
                    exit()
            else:
                print("Input error")
        else:
            print("Input error")