import readdicom
import matplotlib.pyplot as plt

out = readdicom.read_file('./img/img1/DICOMDIR', 'Brain', 8)
print(out)

plt.imshow(out, cmap=plt.cm.bone) 
plt.show()