from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoom(image: list, start_r: int, end_r: int, start_c: int, end_c: int) \
        -> np.ndarray:
    """
    Crop a region of an image and convert it to grayscale.
ft_load
    The function extracts a slice of the image using the given row and
    column indices. If the image has RGB channels, it converts the
    cropped region to grayscale using a luminance formula.

    Args:
        image (list | numpy.ndarray): Image array to process.
        start_r (int): Starting row index of the slice.
        end_r (int): Ending row index of the slice.
        start_c (int): Starting column index of the slice.
        end_c (int): Ending row index of the slice.

    Returns:
        list: Grayscale cropped image with shape (H, W, 1).

    Raises:
        TypeError: If the provided image is not a NumPy array.
        ValueError: If the sake a function that takes a path as argument,
                    writes thelice indices are outside the image bounds
                    or if the start indices are greater than the end indices
    """
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("Image must be a numpy array")
        h, w = image.shape[:2]

        if end_r > h or end_c > w:
            raise ValueError("Slice outside image bounds")
        if start_r > end_r or start_c > end_c:
            raise ValueError("Start value is bigger than End value")

        new_image = image[start_r:end_r, start_c:end_c]

        if new_image.ndim == 3:
            new_image_gray = np.dot(
                new_image[..., :3], [0.2989, 0.5870, 0.1140])
        else:
            new_image_gray = new_image

        new_image_gray_1 = new_image_gray[:, :, np.newaxis]

        print(f"The shape of image is: \
{new_image_gray_1.shape} or {new_image_gray.shape}")
        print(new_image_gray_1.astype(np.uint8))
        return new_image_gray_1
    except TypeError as e:
        raise Exception(f"TypeError: {e}")
    except ValueError as e:
        raise Exception(f"ValueError: {e}")


def rotate(image: list, start_r: int, end_r: int, start_c: int, end_c: int) \
        -> np.ndarray:
    """
    Receive an Image and Transpose it without the use of libraries

    The function extracts a slice of the image using the given row and
    column indices

    Args:
        image (list | numpy.ndarray): Image array to process.
        start_r (int): Starting row index of the slice.
        end_r (int): Ending row index of the slice.
        start_c (int): Starting column index of the slice.
        end_c (int): Ending row index of the slice.

    Returns:
        list: Grayscale Transposed image with shape (H, W).
    """
    crop_image = zoom(image, start_r, end_r, start_c, end_c)

    crop_image = crop_image.squeeze()

    h, w = crop_image.shape

    transposed_image = np.empty((w, h), dtype=crop_image.dtype)

    for i in range(h):
        for j in range(w):
            transposed_image[j, i] = crop_image[i, j]

    print(f"New shape after Transpose: {transposed_image.shape}")
    print(transposed_image)

    return transposed_image


def main():
    image = ft_load("animal.jpeg")
    new_image = rotate(image, 105, 505, 450, 850)
    plt.imshow(new_image, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
