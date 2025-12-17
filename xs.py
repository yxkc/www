import pandas as pd
import streamlit as st
import os

def get_dataframe_from_excel(file_path=None):
    """
    从Excel文件中读取销售数据并进行预处理
    
    参数：
        file_path: Excel文件路径，如果为None则使用默认文件名
    
    返回：
        DataFrame: 处理后的销售数据框
    """
    # 如果没有提供文件路径，使用默认文件名
    if file_path is None:
        file_path = 'supermarket_sales.xlsx'
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        st.warning(f"找不到文件: {file_path}")
        return pd.DataFrame()  # 返回空数据框
    
    try:
        # 读取Excel文件数据
        df = pd.read_excel(file_path,
                           sheet_name='销售数据',
                           skiprows=1,
                           index_col='订单号')
        
        # 检查数据框是否为空
        if df.empty:
            st.error("读取的数据框为空，请检查Excel文件内容")
            return df
        
        # 处理时间列：从时间字符串中提取小时信息
        # 假设时间列名为'时间'，格式如'10:25:30'
        time_columns = [col for col in df.columns if '时间' in col or 'time' in col.lower()]
        
        if time_columns:
            # 使用第一个找到的时间列
            time_col = time_columns[0]
            try:
                # 尝试不同的时间格式
                df['小时'] = pd.to_datetime(df[time_col], format='%H:%M:%S').dt.hour
            except:
                try:
                    # 尝试其他常见格式
                    df['小时'] = pd.to_datetime(df[time_col]).dt.hour
                except Exception as e:
                    st.warning(f"无法解析时间列 '{time_col}': {e}")
        else:
            st.warning("数据框中未找到时间列")
        
        return df
        
    except Exception as e:
        st.error(f"读取Excel文件时出错: {e}")
        return pd.DataFrame()  # 返回空数据框


def get_dataframe_from_uploaded_file(uploaded_file):
    """
    从上传的文件中读取销售数据
    
    参数：
        uploaded_file: Streamlit上传的文件对象
    
    返回：
        DataFrame: 处理后的销售数据框
    """
    try:
        # 读取上传的Excel文件
        df = pd.read_excel(uploaded_file,
                           sheet_name='销售数据',
                           skiprows=1,
                           index_col='订单号')
        
        # 处理时间列
        time_columns = [col for col in df.columns if '时间' in col or 'time' in col.lower()]
        
        if time_columns:
            time_col = time_columns[0]
            try:
                df['小时'] = pd.to_datetime(df[time_col], format='%H:%M:%S').dt.hour
            except:
                try:
                    df['小时'] = pd.to_datetime(df[time_col]).dt.hour
                except:
                    pass
        
        return df
        
    except Exception as e:
        st.error(f"读取上传文件时出错: {e}")
        return pd.DataFrame()


def add_sidebar_func(df):
    """
    创建数据筛选侧边栏
    
    参数：
        df: 原始数据框
    
    返回：
        DataFrame: 筛选后的数据框
    """
    # 检查数据框是否为空
    if df.empty:
        return df
    
    # 创建侧边栏
    with st.sidebar:
        # 添加侧边栏标题
        st.header("数据筛选")
        
        # 检查需要的列是否存在
        available_columns = df.columns.tolist()
        
        # 城市筛选器
        if "城市" in available_columns:
            city_unique = df["城市"].dropna().unique().tolist()
            city = st.multiselect(
                "请选择城市：",
                options=city_unique,
                default=city_unique[:min(3, len(city_unique))] if city_unique else [],
                help="选择一个或多个城市进行筛选"
            )
        else:
            city = []
            st.warning("数据框中未找到'城市'列")
        
        # 顾客类型筛选器
        if "顾客类型" in available_columns:
            customer_type_unique = df["顾客类型"].dropna().unique().tolist()
            customer_type = st.multiselect(
                "请选择顾客类型：",
                options=customer_type_unique,
                default=customer_type_unique,
                help="选择一个或多个顾客类型进行筛选"
            )
        else:
            customer_type = []
            st.warning("数据框中未找到'顾客类型'列")
        
        # 性别筛选器
        if "性别" in available_columns:
            gender_unique = df["性别"].dropna().unique().tolist()
            gender = st.multiselect(
                "请选择性别：",
                options=gender_unique,
                default=gender_unique,
                help="选择一个或多个性别进行筛选"
            )
        else:
            gender = []
            st.warning("数据框中未找到'性别'列")
        
        # 添加重置按钮
        if st.button("重置筛选"):
            st.experimental_rerun()
    
    # 根据筛选条件过滤数据
    filters_applied = False
    query_conditions = []
    
    if "城市" in available_columns and city:
        query_conditions.append(f"城市 in {city}")
        filters_applied = True
    
    if "顾客类型" in available_columns and customer_type:
        query_conditions.append(f"顾客类型 in {customer_type}")
        filters_applied = True
    
    if "性别" in available_columns and gender:
        query_conditions.append(f"性别 in {gender}")
        filters_applied = True
    
    if filters_applied and query_conditions:
        try:
            query_string = " and ".join(query_conditions)
            df_selection = df.query(query_string)
        except Exception as e:
            st.warning(f"筛选时出错: {e}")
            df_selection = df.copy()
    else:
        df_selection = df.copy()
    
    return df_selection


def display_summary_statistics(df):
    """
    显示数据概览统计信息
    
    参数：
        df: 数据框
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("总记录数", df.shape[0])
    
    with col2:
        st.metric("总列数", df.shape[1])
    
    with col3:
        # 寻找金额列
        amount_columns = [col for col in df.columns if '总价' in col or '金额' in col or 'price' in col.lower()]
        if amount_columns and not df[amount_columns[0]].isna().all():
            total_sales = df[amount_columns[0]].sum()
            st.metric("总销售额", f"¥{total_sales:,.2f}")
        else:
            st.metric("总销售额", "N/A")
    
    with col4:
        if amount_columns and not df[amount_columns[0]].isna().all():
            avg_sales = df[amount_columns[0]].mean()
            st.metric("平均销售额", f"¥{avg_sales:,.2f}")
        else:
            st.metric("平均销售额", "N/A")


def main():
    """
    主函数：整合所有功能
    """
    # 设置页面配置
    st.set_page_config(
        page_title="超市销售数据分析",
        page_icon="📊",
        layout="wide"
    )
    
    # 页面标题
    st.title("📊 超市销售数据分析系统")
    
    # 数据来源选择
    st.sidebar.header("数据来源")
    data_source = st.sidebar.radio(
        "选择数据来源:",
        ["上传Excel文件", "使用本地文件 (supermarket_sales.xlsx)"]
    )
    
    sale_df = pd.DataFrame()
    
    if data_source == "上传Excel文件":
        # 文件上传器
        uploaded_file = st.sidebar.file_uploader(
            "选择Excel文件",
            type=['xlsx', 'xls'],
            help="请上传包含销售数据的Excel文件"
        )
        
        if uploaded_file is not None:
            with st.spinner("正在加载上传的数据..."):
                sale_df = get_dataframe_from_uploaded_file(uploaded_file)
        else:
            st.info("请上传Excel文件以开始分析")
            st.stop()
    
    else:  # 使用本地文件
        with st.spinner("正在加载本地数据..."):
            sale_df = get_dataframe_from_excel()
        
        if sale_df.empty:
            st.error("""
            ## 无法找到本地数据文件！
            
            请执行以下操作之一：
            1. 将您的Excel文件重命名为 `supermarket_sales.xlsx` 并放在当前目录下
            2. 或者切换到"上传Excel文件"选项直接上传文件
            
            当前目录: {}
            """.format(os.getcwd()))
            st.stop()
    
    # 检查数据是否成功加载
    if sale_df.empty:
        st.error("数据加载失败，请检查文件格式和内容")
        st.stop()
    
    # 显示数据基本信息
    st.sidebar.success(f"✅ 数据加载成功: {sale_df.shape[0]} 行 × {sale_df.shape[1]} 列")
    
    # 显示原始数据预览
    with st.expander("📋 查看原始数据预览"):
        st.write("**数据列名:**", sale_df.columns.tolist())
        st.write("**数据前5行:**")
        st.dataframe(sale_df.head(), use_container_width=True)
        st.write("**数据类型:**")
        st.dataframe(sale_df.dtypes.rename("数据类型"))
    
    # 添加侧边栏筛选功能
    df_selection = add_sidebar_func(sale_df)
    
    # 显示概览统计
    st.subheader("📈 数据概览")
    display_summary_statistics(df_selection)
    
    # 显示筛选后的数据
    st.subheader("🔍 筛选后的数据")
    
    # 添加数据预览选项
    preview_rows = st.slider("选择要预览的行数", 5, 100, 20)
    st.dataframe(df_selection.head(preview_rows), use_container_width=True)
    
    # 显示数据行数信息
    original_rows = sale_df.shape[0]
    filtered_rows = df_selection.shape[0]
    st.write(f"原始数据: **{original_rows}** 行 | 筛选后数据: **{filtered_rows}** 行")
    
    if filtered_rows < original_rows:
        st.success(f"✅ 已筛选掉 {original_rows - filtered_rows} 行数据")
    
    # 显示数据摘要信息
    with st.expander("📊 查看详细数据摘要"):
        st.write("**缺失值统计:**")
        missing_values = df_selection.isnull().sum()
        if missing_values.sum() > 0:
            st.dataframe(missing_values[missing_values > 0].rename("缺失值数量"))
        else:
            st.success("✅ 无缺失值")
        
        st.write("**数值列统计:**")
        numeric_cols = df_selection.select_dtypes(include=['int64', 'float64']).columns
        if len(numeric_cols) > 0:
            st.dataframe(df_selection[numeric_cols].describe())
        else:
            st.info("未找到数值列")
    
    # 添加下载按钮
    if not df_selection.empty:
        csv = df_selection.to_csv(index=True)
        st.download_button(
            label="📥 下载筛选后的数据 (CSV)",
            data=csv,
            file_name="筛选后的销售数据.csv",
            mime="text/csv",
            help="点击下载当前筛选后的数据"
        )


if __name__ == "__main__":
    main()
