import os


def remove_file(file_path):
    """
    Removes file

    :param file_path:
    :type file_path: string
    """
    if os.path.isfile(file_path):
        os.remove(file_path)


def remove_folder(folder_path):
    """
    Removes directory

    :param folder_path:
    :type folder_path: string
    """
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


def make_directory(directory):
    """
    Creates a directory in specified location

    :param directory:
    :type directory: string
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
