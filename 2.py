import json

# 读取本地 JSON 文件
def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
        return None

# 递归查找数值所在的列及路径
def find_value(data, target_value, path=""):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}/{key}" if path else key
            if value == target_value:
                return new_path
            elif isinstance(value, (dict, list)):
                result = find_value(value, target_value, new_path)
                if result:
                    return result
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"
            result = find_value(item, target_value, new_path)
            if result:
                return result
    return None

# 指定 JSON 文件路径
file_path = r'C:\Users\...\xxx.json'

# 读取 JSON 数据
data = read_json_file(file_path)

# 确保数据被成功读取
if data is not None:
    # 查找目标数值所在的列及路径
    target_value = 12345  # 替换为你要查找的数值
    value_path = find_value(data, target_value)

    # 打印结果
    if value_path:
        print(f"Value '{target_value}' found at path: {value_path}")
    else:
        print(f"Value '{target_value}' not found")
