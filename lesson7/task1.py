import os


def group_rename_files(desired_name, num_digits, source_extension, target_extension, name_range=None):
    if name_range is None:
        name_range = [0, 0]  

    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if f.endswith(source_extension)]

    counter = 1
    for filename in files:
        if name_range[1] <= len(filename) >= name_range[0]:
            original_name = filename[name_range[0] - 1:name_range[1]]
            new_name = desired_name + f"{counter:0{num_digits}d}"
            new_filename = original_name + new_name + target_extension

            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, new_filename))
            counter += 1


if __name__ == "__main__":
    # Example usage
    group_rename_files("NewFile_", 3, ".txt", ".doc", name_range=[3, 6])
