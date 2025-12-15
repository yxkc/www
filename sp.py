import streamlit as st

st.title('电击小子第二部')
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

# 判断内存中有没有ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.video(video_arr[st.session_state['ind']]['url'])

def play(i):
    st.session_state['ind'] = int(i)

#
buttons_per_row = 3  # 每行显示5个按钮

# 将按钮分组，每组buttons_per_row个
for i in range(0, len(video_arr), buttons_per_row):
    # 获取当前行的按钮组
    row_buttons = video_arr[i:i+buttons_per_row]
    
    # 创建列
    cols = st.columns(len(row_buttons))
    
    # 在每个列中放置一个按钮
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
# 在按钮代码后面添加这个简洁版本：

# 添加视频简介
st.divider()
st.subheader(f"第{st.session_state['ind']+1}集简介")

# 简介内容
descriptions = [
    "电击小子第二部开篇，小光面临新的挑战，必须掌握新力量保护城市。",
    "电击小子发现神秘能源源，这可能成为拯救城市的关键。",
    "战斗白热化，电击小子必须做出艰难选择，新盟友出现。"
]

st.info(descriptions[st.session_state['ind']])

# 添加一个展开/收起更多信息的功能
with st.expander("查看更多信息"):
    st.write("**动画信息**:")
    st.write("- 类型: 国产动画")
    st.write("- 适合年龄: 6-12岁")
    st.write("- 主题: 科幻、冒险、友情")
    st.write("- 出品方: 中国动画公司")
    
    st.write("")
    st.write("**温馨提示**:")
    st.write("本视频仅供学习交流使用，请支持正版动画。")
