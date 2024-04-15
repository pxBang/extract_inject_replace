import os
import re
import configparser

# 初始化配置解析器
config = configparser.ConfigParser()

# 使用UTF-8编码打开配置文件
with open('config.ini', 'r', encoding='utf-8') as config_file:
    config.read_file(config_file)

source_folder_extract = config['paths']['source_folder_extract']
target_folder_extract = config['paths']['target_folder_extract']
regex_pattern = config['settings']['regex_pattern']

def extract_texts():
    """从指定的文件夹中提取文本并保存到目标文件夹。"""
    os.makedirs(target_folder_extract, exist_ok=True)
    for filename in os.listdir(source_folder_extract):
        file_path = os.path.join(source_folder_extract, filename)
        if os.path.isfile(file_path) and '.' not in filename:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            matches = re.findall(regex_pattern, content)
            output_path = os.path.join(target_folder_extract, filename + '.txt')
            with open(output_path, 'w', encoding='utf-8') as output_file:
                for match in matches:
                    output_file.write(match + '\n')

extract_texts()
