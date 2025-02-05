import pandas as pd

# 엑셀 파일 경로와 파일명
excel_file = 'data/서버위경도통합본(완성).xlsx'
sheet_name = '한화kit'

# 엑셀 파일 읽기
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# SQL UPDATE 문 생성
update_statements = []
for index, row in df.iterrows():
    sl_id = row['번호']
    pin_xy = row['위경도']
    pin_xy = f'{pin_xy}'
    sql = f"UPDATE dbo.tm_user SET pin_xy = '{pin_xy}' WHERE sl_id = {sl_id};"
    update_statements.append(sql)

# 생성된 SQL 문 출력 또는 파일로 저장
for statement in update_statements:
    print(statement)

# 또는 파일로 저장하려면 다음 코드 사용
with open('data/sqlconversion.txt', 'w') as file:
    for statement in update_statements:
        file.write(statement + '\n')