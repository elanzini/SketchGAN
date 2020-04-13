import ndjson
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.interpolate import interp1d
from bresenham import bresenham
from progressbar import ProgressBar
            
# ---------------------
#  Helpers
# ---------------------
def get_sketch_from_drawing(drawing):
    # Create an empty canvas
    sketch = np.full((256,256), 256)
    for stroke in drawing:
        i = 1
        while i < len(stroke[0]):
            # Draw a line between each point
            for point in bresenham(stroke[1][i-1], stroke[0][i-1], stroke[1][i], stroke[0][i]):
                sketch[point[0]][point[1]] = 0
            i += 1
    return sketch

def draw_sketch(drawing):
    sketch = get_sketch_from_drawing(drawing)
    plt.imshow(sketch, cmap = 'gray')
    plt.show()

def get_average(sketches):
    avg = np.full((28,28), 0)
    for sketch in sketches:
        sketch = np.abs(256 - get_sketch_from_drawing(sketch))
        avg = np.add(sketch, avg)
    avg = avg / len(sketches)
    avg = np.abs(256 - avg)
    return avg

def get_average_sketches(sketches):
    avg = np.full((28,28), 0)
    for sketch in sketches:
        sketch = np.abs(256 - sketch)
        avg = np.add(sketch, avg)
    avg = avg / len(sketches)
    avg = np.abs(256 - avg)
    return avg

def map_to_range(img):
    temp = np.full((28,28), 0)
    m = interp1d([img.min(), img.max()],[0,255])
    for i in range(len(img)):
        for j in range(len(img[0])):
            temp[i][j] = m(img[i][j])
    return temp

def load_n_sketches_for_display(n, filename = 'airplane.ndjson'):
    count = 0
    sketches = []
    with open(filename) as f:
        data = ndjson.load(f)
    bar = ProgressBar(maxval = n).start()
    for i in range(n):
        temp = get_sketch_from_drawing(data[i]["drawing"])
        sketches.append(temp)
        count += 1
        bar.update(count)
    bar.finish()
    return np.asarray(sketches)

# -------------------------------------
#  Core - default file is circle.ndjson
# -------------------------------------

def load_n_sketches(n, filename = 'circle.ndjson'):
    count = 0
    sketches = []
    with open(filename) as f:
        data = ndjson.load(f)
    bar = ProgressBar(maxval = n).start()
    for i in range(n):
        temp = get_sketch_from_drawing(data[i]["drawing"]) / 256
        im = Image.fromarray(np.uint8(temp * 255)).resize((28,28))
        im_norm = map_to_range(np.array(im))
        sketches.append(im_norm)
        count += 1
        bar.update(count)
    bar.finish()
    return np.asarray(sketches)