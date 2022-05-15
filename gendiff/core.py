import json


def generate_diff(file1_path: str, file2_path: str) -> str:
    raw_data_1 = load_data(file1_path)
    raw_data_2 = load_data(file2_path)
    output_data = generate_diff_dict(raw_data_1, raw_data_2)
    return generate_output(output_data)


def generate_diff_dict(data1: dict, data2: dict) -> dict:
    keys = list(set(data1.keys()) | set(data2.keys()))
    keys.sort()
    output_data = dict()
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                output_data[f"  {key}"] = data1[key]
            else:
                output_data[f"- {key}"] = data1[key]
                output_data[f"+ {key}"] = data2[key]
        if key not in data2:
            output_data[f"- {key}"] = data1[key]
        if key not in data1:
            output_data[f"+ {key}"] = data2[key]
    return output_data


def generate_output(dict_differences: dict) -> str:
    data = json.dumps(dict_differences, indent=4, separators=("", ": "))
    return data.replace('"', "")


def load_data(file_path: str) -> dict:
    with open(file_path) as rd:
        return json.load(rd)
