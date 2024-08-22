from transformers import pipeline 
import pandas as pd 
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import keras
import pandas as pd
import numpy as np
classifier = pipeline('sentiment-analysis')
data = pd.read_csv('output.csv')
texts = "\n".join(data["text"]).split("\n")
with open("ReviewsForAnalysis.txt", "w") as f_out: ###
    f_out.write("\n".join(texts))
results = classifier(texts)
count=0
qq = [ result['score'] for text, result in zip(texts, results)]
qqq = [ result['label']  for text, result in zip(texts, results)]
data.insert(5, "sentiment", qqq)
data.insert(6, "confidence", qq)
annotated_data = pd.DataFrame(data)
annotated_data.to_csv('output.csv', index=False)
