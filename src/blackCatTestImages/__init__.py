from importlib.resources import files
from skimage import io, img_as_float
from skimage.color import rgb2gray
from skimage.filters import sobel
from matplotlib import pyplot
from mpl_toolkits.axes_grid1 import ImageGrid


def test_images(process, set):
    if(set == 1):
        img1_path = files('blackCatTestImages.images').joinpath('img1.jpg')
        img2_path = files('blackCatTestImages.images').joinpath('img2.jpg')
        img3_path = files('blackCatTestImages.images').joinpath('img3.jpg')

    else:
        img1_path = files('blackCatTestImages.images').joinpath('img4.jpg')
        img2_path = files('blackCatTestImages.images').joinpath('img5.jpg')
        img3_path = files('blackCatTestImages.images').joinpath('img6.jpg')

    img1 = io.imread(str(img1_path))
    img2 = io.imread(str(img2_path))
    img3 = io.imread(str(img3_path))

    print("processing first image")
    img1p = process(img1)
    print("processing second image")
    img2p = process(img2)
    print("processing third image")
    img3p = process(img3)
    print("processing complete")


    fig = pyplot.figure(figsize=(6, 8))
    grid = ImageGrid(fig, 111, nrows_ncols=(3,2), axes_pad=0.1)

    for ax, img in zip(grid, [img1, img1p, img2, img2p, img3, img3p]):
        ax.imshow(img)
        ax.axis('off')

    pyplot.show()

def process(img):
    processed = rgb2gray(img_as_float(img))
    processed = sobel(img)
    return processed


# test_images(process, 2)
