import json

def process_record(record):
    """
    根据每条记录构造新的数据结构。
    "input"字段为原始的Question字段，
    "output"字段为按照要求拼接的字符串：
    "<think>\n{Complex_CoT}\n</think>\n{Response}"
    """
    question = record.get("Question", "")
    complex_cot = record.get("Complex_CoT", "")
    response = record.get("Response", "")
    
    # 拼接output字符串，可以根据需要调整空格或换行格式
    output = f"<think>\n{complex_cot}\n</think>\n{response}"
    
    return {
        "input": question,
        "output": output
    }

def main():
    # 输入和输出文件名
    input_file = "/Users/xiehuaibing/Documents/med_o1/medical_o1_sft_Chinese.json"
    output_file = "med_o1.json"
    
    # 读取输入文件
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 如果输入数据是列表，则对每条记录进行处理
    processed_data = [process_record(record) for record in data]
    
    # 将处理后的数据写入输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)
    
    print(f"处理完成，结果保存在 {output_file}")

if __name__ == "__main__":
    main()

    