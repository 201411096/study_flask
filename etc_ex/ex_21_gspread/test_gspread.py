# pip install gspread
# pip install oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

"""
1. 구글 개발자 콘솔 접속
https://console.developers.google.com/
2. Google Drive API / Google Sheets API 사용설정
3. 사용자 인증 정보 만들기
4. 서비스 계정 선택
5. 권한 부여
6. json키 생성
"""

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'C:\\IDE\\Projects\\test\\test_25_1125\\02_gspread\\vivid-art-248015-a364ac4e0711.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/14qdx_vcCjPW0tS0Cjrbf3n1f7G4pTR0Z74y7uQXa6w4/edit#gid=0'

# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('시트1')

"""
1. 데이터 가져오기
    1) 특정 셀 데이터 가져오기
    cell_data = worksheet.acell('B1').value
    print(cell_data)
    2) 행 데이터 가져오기
    row_data = worksheet.row_values(1)
    print(row_data)
    3) 열 데이터 가져오기
    column_data = worksheet.col_values(1)
    print(column_data)
    4) 특정 영역 선택하여 데이터 가져오기
    # 범위(셀 위치 리스트) 가져오기
    range_list = worksheet.range('A1:D2')
    print(range_list)
    # 범위에서 각 셀 값 가져오기
    for cell in range_list:
        print(cell.value)
        
2. 데이터 쓰기
    1) 특정 셀에 값 쓰기
    worksheet.update_acell('B1', 'b1 updated')
    2) 행으로 데이터 추가하기
    worksheet.append_row(['new1', 'new2', 'new3', 'new4'])
    worksheet.insert_row(['new1', 'new2', 'new3', 'new4'], 4)
    3) 시트 크기 조정하기
    worksheet.resize(10,4)

3. 스프레드시트 생성/공유하기
    1) 스프레드시트 생성하기
    gs = gc.create('새로운 테스트')
    worksheet = gs.add_worksheet(title='시트1', rows='1', cols='1')
    2) 스프레드시트 공유, 소유권 부여하기
    gs.share('hleecaster@gmail.com', perm_type='user', role='owner')
"""

cell_data = worksheet.acell('B1').value
print(cell_data)

