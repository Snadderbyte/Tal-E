from fastdownload import FastDownload
import zipfile

d = FastDownload()
url = 'https://github.com/Jakobovski/free-spoken-digit-dataset/archive/refs/heads/master.zip'
path = d.download(url)
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('../data/raw')

d.rm(url)