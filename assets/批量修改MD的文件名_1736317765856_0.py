import os
import re

def clean_filename(filename):
    # 只保留字母、数字、汉字和下划线，其他字符替换为下划线
    cleaned = re.sub(r'[^\w\u4e00-\u9fff]', '_', filename)
    cleaned = cleaned.strip('_')  # 去除首尾的下划线
    return cleaned if cleaned else 'default_name'  # 防止空文件名

def rename_md_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        md_files = [f for f in files if f.endswith('.md')]
        total_files = len(md_files)
        
        if total_files == 0:
            print(f"No MD files found in {root}.")
            continue
        
        for index, md_file in enumerate(md_files, start=1):
            file_path = os.path.join(root, md_file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                
                if first_line:
                    new_file_name = clean_filename(first_line) + '.md'
                    new_file_path = os.path.join(root, new_file_name)
                    
                    # 确保文件名不以点号或空格开头
                    if new_file_name.startswith('.') or new_file_name.startswith(' '):
                        new_file_name = '_' + new_file_name
                    
                    # 避免文件名冲突
                    counter = 1
                    while os.path.exists(new_file_path):
                        new_file_name = f"{clean_filename(first_line)}_{counter}.md"
                        new_file_path = os.path.join(root, new_file_name)
                        counter += 1
                    
                    os.rename(file_path, new_file_path)
                    print(f'已替换 {index}/{total_files} in {root} - {md_file} -> {new_file_name}')
                else:
                    print(f'已跳过 {index}/{total_files} in {root} - {md_file} (第一行为空)')
            except Exception as e:
                print(f'处理文件 {md_file} 时出错: {e}')
        
        print(f'目录 {root} 处理完成')
    
    print('所有文件处理已完成')

# 使用示例：指定路径为 '/path/to/your/md/files'
directory_path = r'D:\资料中心\530  网站建设\logseq站点\docsify站点文件\home'  # 替换为你的目录路径
rename_md_files_in_directory(directory_path)