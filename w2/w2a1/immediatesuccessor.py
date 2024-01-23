from datetime import datetime, timedelta

dateinput = input()

valid = '%Y-%m-%d'

try:
    parsed_date = datetime.strptime(dateinput, valid)
    end_date = parsed_date + timedelta(days=1)
    print(f"Next Date:{end_date}")
except ValueError:
    print(f"Input format ERROR. Correct Format: YYYY-MM-DD")