# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

# import os
#
# os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from transformers import AutoTokenizer

check_point = 'distilbert-base-uncased-finetuned-sst-2-english'
tokenizer = AutoTokenizer.from_pretrained(check_point)
inputs = [
    'I‘m hunger',
    'nice to meet you, lihua'
]
input = tokenizer(inputs, padding=True, truncation=True, return_tensors='pt')
print('input: ', input)
