import streamlit as st
import datetime 
import requests
import json
import pandas as pd

page = st.sidebar.selectbox('Choose your page', ['登録', '更新', '削除'])


if page == '登録':
    st.title('製品情報登録画面')
    with st.form(key='create'):
        Product_name: str = st.text_input('製品名', max_chars=12)
        Price: int = st.number_input('製品価格')
        data = {
            'Product_name': Product_name,
            'Price': Price
        }
        submit_button = st.form_submit_button(label='製品情報登録')

    if submit_button:
        st.write('## 送信データ')
        st.json(data)
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8680/create'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        res.status_code
        if res.status_code == 200:
            st.success('製品情報登録完了')
        st.json(res.json())

    # 製品一覧の取得
    url_products = 'http://127.0.0.1:8680/read'
    res = requests.get(url_products)
    products = res.json()
    products_name = {}
    for product in products:
        products_name[product['product_name']] = product['Price']

    st.write('### 会議室一覧')
    df_products = pd.DataFrame(products)
    df_products.columns = ['製品名', '価格']
    st.table(df_products)

elif page == '更新':
    st.title('製品情報更新画面')
    with st.form(key='update'):
        Product_name: str = st.text_input('製品名')
        Price: int = st.number_input('製品価格')
        data = {
            'Product_name': Product_name,
            'Price': Price
        }
        submit_button = st.form_submit_button(label='製品情報更新')

    if submit_button:
        url = 'http://127.0.0.1:8680/update'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('製品情報更新完了')
        st.json(res.json())

    # 製品一覧の取得
    url_products = 'http://127.0.0.1:8680/read'
    res = requests.get(url_products)
    products = res.json()
    products_name = {}
    for product in products:
        products_name[product['product_name']] = product['Price']

    st.write('### 会議室一覧')
    df_products = pd.DataFrame(products)
    df_products.columns = ['製品名', '価格']
    st.table(df_products)

elif page == '削除':
    st.title('製品情報削除画面')
    with st.form(key='create'):
        Product_name: str = st.text_input('製品名', max_chars=12)
        data = {
            'Product_name': Product_name,
        }
        submit_button = st.form_submit_button(label='製品情報削除')

    if submit_button:
        url = 'http://127.0.0.1:8680/update'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('製品情報削除完了')
        st.json(res.json())

    # 製品一覧の取得
    url_products = 'http://127.0.0.1:8680/read'
    res = requests.get(url_products)
    products = res.json()
    products_name = {}
    for product in products:
        products_name[product['product_name']] = product['Price']

    st.write('### 会議室一覧')
    df_products = pd.DataFrame(products)
    df_products.columns = ['製品名', '価格']
    st.table(df_products)