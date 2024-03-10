import matplotlib.pyplot as plt
import numpy as np


img_src_path = 'concat_img.png'


img = plt.imread(img_src_path)


point_list = []

plt.imshow(img)
x = plt.ginput(-1,show_clicks=True, timeout=100)
point_list.append(x)
plt.show()

# === save the points locally
src_list = []
dst_list = []

for i,v in enumerate(point_list[0]):
    if (i+1) % 2 == 0:
        dst_list.append(v)
    else:
        src_list.append(v)

src_list = np.array(src_list)
dst_list = np.array(dst_list)
np.save("img_src_points_2", src_list)
np.save("img_dst_points_2", dst_list)
