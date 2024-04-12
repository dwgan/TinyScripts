import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(source_pdf, output_folder, pages_per_split=100):
    reader = PdfReader(source_pdf)
    total_pages = len(reader.pages)

    base_name = os.path.splitext(os.path.basename(source_pdf))[0]

    for start in range(0, total_pages, pages_per_split):
        writer = PdfWriter()
        end = min(start + pages_per_split, total_pages)
        for page_number in range(start, end):
            writer.add_page(reader.pages[page_number])
        
        split_filename = os.path.join(output_folder, f'{base_name}_{start+1}_{end}.pdf')
        with open(split_filename, 'wb') as output_pdf:
            writer.write(output_pdf)
        
        print(f'Created: {split_filename}')

def process_folder(source_folder, target_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                source_pdf = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_folder)
                output_folder = os.path.join(target_folder, relative_path)
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                split_pdf(source_pdf, output_folder)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python split_pdf.py <source_folder> <target_folder>")
    else:
        source_folder = sys.argv[1]
        target_folder = sys.argv[2]
        process_folder(source_folder, target_folder)
