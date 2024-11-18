import os


def scan_files(folder_path, output_file):
    """
    Scans all files in a folder and writes their names to a text file.
    """
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Error: The folder '{folder_path}' does not exist.")
            return

        # Get a list of all files in the folder
        files = [
            f
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]

        # Write file names to the output text file
        with open(output_file, "w") as file:
            for f in files:
                # { src: "/api/placeholder/800/1000" },
                line = '{ src: "' + f"{folder_path}/{f}" + '" },\n'
                file.write(line)

        print(f"Successfully scanned files. List saved to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    folder_to_scan = "photos"
    output_file_path = "file-path-generator-output.txt"

    scan_files(folder_to_scan, output_file_path)
