import streamlit as st

## Title
st.title("Streamlit Tutorial")
## Header/Subheader
st.header("This is header")
st.subheader("This is subheader")
## Text
st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")

## Markdown syntax
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown header")
st.markdown("### This is a Markdown subheader")
st.markdown("- item 1\n"
" - item 1.1\n"
" - item 1.2\n" "- item 2\n"
"- item 3")
st.markdown("1. item 1\n"
" 1. item 1.1\n"
" 2. item 1.2\n"
           "2. item 2\n"
           "3. item 3")
           
## Latex
st.latex(r"Y = \alpha + \beta X_i")
## Latex-inline
st.markdown(r"회귀분석에서 잔차식은 다음과 같습니다 $e_i = y_i — \hat{y}_i$")

## Error/message text
st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error!")
st.exception("NameError('Error name is not defined')")


## Load data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#GitHub에서 아이리스 데이터 다운로드
url = "iris.csv"
iris_df = pd.read_csv(url)

## Return table/dataframe
# table
st.table(iris_df.head())
# dataframe
st.dataframe(iris_df)
st.write(iris_df)
st.markdown("* * *")

## Checkbox
if st.checkbox("Show/Hide"): st.write("체크박스가 선택되었습니다.")


## Radio button
status = st.radio("Select status.", ("Active", "Inactive"))
if status == "Active":
    st.success("활성화 되었습니다.")
else:
    st.warning("비활성화 되었습니다.")

## Select Box
occupation = st.selectbox("직군을 선택하세요.", [ "Backend Developer",
"Frontend Developer",
"ML Engineer",
    "Engineer",
    "Database Administrator",
    "Scientist",
    "Data Analyst",
    "Security Engineer"
])
st.write(" 직군은 ", occupation, " 입니다.")

## MultiSelect
location = st.multiselect("선호하는 유투브 채널을 선택하세요.",
(
 "운동",
 "IT 기기",
 "브이로그",
 "먹방",
 "반려동물",
 "맛집 리뷰"
 )
)
st.write(len(location), "가지를 선택했습니다.")

## Slider
level = st.slider("레벨을 선택하세요.", 1, 5)


## Buttons
if st.button("About"):
    st.text("Streamlit을 이용한 튜토리얼입니다.")


# Text Input
first_name = st.text_input("Enter Your First Name", "Type Here ...")
if st.button("Submit", key='first_name'):
    result = first_name.title()
    st.success(result)
# Text Area
message = st.text_area("메세지를 입력하세요.", "Type Here ...")
if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)
    
    
## Date Input
import streamlit as st
import datetime
today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.", datetime.time())

## Display Raw Code — one line
st.subheader("Display one-line code")
st.code("import numpy as np")
# Display Raw Code — snippet
st.subheader("Display code snippet")
with st.echo():
# 여기서부터 아래의 코드를 출력합니다.
    import pandas as pd
    df = pd.DataFrame()
## Display JSON
st.subheader("Display JSON")
st.json({"name" : "민수", "gender": "male", "Age": 29})

## Sidebars
st.sidebar.header("사이드바 메뉴")
st.sidebar.selectbox("메뉴를 선택하세요.",["데이터", "EDA", "코드"])

## Plotting
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.subheader("Matplotlib으로 차트 그리기")
#GitHub에서 아이리스 데이터 다운로드
url = "iris.csv"
iris_df = pd.read_csv(url)
## Plotting
st.subheader("Matplotlib으로 차트 그리기")
fig, ax = plt.subplots()
ax = iris_df[iris_df['variety']=='Setosa']['petal.length'].hist()
st.pyplot(fig)

st.title("Registeration form")
first, last = st.columns(2)
first.text_input("First Name")
last.text_input("Last Name")
email, mob = st.columns([3,1])
email.text_input("Email ID")
mob.text_input("Mob Number")
user, pw, pw2 = st.columns(3)
user.text_input("Username")
pw.text_input("Password", type="password")
pw2.text_input("Retype your password", type="password")
ch, bl, sub = st.columns(3)
ch.checkbox("I Agree")
sub.button("Submit")

st.title('Counter Example')
# Streamlit runs from top to bottom on every iteraction so
# we check if `count` has already been initialized in st.session_state.
# If no, then initialize count to 0
# If count is already initialized, don't do anything
if 'count' not in st.session_state:
       st.session_state.count = 0
# Create a button which will increment the counter
increment = st.button('Increment')
if increment:
    st.session_state.count += 1
# A button to decrement the counter
decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1
    
st.write('Count = ', st.session_state.count)


uploaded_files = st.file_uploader("Choose a CSV file",
accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)




import platform
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='AppleGothic') # 스트림릿 앱 생성
st.title("데이터 프로파일링 실습")
# 파일 업로드 위젯
uploaded_file = st.file_uploader("데이터 파일 업로드", type=["csv", "xlsx"])


if uploaded_file is not None:
# 업로드한 파일을 DataFrame 으로 변환
    df = pd.read_csv(uploaded_file) # 엑셀 파일일 경우 pd.read_excel사용
    # 데이터 프로파일링 st.header("데이터 미리보기") st.write(df.head())
    st.header("기본 정보")
    st.write("행 수:", df.shape[0])
    st.write("열 수:", df.shape[1])
    st.header("누락된 값")
    missing_data = df.isnull().sum()
    st.write(missing_data)
    
    st.header("중복된 행 수")
    duplicated_rows = df.duplicated().sum()
    st.write(duplicated_rows)
    
    st.header("수치형 데이터 기술 통계량")
    numerical_stats = df.describe()
    st.write(numerical_stats)
    
    st.header("이상치 탐지 (상자 그림)")
    plt.figure(figsize=(10, 6))
    plt.boxplot(df.select_dtypes(include=['number']).values)
    plt.xticks(range(1, len(df.columns) + 1), df.columns, rotation=45)
    plt.title("Outlier detection (box plot)")
    st.pyplot(plt)
    
    st.header("데이터 분포 시각화")
    column_to_plot = st.selectbox("열 선택", df.columns)
    plt.figure(figsize=(10, 6))
    plt.hist(df[column_to_plot], bins=20, edgecolor='k')
    plt.xlabel(column_to_plot)
    plt.ylabel("빈도")
    plt.title(f"{column_to_plot} Data Distribution")
    st.pyplot(plt)


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
# 아이리스 데이터셋 불러오기 @st.cache_data
def load_data():
#GitHub에서 아이리스 데이터 다운로드
    url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
    iris_df = pd.read_csv(url)
    return iris_df
iris_data = load_data()

#스트림릿 앱 제목 설정
st.title('아이리스 데이터 시각화')
# 데이터프레임 출력 st.subheader('아이리스 데이터셋') st.write(iris_data)
# 품종별 특성 분포 시각화 st.subheader('품종별 특성 분포')
for feature in iris_data.columns[:-1]:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='species', y=feature, data=iris_data)
    plt.title(f'{feature} Distribution')
    plt.xlabel('species')
    plt.ylabel(feature)
    st.pyplot()
# 특성 간 상관 관계 시각화
st.subheader('특성 간 상관 관계')
correlation_matrix = iris_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
st.pyplot()
# 품종별 특성 산점도 시각화
st.subheader('품종별 특성 산점도')
sns.pairplot(iris_data, hue='species', diag_kind='kde')
st.pyplot()
