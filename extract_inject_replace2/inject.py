import os
import re
import configparser

# 初始化配置解析器
config = configparser.ConfigParser()

# 使用UTF-8编码打开配置文件
with open('config.ini', 'r', encoding='utf-8') as config_file:
    config.read_file(config_file)

source_folder = config['paths']['source_folder_inject']
target_folder_inject = config['paths']['target_folder_inject']
texts_folder = config['paths']['texts_folder']
regex_pattern = config['settings']['regex_pattern']

def inject_texts():
    os.makedirs(target_folder_inject, exist_ok=True)
    for filename in os.listdir(texts_folder):
        texts_file_path = os.path.join(texts_folder, filename)
        original_file_path = os.path.join(source_folder, filename.replace('.txt', ''))
        with open(texts_file_path, 'r', encoding='utf-8') as file:
            replaced_texts = file.readlines()
        if os.path.exists(original_file_path):
            with open(original_file_path, 'r', encoding='utf-8') as file:
                original_content = file.read()
            def replace_match(match):
                return match.group(0).replace(match.group(1), replaced_texts.pop(0).strip())
            modified_content, _ = re.subn(regex_pattern, replace_match, original_content)
            output_path = os.path.join(target_folder_inject, filename.replace('.txt', ''))
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)

inject_texts()
