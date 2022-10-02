import streamlit as st
import io
from PIL import Image
import similar_search


st.title = "類似画像検索アプリ"

uploaded_file = st.file_uploader("Choose an image..", type='png')

if uploaded_file is not None:

    img = Image.open(uploaded_file)

    #st.image(img, caption='Uploaded Image.', use_column_width=True)

    with io.BytesIO() as output:

        # img.save("similar.png", output, format = "png")
        img.save("similar.png", format = "png")
        # binary_img = output.getvalue() #バイナリ取得

    from PIL import ImageDraw, ImageFont
    fontsize=40

    font = ImageFont.truetype(font="fonts\meiryo.ttc",
        size=fontsize)

    draw = ImageDraw.Draw(img)
    st.write('入力画像')
    st.image(img)

    dists = similar_search.similar_search()
    asend_dists = sorted(dists.items(), key=lambda x:x[1])

    for i in range(0,5):
        st.write(f'{i+1}番目に似ている画像です')
        st.write(f'{asend_dists[i][0]}')
        st.image(asend_dists[i][0])

"""
#類似した画像を抽出したい画像を選択してください
#上位5位までが表示されます
"""