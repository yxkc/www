import streamlit as st
import pandas as pd
from PIL import Image
import io

# 页面基础配置
st.set_page_config(
    page_title="个人简历生成器",
    page_icon="✨",
    layout="wide"
)

# -------------- 自定义深色主题样式（优化版） --------------
st.markdown("""
    <style>
    /* 全局背景与文本颜色 */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    /* 分栏容器 */
    .stColumn {
        background-color: #121212;
    }
    /* 表单组件样式 */
    .stTextInput > div > div > input,
    .stDateInput > div > div > input,
    .stTimeInput > div > div > input,
    .stSelectbox > div > div > select,
    .stMultiSelect > div > div > div,
    .stNumberInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #2d2d2d;
        color: #ffffff;
        border: 1px solid #444444;
        border-radius: 6px;
        padding: 8px;
    }
    /* 标题/子标题样式 */
    h1 {
        color: #ffffff;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    h2, h3, h4 {
        color: #ffffff;
        border-bottom: 1px solid #333;
        padding-bottom: 8px;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    /* 预览卡片样式 */
    .stContainer {
        background-color: #1e1e1e;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    /* 滑块样式 */
    .stSlider > div > div > div {
        background-color: #444444;
    }
    .stSlider > div > div > div > div {
        background-color: #6366f1;
    }
    /* 上传组件样式 */
    .stFileUploader > div > div {
        background-color: #2d2d2d;
        border: 1px dashed #444444;
        border-radius: 8px;
        padding: 1.5rem;
    }
    /* 按钮样式 */
    .stButton > button {
        background-color: #6366f1;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
    }
    .stButton > button:hover {
        background-color: #4f46e5;
    }
    /* 单选框样式 */
    .stRadio > div {
        gap: 0.5rem;
    }
    /* 分割线样式 */
    hr {
        border-color: #333;
    }
    /* 卡片边框优化 */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 8px;
        overflow: hidden;
    }
    /* 图片容器样式 */
    .image-container img {
        width: 100% !important;
        border-radius: 8px;
    }
    /* 简历信息项样式 */
    .resume-item {
        margin-bottom: 0.8rem;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    /* 简历标题样式 */
    .resume-title {
        color: #6366f1;
        margin-bottom: 1.2rem;
    }
    /* 简历头部信息 */
    .resume-header-info {
        padding-left: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 页面标题
st.title("✨ 个人简历生成器")
st.caption("使用Streamlit创建你的个性化简历 | 实时预览 · 简单易用")
st.divider()

# 分栏布局：左侧表单栏 + 右侧预览栏
form_col, preview_col = st.columns((1, 2), gap="large")

# ---------------------- 左侧表单区域（优化版） ----------------------
with form_col:
    st.subheader("📝 个人信息填写")
    st.markdown("---")
    
    # 基础信息卡片
    with st.container(border=True):
        st.markdown("### 基础信息")
        user_name = st.text_input("姓名", placeholder="请输入您的姓名", help="必填项，填写后才能显示预览")
        user_position = st.text_input("求职意向", placeholder="例如：Python开发工程师、产品经理等")
        user_phone = st.text_input("联系电话", placeholder="请输入您的手机号码")
        user_email = st.text_input("电子邮箱", placeholder="请输入您的邮箱地址")
    
    # 个人详情卡片
    with st.container(border=True):
        st.markdown("### 个人详情")
        col1, col2 = st.columns(2)
        with col1:
            user_gender = st.radio("性别", ["男", "女", "其他"], index=None, horizontal=True)
            user_birth = st.date_input("出生日期", value=None, format="YYYY/MM/DD")
            user_time = st.time_input("最佳联系时间", value=None)
        with col2:
            user_edu = st.selectbox("学历", ["请选择", "高中", "大专", "本科", "硕士", "博士"], index=0)
            user_exp = st.number_input("工作年限（年）", min_value=0, step=1, placeholder="0")
            user_lang = st.selectbox("语言能力", ["请选择", "普通话", "英语", "日语", "德语", "法语"], index=0)
    
    # 求职期望卡片
    with st.container(border=True):
        st.markdown("### 求职期望")
        user_salary = st.slider(
            "期望薪资范围（元/月）", 
            min_value=3000, 
            max_value=100000, 
            value=(10000, 20000),
            format="%d元"
        )
        user_skill = st.selectbox("核心技能", ["请选择", "Python", "Java", "项目管理", "数据分析", "UI设计"], index=0)
        user_grad = st.selectbox("毕业院校及时间", ["请选择", "2024年 某某大学", "2023年 某某大学", "2022年 某某大学"], index=0)
    
    # 个人简介和照片
    with st.container(border=True):
        st.markdown("### 更多信息")
        user_intro = st.text_area(
            "个人简介", 
            placeholder="请简要介绍您的专业能力、职业目标和个人特征（100-500字）",
            height=120
        )
        
        st.markdown("#### 个人照片")
        user_photo = st.file_uploader(
            "上传照片（支持PNG/JPG/JPEG）", 
            type=["png", "jpg", "jpeg"],
            help="建议尺寸：200x250像素，大小不超过2MB"
        )

# ---------------------- 右侧预览区域（优化版） ----------------------
with preview_col:
    st.subheader("🖥️ 简历实时预览")
    st.markdown("---")
    
    # 只有填写姓名后才显示预览内容
    if user_name:
        # 简历头部（包含照片和基础信息）
        with st.container(border=True):
            header_col = st.columns((1, 4))
            
            # 照片显示区域
            with header_col[0]:
                st.markdown("#### 照片")
                # 使用自定义容器确保图片占满列宽
                st.markdown('<div class="image-container">', unsafe_allow_html=True)
                if user_photo:
                    try:
                        # 读取并调整图片大小
                        image = Image.open(user_photo)
                        # 调整图片尺寸，保持比例
                        image.thumbnail((150, 200))
                        # 使用官方支持的参数：stretch（拉伸至容器宽度）
                        st.image(image, width="stretch", caption=user_name)
                    except Exception as e:
                        st.error(f"图片加载失败: {str(e)}")
                else:
                    # 占位图片 - 使用stretch参数
                    st.image(
                        "https://via.placeholder.com/150x200/333333/ffffff?text=暂无照片",
                        width="stretch",
                        caption="点击左侧上传照片"
                    )
                st.markdown('</div>', unsafe_allow_html=True)
            
            # 基础信息区域 - 优化排版
            with header_col[1]:
                st.markdown(f"<h1 style='margin-bottom: 1rem;'>{user_name}</h1>", unsafe_allow_html=True)
                
                # 求职意向
                pos_text = user_position if user_position else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <strong style='color: #6366f1;'>求职意向：</strong> {pos_text}
                </div>
                """, unsafe_allow_html=True)
                
                # 联系电话
                phone_text = user_phone if user_phone else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <strong style='color: #6366f1;'>联系电话：</strong> {phone_text}
                </div>
                """, unsafe_allow_html=True)
                
                # 电子邮箱
                email_text = user_email if user_email else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <strong style='color: #6366f1;'>电子邮箱：</strong> {email_text}
                </div>
                """, unsafe_allow_html=True)
        
        # 详细信息区域 - 优化排版
        with st.container(border=True):
            st.markdown("<h3 class='resume-title'>个人信息</h3>", unsafe_allow_html=True)
            
            # 两列布局显示详细信息
            info_col1, info_col2 = st.columns(2, gap="medium")
            
            with info_col1:
                # 性别
                gender_text = user_gender if user_gender else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>📌</span> 
                    <strong>性别：</strong> {gender_text}
                </div>
                """, unsafe_allow_html=True)
                
                # 学历
                edu_text = user_edu if user_edu != "请选择" else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>🎓</span> 
                    <strong>学历：</strong> {edu_text}
                </div>
                """, unsafe_allow_html=True)
                
                # 工作年限
                exp_text = f"{user_exp}年" if user_exp > 0 else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>💼</span> 
                    <strong>工作年限：</strong> {exp_text}
                </div>
                """, unsafe_allow_html=True)
                
                # 语言能力
                lang_text = user_lang if user_lang != "请选择" else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>🎯</span> 
                    <strong>语言能力：</strong> {lang_text}
                </div>
                """, unsafe_allow_html=True)
            
            with info_col2:
                # 出生日期
                birth_text = user_birth.strftime('%Y/%m/%d') if user_birth else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>📅</span> 
                    <strong>出生日期：</strong> {birth_text}
                </div>
                """, unsafe_allow_html=True)
                
                # 最佳联系时间
                time_text = user_time if user_time else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>🕒</span> 
                    <strong>最佳联系时间：</strong> {time_text}
                </div>
                """, unsafe_allow_html=True)
                
                # 期望薪资
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>💰</span> 
                    <strong>期望薪资：</strong> {user_salary[0]} - {user_salary[1]}元/月
                </div>
                """, unsafe_allow_html=True)
                
                # 毕业信息
                grad_text = user_grad if user_grad != "请选择" else "未填写"
                st.markdown(f"""
                <div class='resume-item'>
                    <span style='color: #6366f1;'>🎓</span> 
                    <strong>毕业信息：</strong> {grad_text}
                </div>
                """, unsafe_allow_html=True)
        
        # 技能和简介区域 - 优化排版
        with st.container(border=True):
            # 专业技能
            st.markdown("<h3 class='resume-title'>专业技能</h3>", unsafe_allow_html=True)
            skill_text = user_skill if user_skill != "请选择" else "未填写"
            st.markdown(f"""
            <div class='resume-item' style='padding: 0.8rem; background-color: #252525; border-radius: 6px;'>
                <span style='color: #6366f1;'>🔧</span> 
                <span style='font-size: 1.1rem;'>{skill_text}</span>
            </div>
            """, unsafe_allow_html=True)
            
            # 个人简介
            st.markdown("<h3 class='resume-title'>个人简介</h3>", unsafe_allow_html=True)
            if user_intro:
                st.markdown(f"""
                <div style='
                    padding: 1rem; 
                    background-color: #252525; 
                    border-radius: 6px;
                    border-left: 4px solid #6366f1;
                    font-size: 1.05rem;
                    line-height: 1.8;
                '>
                    {user_intro}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='
                    padding: 1rem; 
                    background-color: #252525; 
                    border-radius: 6px;
                    border-left: 4px solid #888;
                    color: #999;
                '>
                    请在左侧填写个人简介，突出您的优势和职业目标。
                </div>
                """, unsafe_allow_html=True)
        
        # 添加下载按钮 - 居中显示
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col2:
            st.download_button(
                label="📥 下载简历",
                data=f"""
# 个人简历

## 基本信息
姓名：{user_name}
求职意向：{user_position if user_position else '未填写'}
联系电话：{user_phone if user_phone else '未填写'}
电子邮箱：{user_email if user_email else '未填写'}

## 个人详情
性别：{user_gender if user_gender else '未填写'}
出生日期：{user_birth.strftime('%Y/%m/%d') if user_birth else '未填写'}
学历：{user_edu if user_edu != '请选择' else '未填写'}
工作年限：{user_exp}年
语言能力：{user_lang if user_lang != '请选择' else '未填写'}

## 求职期望
期望薪资：{user_salary[0]} - {user_salary[1]}元/月
核心技能：{user_skill if user_skill != '请选择' else '未填写'}
毕业信息：{user_grad if user_grad != '请选择' else '未填写'}
最佳联系时间：{user_time if user_time else '未填写'}

## 个人简介
{user_intro if user_intro else '未填写'}
                """,
                file_name=f"{user_name}_简历.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    else:
        # 未填写姓名时的提示
        with st.container(border=True):
            st.markdown("""
            <div style="text-align: center; padding: 3rem 0;">
                <h3 style='color: #ffffff;'>👋 欢迎使用简历生成器</h3>
                <p style="color: #999; font-size: 1.1rem; margin: 1rem 0;">请先在左侧表单填写您的姓名，简历预览内容会实时更新</p>
                <p style="color: #6366f1; font-size: 1.1rem;">填写完成后，您可以预览、下载您的个性化简历</p>
            </div>
            """, unsafe_allow_html=True)

# 页脚
st.markdown("---")
st.markdown("<div style='text-align: center; color: #666; font-size: 0.9rem;'>© 2025 个人简历生成器 | 使用 Streamlit 构建</div>", unsafe_allow_html=True)
