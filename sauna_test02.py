import streamlit as st
import random

# --- 初期設定 ---
st.set_page_config(page_title="サ飯パスポート", layout="centered")

# --- CSS埋め込み（スクショ風UI） ---
st.markdown("""
<style>
h1 {
    text-align: center;
    color: #8b0000;
}
.main-button {
    background-color: #8b0000;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    border-radius: 4px;
    width: 250px;
    margin: 10px auto;
    display: block;
    cursor: pointer;
    text-align: center;
}
.main-button:hover {
    background-color: #a52a2a;
}
.secondary-button {
    background-color: #dddddd;
    color: black;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    border-radius: 4px;
    width: 250px;
    margin: 10px auto;
    display: block;
    cursor: pointer;
}
.secondary-button:hover {
    background-color: #bbbbbb;
}
.menu-card {
    background-color: #2c3e50;
    color: white;
    border-radius: 6px;
    padding: 12px;
    margin: 12px 0;
    font-size: 18px;
    text-align: center;
}
.total-price {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    margin: 24px 0;
}
.footer-text {
    text-align: center;
    font-size: 12px;
    color: #666666;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# --- ダミーデータ ---
saunas = [
    {"id": 1, "name": "サウナ富士山", "entry_fee": 1200},
    {"id": 2, "name": "渋谷リラックスサウナ", "entry_fee": 1500},
    {"id": 3, "name": "札幌雪サウナ", "entry_fee": 1000}
]

menu_items = [
    {"id": 1, "name": "北欧特製カレーライス", "price": 950},
    {"id": 2, "name": "キリン一番搾り", "price": 670},
    {"id": 3, "name": "味噌汁", "price": 150},
    {"id": 4, "name": "玉子", "price": 100},
    {"id": 5, "name": "唐揚げ", "price": 500},
    {"id": 6, "name": "ポテトフライ", "price": 300}
]

# --- セッション管理 ---
if "selected_sauna" not in st.session_state:
    st.session_state.selected_sauna = saunas[0]
if "selected_menus" not in st.session_state:
    st.session_state.selected_menus = []

# --- UIタイトル ---
st.title("サ飯パスポート")

# --- サウナ選択 ---
sauna_names = [s["name"] for s in saunas]
selected_sauna_name = st.selectbox("施設名を選ぶ", sauna_names, index=0)
st.session_state.selected_sauna = next(s for s in saunas if s["name"] == selected_sauna_name)

# --- ガチャボタン（中央 + 赤背景） ---
if st.button("✨ ガチャを回す！", key="roll"):
    st.session_state.selected_menus = random.sample(menu_items, k=3)

# --- 結果表示 ---
if st.session_state.selected_menus:
    st.header("🎉 結果")

    for menu in st.session_state.selected_menus:
        st.markdown(f"""
        <div class="menu-card">
            {menu['name']}<br>{menu['price']}円
        </div>
        """, unsafe_allow_html=True)

    total = sum(m["price"] for m in st.session_state.selected_menus) + st.session_state.selected_sauna["entry_fee"]
    st.markdown(f'<div class="total-price">合計<br>{total}円</div>', unsafe_allow_html=True)

    # --- ボタン：もう一度回す / トップへ戻る（中央配置） ---
    if st.button("🔁 もう一度回す"):
        st.session_state.selected_menus = random.sample(menu_items, k=3)

    if st.button("⬅️ トップへ戻る"):
        st.session_state.selected_menus = []

# --- 注意書き ---
st.markdown('<div class="footer-text">このアプリは非公式です。実際のメニューや価格とは異なる可能性があります。</div>', unsafe_allow_html=True)
