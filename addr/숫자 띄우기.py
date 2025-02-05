# 파일 읽기
with open("addr/input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 쉼표(,) 뒤에 공백 추가
updated_lines = [line.replace(",", ", ") if "," in line and ", " not in line else line for line in lines]

# 파일 다시 쓰기
with open("addr/input.txt", "w", encoding="utf-8") as file:
    file.writelines(updated_lines)

print("input.txt 파일이 정상적으로 수정되었습니다.")