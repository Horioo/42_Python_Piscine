import numpy as np
from PIL import Image
from load_image import ft_load


def ft_invert(image: np.ndarray) -> np.ndarray:
    print(image)
    image = image.squeeze()
    inverted_image_arr = 255 - image

    inverted_image = Image.fromarray(inverted_image_arr)
    inverted_image.show()
    return inverted_image


def ft_red(image: np.ndarray) -> np.ndarray:
    print(image)


def ft_green(image: np.ndarray) -> np.ndarray:
    print(image)


def ft_blue(image: np.ndarray) -> np.ndarray:
    print(image)


def ft_grey(image: np.ndarray) -> np.ndarray:
    print(image)


def main():
    image = ft_load("landscape.jpg")
    ft_invert(image)


if __name__ == "__main__":
    main()
