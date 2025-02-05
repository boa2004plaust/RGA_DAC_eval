# The Code of RGA-DAC for Evaluating the Effectiveness of Rubrics in Automated Essay Scoring

## Data
The data is sampled from the training dataset of the Learning-Agency-Lab---Automated-Essay-Scoring-2.0 competition.
data1200: the first 1,200 samples of the training dataset
data1156: the samples representing scores 1-6, each with 200 samples (except for score 6, which has 156 samples)

## Running
Obtain the ZhipuAI API_KEY and input it into the zhipuAI_SDK.py file.
Run zhipuAI_SDK.py using the command: python zhipuAI_SDK.py. The result file (resultxxx.csv) will be generated in the root directory.
To evaluate different methods, uncomment the relevant sections of the text.

## Note
The results may vary due to the potential for different responses from the LLM for the same input.

