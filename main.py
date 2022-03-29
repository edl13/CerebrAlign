import readdicom
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

out = readdicom.read_file('./img/img1/DICOMDIR', 'Brain', 8)

print(out)

Plot, Axis = plt.subplots()
plt.subplots_adjust(bottom=0.25)

frame = 0
plt.imshow(out[frame,:,:], cmap=plt.cm.bone) 
axframe = plt.axes([0.25, 0.1, 0.65, 0.03])
sframe = Slider(axframe, 'Frame', 0, 24, valinit=0)

def update(val):
    frame = int(np.around(sframe.val))
    print(frame)
    plt.subplot(111)
    plt.subplots_adjust(left=0.25, bottom=0.25)
    plt.imshow(out[frame,:,:])

sframe.on_changed(update)

plt.show()