import os
import PyPDF2

def list_pdf_files(folder_path):
    """List full path of all PDF files in the folder."""
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

def get_pdf_text(file_path):
    """Extract text from all pages of a PDF file."""
    text = ''
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def compare_pdf_files(folder_a, folder_b):
    # List and sort PDF files in both folders
    pdfs_folder_a = sorted(list_pdf_files(folder_a))
    pdfs_folder_b = sorted(list_pdf_files(folder_b))
    
    # Compare file names and count
    names_a = [os.path.basename(f) for f in pdfs_folder_a]
    names_b = [os.path.basename(f) for f in pdfs_folder_b]
    
    if names_a == names_b and len(pdfs_folder_a) == len(pdfs_folder_b):
        print("The names and number of files are the same.")
    else:
        print("The names or number of files differ.")
    
    # For files with the same name, compare their contents
    for file_a, file_b in zip(pdfs_folder_a, pdfs_folder_b):
        if os.path.basename(file_a) == os.path.basename(file_b):
            text_a = get_pdf_text(file_a)
            text_b = get_pdf_text(file_b)
            
            if text_a == text_b:
                print(f"The contents of {os.path.basename(file_a)} are the same.")
            else:
                print(f"The contents of {os.path.basename(file_a)} differ.")
        else:
            print(f"Cannot compare contents of {os.path.basename(file_a)} and {os.path.basename(file_b)} because their names differ.")

# Example usage:
folder_a = 'path/to/folder/A'
folder_b = 'path/to/folder/B'
compare_pdf_files(folder_a, folder_b)
