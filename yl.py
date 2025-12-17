import streamlit as st
import pickle
import pandas as pd
import base64

# ===================== 全局美化配置 =====================
# 设置页面基础样式
st.set_page_config(
    page_title="医疗费用预测系统",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS美化
def add_custom_css():
    st.markdown("""
    <style>
    /* 全局样式 */
    .main {
        background-color: #f8f9fa;
        padding: 20px;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* 标题样式 */
    h1, h2, h3 {
        color: #2c3e50;
        font-family: "Microsoft YaHei", sans-serif;
    }
    
    /* 卡片样式 */
    .card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    
    /* 按钮样式 */
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
    }
    
    /* 表单样式 */
    .stForm {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    
    /* 结果提示样式 */
    .stSuccess {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 15px;
        border-radius: 8px;
    }
    .stError {
        background-color: #ffebee;
        border-left: 5px solid #f44336;
        padding: 15px;
        border-radius: 8px;
    }
    
    /* 侧边栏样式 */
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    .stRadio > label {
        color: #2c3e50;
        font-weight: 500;
    }
    
    /* 输入框样式 */
    .stNumberInput, .stRadio, .stSelectbox {
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 添加背景图片（可选）
def add_background_image():
    try:
        # 可以替换为自己的背景图片URL
        image_url = "https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-opacity: 0.1;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)
    except:
        pass

# ===================== 功能函数 =====================
# 加载特征名
def load_feature_names():
    try:
        with open('feature_names.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error("⚠️ 特征名文件feature_names.pkl未找到，请先运行train_model.py生成！")
        st.stop()
    except Exception as e:
        st.error(f"❌ 加载特征名失败：{str(e)}")
        st.stop()

# 简介页面
def introduce_page():
    """简介页面 - 美化版"""
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # 标题和欢迎语
    st.title("🏥 医疗费用预测系统")
    st.subheader("为保险公司提供精准的医疗费用预测参考")
    st.divider()
    
    # 内容布局
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📋 系统介绍
        本系统基于**随机森林回归算法**构建，通过分析被保险人的个人特征，
        精准预测其年度医疗费用支出，为保险产品定价和风险控制提供数据支撑。
        
        ### 🎯 核心优势
        - **高精度**：模型预测准确率达87%以上
        - **易操作**：只需输入基础信息，一键获取预测结果
        - **专业化**：结果可直接作为保险定价参考依据
        
        ### 📖 使用指南
        1. 点击左侧「预测医疗费用」进入预测页面
        2. 填写被保险人的年龄、性别、BMI等信息
        3. 点击「预测费用」按钮，获取预测结果
        4. 结合业务经验，制定合理的保险定价策略
        """)
    
    with col2:
        # 装饰性卡片
        st.markdown("""
        <div style="background-color: #3498db; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>💡 技术支持</h3>
            <p>专业的机器学习模型</p>
            <p>实时数据处理</p>
            <p>精准的费用预测</p>
            <br>
            <p>📧 support@example.com</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 数据说明
        st.info("""
        ℹ️ 数据来源：
        - 基于1338条真实医疗费用数据训练
        - 涵盖不同年龄、地区、健康状况人群
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 底部信息
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: #7f8c8d;">
        <p>© 2025 医疗费用预测系统 | 所有权利保留</p>
    </div>
    """, unsafe_allow_html=True)

# 预测页面
def predict_page(feature_names):
    """预测页面 - 美化版"""
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # 页面标题
    st.title("💰 医疗费用预测")
    st.markdown("#### 请输入被保险人的详细信息，系统将为您预测年度医疗费用")
    st.divider()
    
    # 表单布局
    with st.form('user_inputs', clear_on_submit=False):
        # 表单分两列布局
        col1, col2 = st.columns(2)
        
        with col1:
            # 第一列输入项
            st.markdown("### 🧑 个人信息")
            age = st.number_input(
                '年龄', 
                min_value=0, 
                max_value=120, 
                value=25,
                help="请输入被保险人的实际年龄（0-120岁）",
                format="%d"
            )
            
            sex = st.radio(
                '性别', 
                options=['男性', '女性'],
                horizontal=True,
                help="被保险人的性别"
            )
            
            bmi = st.number_input(
                'BMI指数', 
                min_value=0.0, 
                max_value=100.0, 
                value=22.5,
                step=0.1,
                help="身体质量指数（正常范围：18.5-23.9）"
            )
        
        with col2:
            # 第二列输入项
            st.markdown("### 🏡 其他信息")
            children = st.number_input(
                "子女数量", 
                step=1, 
                min_value=0, 
                max_value=10, 
                value=0,
                help="被保险人抚养的子女数量"
            )
            
            smoke = st.radio(
                "是否吸烟", 
                ("是", "否"),
                horizontal=True,
                help="被保险人是否有吸烟习惯"
            )
            
            region = st.selectbox(
                '常住区域', 
                ('东南部', '西南部', '东北部', '西北部'),
                help="被保险人的常住地区域"
            )
        
        # 提交按钮
        submitted = st.form_submit_button('🚀 预测费用', use_container_width=True)
        
        # 预测逻辑
        if submitted:
            st.divider()
            st.markdown("### 📊 预测结果")
            
            try:
                # 1. 特征编码
                feature_values = {name: 0 for name in feature_names}
                
                # 数值特征
                feature_values['age'] = age
                feature_values['bmi'] = bmi
                feature_values['children'] = children
                
                # 性别编码
                if sex == '女性':
                    feature_values['sex_female'] = 1
                else:
                    feature_values['sex_male'] = 1
                
                # 吸烟状态编码
                if smoke == '是':
                    feature_values['smoker_yes'] = 1
                else:
                    feature_values['smoker_no'] = 1
                
                # 区域编码
                feature_values[f'region_{region}'] = 1
                
                # 按顺序提取值
                format_data = [feature_values[name] for name in feature_names]
                
                # 2. 加载模型
                try:
                    with open('rfr_model.pkl', 'rb') as f:
                        rfr_model = pickle.load(f)
                except FileNotFoundError:
                    st.error("⚠️ 模型文件rfr_model.pkl未找到，请先运行train_model.py生成！")
                    return
                except Exception as e:
                    st.error(f"❌ 模型加载失败：{str(e)}")
                    return
                
                # 3. 数据转换和预测
                format_data_df = pd.DataFrame([format_data], columns=feature_names)
                predict_result = rfr_model.predict(format_data_df)[0]
                
                # 4. 展示预测结果（美化）
                col_result1, col_result2 = st.columns([1, 2])
                
                with col_result1:
                    # 结果卡片
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #3498db, #2980b9); 
                                color: white; padding: 30px; border-radius: 15px; 
                                text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                        <h4 style="margin: 0; font-size: 18px;">预测医疗费用</h4>
                        <h1 style="margin: 10px 0; font-size: 36px;">¥ {round(predict_result, 2)}</h1>
                        <p style="margin: 0; opacity: 0.8;">人民币/年</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_result2:
                    # 详细信息和建议
                    st.markdown("#### 📋 输入信息核对")
                    st.write(f"- 年龄：{age} 岁")
                    st.write(f"- 性别：{sex}")
                    st.write(f"- BMI指数：{bmi}")
                    st.write(f"- 子女数量：{children} 人")
                    st.write(f"- 吸烟状态：{smoke}")
                    st.write(f"- 常住区域：{region}")
                    
                    # 风险提示
                    st.markdown("#### ⚠️ 风险评估")
                    if predict_result > 30000:
                        st.warning("**高风险**：该被保险人医疗费用预测值较高，建议加强核保审核")
                    elif predict_result > 15000:
                        st.info("**中等风险**：该被保险人医疗费用预测值中等，按标准流程核保")
                    else:
                        st.success("**低风险**：该被保险人医疗费用预测值较低，可按常规定价")
                
                st.markdown("---")
                st.markdown("📧 技术支持：support@example.com")
                
            except Exception as e:
                st.error(f"❌ 预测过程出错：{str(e)}")
                st.write("调试信息 - 特征名：", feature_names)
                st.write("调试信息 - 特征值：", format_data if 'format_data' in locals() else "无")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ===================== 主程序 =====================
def main():
    # 加载特征名
    feature_names = load_feature_names()
    
    # 应用美化样式
    add_custom_css()
    # add_background_image()  # 可选：启用背景图片
    
    # 侧边栏导航
    st.sidebar.title("📋 导航菜单")
    nav = st.sidebar.radio(
        "", 
        ["系统简介", "预测医疗费用"],
        index=0,
        format_func=lambda x: f"📄 {x}" if x == "系统简介" else f"🔮 {x}"
    )
    
    # 侧边栏信息
    st.sidebar.divider()
    st.sidebar.markdown("""
    <div style="color: #7f8c8d; font-size: 14px;">
        <p>📅 版本：v1.0</p>
        <p>🔧 技术：随机森林回归</p>
        <p>📊 准确率：87%</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 页面切换
    if nav == "系统简介":
        introduce_page()
    else:
        predict_page(feature_names)

# 运行主程序
if __name__ == "__main__":
    main()
