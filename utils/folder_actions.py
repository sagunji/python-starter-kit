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
    print("hello")
    # if not os.path.exists(directory):
    #     os.makedirs(directory)


def is_file_accepted(accepted_files, filename):
    """
    Checks if file is acceptable or not

    :param accepted_files:
    :type accepted_files: list of files accepted
    :param filename: name of the file to be checked
    :type filename: string
    :return: True if file is accepted else false
    :rtype: boolean
    """
    ext = filename.split(".").pop()
    return ext in accepted_files
