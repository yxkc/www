import pandas as pd
import streamlit as st
import os
import plotly.express as px

def get_dataframe_from_excel(file_path=None):
    """从Excel文件中读取销售数据并进行预处理"""
    if file_path is None:
        file_path = 'supermarket_sales.xlsx'
    
    if not os.path.exists(file_path):
        st.warning(f"找不到文件: {file_path}")
        return pd.DataFrame()  
    
    try:
        df = pd.read_excel(
            file_path,
            sheet_name='销售数据',
            skiprows=1,
            index_col='订单号'
        )
        
        if df.empty:
            st.error("读取的数据框为空，请检查Excel文件内容")
            return df
        
        # 处理时间列（提取小时）
        if "时间" in df.columns:
            df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
        else:
            st.warning("数据框中未找到'时间'列")
        
        return df
        
    except Exception as e:
        st.error(f"读取Excel文件时出错: {e}")
        return pd.DataFrame()  


def get_dataframe_from_uploaded_file(uploaded_file):
    """从上传的文件中读取销售数据"""
    try:
        df = pd.read_excel(
            uploaded_file,
            sheet_name='销售数据',
            skiprows=1,
            index_col='订单号'
        )
        
        if "时间" in df.columns:
            df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
        
        return df
        
    except Exception as e:
        st.error(f"读取上传文件时出错: {e}")
        return pd.DataFrame()


def add_sidebar_func(df):
    """创建数据筛选侧边栏"""
    if df.empty:
        return df
    
    with st.sidebar:
        st.header("请筛选数据：")
        
        # 城市筛选
        city_unique = df["城市"].unique()
        city = st.multiselect(
            "请选择城市：",
            options=city_unique,
            default=city_unique
        )
        
        # 顾客类型筛选
        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique,
            default=customer_type_unique
        )
        
        # 性别筛选
        gender_unique = df["性别"].unique()
        gender = st.multiselect(
            "请选择性别",
            options=gender_unique,
            default=gender_unique
        )
        
        # 筛选逻辑
        df_selection = df.query(
            "城市 == @city & 顾客类型 ==@customer_type & 性别 == @gender"
        )
    return df_selection


def product_line_chart(df):
    """生成“按产品类型划分的销售额”横向条形图"""
    sales_by_product = df.groupby("产品类型")["总价"].sum().sort_values()
    fig = px.bar(
        sales_by_product,
        x="总价",
        y=sales_by_product.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
        template="plotly_white"
    )
    fig.update_layout(
        xaxis_title="销售额（RMB）",
        yaxis_title="产品类型",
        height=400
    )
    return fig


def hour_chart(df):
    """生成“按小时数划分的销售额”纵向条形图"""
    sales_by_hour = df.groupby("小时数")["总价"].sum()
    fig = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价",
        title="<b>按小时数划分的销售额</b>",
        template="plotly_white"
    )
    fig.update_layout(
        xaxis_title="交易小时（24小时制）",
        yaxis_title="销售额（RMB）",
        height=400
    )
    return fig


def main():
    """主函数：整合所有功能"""
    st.set_page_config(
        page_title="销售仪表板",
        page_icon=":bar_chart:",
        layout="wide"
    )
    
    # 页面标题
    st.title(':bar_chart: 销售仪表板')
    
    # 数据来源选择
    st.sidebar.header("数据来源")
    data_source = st.sidebar.radio(
        "选择数据来源:",
        ["上传Excel文件", "使用本地文件 (supermarket_sales.xlsx)"]
    )
    
    sale_df = pd.DataFrame()
    
    if data_source == "上传Excel文件":
        uploaded_file = st.sidebar.file_uploader(
            "选择Excel文件",
            type=['xlsx', 'xls']
        )
        
        if uploaded_file is not None:
            with st.spinner("正在加载上传的数据..."):
                sale_df = get_dataframe_from_uploaded_file(uploaded_file)
        else:
            st.info("请上传Excel文件以开始分析")
            st.stop()
    
    else:
        with st.spinner("正在加载本地数据..."):
            sale_df = get_dataframe_from_excel()
        
        if sale_df.empty:
            st.error("无法找到本地数据文件！请上传文件或检查文件路径")
            st.stop()
    
    if sale_df.empty:
        st.error("数据加载失败，请检查文件格式和内容")
        st.stop()
    
    # 筛选数据
    df_selection = add_sidebar_func(sale_df)
    
    # 显示关键指标（3列布局）
    left_key_col, middle_key_col, right_key_col = st.columns(3)
    with left_key_col:
        total_sales = int(df_selection["总价"].sum())
        st.subheader("总销售额：")
        st.subheader(f"RMB ¥ {total_sales:,}")
    
    with middle_key_col:
        average_rating = round(df_selection["评分"].mean(), 1)
        star_rating = ":star:" * int(round(average_rating, 0))
        st.subheader("顾客评分的平均值：")
        st.subheader(f"{average_rating} {star_rating}")
    
    with right_key_col:
        avg_sale = round(df_selection["总价"].mean(), 2)
        st.subheader("每单的平均销售额：")
        st.subheader(f"RMB ¥ {avg_sale}")
    
    st.divider()  # 分割线
    
    # 显示双图表（2列布局）
    left_chart_col, right_chart_col = st.columns(2)
    with left_chart_col:
        hour_fig = hour_chart(df_selection)
        st.plotly_chart(hour_fig, use_container_width=True)
    
    with right_chart_col:
        product_fig = product_line_chart(df_selection)
        st.plotly_chart(product_fig, use_container_width=True)


if __name__ == "__main__":
    main()
