# 文本处理工具集

本项目提供一组文本处理工具，用于从文件中提取文本、替换文本以及将文本重新注入文件，特别适用于本地化和翻译工作流程中的文件处理。

## ⚠️ 重要注意事项

请在开始之前仔细阅读以下注意事项：

1. **文件编码**：所有的脚本文件都以**UTF-8编码格式**读写，请保证你的脚本文件为UTF-8编码格式。
2. **编码转换工具**：一键改变文本的编码格式为UTF-8的工具，我推荐使用 **EmEditor**。
3. **配置文件**：确保所有路径和文件名在`config.ini`中正确配置，并且文件的编码格式与程序设置一致。

## 功能描述

- **文本提取**：从指定目录的文件中提取符合正则表达式的文本，并保存到新的文件中。
- **文本替换**：根据给定的字符映射字典，替换文件中的特定文本。
- **文本注入**：将处理后的文本重新注入到原始文件中，保证文本的位置和格式不变。

## 使用场景

- **游戏本地化**：在游戏翻译和本地化过程中，提取游戏脚本中的文本，进行翻译后再将其注入回游戏文件。
- **文档翻译**：批量处理文档中的特定语言文本，实现快速翻译和替换。
- **数据迁移**：在软件迁移或数据转换过程中，提取和替换数据文件中的文本。

## 环境要求

- Python 3.6+
- 需要`configparser`模块来读取配置文件。

## 快速开始

1. **准备配置文件**：在项目根目录下创建`config.ini`，根据需要配置以下参数：

    ```ini
    [paths]
    source_folder_extract = script-jp
    target_folder_extract = txt-jp
    source_folder_replace = txt-cn
    target_folder_replace = txt-cn-replaced
    source_folder_inject = script-jp
    target_folder_inject = script-cn
    texts_folder = texts_cn_folder
    dictionary_file = dic.txt

    [settings]
    regex_pattern = "(.*?)"
    ```

2. **运行提取程序**：

    ```bash
    python extract.py
    ```

    这将从`source_folder_extract`中的文件提取文本，并将结果保存到`target_folder_extract`。

3. **运行替换程序**：

    ```bash
    python replace.py
    ```

    这将根据`dictionary_file`中的映射关系替换`source_folder_replace`中的文本，并保存到`target_folder_replace`。

4. **运行注入程序**：

    ```bash
    python inject.py
    ```

    这将把`texts_folder`中的文本注入到`source_folder_inject`对应的原始文件中，并保存到`target_folder_inject`。

## 贡献指南

感兴趣的开发者可以通过提交PR来提供新功能或改进现有功能。请确保您的代码清晰并有适当的注释。

## 许可证

此项目采用MIT许可证。详情请查阅LICENSE文件。
