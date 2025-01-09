import os

def count_words_in_file(file_path):
    """统计单个文件中的字数"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 去除空格和换行符后统计字数
        word_count = len(content.replace(' ', '').replace('\n', ''))
    return word_count

def count_words_in_directory(directory):
    """统计指定目录下所有MD文件中的字数"""
    total_word_count = 0
    file_word_counts = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                word_count = count_words_in_file(file_path)
                file_word_counts[file_path] = word_count
                total_word_count += word_count
                print(f"File: {file_path}, Word Count: {word_count}")

    return total_word_count, file_word_counts

def main():
    # 替换为你实际的目录路径
    directory_path = r"D:\资料中心\530  网站建设\logseq站点\pages"
    
    total_word_count, file_word_counts = count_words_in_directory(directory_path)
    
    print("\nSummary:")
    for file_path, word_count in file_word_counts.items():
        print(f"File: {file_path}, Word Count: {word_count}")
    
    print(f"\nTotal Word Count: {total_word_count}")

if __name__ == "__main__":
    main()