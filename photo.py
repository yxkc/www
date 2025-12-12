import streamlit as st

st.set_page_config(page_title="相册", page_icon="🐱")

st.title("我的相册")

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

images = [
    {
        'url': "https://www.thehappycatsite.com/wp-content/uploads/2020/12/What-does-it-mean-if-a-cat-winks-at-you-HC-long.jpg",
        'text': '猫'
    }, {
        'url': "https://www.2008php.com/2012_Website_appreciate/2012-06-20/20120620130237.jpg",
        'text': '狗'
    }, {
        'url': "https://i-1-shuajizhijia.zswxy.cn/2025/0711/ca230ae156e54830a802d2250ab494bf.jpg?imageView2/2/q/50",
        'text': '猴'
    }]

st.image(images[st.session_state['ind']]['url'], 
         caption=images[st.session_state['ind']]['text'])

def lastImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

c1, c2 = st.columns(2)

with c1:
    st.button("上一张", on_click=lastImg, use_container_width=True)
with c2:
    st.button("下一张", on_click=nextImg, use_container_width=True)
