import os


def get_all_folders(root_path=None, level=1):
    """
    Get a list of all folders found on the root path
    :param root_path: folder path
    :param level: how many folders level do you need to scan
    :return: list of folders
    """
    if not os.path.exists(root_path):
        return []

    all_paths = []
    for content in os.listdir(root_path):
        content_path = os.path.join(root_path, content)
        if not os.path.isdir(content_path):
            continue

        if level > 1:
            paths = get_all_folders(content_path, level-1)
            all_paths.extend(paths)
        else:
            all_paths.append(content_path)
    return all_paths
