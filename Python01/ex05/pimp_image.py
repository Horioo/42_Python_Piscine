import numpy as np
from PIL import Image
from load_image import ft_load


def ft_invert(image: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image received

    Args:
        image (np.ndarray): Image to invert colors

    Returns:
        np.ndarray: An array with the inverted colors
    """
    print(image)
    image = image.squeeze()
    inverted_image_arr = 255 - image

    inverted_image = Image.fromarray(inverted_image_arr)
    inverted_image.show()
    return inverted_image


def ft_red(image: np.ndarray) -> np.ndarray:
    """
    Applies a Red Filter to the image by nullyfing the Green and Blue Values
    on RGB

    Args:
        image (np.ndarray): Image to apply the red filter

    Returns:
        np.ndarray: An array with the red filter applied
    """
    print(image)
    red_image_arr = image.copy()
    red_image_arr[..., 1] = 0
    red_image_arr[..., 2] = 0

    red_image = Image.fromarray(red_image_arr)
    red_image.show()
    return red_image


def ft_green(image: np.ndarray) -> np.ndarray:
    """
    Applies a Green Filter to the image by nullyfing the Red and Blue Values
    on RGB

    Args:
        image (np.ndarray): Image to apply the green filter

    Returns:
        np.ndarray: An array with the green filter applied
    """
    print(image)
    green_image_arr = image.copy()
    green_image_arr[..., 0] = 0
    green_image_arr[..., 2] = 0

    green_image = Image.fromarray(green_image_arr)
    green_image.show()
    return green_image


def ft_blue(image: np.ndarray) -> np.ndarray:
    """
    Applies a Blue Filter to the image by nullyfing the Green and Red Values
    on RGB

    Args:
        image (np.ndarray): Image to apply the blue filter

    Returns:
        np.ndarray: An array with the blue filter applied
    """
    print(image)
    blue_image_arr = image.copy()
    blue_image_arr[..., 0] = 0
    blue_image_arr[..., 1] = 0

    blue_image = Image.fromarray(blue_image_arr)
    blue_image.show()
    return blue_image


def ft_grey(image: np.ndarray) -> np.ndarray:
    """
    Applies a GreyScale Filter to the image by using the Luminosity formula
    on the RGB values
    Formula: Y = 0.299 * R + 0.587 * G + 0.114 * B

    Args:
        image (np.ndarray): Image to apply the red filter

    Returns:
        np.ndarray: An array with the red filter applied
    """
    print(image)
    grey_image_arr = np.dot(
                image[..., :3], [0.2989, 0.5870, 0.1140])

    grey_image = Image.fromarray(grey_image_arr)
    grey_image.show()
    return grey_image


def main():
    image = ft_load("landscape.jpg")

    ft_invert(image)
    ft_red(image)
    ft_green(image)
    ft_blue(image)
    ft_grey(image)

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
