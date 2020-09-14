#!/home/woongsup/anaconda3/bin/python

# import stylecloud
# stylecloud.gen_stylecloud(
#     file_path="text.txt", # text, 대신에 file_path로 경로를 넣을 수도 있음. text옵션을 쓸 땐 단어를 단순히 띄어쓰기로만 토큰화시켜 빈도수 계산.
#     size = 1028,                   # file_path로 할 땐 단어: 빈도 형태의 딕셔너리 파일을 넣어야 함.
#     icon_name = "fas fa-comment-alt",
#     palette='colorbrewer.qualitative.Paired_10',
#     background_color ='white',
#     font_path='/usr/share/fonts/NanumBarunGothic.ttf',
#     output_name="./img/testwordcloud6.png")

import csv

#워드 클라우드를 만드는 코드
def make_cloud():
    dic = dict()
    with open("./data/total_disease2_count_FINAL.csv", 'r', encoding='cp949') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dic[row['title']] = int(row['count'])
    # print(dic)
    import stylecloud
    stylecloud.gen_stylecloud(
        text=dic,  # text, 대신에 file_path로 경로를 넣을 수도 있음. text옵션을 쓸 땐 단어를 단순히 띄어쓰기로만 토큰화시켜 빈도수 계산.
        size=1028,  # file_path로 할 땐 단어: 빈도 형태의 딕셔너리 파일을 넣어야 함.
        icon_name="fas fa-comment-alt",
        palette='colorbrewer.qualitative.Paired_10',
        background_color='white',
        font_path='/usr/share/fonts/NanumBarunGothic.ttf',
        output_name="./img/testwordcloud.png")
#
# make_cloud()
