import os
import json

# 이미지 폴더 경로
image_dir = 'images'
output_file = os.path.join(image_dir, 'images.json')

# 파일명 기준으로 이름 추출
def extract_name(filename):
    return os.path.splitext(filename)[0]  # 확장자 제거

# 이미지 목록 수집
image_list = [
    {"name": extract_name(f), "file": f}
    for f in os.listdir(image_dir)
    if f.lower().endswith('.jpg')
]

# JSON 저장
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(image_list, f, ensure_ascii=False, indent=2)

print(f"{len(image_list)}개의 항목이 images.json에 저장되었습니다.")
