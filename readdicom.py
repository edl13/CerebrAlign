from pydicom import dcmread
from pydicom.fileset import FileSet
import numpy as np

def read_file(filename, SD, SN):
    path = filename
    dsAll = dcmread(path)
    fs = FileSet(dsAll)
    print(fs)
   
    dsArr = fs.find(StudyDescription=SD, SeriesNumber=SN, load=True)
    ds = dsArr[0].load()
    data = ds.pixel_array
    return data