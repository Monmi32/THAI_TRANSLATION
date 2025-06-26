import pandas as pd
from datasets import Dataset, DatasetDict

train_df = pd.read_csv("/content/train.csv")
val_df = pd.read_csv("/content/validation.csv")

import ast

# Function to extract English and Thai from the 'translation' string
def extract_translation(row):
    try:
        data = ast.literal_eval(row)
        return pd.Series([data.get("en", ""), data.get("th", "")])
    except Exception as e:
        return pd.Series(["", ""])

# Apply to train and validation DataFrames
train_df[['english_text', 'thai_text']] = train_df['translation'].apply(extract_translation)
val_df[['english_text', 'thai_text']] = val_df['translation'].apply(extract_translation)

# Drop the original 'translation' or duplicated column
train_df = train_df.drop(columns=['translation'])
val_df = val_df.drop(columns=['translation'])

# Double-check column names
print(train_df.columns)  

train_dataset = Dataset.from_pandas(train_df)
val_dataset = Dataset.from_pandas(val_df)

raw_datasets = DatasetDict({
    "train": train_dataset,
    "validation": val_dataset
})

# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/mt5-small")

prefix = "translate English to Thai: "

def preprocess_function(examples):
    inputs = [prefix + text for text in examples["english_text"]]
    model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["thai_text"], max_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Check column names
print("Train columns:", train_df.columns)
print("Validation columns:", val_df.columns)

# Rename if needed
train_df.rename(columns={'translation': 'english_text', 'target': 'thai_text'}, inplace=True)  # Adjust to your actual column names
val_df.rename(columns={'translation': 'english_text', 'target': 'thai_text'}, inplace=True)

tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)

from transformers import Seq2SeqTrainingArguments , DataCollatorForSeq2Seq , Seq2SeqTrainer
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    fp16=True  # Optional, if using GPU
)

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    tokenizer=tokenizer,
    data_collator=data_collator
)

print(train_df[['english_text', 'thai_text']].sample(5))
print(train_df[['english_text', 'thai_text']].isnull().sum())

trainer.train()

model.save_pretrained("./my-en-th-model")
tokenizer.save_pretrained("./my-en-th-model")





