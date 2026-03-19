import numpy as np
from PIL import Image
from load_image import ft_load


def ft_invert(array) -> np.ndarray:
    """
    Inverts the colors of the image received

    Args:
        array : Image to invert colors

    Returns:
        np.ndarray: An array with the inverted colors

    Raises:
        AssertError: If the image is not RGB
    """
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except AssertionError as e:
        raise Exception(f"AssertError: {e}")

    print(array)
    array = array.squeeze()
    inverted_image_arr = 255 - array

    inverted_image = Image.fromarray(inverted_image_arr)
    inverted_image.show()
    return inverted_image


def ft_red(array) -> np.ndarray:
    """
    Applies a Red Filter to the image by nullyfing the Green and Blue Values
    on RGB

    Args:
        array : Image to apply the red filter

    Returns:
        np.ndarray: An array with the red filter applied

    Raises:
        AssertError: If the image is not RGB
    """
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except AssertionError as e:
        raise Exception(f"AssertError: {e}")

    print(array)
    red_image_arr = array.copy()
    red_image_arr[..., 1] = 0
    red_image_arr[..., 2] = 0

    red_image = Image.fromarray(red_image_arr)
    red_image.show()
    return red_image


def ft_green(array) -> np.ndarray:
    """
    Applies a Green Filter to the image by nullyfing the Red and Blue Values
    on RGB

    Args:
        array : Image to apply the green filter

    Returns:
        np.ndarray: An array with the green filter applied

    Raises:
        AssertError: If the image is not RGB
    """
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except AssertionError as e:
        raise Exception(f"AssertError: {e}")

    print(array)
    green_image_arr = array.copy()
    green_image_arr[..., 0] = 0
    green_image_arr[..., 2] = 0

    green_image = Image.fromarray(green_image_arr)
    green_image.show()
    return green_image


def ft_blue(array) -> np.ndarray:
    """
    Applies a Blue Filter to the image by nullyfing the Green and Red Values
    on RGB

    Args:
        array : Image to apply the blue filter

    Returns:
        np.ndarray: An array with the blue filter applied

    Raises:
        AssertError: If the image is not RGB
    """
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except AssertionError as e:
        raise Exception(f"AssertError: {e}")

    print(array)
    blue_image_arr = array.copy()
    blue_image_arr[..., 0] = 0
    blue_image_arr[..., 1] = 0

    blue_image = Image.fromarray(blue_image_arr)
    blue_image.show()
    return blue_image


def ft_grey(array) -> np.ndarray:
    """
    Applies a GreyScale Filter to the image using only Division
    It take only the green value because its the closest for the human eye

    Args:
        array : Image to apply the red filter

    Returns:
        np.ndarray: An array with the red filter applied

    Raises:
        AssertError: If the image is not RGB
    """
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except AssertionError as e:
        raise Exception(f"AssertError: {e}")

    print(array)
    grey_image_arr = array.copy()
    grey_image_arr = array[..., 1]

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
