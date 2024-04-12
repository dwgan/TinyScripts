import os
import sys
import fitz  # PyMuPDF

def remove_signatures(source_folder, target_folder):
    # 遍历源文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith(".pdf"):
                source_path = os.path.join(root, filename)
                # 创建与源文件夹结构相同的目标文件夹结构
                relative_path = os.path.relpath(root, source_folder)
                target_path_root = os.path.join(target_folder, relative_path)
                if not os.path.exists(target_path_root):
                    os.makedirs(target_path_root)

                target_path = os.path.join(target_path_root, filename)

                # 打开源PDF文件
                doc = fitz.open(source_path)
                new_doc = fitz.open()

                # 复制内容到新文档
                for page in doc:
                    new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
                    new_page.show_pdf_page(new_page.rect, doc, page.number)

                # 保存新文档到目标文件夹
                new_doc.save(target_path)
                new_doc.close()
                doc.close()
                print(f"Processed {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_signature.py <source_folder> <target_folder>")
    else:
        source_folder = sys.argv[1]
        target_folder = sys.argv[2]
        remove_signatures(source_folder, target_folder)
