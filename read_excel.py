import pandas as pd

# 方案1：正斜杠路径（已修正转义问题）
file_path = "C:/Users/712/Desktop/(商场销售数据）supermarket_sales.xlsx"

try:
    # 关键参数说明：
    # header=1：指定第2行（索引1）为列名（因为第1行是标题）
    # skiprows=0：不跳过行（header=1已自动处理标题行）
    # usecols：只读取有效列（避免空列干扰）
    df = pd.read_excel(
        file_path,
        engine="openpyxl",
        header=1,  # 核心！列名在第2行
        sheet_name=0  # 读取第一个sheet页（默认也是0，保险起见显式指定）
    )

    # 清理空列（删除全是Unnamed的列）
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    print("✅ 读取成功！")
    print(f"有效数据：{df.shape[0]} 行，{df.shape[1]} 列")
    print("\n列名：", df.columns.tolist())
    print("\n前5行数据：")
    print(df.head())

    # 检查是否真的为空
    if df.empty:
        print("\n⚠️  数据框为空！尝试读取所有行（包括标题）：")
        # 兜底方案：读取所有内容，不指定列名
        df_all = pd.read_excel(file_path, engine="openpyxl", header=None)
        print("文件所有内容（前10行）：")
        print(df_all.head(10))

except Exception as e:
    print(f"❌ 读取失败：{str(e)}")
