import re

def fix_alignment_flags(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    content = re.sub(r'Qt.AlignmentFlag.Qt.AlignmentFlag', r'Qt.AlignmentFlag', content)
    content = re.sub(r'setWeight\(QFont\.\)', r'setWeight(QFont.Weight(50))', content)
    with open(file_path, 'w') as file:
        file.write(content)

fix_alignment_flags('UI_files/modules/ui_main.py')  # 수정할 파일 경로 입력