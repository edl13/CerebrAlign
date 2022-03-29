from http.cookies import SimpleCookie
from pydicom import dcmread
from pydicom.fileset import FileSet
import numpy as np

def read_file(filename, SD, SN):
    path = filename
    dsAll = dcmread(path)
    fs = FileSet(dsAll)
    #print(fs)
   
    
    dsArr = fs.find(StudyDescription=SD, SeriesNumber=SN, load=True)

    dsStack = []
    for instance in dsArr:
        ds = instance.load()
        slice = np.array(ds.pixel_array)
        dsStack.append(slice)

    dsStack = np.stack(dsStack)

    return dsStack