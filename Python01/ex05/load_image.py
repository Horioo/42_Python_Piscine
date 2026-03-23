import matplotlib.image as mpimg


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
        print(f"Error: FileNotFoundError: {e}")
        return None
    except PermissionError as e:
        print(f"Error: PermissionError: {e}")
        return None
    except OSError as e:
        print(f"Error: OSError: {e}")
        return None
    except Exception as e:
        print(f"Error: Exception: {e}")
        return None

    print(f"The shape of image is: {img.shape}")
    print(img)
    return img


def main():
    print(ft_load("ladsadasdndscape.jpg"))


if __name__ == "__main__":
    main()
