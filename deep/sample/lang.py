import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. 데이터 준비
# 예시로, Hugging Face 'datasets' 라이브러리를 사용해 텍스트 분류 데이터셋을 불러옵니다.
# 사용하려는 데이터셋에 맞게, 포털 뉴스와 댓글 데이터를 준비하세요.

# 예시로 IMDB 감성 분석 데이터를 사용
dataset = load_dataset("imdb")

# 2. 텍스트 데이터와 라벨을 준비
train_data = dataset['train']
test_data = dataset['test']

# 3. 데이터 전처리 (BERT 토크나이저 사용)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def encode_batch(batch):
    return tokenizer(batch['text'], padding=True, truncation=True, max_length=512)

train_data = train_data.map(encode_batch, batched=True)
test_data = test_data.map(encode_batch, batched=True)

# 4. 데이터셋 준비 (tf.data.Dataset 형식으로 변환)
train_data = train_data.rename_column("label", "labels")
test_data = test_data.rename_column("label", "labels")

train_data.set_format(type='tensorflow', columns=['input_ids', 'attention_mask', 'labels'])
test_data.set_format(type='tensorflow', columns=['input_ids', 'attention_mask', 'labels'])

# BERT 모델을 위한 데이터 준비
train_dataset = tf.data.Dataset.from_tensor_slices((
    {'input_ids': train_data['input_ids'], 'attention_mask': train_data['attention_mask']},
    train_data['labels']
)).batch(8)

test_dataset = tf.data.Dataset.from_tensor_slices((
    {'input_ids': test_data['input_ids'], 'attention_mask': test_data['attention_mask']},
    test_data['labels']
)).batch(8)

# 5. BERT 모델 설정
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# 6. 컴파일 (optimizer, loss function, metric 설정)
optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5)
model.compile(optimizer=optimizer, loss=model.compute_loss, metrics=['accuracy'])

# 7. 모델 학습
history = model.fit(train_dataset, epochs=3, validation_data=test_dataset)

# 8. 모델 평가
predictions = model.predict(test_dataset)
predicted_labels = tf.argmax(predictions.logits, axis=-1)

# 9. 평가 결과 출력 (classification report)
print(classification_report(test_data['labels'], predicted_labels))

# 10. 모델 저장
model.save_pretrained('./news_comment_sentiment_model')
tokenizer.save_pretrained('./news_comment_sentiment_tokenizer')
