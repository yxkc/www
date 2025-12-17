import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io

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


