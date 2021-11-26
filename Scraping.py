import csv
import pandas as pd
import requests
from utilities import GetFirstNumbersFromString
from bs4 import BeautifulSoup
url_prefix = "https://www.estesparkweather.net/archive_reports.php?date=202107"
total_days = 31
with open('July_report.csv', mode='w',encoding="utf-8") as csv_file:
    fieldnames = [
        'Date', 'Average temperature (°F)', 'Average humidity(%)',
        'Average dewpoint(°F)', 'Average barometer(in)', 'Average windspeed(pmh)',
        'Average gustspeed(mph)', 'Average direction (°deg)', 'Rainfall for month (in)',
        'Rainfall for year (in)', 'Maximum rain per minute', 'Maximum temperature (°F)',
        'Minimum temperature (°F)', 'Maximum humidity (%)'
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    page_html = requests.get(url_prefix)
    soup = BeautifulSoup(page_html.content,"html.parser")
    div = soup.find(id="main-copy")
    if(div):
        tables = div.find_all("table")
        i = 0
        for table in tables:
            if(i == total_days):
                break
            trs = table.find_all("tr")
            day = GetFirstNumbersFromString(trs[0].find("td").text)
            date = "2021-07-" + str(day)

            average_temperature = trs[1].find_all("td")
            average_humidity = trs[2].find_all("td")
            average_dewpoint = trs[3].find_all("td")
            average_barometer = trs[4].find_all("td")
            average_windspeed = trs[5].find_all("td")
            average_gustspeed = trs[6].find_all("td")
            average_direction = trs[7].find_all("td")
            rainfall_for_month = trs[8].find_all("td")
            rainfall_for_year = trs[9].find_all("td")
            maximum_rain_per_minute = trs[10].find_all("td")
            maximum_temperature = trs[11].find_all("td")
            minimum_temperature = trs[12].find_all("td")
            maximum_humidity = trs[13].find_all("td")
            writer.writerow({
                'Date':date,
                'Average temperature (°F)':GetFirstNumbersFromString(average_temperature[1].text),
                'Average humidity(%)':GetFirstNumbersFromString(average_humidity[1].text),
                'Average dewpoint(°F)':GetFirstNumbersFromString(average_dewpoint[1].text),
                'Average barometer(in)':GetFirstNumbersFromString(average_barometer[1].text),
                'Average windspeed(pmh)':GetFirstNumbersFromString(average_windspeed[1].text),
                'Average gustspeed(mph)':GetFirstNumbersFromString(average_gustspeed[1].text),
                'Average direction (°deg)':GetFirstNumbersFromString(average_direction[1].text),
                'Rainfall for month (in)':GetFirstNumbersFromString(rainfall_for_month[1].text),
                'Rainfall for year (in)':GetFirstNumbersFromString(rainfall_for_year[1].text),
                'Maximum rain per minute':GetFirstNumbersFromString(maximum_rain_per_minute[1].text),
                'Maximum temperature (°F)':GetFirstNumbersFromString(maximum_temperature[1].text),
                'Minimum temperature (°F)':GetFirstNumbersFromString(minimum_temperature[1].text),
                'Maximum humidity (%)':GetFirstNumbersFromString(maximum_humidity[1].text)

            })
            i = i + 1


file_name = "July_report.csv"
file_name_output = "July_report.csv"

df = pd.read_csv(file_name, sep=",")

# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  
df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
df.to_csv(file_name_output, index=False)