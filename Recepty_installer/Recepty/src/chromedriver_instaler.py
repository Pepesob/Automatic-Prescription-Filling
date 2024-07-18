import requests
import wget
import zipfile
import os


def instal_chromedriver():
    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    with open(os.path.join(os.path.dirname(__file__), "resources", "chromedriver_version.txt"), "r") as f:
        if f.readline() == version_number:
            print("Driver is up to date")
            return

    # build the donwload url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    # download the zip file using the url built above
    try:
        latest_driver_zip = wget.download(download_url,'chromedriver.zip')
    except:
        print("Error when downloading")
        return

    # extract the zip file
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(os.path.dirname(__file__), "resources")) # you can specify the destination folder path here
    # delete the zip file downloaded above
    os.remove(latest_driver_zip)
    with open(os.path.join(os.path.dirname(__file__), "resources", "chromedriver_version.txt"), "w") as f:
        f.write(version_number)
    print("Succesfully instaled latest version of chromedriver")
