import streamlit as st
import pandas as pd

# -------------------------- 页面基础配置 --------------------------
st.set_page_config(page_title="学生数字档案", layout="wide", initial_sidebar_state="collapsed")

# 调整为灰色系美化样式：中性灰背景+适配配色
st.markdown("""
    <style>
    /* 全局样式 - 灰色背景 */
    .stApp { 
        background-color: #F0F2F6;  /* 主背景：浅灰色 */
        color: #333333;            /* 主文字：深灰色 */
        padding: 0 20px;
    }
    /* 标题样式 */
    h1 { color: #2D3748; margin-bottom: 20px; }
    h2 { color: #4A5568; border-bottom: 1px solid #CBD5E0; padding-bottom: 8px; }
    /* 卡片/面板样式 */
    .stExpander { 
        background-color: #FFFFFF !important;  /* 面板背景：纯白色 */
        border-radius: 12px; 
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stExpander > div:first-child { 
        background-color: #F8FAFC !important;  /* 面板头部：极浅灰 */
        border-radius: 12px 12px 0 0;
    }
    /* 指标卡片 */
    .stMetric { 
        background-color: #FFFFFF; 
        padding: 15px; 
        border-radius: 10px; 
        margin: 5px;
        border-left: 3px solid #4299E1;  /* 蓝色点缀 */
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    /* 表格样式 */
    .dataframe {
        background-color: #FFFFFF !important;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    th {
        background-color: #F8FAFC !important;
        color: #2D3748 !important;
        border: none !important;
        padding: 12px !important;
    }
    td {
        border-color: #E2E8F0 !important;
        padding: 12px !important;
    }
    /* 代码块 */
    .stCodeBlock {
        background-color: #F8FAFC !important;
        border-radius: 10px;
        padding: 15px !important;
        margin: 10px 0;
        border: 1px solid #E2E8F0;
    }
    /* 分割线和底部文字 */
    hr { border-color: #E2E8F0 !important; }
    .stCaption { color: #718096; }
    </style>
""", unsafe_allow_html=True)


# -------------------------- 标题区域 --------------------------
st.title("📁 学生 小杰 数字档案")


# -------------------------- 基础信息区域 --------------------------
with st.expander("📄 基础信息", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**学生ID**: N03-2023-001")
    with col2:
        st.write("**注册时间**: 2023-09-01")
        st.write("**精神状态**: ✅ 正常")
    with col3:
        st.write("**当前徽章**: 🛡️ 技能安全·普通")


# -------------------------- 技能矩阵区域 --------------------------
st.subheader("🎯 技能矩阵")
skill_cols = st.columns(3)
with skill_cols[0]:
    st.metric(label="Python", value="88%", delta="+3%")
with skill_cols[1]:
    st.metric(label="SQL", value="66%", delta="-2%")
with skill_cols[2]:
    st.metric(label="Vue", value="33%", delta="-10%")

# 进度条美化
st.write("📚 Streamlit课程进度")
st.progress(60, text="完成度 60%")  # 添加进度文本
st.caption("目标进度：80% | 剩余课时：4节")


# -------------------------- 任务日志区域（表格） --------------------------
st.subheader("📝 任务日志")
task_data = {
    "日期": ["2023-10-01", "2023-10-12"],
    "任务名称": ["学生信息管理系统", "课程管理系统"],
    "状态": ["🟢 进行中", "🔴 未完成"],
    "难度": ["★★☆☆☆", "★★★☆☆"]
}
task_df = pd.DataFrame(task_data)

# 展示美化后的表格
st.dataframe(
    task_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "日期": st.column_config.TextColumn("日期", width="small"),
        "任务名称": st.column_config.TextColumn("任务名称", width="medium"),
        "状态": st.column_config.TextColumn("状态", width="small"),
        "难度": st.column_config.TextColumn("难度", width="small")
    }
)


# -------------------------- 最新代码成果区域 --------------------------
st.subheader("💻 最新代码成果")
code_content = '''import streamlit as st

st.title("我的第一个Streamlit应用")
st.text("Hello World!")'''
st.code(code_content, language="python", line_numbers=True)


# -------------------------- 底部信息 --------------------------
st.markdown("---")
col_foot1, col_foot2, col_foot3 = st.columns(3)
with col_foot1:
    st.caption("SYSTEM MESSAGE: 下一个任务目标已解锁。")
with col_foot2:
    st.caption("SYS INFO: 课程管理系统 | CONTENT: 2025-03-01 12:42:48")
with col_foot3:
    st.caption("系统状态: 🟢 在线 | 服务状态: 🚀 已加速")
