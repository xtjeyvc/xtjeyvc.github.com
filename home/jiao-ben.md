### Python脚本



#### 1、采集脚本

```
# 打开TXT文件里的每一行网址，每10秒钟打开一个，每一个网址生成一个MD文件，文命以FYGB+四位数字的方式命名

import requests
from bs4 import BeautifulSoup
import os
import time

# 指定文件夹路径和TXT文件名
folder_path = r"G:\33"
txt_filename = "gongbao.txt"

# 读取TXT文件中的网址
with open(os.path.join(folder_path, txt_filename), 'r', encoding='utf-8') as file:
    urls = file.readlines()

# 计数器，用于生成四位数字
counter = 1

# 遍历每个网址
for url in urls:
    url = url.strip()  # 去除换行符

    # 发起GET请求获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取标题和正文内容
    #title = soup.title.text  #有titile的可以加上这个，注释去掉
    paragraphs = [p.text for p in soup.find_all('p')]

    # 生成Markdown文件名
    markdown_filename = f"FYGB{counter:04}.md"
    counter += 1

    # 写入Markdown文件
    with open(os.path.join(folder_path, markdown_filename), 'w', encoding='utf-8') as md_file:
        #md_file.write(f"# {title}\n\n") #有titile的可以加上这个，注释去掉
        for paragraph in paragraphs:
            md_file.write(f"{paragraph}\n\n")

    print("Successfully")

    # 控制每10秒打开一个网页
    time.sleep(10)

```

2、批量TXT转MD文档格式

```
# 这个脚本主要是将TXT文件批量转为MD文件
import os
import subprocess

# 获取当前文件夹路径
folder_path = r"G:\niwen"  # 替换为你的文件夹路径

# 循环遍历文件夹中的所有文件
for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        input_file = os.path.join(folder_path, file)
        output_file = os.path.join(folder_path, file.replace(".txt", ".md"))

        # 使用 Pandoc 转换文件
        subprocess.run(["pandoc", input_file, "-o", output_file])

print("finished.")

```

3、提取MD文件链接生成目录文件

```
#提取MD文件的文件链接并将文件的第一行的内容作为文件名

import os

# 指定文件夹路径
folder_path = r"G:\1prejects\0note\doc\zt-qita"

# 获取文件夹中所有的MD文件
md_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]

# 生成link.md文件
with open(os.path.join(folder_path, "link.md"), "w", encoding='UTF-8') as link_file:
    for md_file in md_files:
        with open(os.path.join(folder_path, md_file), "r", encoding='UTF-8') as f:
            first_line = f.readline().strip()
            link = f"[{first_line}]({md_file})"
            link_file.write(link + "\n")
print("finished")
```

4、TXT文件的批量重命名

```
# 这个脚本的作用是将TXT文件批量重命名，以SS+四位数字的形式
import os

# 指定文件夹路径
folder_path = r'G:\niwen'

# 获取文件夹下所有文件名
file_list = os.listdir(folder_path)

# 初始化计数器
count = 1

# 遍历文件列表
for file_name in file_list:
    if file_name.endswith('.txt'):
        # 构建新文件名
        new_file_name = f'niwen{count:04d}.txt'
        
        # 构建完整的文件路径
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        
        # 更新计数器
        count += 1

print("finished")

```

5、批量删除

```
#删除MD文件里的所有等号
import os

# 指定文件夹路径
folder_path = r'G:\1prejects\0note\doc\zt-niwenwoda'

# 获取文件夹中所有MD文件的路径
md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

# 遍历每个MD文件
for file_name in md_files:
    file_path = os.path.join(folder_path, file_name)
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 删除每行中的等号
    modified_lines = [line.replace('=', '') for line in lines]
    
    # 将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

print("finished")

```

6、删除特定词之后的内容

```
import os

# 指定目录路径
folder_path = r"G:\33"

# 遍历指定目录下的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):  # 仅处理 TXT 文件
        file_path = os.path.join(folder_path, file_name)
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 查找关键词并删除关键词之后的内容
        keyword = "法律声明"
        new_lines = []
        found_keyword = False
        for line in lines:
            if keyword in line:
                found_keyword = True
            if not found_keyword:
                new_lines.append(line)

        # 将处理后的内容写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        print(f"Processed file: {file_name}")

```

