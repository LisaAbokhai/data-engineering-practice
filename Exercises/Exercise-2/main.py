import pandas as pd
from requests import get
from bs4 import BeautifulSoup as bs


# assign the url 
url_download = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'


def main():
    # your code here 
    response = get(url_download)
    soup = bs(response.text, 'html.parser')
    files= soup.find_all('tr')
    
    # fetch the csv file based  on the date
    for file in files:
        if '2022-02-07 14:03' in file.get_text():
            download = file.a['href']
            break
    
    # create the link to the csv
    download_site = url_download + download

    # Turn the csv file into a dataframe
    csv_df = pd.read_csv(download_site, header= 0)

    #  find the max valyue in HourlyDryBulbTemperature col and return the records    
    print(csv_df.iloc[csv_df['HourlyDryBulbTemperature'].idxmax()])
    print(csv_df.query('HourlyDryBulbTemperature == HourlyDryBulbTemperature.max()'))
    print(csv_df.nlargest(1,['HourlyDryBulbTemperature']))
    



if __name__ == '__main__':
    main()
