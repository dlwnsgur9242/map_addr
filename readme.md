# 주소 -> 위도, 경도 자동 변환 프로그램

## 사용방법

    1. Naver map api 발급 받는다. (geocoding api) 
    2. Naver map api 발급 주소 https://console.ncloud.com/naver-service/application
    3. AddressConversion.py 파일에 client_id = "API_ID", client_secret = "API_SECRET"를 key 값을 넣는다.
    4. input.txt에 주소를 입력한다. (다수의 주소일 경우 1줄에 1주소 입력)
    5. AddressConversion.py를 실행하면 output.txt 파일이 생성되고 변환된 위도, 경로 값이 있다.