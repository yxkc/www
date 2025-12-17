import streamlit as st

st.set_page_config(page_title="音乐播放器", page_icon="🎵")

# 添加自定义CSS样式
st.markdown("""
<style>
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
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎵 我的音乐播放器")
st.markdown("---")

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 歌曲数据 - 已填入音频URL
images = [
    {
        'url': "https://d.musicapp.migu.cn/prod/playlist-service/playListimg/402bdb81-c298-4582-b208-543920fb8b08.jpg",
        'text': '告白气球',
        'audio_url': 'https://music.163.com/song/media/outer/url?id=2649263922.mp3'
    }, {
        'url': "https://images.genius.com/2f9fcf00e373d592f6da1835a7638469.1000x1000x1.jpg",
        'text': '天外来物',
        'audio_url': 'https://music.163.com/song/media/outer/url?id=2759345435.mp3'
    }, {
        'url': "https://n.sinaimg.cn/sinakd10117/110/w700h1010/20200728/3c5f-iwxpesx6821977.jpg",
        'text': '天后',
        'audio_url': 'https://music.163.com/song/media/outer/url?id=2636693518.mp3'
    }]

# 创建左右两列布局
left_col, right_col = st.columns([1, 1])

with left_col:
    # 左侧显示专辑封面
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(
        images[st.session_state['ind']]['url'], 
        caption=images[st.session_state['ind']]['text'],
        width=300
    )
    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    # 右侧显示歌曲标题
    st.markdown(f"<div class='song-title'>{images[st.session_state['ind']]['text']}</div>", unsafe_allow_html=True)
    
    # 显示当前歌曲序号
    st.markdown(f"**歌曲 {st.session_state['ind'] + 1}/{len(images)}**")
    
    # 添加分隔符
    st.divider()
    
    # 按钮回调函数
    def lastImg():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

    def nextImg():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
    
    # 在右侧创建三个并排的按钮
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        if st.button("◀◀ 上一首", use_container_width=True):
            lastImg()
            st.rerun()
    
    with btn_col2:
        if st.button("下一首 ▶▶", use_container_width=True):
            nextImg()
            st.rerun()
    
    st.divider()
    
    # 播放列表显示
    st.markdown("### 📋 播放列表")
    for i, img in enumerate(images):
        if i == st.session_state['ind']:
            st.markdown(f"🎵 **{img['text']}** (正在播放)")
        else:
            st.markdown(f"- {img['text']}")

# 音频播放器部分
st.markdown("---")
st.markdown("<div class='player-section'>", unsafe_allow_html=True)

st.markdown("### 🔊 音频播放器")

# 显示当前歌曲的音频播放器
current_audio_url = images[st.session_state['ind']]['audio_url']

# 直接显示音频播放器
st.audio(current_audio_url, format='audio/mp3')

# 添加一个简洁的当前播放信息
st.info(f"正在播放: **{images[st.session_state['ind']]['text']}**")

st.markdown("</div>", unsafe_allow_html=True)

# 底部信息
st.markdown("---")
st.caption("音乐播放器 v1.0 | 使用Streamlit构建")
