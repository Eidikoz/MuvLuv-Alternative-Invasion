import os

def remove_script_blocks(text):
    """Manually remove script blocks that start with '2099.1.1 = {' and end with '}'."""
    lines = text.splitlines()
    new_lines = []
    inside_block = False
    brace_count = 0

    for line in lines:
        if "1938.10.25 =" in line:  
            inside_block = True
            brace_count = line.count("{") - line.count("}")  
            continue  

        if inside_block:
            brace_count += line.count("{") - line.count("}")  
            if brace_count <= 0:  
                inside_block = False
            continue  

        new_lines.append(line)  

    return "\n".join(new_lines)

def process_folder(folder_path):
    """Process all files in the folder with a stack-based removal approach."""
    processed_count = 0  

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()

                cleaned_content = remove_script_blocks(content)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(cleaned_content)

                processed_count += 1
                print(f"Processed: {filename} ({processed_count})")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Specify your folder path here
folder_path = r"C:/Users/Stang/Documents/Paradox Interactive/Hearts of Iron IV/mod/MuvLuvAlternativeInvasion/history/states"  # Change this to your actual folder path
process_folder(folder_path)