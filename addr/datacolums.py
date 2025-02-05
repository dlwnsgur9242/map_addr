import pandas as pd

# 엑셀 파일 경로와 파일명
excel_file = 'data/서버위경도통합본(완성).xlsx'

# 엑셀 파일 읽기
df = pd.read_excel(excel_file)

# 데이터프레임의 열 이름 출력
print("데이터프레임의 열 이름:", df.columns.tolist())