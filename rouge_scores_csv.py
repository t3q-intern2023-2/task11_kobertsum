import os
import argparse
import pandas as pd
from rouge_score import rouge_scorer
from konlpy.tag import Mecab
import datetime

# 명령행 인수 파서 생성
parser = argparse.ArgumentParser()
parser.add_argument('--gold_file', required=True, help="Path to the gold standard summary file")
parser.add_argument('--candidate_file', required=True, help="Path to the candidate summary file")
args = parser.parse_args()

#mecab = Mecab(dicpath="C:/mecab/mecab-ko-dic")  # mecab 초기화
mecab = Mecab()

RESULT_DIR = "intern_task5/task11/ext/results"  # 결과파일 경로

# 가장 최신 파일 가져오기
def get_latest_file(directory, extension):
    files = [f for f in os.listdir(directory) if f.endswith(f".{extension}")]
    if not files:
        print(f"No files with extension '{extension}' found in directory '{directory}'")
        exit(1)  # 프로그램 종료
    latest_file = max(files, key=os.path.getctime)
    return os.path.join(directory, latest_file)

# 최신 골드 표준 요약본 파일과 후보 요약본 파일 경로 설정
latest_gold_file = args.gold_file
latest_candidate_file = args.candidate_file

# 텍스트 파일 읽기 함수
def read_text_file(file_path):
    with open(file_path, "r", encoding="cp949") as f:
        return f.read().split('\n')

# mecab을 사용하여 토큰화
def tokenize_with_mecab(texts):
    return [' '.join(mecab.morphs(text)) for text in texts]

# 텍스트 파일 읽기 및 토큰화
reference_texts = tokenize_with_mecab(read_text_file(latest_gold_file))
candidate_texts = tokenize_with_mecab(read_text_file(latest_candidate_file))

# rouge_scorer 초기화
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)

# 점수 계산 및 데이터 프레임 생성
data = []

for ref_text, cand_text in zip(reference_texts, candidate_texts):
    scores = scorer.score(ref_text, cand_text)
    rouge1 = scores['rouge1']
    rouge2 = scores['rouge2']
    rougeL = scores['rougeL']
    data.append([rouge1[0], rouge1[1], rouge1[2], rouge2[0], rouge2[1], rouge2[2], rougeL[0], rougeL[1], rougeL[2]])

# DataFrame 생성
df = pd.DataFrame(data, columns=['Rouge-1 Precision', 'Rouge-1 Recall', 'Rouge-1 F1-score',
                                  'Rouge-2 Precision', 'Rouge-2 Recall', 'Rouge-2 F1-score',
                                  'Rouge-L Precision', 'Rouge-L Recall', 'Rouge-L F1-score'])

# 결과 파일 경로 생성
now = datetime.datetime.now().strftime('%Y%m%d_%H%M')
output_file_path = os.path.join(RESULT_DIR, f"rouge_score_{now}.csv")
# DataFrame 출력 및 CSV 파일로 저장
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_columns', None)
df.to_csv(output_file_path, index=False, encoding='utf-8')
print(f"ROUGE scores saved to: {output_file_path}")