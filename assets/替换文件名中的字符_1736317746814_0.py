import os

def remove_text_between_underscores_and_md(directory):
    for filename in os.listdir(directory):
        if '_文_' in filename and '.md' in filename:
            # 找到“_文_”和“.md”之间的字符串
            start_index = filename.find('_文_') + len('_文_')
            end_index = filename.find('.md')
            
            # 构造新的文件名
            new_filename = filename[:start_index] + filename[end_index:]
            
            # 重命名文件
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# 使用示例
directory_path = r'D:\资料中心\530  网站建设\logseq站点\pages\人民司法案例'
remove_text_between_underscores_and_md(directory_path)