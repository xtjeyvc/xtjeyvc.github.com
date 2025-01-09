import pandas as pd
from markdownify import markdownify
import os

# 替换为你实际存放Excel文件的路径
excel_file_path = r"C:\Users\one\Desktop\业务讲堂\112.xlsx"

# 读取Excel文件
try:
    df = pd.read_excel(excel_file_path)
except Exception as e:
    print(f"Error reading Excel file: {e}")
    exit(1)

# 确保Excel文件有两列
if len(df.columns) != 2:
    print("Excel file must have exactly two columns: Title and Content.")
    exit(1)

# 获取列名
title_col = df.columns[0]
content_col = df.columns[1]

# 创建保存Markdown文件的目录
output_dir = r"C:\Users\one\Desktop\业务讲堂"
os.makedirs(output_dir, exist_ok=True)

# 处理每一行数据
for index, row in df.iterrows():
    title = row[title_col]
    content = row[content_col]
    
    # 确保title和content是字符串类型
    if pd.isna(title):
        title = ""
    else:
        title = str(title)
    
    if pd.isna(content):
        content = ""
    else:
        content = str(content)
    
    # 将HTML内容转换为Markdown
    markdown_content = markdownify(content)
    
    # 创建文件名，去除非法字符
    safe_title = ''.join(c for c in title if c.isalnum() or c in ' _-')
    file_name = f"{index + 1}_{safe_title}.md"
    file_path = os.path.join(output_dir, file_name)
    
    # 保存Markdown文件
    with open(file_path, "w", encoding="utf-8") as md_file:
        md_file.write(f"# {title}\n\n{markdown_content}")
    
    print(f"Successfully saved {title} as {file_name}")
    
    # 更新Excel文件中的文件名
    df.at[index, title_col] = file_name

# 保存更新后的Excel文件
updated_excel_file_path = r"C:\Users\one\Desktop\业务讲堂\112_updated.xlsx"
df.to_excel(updated_excel_file_path, index=False, engine='openpyxl')

print(f"All Markdown files have been created and Excel file has been updated to {updated_excel_file_path}.")