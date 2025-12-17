import pandas as pd
import streamlit as st
import os

# 全局样式设置（新增：统一字体和间距）
st.set_page_config(
    page_title="商场销售数据筛选",  # 浏览器标签页标题
    page_icon="📊",  # 浏览器标签页图标
    layout="wide"  # 宽屏布局，适配更多数据列
)

# 读取Excel数据的函数（无功能修改）
def get_dataframe_from_excel():
    try:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        excel_file_path = os.path.join(desktop_path, "（商场销售数据）supermarket_sales.xlsx")
        
        df = pd.read_excel(excel_file_path,
                           sheet_name='销售数据',
                           skiprows=1,
                           index_col='订单号'
                           )
        df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
        return df
    except FileNotFoundError:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        st.error(f"未找到文件！请确认Excel在桌面，且文件名为：\n{desktop_path}\\（商场销售数据）supermarket_sales.xlsx")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"读取Excel出错：{str(e)}")
        return pd.DataFrame()

# 侧边栏筛选函数（美化筛选器样式和文字）
def add_sidebar_func(df):
    with st.sidebar:
        # 侧边栏标题美化：加图标+调整颜色
        st.markdown("<h3 style='color:#2E86AB; margin-bottom:20px;'>📌 数据筛选条件</h3>", unsafe_allow_html=True)
        
        # 城市筛选：加提示文字+调整间距
        st.markdown("<p style='margin-bottom:5px; font-size:14px;'>选择目标城市</p>", unsafe_allow_html=True)
        city_unique = df["城市"].unique()
        city = st.multiselect(
            label="",  # 清空默认标签，用自定义文字替代
            options=city_unique,
            default=city_unique,
            key="city_select",
            help="可多选城市，默认显示所有城市数据"  # 鼠标悬浮提示
        )
        
        # 顾客类型筛选：统一样式
        st.markdown("<p style='margin:20px 0 5px; font-size:14px;'>选择顾客类型</p>", unsafe_allow_html=True)
        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(
            label="",
            options=customer_type_unique,
            default=customer_type_unique,
            key="customer_select",
            help="可多选顾客类型（会员/普通）"
        )
        
        # 性别筛选：统一样式
        st.markdown("<p style='margin:20px 0 5px; font-size:14px;'>选择性别</p>", unsafe_allow_html=True)
        gender_unique = df["性别"].unique()
        gender = st.multiselect(
            label="",
            options=gender_unique,
            default=gender_unique,
            key="gender_select",
            help="可多选性别"
        )
        
        # 侧边栏底部加分隔线，提升整洁度
        st.markdown("<hr style='margin-top:30px; border-color:#E0E0E0;'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; color:#888;'>筛选后数据实时更新</p>", unsafe_allow_html=True)
    
    df_selection = df.query("城市 == @city & 顾客类型 ==@customer_type & 性别 == @gender")
    return df_selection

# 主程序入口（美化结果展示）
if __name__ == "__main__":
    sale_df = get_dataframe_from_excel()
    
    if not sale_df.empty:
        df_selection = add_sidebar_func(sale_df)
        
        # 主标题美化：加图标+渐变色+间距
        st.markdown("""
            <div style='text-align:center; margin:20px 0 30px;'>
                <h2 style='color:#2E86AB;'>📊 商场销售数据筛选结果</h2>
                <p style='color:#666; font-size:15px;'>实时展示筛选后的销售明细数据</p>
            </div>
        """, unsafe_allow_html=True)
        
        # 数据统计卡片：突出显示关键信息（新增）
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"总数据行数\n**{sale_df.shape[0]}**")  # 蓝色信息卡片
        with col2:
            st.success(f"筛选后行数\n**{df_selection.shape[0]}**")  # 绿色成功卡片
        with col3:
            st.warning(f"涉及城市数\n**{len(df_selection['城市'].unique())}**")  # 黄色警告卡片
        
        # 数据表格美化：加边框+调整字体大小
        st.markdown("<h4 style='margin:20px 0 10px; color:#4A4A4A;'>数据明细</h4>", unsafe_allow_html=True)
        st.dataframe(
            df_selection,
            use_container_width=True,  # 自适应宽度
            height=500,  # 固定表格高度
            column_config={
                # 自定义列样式：关键列加粗
                "总金额": st.column_config.NumberColumn(format="%.2f", help="交易总金额（元）"),
                "单价": st.column_config.NumberColumn(format="%.2f", help="商品单价（元）"),
                "小时数": st.column_config.NumberColumn(help="交易发生小时（24小时制）")
            }
        )
    else:
        # 空数据提示美化：居中显示+加图标
        st.markdown("""
            <div style='text-align:center; margin-top:50px;'>
                <h3 style='color:#888;'>⚠️ 暂无数据可展示</h3>
                <p style='color:#AAA; margin-top:10px;'>请检查Excel文件路径或文件名是否正确</p>
            </div>
        """, unsafe_allow_html=True)
