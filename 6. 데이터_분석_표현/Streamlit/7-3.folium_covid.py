import streamlit as st
import folium
import pandas as pd

# '.\streamlit\covid_map.csv' 읽어서 map_data에 저장하기
map_data = pd.read_csv('.\streamlit\covid_map.csv')

# 1. 타이틀과 캡션 표시하기
# 타이틀 : 'Covid-19 감염현황'
# 캡션 : 'Displaying geographical data on a map using Streamlit and Folium'
st.title('Covid-19 감염현황')
st.caption('Displaying geographical data on a map using Streamlit and Folium')

# 2. checkbox를 이용하여 checkbox 선택여부에 따라 write 코드를 사용하여 화면에 데이터프레임 값 나타내기 
if st.checkbox('Display Data?'):
    st.write(map_data)

my_map = folium.Map(location=[map_data['lat'].mean(),map_data['lon'].mean()], zoom_start=3)

# 3. 지도에 원형 마커와 값 추가

#데이터프레임 한 행 씩 index, row에 담아서 처리 
for index, row in map_data.iterrows(): 
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=row['value'] / 10000, #원 크기 조정
        color='pink', 
        fill=True, 
        fill_opacity=1.0).add_to(my_map) 

    folium.Marker(
        location=[row['lat'], row['lon']], 
        icon=folium.DivIcon(html=f"<div>{row['name']} {row['value']}</div>"),).add_to(my_map) 

# # 타이틀과 캡션 표시하기
# st.title('Map with Location Data')
# st.caption("Displaying geographical data on a map using Streamlit and Folium")


# 지도 그리기
# st.components.v1.html : Streamlit 라이브러리의 components 모듈에서 html 함수 사용
# ._repr_html_() : 지도를 HTML 형식으로 표시
st.components.v1.html(my_map._repr_html_(),width=1000, height=800)

# # 파일실행: File > New > Terminal(anaconda prompt) → python -m streamlit run streamlit\7-3.folium_covid.py