import streamlit as st
import pandas as pd
from PIL import Image
import io
import numpy as np

# ===================== 全局页面配置（必须放在所有组件前） =====================
# 注意：st.set_page_config 必须是第一个 Streamlit 命令，不能放在 tab/expander 内
st.set_page_config(
    page_title="多功能选项卡应用", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ===================== 全局样式美化（统一配置） =====================
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
    /* 音乐播放器样式 */
    .song-title {
        font-size: 26px;
        color: #1E88E5;
        font-weight: bold;
        margin-bottom: 10px;
        text-align: center;
    }
    .player-section {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .audio-player {
        margin-top: 15px;
    }
    /* 简历生成器深色主题 */
    .resume-dark .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .resume-dark .stTextInput > div > div > input,
    .resume-dark .stDateInput > div > div > input,
    .resume-dark .stSelectbox > div > div > select,
    .resume-dark .stTextArea > div > div > textarea {
        background-color: #2d2d2d;
        color: #ffffff;
        border: 1px solid #444444;
        border-radius: 6px;
        padding: 8px;
    }
    .resume-dark h1, .resume-dark h2, .resume-dark h3 {
        color: #ffffff;
        border-bottom: 1px solid #333;
        padding-bottom: 8px;
    }
    .resume-dark .stContainer {
        background-color: #1e1e1e;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .resume-dark .stButton > button {
        background-color: #6366f1;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
    }
    </style>
""", unsafe_allow_html=True)

# ===================== 选项卡主容器 =====================
st.title("多功能选项卡应用")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "学生数字档案", "餐厅数据可视化", "音乐播放器", 
    "相册", "个人简历生成器", "电击小子视频播放"
])

# ===================== 选项卡1：学生数字档案 =====================
with tab1:  # 核心修复：tab1下的所有代码必须缩进
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

# ===================== 选项卡2：餐厅数据可视化 =====================
with tab2:  # 缩进：tab2下的代码全部缩进
    # ===================== 1. 基础数据 =====================
    # 固定5家餐厅基础信息
    restaurants_base = {
        "餐厅名称": ["东方广场", "万达广场", "朝阳广场", "好友缘", "西冷牛排店"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "latitude": [22.807814, 22.832476, 22.819243, 22.809105, 22.839699],
        "longitude": [108.448890, 108.286408, 108.321189, 108.378664, 108.245804]
    }

    # 生成12个月的价格数据
    np.random.seed(123)
    months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    price_data = {
        "月份": months,
        "东方广场": np.random.uniform(14, 18, 12).round(1),
        "万达广场": np.random.uniform(19, 23, 12).round(1),
        "朝阳广场": np.random.uniform(24, 28, 12).round(1),
        "好友缘": np.random.uniform(34, 38, 12).round(1),
        "西冷牛排店": np.random.uniform(48, 52, 12).round(1)
    }

    # 生成高峰时段客流数据
    peak_hours = ["11:00", "12:00", "13:00", "14:00", "17:00", "18:00", "19:00", "20:00"]
    peak_flow_data = {
        "时段": peak_hours,
        "东方广场": np.random.uniform(80, 120, 8).round(0),
        "万达广场": np.random.uniform(90, 130, 8).round(0),
        "朝阳广场": np.random.uniform(150, 200, 8).round(0),
        "好友缘": np.random.uniform(70, 100, 8).round(0),
        "西冷牛排店": np.random.uniform(60, 90, 8).round(0)
    }

    # ===================== 2. 数据整理 =====================
    df_base = pd.DataFrame(restaurants_base)
    df_base.index = pd.RangeIndex(start=1, stop=6, name="序号")
    df_price = pd.DataFrame(price_data)
    df_peak = pd.DataFrame(peak_flow_data)

    # ===================== 3. 页面展示 =====================
    st.title("餐厅数据可视化分析")

    # 3.1 基础信息
    st.header("ℹ️ 一、5家餐厅基础信息")
    st.dataframe(df_base, use_container_width=True)

    # 3.2 评分柱状图
    st.header("👍 二、餐厅评分对比")
    st.bar_chart(
        df_base,
        x="餐厅名称",
        y="评分",
        color="#FF6347",
        width=800,
        height=400,
        use_container_width=False
    )

    # 3.3 价格走势折线图
    st.header("💰 三、5家餐厅12个月人均消费走势")
    st.line_chart(
        df_price,
        x="月份",
        y=["东方广场", "万达广场", "朝阳广场", "好友缘", "西冷牛排店"],
        width=800,
        height=500,
        use_container_width=False
    )

    # 3.4 客流面积图
    st.header("🍽 四、餐厅高峰时段客流分布")
    st.area_chart(
        df_peak,
        x="时段",
        y=["东方广场", "万达广场", "朝阳广场", "好友缘", "西冷牛排店"],
        color=["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#FF99CC"],
        width=800,
        height=500,
        use_container_width=False
    )

    # 3.5 地理位置地图
    st.header("🗺 五、餐厅地理位置分布")
    st.map(df_base[["latitude", "longitude"]], zoom=10)

# ===================== 选项卡3：音乐播放器 =====================
with tab3:  # 缩进：tab3下的代码全部缩进
    st.title("🎵 我的音乐播放器")
    st.markdown("---")

    # 初始化会话状态
    if 'music_ind' not in st.session_state:
        st.session_state['music_ind'] = 0

    # 歌曲数据
    songs = [
        {
            'cover_url': "https://d.musicapp.migu.cn/prod/playlist-service/playListimg/402bdb81-c298-4582-b208-543920fb8b08.jpg",
            'title': '告白气球',
            'audio_url': 'https://music.163.com/song/media/outer/url?id=2649263922.mp3'
        }, {
            'cover_url': "https://images.genius.com/2f9fcf00e373d592f6da1835a7638469.1000x1000x1.jpg",
            'title': '天外来物',
            'audio_url': 'https://music.163.com/song/media/outer/url?id=2759345435.mp3'
        }, {
            'cover_url': "https://n.sinaimg.cn/sinakd10117/110/w700h1010/20200728/3c5f-iwxpesx6821977.jpg",
            'title': '天后',
            'audio_url': 'https://music.163.com/song/media/outer/url?id=2636693518.mp3'
        }
    ]

    # 左右分栏
    left_col, right_col = st.columns([1, 1])
    with left_col:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(
            songs[st.session_state['music_ind']]['cover_url'],
            caption=songs[st.session_state['music_ind']]['title'],
            width=300
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        # 歌曲标题
        st.markdown(f"<div class='song-title'>{songs[st.session_state['music_ind']]['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"**歌曲 {st.session_state['music_ind'] + 1}/{len(songs)}**")
        st.divider()

        # 切换函数
        def prev_song():
            st.session_state['music_ind'] = (st.session_state['music_ind'] - 1) % len(songs)

        def next_song():
            st.session_state['music_ind'] = (st.session_state['music_ind'] + 1) % len(songs)

        # 切换按钮
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("◀◀ 上一首", use_container_width=True):
                prev_song()
                st.rerun()
        with btn_col2:
            if st.button("下一首 ▶▶", use_container_width=True):
                next_song()
                st.rerun()

        # 播放列表
        st.divider()
        st.markdown("### 📋 播放列表")
        for i, song in enumerate(songs):
            if i == st.session_state['music_ind']:
                st.markdown(f"🎵 **{song['title']}** (正在播放)")
            else:
                st.markdown(f"- {song['title']}")

    # 音频播放器
    st.markdown("---")
    st.markdown("<div class='player-section'>", unsafe_allow_html=True)
    st.markdown("### 🔊 音频播放器")
    st.audio(songs[st.session_state['music_ind']]['audio_url'], format='audio/mp3')
    st.info(f"正在播放: **{songs[st.session_state['music_ind']]['title']}**")
    st.markdown("</div>", unsafe_allow_html=True)

    # 底部信息
    st.markdown("---")
    st.caption("音乐播放器 v1.0 | 使用Streamlit构建")

# ===================== 选项卡4：相册 =====================
with tab4:  # 缩进：tab4下的代码全部缩进
    st.title("🐱 我的相册")

    # 初始化会话状态
    if 'photo_ind' not in st.session_state:
        st.session_state['photo_ind'] = 0

    # 图片数据
    photos = [
        {
            'url': "https://www.thehappycatsite.com/wp-content/uploads/2020/12/What-does-it-mean-if-a-cat-winks-at-you-HC-long.jpg",
            'text': '猫'
        }, {
            'url': "https://www.2008php.com/2012_Website_appreciate/2012-06-20/20120620130237.jpg",
            'text': '狗'
        }, {
            'url': "https://i-1-shuajizhijia.zswxy.cn/2025/0711/ca230ae156e54830a802d2250ab494bf.jpg?imageView2/2/q/50",
            'text': '猴'
        }
    ]

    # 显示图片
    st.image(photos[st.session_state['photo_ind']]['url'], caption=photos[st.session_state['photo_ind']]['text'])

    # 切换函数
    def prev_photo():
        st.session_state['photo_ind'] = (st.session_state['photo_ind'] - 1) % len(photos)

    def next_photo():
        st.session_state['photo_ind'] = (st.session_state['photo_ind'] + 1) % len(photos)

    # 切换按钮
    c1, c2 = st.columns(2)
    with c1:
        st.button("上一张", on_click=prev_photo, use_container_width=True)
    with c2:
        st.button("下一张", on_click=next_photo, use_container_width=True)

# ===================== 选项卡5：个人简历生成器 =====================
with tab5:  # 缩进：tab5下的代码全部缩进
    # 启用深色主题
    st.markdown('<div class="resume-dark">', unsafe_allow_html=True)
    
    st.title("✨ 个人简历生成器")
    st.caption("使用Streamlit创建你的个性化简历 | 实时预览 · 简单易用")
    st.divider()

    # 分栏布局
    form_col, preview_col = st.columns((1, 2), gap="large")

    # 左侧表单区域
    with form_col:
        st.subheader("📝 个人信息填写")
        st.markdown("---")

        # 基础信息
        with st.container(border=True):
            st.markdown("### 基础信息")
            user_name = st.text_input("姓名", placeholder="请输入您的姓名", help="必填项，填写后才能显示预览")
            user_position = st.text_input("求职意向", placeholder="例如：Python开发工程师")
            user_phone = st.text_input("联系电话", placeholder="请输入您的手机号码")
            user_email = st.text_input("电子邮箱", placeholder="请输入您的邮箱地址")

        # 个人详情
        with st.container(border=True):
            st.markdown("### 个人详情")
            col1, col2 = st.columns(2)
            with col1:
                user_gender = st.radio("性别", ["男", "女", "其他"], index=None, horizontal=True)
                user_birth = st.date_input("出生日期", value=None, format="YYYY/MM/DD")
            with col2:
                user_edu = st.selectbox("学历", ["请选择", "高中", "大专", "本科", "硕士", "博士"], index=0)
                user_exp = st.number_input("工作年限（年）", min_value=0, step=1, placeholder="0")

        # 求职期望
        with st.container(border=True):
            st.markdown("### 求职期望")
            user_salary = st.slider(
                "期望薪资范围（元/月）",
                min_value=3000,
                max_value=100000,
                value=(10000, 20000),
                format="%d元"
            )
            user_skill = st.selectbox("核心技能", ["请选择", "Python", "Java", "数据分析"], index=0)

        # 更多信息
        with st.container(border=True):
            st.markdown("### 更多信息")
            user_intro = st.text_area(
                "个人简介",
                placeholder="请简要介绍您的专业能力（100-500字）",
                height=120
            )
            user_photo = st.file_uploader(
                "上传照片（PNG/JPG）",
                type=["png", "jpg"],
                help="建议尺寸：200x250像素"
            )

    # 右侧预览区域
    with preview_col:
        st.subheader("🖥️ 简历实时预览")
        st.markdown("---")

        if user_name:
            # 简历头部
            with st.container(border=True):
                header_col = st.columns((1, 4))
                with header_col[0]:
                    st.markdown("#### 照片")
                    st.markdown('<div class="image-container">', unsafe_allow_html=True)
                    if user_photo:
                        try:
                            image = Image.open(user_photo)
                            image.thumbnail((150, 200))
                            st.image(image, width="stretch", caption=user_name)
                        except Exception as e:
                            st.error(f"图片加载失败: {str(e)}")
                    else:
                        st.image(
                            "https://via.placeholder.com/150x200/333333/ffffff?text=暂无照片",
                            width="stretch",
                            caption="点击左侧上传照片"
                        )
                    st.markdown('</div>', unsafe_allow_html=True)

                with header_col[1]:
                    st.markdown(f"<h1 style='margin-bottom: 1rem;'>{user_name}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<div class='resume-item'><strong>求职意向：</strong> {user_position if user_position else '未填写'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='resume-item'><strong>联系电话：</strong> {user_phone if user_phone else '未填写'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='resume-item'><strong>电子邮箱：</strong> {user_email if user_email else '未填写'}</div>", unsafe_allow_html=True)

            # 个人信息
            with st.container(border=True):
                st.markdown("<h3>个人信息</h3>", unsafe_allow_html=True)
                info_col1, info_col2 = st.columns(2)
                with info_col1:
                    st.markdown(f"<div class='resume-item'><strong>性别：</strong> {user_gender if user_gender else '未填写'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='resume-item'><strong>学历：</strong> {user_edu if user_edu != '请选择' else '未填写'}</div>", unsafe_allow_html=True)
                with info_col2:
                    st.markdown(f"<div class='resume-item'><strong>出生日期：</strong> {user_birth.strftime('%Y/%m/%d') if user_birth else '未填写'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='resume-item'><strong>工作年限：</strong> {user_exp}年</div>", unsafe_allow_html=True)

            # 求职期望
            with st.container(border=True):
                st.markdown("<h3>求职期望</h3>", unsafe_allow_html=True)
                st.markdown(f"<div class='resume-item'><strong>期望薪资：</strong> {user_salary[0]} - {user_salary[1]}元/月</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='resume-item'><strong>核心技能：</strong> {user_skill if user_skill != '请选择' else '未填写'}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='resume-item'><strong>个人简介：</strong> {user_intro if user_intro else '未填写'}</div>", unsafe_allow_html=True)

            # 下载按钮
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col2:
                resume_content = f"""
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

## 求职期望
期望薪资：{user_salary[0]} - {user_salary[1]}元/月
核心技能：{user_skill if user_skill != '请选择' else '未填写'}
个人简介：{user_intro if user_intro else '未填写'}
                """
                st.download_button(
                    label="📥 下载简历",
                    data=resume_content,
                    file_name=f"{user_name}_简历.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            # 未填写姓名提示
            with st.container(border=True):
                st.markdown("""
                <div style="text-align: center; padding: 3rem 0;">
                    <h3>👋 欢迎使用简历生成器</h3>
                    <p style="color: #999; font-size: 1.1rem;">请先在左侧填写姓名，简历预览会实时更新</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # 关闭深色主题容器

# ===================== 选项卡6：电击小子视频播放 =====================
with tab6:  # 缩进：tab6下的代码全部缩进
    st.title('⚡ 电击小子第二部')

    # 视频数据
    video_arr = [
        {
            'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/53/13/430521353/430521353-1-208.mp4?e=ig8euxZM2rNcNbRV7wdVhwdlhWdMhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=cos&mid=0&nbs=1&platform=html5&trid=c761618f77944b998e5b76d4d617d9dh&uipk=5&gen=playurlv3&deadline=1765768541&oi=771356656&os=cosovbv&upsig=50cd45567506ba9c8d9e03b9dea81bde&uparams=e,og,mid,nbs,platform,trid,uipk,gen,deadline,oi,os&bvc=vod&nettype=0&bw=834536&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
            'title': '第1集',
            'episode': 1
        },
        {
            'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/01/15/430521501/430521501-1-208.mp4?e=ig8euxZM2rNcNbR1hWdVhwdlhWR1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&og=hw&platform=html5&nbs=1&trid=d6ce221317b64a8ab0183c546653874h&mid=0&uipk=5&gen=playurlv3&oi=771356656&deadline=1765768644&upsig=c75eaedbe405537dd5b255269763cd85&uparams=e,os,og,platform,nbs,trid,mid,uipk,gen,oi,deadline&bvc=vod&nettype=0&bw=893081&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
            'title': '第2集',
            'episode': 2
        },
        {
            'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/55/17/430521755/430521755-1-208.mp4?e=ig8euxZM2rNcNbRV7WdVhwdlhWdBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&platform=html5&gen=playurlv3&deadline=1765768743&oi=771356656&nbs=1&trid=4404d71fd1aa43de990196b5df441fbh&uipk=5&os=cosovbv&og=cos&upsig=2e7489a10567158ffa375421899d808a&uparams=e,mid,platform,gen,deadline,oi,nbs,trid,uipk,os,og&bvc=vod&nettype=0&bw=842386&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
            'title': '第3集',
            'episode': 3
        }
    ]

    # 初始化会话状态
    if 'video_ind' not in st.session_state:
        st.session_state['video_ind'] = 0

    # 播放当前视频
    st.video(video_arr[st.session_state['video_ind']]['url'])

    # 切换视频函数
    def play_video(i):
        st.session_state['video_ind'] = int(i)

    # 视频按钮（每行3个）
    buttons_per_row = 3
    for i in range(0, len(video_arr), buttons_per_row):
        row_buttons = video_arr[i:i+buttons_per_row]
        cols = st.columns(len(row_buttons))
        for j, video in enumerate(row_buttons):
            with cols[j]:
                episode_num = i + j
                st.button(
                    f'第{episode_num+1}集',
                    use_container_width=True,
                    on_click=play_video,
                    args=(episode_num,),
                    key=f'btn_{episode_num}'
                )

    # 视频简介
    st.divider()
    st.subheader(f"第{st.session_state['video_ind']+1}集简介")
    descriptions = [
        "电击小子第二部开篇，小光面临新的挑战，必须掌握新力量保护城市。",
        "电击小子发现神秘能源源，这可能成为拯救城市的关键。",
        "战斗白热化，电击小子必须做出艰难选择，新盟友出现。"
    ]
    st.info(descriptions[st.session_state['video_ind']])

    # 更多信息
    with st.expander("查看更多信息"):
        st.write("**动画信息**:")
        st.write("- 类型: 国产动画")
        st.write("- 适合年龄: 6-12岁")
        st.write("- 主题: 科幻、冒险、友情")
        st.write("**温馨提示**: 本视频仅供学习交流使用，请支持正版动画。")
