# coding:utf-8
'''
    批量yaml转json
'''

import os
import yaml
import json

out_base_path = r"C:\Users\Administrator\Desktop\out_json"


# 时间格式处理
def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError


def yaml_to_json(file_path, file_name):
    print('输入：' + file_path)
    out_path = os.path.join(out_base_path, file_name)
    portion = os.path.splitext(out_path)
    if portion[1] == '.yaml':
        out_path = portion[0] + '.json'
        with open(
                out_path, 'w', encoding='utf8') as out_file, open(
                    file_path, encoding='utf8') as in_file:
            out_file.write(
                json.dumps(
                    yaml.load(in_file),
                    indent=4,
                    ensure_ascii=False,
                    default=date_handler))
        print('输出：' + out_path)
    else:
        print("非yaml文件")

    print()


for root, dirs, files in os.walk('F:\aa'):
    for filespath in files:
        yaml_to_json(os.path.join(root, filespath), filespath)
