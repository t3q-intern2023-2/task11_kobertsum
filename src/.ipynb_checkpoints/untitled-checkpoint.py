from transformers import BertTokenizer, BertModel
from models.model_builder import ExtSummarizer  # model_builder.py에서 ExtSummarizer 클래스를 가져옵니다.
import torch
from prepro.data_builder import BertData
from models.data_loader import Batch

# 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained("monologg/kobert", do_lower_case=True)

# 모델 설정값 정의 (기본 설정 사용)
class Args:
    def __init__(self):
        self.beta1 = 0.9
        self.beta2 = 0.999
        self.dec_dropout = 0.2
        self.dec_ff_size = 2048
        self.dec_heads = 8
        self.dec_hidden_size = 768
        self.dec_layers = 6
        self.enc_dropout = 0.2
        self.enc_ff_size = 512
        self.enc_hidden_size = 512
        self.enc_layers = 6
        self.encoder = 'bert'
        self.ext_dropout = 0.2
        self.ext_ff_size = 2048
        self.ext_heads = 8
        self.ext_hidden_size = 768
        self.ext_layers = 2
        self.finetune_bert = True
        self.large = False
        self.lr = 1e-3
        self.lr_bert = 2e-3
        self.lr_dec = 2e-3
        self.max_grad_norm = 0.1
        self.max_pos = 512
        self.optim = 'adam'
        self.param_init = 0.0
        self.param_init_glorot = True
        self.share_emb = False
        self.temp_dir = './temp'
        self.use_bert_emb = False
        self.visible_gpus = '-1'
        self.warmup_steps = 8000
        self.warmup_steps_bert = 8000
        self.warmup_steps_dec = 8000

args = Args()

# 모델 로드
model_path = 'model_step_5000.pt'  # 복원된 .pt 파일의 경로를 지정합니다.
model = ExtSummarizer(args, device="cpu", checkpoint=None)  # 설정값을 통해 모델 초기화
#model.load_state_dict(torch.load(model_path))
#model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
model.load_state_dict(checkpoint['model'])
model.eval()

'''
def summarize(text):
    # 텍스트를 토크나이저로 인코딩
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding='max_length')
    
    # 모델에 입력하여 요약 생성 (출력 구조에 따라 코드를 수정해야 할 수 있습니다.)
    with torch.no_grad():
        summary_ids = model(inputs['input_ids'], attention_mask=inputs['attention_mask'])
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
'''

# BertData
class Args2:
    def __init__(self):
        self.min_src_ntokens_per_sent = 1
        self.max_src_ntokens_per_sent = 300
        self.max_src_nsents = 120
        self.min_src_nsents = 1
        self.max_tgt_ntokens = 500
        self.min_tgt_ntokens = 1

args2 = Args2()


def summarize(text):
    # Initialize BertData
    bertdata = BertData(args2)
    
    # Preprocess the input text
    # Assuming the text is a single document and doesn't have a target summary, hence using dummy values
    b_data = bertdata.preprocess(text.split('.'), ['dummy_tgt'], [0] * len(text.split('.')))
    
    # If the preprocess function returns None, handle this case
    if b_data is None:
        return "Error: Preprocessing failed or returned None."
    
    src_subtoken_idxs, sent_labels, tgt_subtoken_idxs, segments_ids, cls_ids, src_txt, tgt_txt = b_data
    
    # Convert preprocessed data to model's input batch
    batch = Batch(src_txt)
    
    # Make inference using the model
    with torch.no_grad():
        summary_ids = model(batch)
    
    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


text = "미국 정부가 양자컴퓨팅·AI(인공지능)·반도체에 대한 대중(對中) 투자를 제한한다. 반도체 장비 등 설비·부품 등을 위주로 이어지던 대중 압박이 자금줄까지 확대되는 것이다. 당장 국내 산업계에 끼치는 영향은 없겠지만, 동맹에 대한 동참 압박이 커질 경우 영향이 불가피할 것이란 전망이 나온다. 10일 외신에 따르면 조 바이든 미국 대통령은 9일(현지 시각) 사모펀드와 벤처 캐피탈 등 미국의 자본이 투자우려국인 중국의 첨단 반도체와 양자 컴퓨팅, AI 등 3개 분야에 대해 투자하는 것을 규제하는 행정명령을 발표했다. 이번 행정명령에 따라 해당 분야에서 중국에 투자를 진행하려는 미국인과 미국기업들은 사전에 투자 계획을 의무적으로 신고해야 하며, 재닛 옐런 재무장관이 규제권을 행사하게 된다."

print(summarize(text))
