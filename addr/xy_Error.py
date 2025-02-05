import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Alignment

# 엑셀 파일 경로
file_path = "data/주소,좌표변환.xlsx"

# 엑셀 파일의 모든 시트 읽기
sheets = pd.read_excel(file_path, sheet_name=None)

# 빈 리스트 생성 (결과를 저장할 데이터 리스트)
result_data = []

# 모든 시트를 순회하며 처리
for sheet_name, df in sheets.items():
    # 위도,경도 컬럼 찾기
    for col in df.columns:
        if df[col].astype(str).str.contains("0.00,0.00").any():
            # "0.00,0.00"을 포함하는 행 찾기
            filtered_rows = df[df[col] == "0.00,0.00"].copy()
            # 시트 이름 추가
            filtered_rows["Sheet"] = sheet_name
            # 결과 저장
            result_data.append(filtered_rows)

# 결과가 있으면 데이터프레임으로 변환
if result_data:
    result_df = pd.concat(result_data, ignore_index=True)
    
    # 원하는 열 순서로 데이터프레임 정렬
    columns_order = ["번호", "발전소명", "전력", "주소", "위경도", "Sheet"]
    result_df = result_df[columns_order]
    
    # 새로운 엑셀 파일 생성
    wb = Workbook()
    ws = wb.active
    ws.title = "위도경도_오류_데이터"
    
    # 데이터프레임을 엑셀 시트에 추가
    for r in dataframe_to_rows(result_df, index=False, header=True):
        ws.append(r)
    
    # 셀 서식 지정
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # 엑셀 파일 저장
    output_file = "c:/Users/Administrator/Desktop/junfile/iamjun/map_addr/data/위도경도_오류_데이터.xlsx"
    wb.save(output_file)
    print("위도,경도가 0.00,0.00인 데이터를 엑셀 파일로 저장했습니다.")
else:
    print("위도,경도가 0.00,0.00인 데이터가 없습니다.")