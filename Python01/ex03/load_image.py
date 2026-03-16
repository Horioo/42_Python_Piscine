import matplotlib.image as mpimg
import sys


# Needs a return type
def ft_load(path: str) -> list:
    """
    Load an image from a file and return it as a nested list
    of pixel values in RGB

    Args:
        path (str): Path to the image file to load.

    Returns:
        list: A 3D nested list representing the image
        For RGB images, the shape is (height, width, 3)

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be accessed due to permissions
        OSError: If the file cannot be read as an image.
    """
    try:
        img = mpimg.imread(path)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        sys.exit(0)
    except PermissionError as e:
        print(f"PermissionError: {e}")
        sys.exit(0)
    except OSError as e:
        print(f"OSError: {e}")
        sys.exit(0)

    print(f"The shape of image is: {img.shape}")
    print(img)
    return img


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
