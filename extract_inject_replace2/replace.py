import os
import configparser


# 初始化配置解析器
config = configparser.ConfigParser()

# 使用UTF-8编码打开配置文件
with open('config.ini', 'r', encoding='utf-8') as config_file:
    config.read_file(config_file)

dictionary_file = config['paths']['dictionary_file']
source_folder_replace = config['paths']['source_folder_replace']
target_folder_replace = config['paths']['target_folder_replace']


def load_character_mapping(filename):
    """从指定的文件中加载字符映射关系。"""
    with open(filename, 'r', encoding='utf-8') as file:
        jp_line = file.readline().strip()  # 第一行是日文字符
        cn_line = file.readline().strip()  # 第二行是中文字符
    return dict(zip(cn_line, jp_line))

def replace_text_in_files(source_folder, target_folder, mapping):
    """读取指定文件夹内的txt文件，替换文本后存储到目标文件夹。"""
    # 确保目标文件夹存在
    os.makedirs(target_folder, exist_ok=True)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 替换所有中文字符为对应的日文字符
            for cn_char, jp_char in mapping.items():
                content = content.replace(cn_char, jp_char)

            # 写入新文件
            output_path = os.path.join(target_folder, filename)
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(content)

# 加载字符映射
mapping = load_character_mapping(dictionary_file)

# 替换文件中的文本并输出到新的文件夹
replace_text_in_files(source_folder_replace, target_folder_replace, mapping)
