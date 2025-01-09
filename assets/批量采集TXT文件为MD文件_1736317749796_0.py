from bs4 import BeautifulSoup
import requests
from markdownify import markdownify
import time
import random

# 替换为你实际存放网址列表的TXT文件路径
txt_file_path = r"C:\Users\one\Desktop\piliang.txt"  

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

with open(txt_file_path, 'r') as file:
    urls = file.readlines()
    for index, url in enumerate(urls):
        url = url.strip()  # 去除每行网址前后可能存在的空格、换行符等
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 检查请求是否成功，若不成功则抛出异常
            soup = BeautifulSoup(response.text, 'html.parser')
            markdown_content = markdownify(str(soup))
            # 以序号加网页标题（这里简单从网址中提取一部分作为文件名示例，你可优化）作为文件名保存
            file_name = f"{index + 1}_{url.split('/')[-1].split('.')[0]}.md"
            with open(file_name, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_content)
            print(f"Successfully saved {url} as {file_name}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 420:
                print(f"Received 420 error for {url}. Retrying after a longer delay...")
                # 增加更长的延时时间
                delay = random.uniform(10, 20)
                print(f"Waiting for {delay:.2f} seconds before retrying.")
                time.sleep(delay)
                # 重试请求
                try:
                    response = requests.get(url, headers=headers)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'html.parser')
                    markdown_content = markdownify(str(soup))
                    file_name = f"{index + 1}_{url.split('/')[-1].split('.')[0]}.md"
                    with open(file_name, "w", encoding="utf-8") as md_file:
                        md_file.write(markdown_content)
                    print(f"Successfully saved {url} as {file_name} after retry.")
                except requests.RequestException as e:
                    print(f"Error processing {url} after retry: {e}")
            else:
                print(f"Error processing {url}: {e}")
        except requests.RequestException as e:
            print(f"Error processing {url}: {e}")
        
        # 随机延时2-3秒
        delay = random.uniform(2, 3)
        print(f"Waiting for {delay:.2f} seconds before processing the next URL.")
        time.sleep(delay)