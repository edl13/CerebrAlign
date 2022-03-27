import pydicom
from pydicom.data import get_testdata_file


def test_file():
    filename = get_testdata_file('MR_small.dcm')
    ds = pydicom.dcmread(filename)

    data = ds.pixel_array
    print('The image has {} x {} voxels'.format(data.shape[0], data.shape[1]))