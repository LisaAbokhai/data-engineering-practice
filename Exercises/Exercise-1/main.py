import requests
import os, zipfile
from io import BytesIO


download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def main():
    # your code here

    def extract(download):
        directory_name = 'downloads'
        if not os.path.exists(directory_name):   # Make downloads folder if it does not exist
            os.makedirs(directory_name)
        
        for uri in download:
            filename= uri.split('/')[-1]  # Extract filename from url 
            file_path = os.path.join(directory_name, filename)
            r = requests.get(uri)  
            if r.ok: 
                    print(f'Downloading {filename} into {file_path}')
                    uri_zip= zipfile.ZipFile(BytesIO(r.content)) # Extract csv file from dowloaded zip file
                    uri_zip.extractall(file_path)
            else:
                print(f'Download failed with {filename}')


    extract(download_uris)



if __name__ == '__main__':
    main()
