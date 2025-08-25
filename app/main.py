def copy_file(command: str) -> None:
    try:
        parts = command.split()
        if len(parts) != 3:
            print("Invalid command format. Please provide a valid 'cp' command.")
            return

        _, source_file, destination_file = parts

        if source_file == destination_file:
            print("Source and destination files have the same name. Nothing to copy.")
            return

        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
            print(f"Content from '{source_file}' copied to '{destination_file}' successfully.")

    except FileNotFoundError:
        print("One or both files not found. Please check the file names.")
