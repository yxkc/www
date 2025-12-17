import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io

# -------------------------- 全局配置 --------------------------
st.set_page_config(
    page_title="多功能应用平台",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"  # 默认展开侧边栏
)

# -------------------------- 侧边栏导航 --------------------------
with st.sidebar:
    st.title("📚 功能导航")
    # 选择功能页面
    selected_page = st.radio(
        "选择功能",
        [
            "首页",
            "学生数字档案",
            "餐厅数据可视化",
            "音乐播放器",
            "我的相册",
            "个人简历生成器",
            "电击小子第二部"
        ]
    )


# -------------------------- 页面路由（根据选择加载对应功能） --------------------------
if selected_page == "首页":
    # 首页内容（参考你提供的广西职业师范学院页面）
    st.title("🏫 广西职业师范学院")
    st.image(
        "https://ts1.tc.mm.bing.net/th/id/R-C.5bd01325b7f811db419ed35caac5f245?rik=si%2ffoIflFg4Fjg&riu=http%3a%2f%2f19654776.s21i.faiusr.com%2f4%2fABUIABAEGAAg4NvEhwYopbP8sgUwhAc42AQ!600x600.png&ehk=Lp%2b6lHsH1opRVVGXbtE00thhQcE2H9J82Ls0Mi8w3H0%3d&risl=&pid=ImgRaw&r=0",
        use_container_width=True
    )
    st.markdown("""
    广西职业师范学院（原广西经济管理干部学院）坐落于广西南宁市，是自治区人民政府直属的公办全日制普通本科学校，致力于培养区域经济社会发展所需的高素质应用型、技术技能型人才和职业教育师资。
    """)
    st.subheader("学校概况")
    st.write("学校拥有12个二级学院，33个本科专业，涵盖8大学科，现有教职工427人...")


elif selected_page == "学生数字档案":
    # 学生数字档案页面
    st.set_page_config(page_title="学生数字档案", layout="wide")
    # 灰色系样式
    st.markdown("""
        <style>
        .stApp { background-color: #F0F2F6; color: #333333; padding: 0 20px; }
        h1 { color: #2D3748; margin-bottom: 20px; }
        h2 { color: #4A5568; border-bottom: 1px solid #CBD5E0; padding-bottom: 8px; }
        .stExpander { background-color: #FFFFFF !important; border-radius: 12px; margin: 10px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .stExpander > div:first-child { background-color: #F8FAFC !important; border-radius: 12px 12px 0 0; }
        .stMetric { background-color: #FFFFFF; padding: 15px; border-radius: 10px; margin: 5px; border-left: 3px solid #4299E1; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .dataframe { background-color: #FFFFFF !important; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        th { background-color: #F8FAFC !important; color: #2D3748 !important; border: none !important; padding: 12px !important; }
        td { border-color: #E2E8F0 !important; padding: 12px !important; }
        .stCodeBlock { background-color: #F8FAFC !important; border-radius: 10px; padding: 15px !important; margin: 10px 0; border: 1px solid #E2E8F0; }
        hr { border-color: #E2E8F0 !important; }
        .stCaption { color: #718096; }
        </style>
    """, unsafe_allow_html=True)

    st.title("📁 学生 小杰 数字档案")

    # 基础信息
    with st.expander("📄 基础信息", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**学生ID**: N03-2023-001")
        with col2:
            st.write("**注册时间**: 2023-09-01")
            st.write("**精神状态**: ✅ 正常")
        with col3:
            st.write("**当前徽章**: 🛡️ 技能安全·普通")

    # 技能矩阵
    st.subheader("🎯 技能矩阵")
    skill_cols = st.columns(3)
    with skill_cols[0]:
        st.metric(label="Python", value="88%", delta="+3%")
    with skill_cols[1]:
        st.metric(label="SQL", value="66%", delta="-2%")
    with skill_cols[2]:
        st.metric(label="Vue", value="33%", delta="-1%")

    # 进度条
    st.write("📚 Streamlit课程进度")
    st.progress(60, text="完成度 60%")
    st.caption("目标进度：80% | 剩余课时：4节")

    # 任务日志
    st.subheader("📝 任务日志")
    task_data = {
        "日期": ["2023-10-01", "2023-10-12"],
        "任务名称": ["学生信息管理系统", "课程管理系统"],
        "状态": ["🟢 进行中", "🔴 未完成"],
        "难度": ["★★☆☆☆", "★★★☆☆"]
    }
    task_df = pd.DataFrame(task_data)
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

    # 代码成果
    st.subheader("💻 最新代码成果")
    code_content = '''import streamlit as st
st.title("我的第一个Streamlit应用")
st.text("Hello World!")'''
    st.code(code_content, language="python", line_numbers=True)

    # 底部信息
    st.markdown("---")
    col_foot1, col_foot2, col_foot3 = st.columns(3)
    with col_foot1:
        st.caption("SYSTEM MESSAGE: 下一个任务目标已解锁。")
    with col_foot2:
        st.caption("SYS INFO: 课程管理系统 | CONTENT: 2025-03-01 12:42:48")
    with col_foot3:
        st.caption("系统状态: 🟢 在线 | 服务状态: 🚀 已加速")


elif selected_page == "餐厅数据可视化":
    # 餐厅数据可视化页面
    st.title("餐厅数据可视化分析")

    # 基础数据
    restaurants_base = {
        "餐厅名称": ["东方广场", "万达广场", "朝阳广场", "好友缘", "西冷牛排店"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "latitude": [22.807814, 22.832476, 22.819243, 22.809105, 22.839699],
        "longitude": [108.448890, 108.286408, 108.321189, 108.378664, 108.245804]
    }
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
    peak_hours = ["11:00", "12:00", "13:00", "14:00", "17:00", "18:00", "19:00", "20:00"]
    peak_flow_data = {
        "时段": peak_hours,
        "东方广场": np.random.uniform(80, 120, 8).round(0),
        "万达广场": np.random.uniform(90, 130, 8).round(0),
        "朝阳广场": np.random.uniform(150, 200, 8).round(0),
        "好友缘": np.random.uniform(70, 100, 8).round(0),
        "西冷牛排店": np.random.uniform(60, 90, 8).round(0)
    }

    # 数据整理
    df_base = pd.DataFrame(restaurants_base)
    df_base.index = pd.RangeIndex(start=1, stop=6, name="序号")
    df_price = pd.DataFrame(price_data)
    df_peak = pd.DataFrame(peak_flow_data)

    # 展示内容
    st.header("ℹ️ 一、5家餐厅基础信息")
    st.dataframe(df_base, use_container_width=True)

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

    st.header("💰 三、5家餐厅12个月人均消费走势")
    st.line_chart(
        df_price,
        x="月份",
        y=["东方广场", "万达广场", "朝阳广场", "好友缘", "西冷牛排店"],
        width=800,
        height=500,
        use_container_width=False
    )

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

    st.header("🗺 五、餐厅地理位置分布")
    st.map(df_base[["latitude", "longitude"]], zoom=10)


elif selected_page == "音乐播放器":
    # 音乐播放器页面
    st.set_page_config(page_title="音乐播放器", page_icon="🎵")
    st.markdown("""
        <style>
        .song-title { font-size: 26px; color: #1E88E5; font-weight: bold; margin-bottom: 10px; text-align: center; }
        .player-section { background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin-top: 20px; }
        .stButton>button { width: 100%; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🎵 我的音乐播放器")
    st.markdown("---")

    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    # 歌曲数据
    songs = [
        {
            'url': "https://d.musicapp.migu.cn/prod/playlist-service/playListimg/402bdb81-c298-4582-b208-543920fb8b08.jpg",
            'text': '告白气球',
            'audio_url': 'https://music.163.com/song/media/outer/url?id=2649263922.mp3'
        },
        {
            'url': "https://images.genius.com/2f9fcf00e373d592f6da1835a7638469.1000x1000x1.jpg",
            'text': '天外来物',
            'audio_url': 'https://music.163.com/song/media/outer/url?id=2759345435.mp3'
        },
        {
            'url': "https://n.sinaimg.cn/sinakd10117/110/w700h1010/20200728/3c5f-iwxpesx6821977.jpg",
            'text': '天后',
            'audio_url': 'https://music.163.com/song/media/outer/url?id=2636693518.mp3'
        }
    ]

    # 布局
    left_col, right_col = st.columns([1, 1])
    with left_col:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(
            songs[st.session_state['ind']]['url'],
            caption=songs[st.session_state['ind']]['text'],
            width=300
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown(f"<div class='song-title'>{songs[st.session_state['ind']]['text']}</div>", unsafe_allow_html=True)
        st.markdown(f"**歌曲 {st.session_state['ind'] + 1}/{len(songs)}**")
        st.divider()

        # 按钮函数
        def last_song():
            st.session_state['ind'] = (st.session_state['ind'] - 1) % len(songs)
        def next_song():
            st.session_state['ind'] = (st.session_state['ind'] + 1) % len(songs)

        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("◀◀ 上一首", use_container_width=True):
                last_song()
                st.rerun()
        with btn_col2:
            if st.button("下一首 ▶▶", use_container_width=True):
                next_song()
                st.rerun()

        st.divider()
        st.markdown("### 📋 播放列表")
        for i, song in enumerate(songs):
            if i == st.session_state['ind']:
                st.markdown(f"🎵 **{song['text']}** (正在播放)")
            else:
                st.markdown(f"- {song['text']}")

    # 音频播放
    st.markdown("---")
    st.markdown("<div class='player-section'>", unsafe_allow_html=True)
    st.markdown("### 🔊 音频播放器")
    current_audio = songs[st.session_state['ind']]['audio_url']
    st.audio(current_audio, format='audio/mp3')
    st.info(f"正在播放: **{songs[st.session_state['ind']]['text']}**")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.caption("音乐播放器 v1.0 | 使用Streamlit构建")


elif selected_page == "我的相册":
    # 我的相册页面
    st.set_page_config(page_title="相册", page_icon="🐱")
    st.title("我的相册")

    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    images = [
        {
            'url': "https://www.thehappycatsite.com/wp-content/uploads/2020/12/What-does-it-mean-if-a-cat-winks-at-you-HC-long.jpg",
            'text': '猫'
        },
        {
            'url': "https://www.2008php.com/2012_Website_appreciate/2012-06-20/20120620130237.jpg",
            'text': '狗'
        },
        {
            'url': "https://i-1-shuajizhijia.zswxy.cn/2025/0711/ca230ae156e54830a802d2250ab494bf.jpg?imageView2/2/q/50",
            'text': '猴'
        }
    ]

    st.image(
        images[st.session_state['ind']]['url'],
        caption=images[st.session_state['ind']]['text'],
        use_container_width=True
    )

    def last_img():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)
    def next_img():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

    c1, c2 = st.columns(2)
    with c1:
        st.button("上一张", on_click=last_img, use_container_width=True)
    with c2:
        st.button("下一张", on_click=next_img, use_container_width=True)


elif selected_page == "个人简历生成器":
    # 个人简历生成器页面
    st.set_page_config(page_title="个人简历生成器", page_icon="✨", layout="wide")
    # 深色主题样式
    st.markdown("""
        <style>
        .stApp { background-color: #121212; color: #e0e0e0; }
        .stTextInput>div>div>input, .stDateInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>div>textarea {
            background-color: #2d2d2d; color: #ffffff; border: 1px solid #444444; border-radius: 6px; padding: 8px;
        }
        h1 { color: #ffffff; font-size: 2.5rem; margin-bottom: 0.5rem; }
        h2, h3, h4 { color: #ffffff; border-bottom: 1px solid #333; padding-bottom: 8px; margin-top: 1.5rem; margin-bottom: 1rem; }
        .stContainer { background-color: #1e1e1e; border: 1px solid #333333; border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem; }
        .stButton>button { background-color: #6366f1; color: white; border: none; border-radius: 6px; padding: 8px 16px; }
        .stButton>button:hover { background-color: #4f46e5; }
        .image-container img { width: 100% !important; border-radius: 8px; }
        .resume-item { margin-bottom: 0.8rem; font-size: 1.05rem; line-height: 1.6; }
        .resume-title { color: #6366f1; margin-bottom: 1.2rem; }
        </style>
    """, unsafe_allow_html=True)

    st.title("✨ 个人简历生成器")
    st.caption("使用Streamlit创建你的个性化简历 | 实时预览 · 简单易用")
    st.divider()

    # 分栏布局
    form_col, preview_col = st.columns((1, 2), gap="large")

    with form_col:
        st.subheader("📝 个人信息填写")
        st.markdown("---")

        # 基础信息
        with st.container(border=True):
            st.markdown("### 基础信息")
            user_name = st.text_input("姓名", placeholder="请输入您的姓名", help="必填项")
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
                user_time = st.time_input("最佳联系时间", value=None)
            with col2:
                user_edu = st.selectbox("学历", ["请选择", "高中", "大专", "本科", "硕士", "博士"], index=0)
                user_exp = st.number_input("工作年限（年）", min_value=0, step=1, placeholder="0")
                user_lang = st.selectbox("语言能力", ["请选择", "普通话", "英语", "日语", "德语", "法语"], index=0)

        # 求职期望
        with st.container(border=True):
            st.markdown("### 求职期望")
            user_salary = st.slider(
                "期望薪资范围（元/月）", min_value=3000, max_value=100000, value=(10000, 20000), format="%d元"
            )
            user_skill = st.selectbox("核心技能", ["请选择", "Python", "Java", "项目管理", "数据分析", "UI设计"], index=0)
            user_grad = st.selectbox("毕业院校及时间", ["请选择", "2024年 某某大学", "2023年 某某大学", "2022年 某某大学"], index=0)

        # 更多信息
        with st.container(border=True):
            st.markdown("### 更多信息")
            user_intro = st.text_area(
                "个人简介", placeholder="请简要介绍您的专业能力、职业目标（100-500字）", height=120
            )
            st.markdown("#### 个人照片")
            user_photo = st.file_uploader(
                "上传照片（支持PNG/JPG/JPEG）", type=["png", "jpg", "jpeg"], help="建议尺寸：200x250像素"
            )

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
                    pos_text = user_position if user_position else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <strong style='color: #6366f1;'>求职意向：</strong> {pos_text}
                    </div>
                    """, unsafe_allow_html=True)
                    phone_text = user_phone if user_phone else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <strong style='color: #6366f1;'>联系电话：</strong> {phone_text}
                    </div>
                    """, unsafe_allow_html=True)
                    email_text = user_email if user_email else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <strong style='color: #6366f1;'>电子邮箱：</strong> {email_text}
                    </div>
                    """, unsafe_allow_html=True)

            # 个人信息
            with st.container(border=True):
                st.markdown("<h3 class='resume-title'>个人信息</h3>", unsafe_allow_html=True)
                info_col1, info_col2 = st.columns(2, gap="medium")
                with info_col1:
                    gender_text = user_gender if user_gender else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>📌</span> <strong>性别：</strong> {gender_text}
                    </div>
                    """, unsafe_allow_html=True)
                    edu_text = user_edu if user_edu != "请选择" else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>🎓</span> <strong>学历：</strong> {edu_text}
                    </div>
                    """, unsafe_allow_html=True)
                    exp_text = f"{user_exp}年" if user_exp > 0 else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>💼</span> <strong>工作年限：</strong> {exp_text}
                    </div>
                    """, unsafe_allow_html=True)
                    lang_text = user_lang if user_lang != "请选择" else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>🎯</span> <strong>语言能力：</strong> {lang_text}
                    </div>
                    """, unsafe_allow_html=True)
                with info_col2:
                    birth_text = user_birth.strftime('%Y/%m/%d') if user_birth else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>📅</span> <strong>出生日期：</strong> {birth_text}
                    </div>
                    """, unsafe_allow_html=True)
                    time_text = user_time if user_time else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>🕒</span> <strong>最佳联系时间：</strong> {time_text}
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>💰</span> <strong>期望薪资：</strong> {user_salary[0]} - {user_salary[1]}元/月
                    </div>
                    """, unsafe_allow_html=True)
                    grad_text = user_grad if user_grad != "请选择" else "未填写"
                    st.markdown(f"""
                    <div class='resume-item'>
                        <span style='color: #6366f1;'>🎓</span> <strong>毕业信息：</strong> {grad_text}
                    </div>
                    """, unsafe_allow_html=True)

            # 技能和简介
            with st.container(border=True):
                st.markdown("<h3 class='resume-title'>专业技能</h3>", unsafe_allow_html=True)
                skill_text = user_skill if user_skill != "请选择" else "未填写"
                st.markdown(f"""
                <div class='resume-item' style='padding: 0.8rem; background-color: #252525; border-radius: 6px;'>
                    <span style='color: #6366f1;'>🔧</span> <span style='font-size: 1.1rem;'>{skill_text}</span>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("<h3 class='resume-title'>个人简介</h3>", unsafe_allow_html=True)
                if user_intro:
                    st.markdown(f"""
                    <div style='padding: 1rem; background-color: #252525; border-radius: 6px; border-left: 4px solid #6366f1; font-size: 1.05rem; line-height: 1.8;'>
                        {user_intro}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style='padding: 1rem; background-color: #252525; border-radius: 6px; border-left: 4px solid #888; color: #999;'>
                        请在左侧填写个人简介，突出您的优势和职业目标。
                    </div>
                    """, unsafe_allow_html=True)

            # 下载按钮
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
            with st.container(border=True):
                st.markdown("""
                <div style="text-align: center; padding: 3rem 0;">
                    <h3 style='color: #ffffff;'>👋 欢迎使用简历生成器</h3>
                    <p style="color: #999; font-size: 1.1rem; margin: 1rem 0;">请先在左侧表单填写您的姓名，简历预览内容会实时更新</p>
                    <p style="color: #6366f1; font-size: 1.1rem;">填写完成后，您可以预览、下载您的个性化简历</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #666; font-size: 0.9rem;'>© 2025 个人简历生成器 | 使用 Streamlit 构建</div>", unsafe_allow_html=True)


elif selected_page == "电击小子第二部":
    # 电击小子视频页面
    st.title("电击小子第二部")
    video_arr = [
        {
            'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/53/13/430521353/430521353-1-208.mp4?e=ig8euxZM2rNcNbRV7wdVhwdlhWdMhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=cos&mid=0&nbs=1&platform=html5&trid=c761618f77944b998e5b76d4d617d9dh&uipk=5&gen=playurlv3&deadline=1765768541&oi=771356656&os=cosovbv&upsig=50cd45567506ba9c8d9e03b9dea81bde&uparams=e,og,mid,nbs,platform,trid,uipk,gen,deadline,oi,os&bvc=vod&nettype=0&bw=834536&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
            'title': '第1集',
            'episode': 1
        },
        {
            'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/01/15/430521501/430521501-1-208.mp4?e=ig8euxZM2rNcNbR1hWdVhwdlhWR1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&og=hw&platform=html5&nbs=1&trid=d6ce221317b64a8ab0183c546653874h&mid=0&uipk=5&gen=playurlv3&oi=771356656&deadline=1765768644&upsig=c75eaedbe405537dd5b255269763cd85&uparams=e,os,og,platform,nbs,trid,mid,uipk,gen,oi,deadline&bvc=vod&nettype=0&bw=893081&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
            'title': '第2集',
            'episode': 2
        },
        {
            'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/55/17/430521755/430521755-1-208.mp4?e=ig8euxZM2rNcNbRV7WdVhwdlhWdBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&platform=html5&gen=playurlv3&deadline=1765768743&oi=771356656&nbs=1&trid=4404d71fd1aa43de990196b5df441fbh&uipk=5&os=cosovbv&og=cos&upsig=2e7489a10567158ffa375421899d808a&uparams=e,mid,platform,gen,deadline,oi,nbs,trid,uipk,os,og&bvc=vod&nettype=0&bw=842386&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
            'title': '第3集',
            'episode': 3
        }
    ]

    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    # 播放视频
    st.video(video_arr[st.session_state['ind']]['url'])

    # 切换集数
    def play(i):
        st.session_state['ind'] = int(i)

    # 集数按钮
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
                    on_click=play,
                    args=(episode_num,),
                    key=f'btn_{episode_num}'
                )

    # 简介
    st.divider()
    st.subheader(f"第{st.session_state['ind']+1}集简介")
    descriptions = [
        "电击小子第二部开篇，小光面临新的挑战，必须掌握新力量保护城市。",
        "电击小子发现神秘能源，这可能成为拯救城市的关键。",
        "战斗白热化，电击小子必须做出艰难选择，新盟友出现。"
    ]
    st.info(descriptions[st.session_state['ind']])

    with st.expander("查看更多信息"):
        st.write("**动画信息**:")
        st.write("- 类型: 国产动画")
        st.write("- 适合年龄: 6-12岁")
        st.write("- 主题: 科幻、冒险、友情")
        st.write("- 出品方: 中国动画公司")
        st.write("")
        st.write("**温馨提示**:")
        st.write("本视频仅供学习交流使用，请支持正版动画。")
