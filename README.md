# Binary text classification per sarcasm, not sarcam in Ukrainian texts
> Data Sources : X (Twitter), Telegram, Gemini Experimental and GPT-4 Turbo (both synthetic)
> Models: traditional ML (Linear Regression, Random Forest) + [Ukrainian RoBERTa](https://github.com/youscan/language-models)

### [0scraping](https://github.com/botvyns/bachelor_project/tree/main/0scraping)
CSV files with scraped conversational threadі by keywords (sarc, sarcasm, сарк, сарказм) for 23 Telegram channels + python code with a script

### [1data_merge](https://github.com/botvyns/bachelor_project/tree/main/1data_merge)
**Input**:
  - twitter_sarcastic_not_sarcastic.csv (previous dataset from X (Twitter) with text on 2 classes: sarcasm, not sarcasm)
  - telegram_sarcastic.csv (manually reviwed only sarcastic messages from scraped conversational threads)
  - telegram_not_sarcastic_23k.csv (not sarcastic messages from Telelgram)
    
**Output**:
  - dataset.csv (concatenated data from X, Telegram)
  - dataset_cleaned.csv (removed duplicates, ensure class balance)

### [2sampling_synth_real](https://github.com/botvyns/bachelor_project/tree/main/2sampling_synth_real)
**Input**:
  - dataset_cleaned.csv
  - TXT files with generated synthetic sarcastic data per Gemini Experimental, GPT-4 Turbo ber zero-shot, one-shot, few-shot prompting

**Output**:
  - synthetic_data_combined.csv (combined all synthetic sarcastic data)
  - openai_sample.csv (sample for GPT-4 Turbo)
  - gemini_sample.csv (sample for Gemini Eperimental)
  - real_sarc_sample.csv (sample for real sarcastic data)

### [3comparing_synth_real](https://github.com/botvyns/bachelor_project/tree/main/3comparing_synth_real)
**Input**:
  - real_sarc_sample.csv, gemini_sample.csv, openai_sample.csv (equal by words samples for comparing synthetic sarcastic data)

**Output**
  - gemini_sample_lemmatized_ents_ngrams.csv, openai_sample_lemmatized_ents_ngrams.csv, real_sarc_sample_lemmatized_ents_ngrams.csv (equal by words samples with columns for lemmas, NERs, bigrams, trigrams)

### [4prep_data_for_models](https://github.com/botvyns/bachelor_project/tree/main/4prep_data_for_models)
**Input**:
  - dataset_cleaned.csv
  - telegram_not_sarcastic_sample_left.csv (part of telegram_not_sarcastic_23k.csv that was not used for adding not sarcastic data to dataset.csv)
  - synthetic_data_combined.csv

**Output**:
  - dataset_ready_for_models.csv (further cleaned data, ready for ML models)
  - synth_openai_sarc_and_not.csv (GPT-4 Turebo sytnhetic sarcatic data + not sarcastic Telegram data, balanced)

### [5models_training](https://github.com/botvyns/bachelor_project/tree/main/5models_training)
**Input**:
  - dataset_ready_for_models.csv 
  - synth_openai_sarc_and_not.csv

**Output**:
  - test_ready_for_models.csv, train_ready_for_models.csv (train-test split from dataset_ready_for_models.csv)

### Hosted at [Hugging Face Spaces](https://huggingface.co/spaces/Snizhanna/sarcasm_detection)

![HF Spaces](https://github.com/botvyns/bachelor_project/blob/main/image_2024-05-14_10-56-00.png)
