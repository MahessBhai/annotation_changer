import os

def swap_values_in_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.txt')]
    
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
        modified_lines = []
        for line in lines:
            parts = line.split()
            if len(parts) > 0:
                if parts[0] == '0': # previous label
                    parts[0] = '1' # updated label
                elif parts[0] == '1': #add more conditions for multi-class annotations
                    parts[0] = '0'
                else:
                    pass
            modified_line = ' '.join(parts) + '\n'
            modified_lines.append(modified_line)
        with open(file_path, 'w') as f:
            f.writelines(modified_lines)
directory_path = r"" # path
swap_values_in_files(directory_path)
print("Values swapped in all .txt files in the directory.")
