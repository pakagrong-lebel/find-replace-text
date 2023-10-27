# Python script to find and replace text in a file
def find_replace(file_path, search_text, replace_text):
    with open(file_path, search_text, replace_text):
        with open(file_path, 'r') as f:
            text = f.read()
            modified_text = text.replace(search_text, replace_text)
            with open(file_path, 'w') as f:
                f.write(modified_text)