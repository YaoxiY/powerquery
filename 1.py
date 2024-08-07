import json

# 读取本地 JSON 文件
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 递归查找列所在层级
def find_column(data, column_name, path=""):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}/{key}" if path else key
            if key == column_name:
                return new_path
            result = find_column(value, column_name, new_path)
            if result:
                return result
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"
            result = find_column(item, column_name, new_path)
            if result:
                return result
    return None

# 指定 JSON 文件路径
file_path = r'C:\Users\...\xxx.json'

# 读取 JSON 数据
data = read_json_file(file_path)

# 查找 "city" 列所在层级（你可以替换 "city" 为你要查找的列名）
column_name = "city"  # 替换为你要查找的列名
column_path = find_column(data, column_name)

# 打印结果
if column_path:
    print(f"Column '{column_name}' found at path: {column_path}")
else:
    print(f"Column '{column_name}' not found")
