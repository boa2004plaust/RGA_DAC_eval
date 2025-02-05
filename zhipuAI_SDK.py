# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:23:09 2025

@author: Jiabao Wang
"""

from zhipuai import ZhipuAI
client = ZhipuAI(api_key="")  # 请填写您自己的APIKey

#######################################对照组1：不使用评价量规和参考答案#############################################
# text = "你是一位专门从事教学的老师，有着丰富的写作和评阅经验。请为以下写作内容打分，分值由低到高分别为数字1，2，3，4，5，6共六种，\
#     直接给出最终得分，如数字：2，无需输出评价结果、评分理由等任何内容。作文内容如下："

#######################################对照组2：仅使用竞赛提供的评价量规#############################################
# text = "你是一位专门从事教学的老师，有着丰富的写作和评阅经验。现给定评价量规：“Holistic Rating for Independent Writing \
# After reading each essay and completing the analytical rating form, assign a holistic score based on the rubric \
# below. For the following evaluations you will need to use a grading scale between 1 (minimum) and 6 \
# (maximum). As with the analytical rating form, the distance between each grade (e.g., 1-2, 3-4, 4-5) should \
# be considered equal. \
# SCORE OF 6: An essay in this category demonstrates clear and consistent mastery, although it may have a \
# few minor errors. A typical essay effectively and insightfully develops a point of view on the issue and \
# demonstrates outstanding critical thinking, using clearly appropriate examples, reasons, and other evidence to \
# support its position; the essay is well organized and clearly focused, demonstrating clear coherence and \
# smooth progression of ideas; the essay exhibits skillful use of language, using a varied, accurate, and apt \
# vocabulary and demonstrates meaningful variety in sentence structure; the essay is free of most errors in \
# grammar, usage, and mechanics. \
# SCORE OF 5: An essay in this category demonstrates reasonably consistent mastery, although it will \
# have occasional errors or lapses in quality. A typical essay effectively develops a point of view on the issue \
# and demonstrates strong critical thinking, generally using appropriate examples, reasons, and other evidence \
# to support its position; the essay is well organized and focused, demonstrating coherence and progression of \
# ideas; the essay exhibits facility in the use of language, using appropriate vocabulary demonstrates variety in \
# sentence structure; the essay is generally free of most errors in grammar, usage, and mechanics. \
# SCORE OF 4: An essay in this category demonstrates adequate mastery, although it will have lapses in \
# quality. A typical essay develops a point of view on the issue and demonstrates competent critical thinking, \
# using adequate examples, reasons, and other evidence to support its position; the essay is generally organized \
# and focused, demonstrating some coherence and progression of ideas exhibits adequate; the essay may \
# demonstrate inconsistent facility in the use of language, using generally appropriate vocabulary demonstrates \
# some variety in sentence structure; the essay may have some errors in grammar, usage, and mechanics. \
# SCORE OF 3: An essay in this category demonstrates developing mastery, and is marked by ONE OR \
# MORE of the following weaknesses: develops a point of view on the issue, demonstrating some critical \
# thinking, but may do so inconsistently or use inadequate examples, reasons, or other evidence to support its \
# position; the essay is limited in its organization or focus, or may demonstrate some lapses in coherence or \
# progression of ideas displays; the essay may demonstrate facility in the use of language, but sometimes \
# uses weak vocabulary or inappropriate word choice and/or lacks variety or demonstrates problems in \
# sentence structure; the essay may contain an accumulation of errors in grammar, usage, and mechanics. \
# SCORE OF 2: An essay in this category demonstrates little mastery, and is flawed by ONE OR MORE of \
# the following weaknesses: develops a point of view on the issue that is vague or seriously limited, and \
# demonstrates weak critical thinking, providing inappropriate or insufficient examples, reasons, or other \
# evidence to support its position; the essay is poorly organized and/or focused, or demonstrates serious \
# problems with coherence or progression of ideas; the essay displays very little facility in the use of \
# language, using very limited vocabulary or incorrect word choice and/or demonstrates frequent problems in \
# sentence structure; the essay contains errors in grammar, usage, and mechanics so serious that meaning is \
# somewhat obscured. \
# SCORE OF 1: An essay in this category demonstrates very little or no mastery, and is severely flawed by \
# ONE OR MORE of the following weaknesses: develops no viable point of view on the issue, or provides \
# little or no evidence to support its position; the essay is disorganized or unfocused, resulting in a disjointed or \
# incoherent essay; the essay displays fundamental errors in vocabulary and/or demonstrates severe flaws in \
# sentence structure; the essay contains pervasive errors in grammar, usage, or mechanics that \
# persistently interfere with meaning.”请根据给定的评价量规，为以下写作内容打分，分值由低到高分别为数字1，2，3，4，5，6共六种，\
# 直接给出最终得分，如数字：2，无需输出评价结果、评分理由等任何内容。作文内容如下："

#######################################对照组3：同时使用竞赛提供的评价量规和参考答案############################################## text = "你是一位专门从事教学的老师，有着丰富的写作和评阅经验。现给定评价量规：“Holistic Rating for Independent Writing \
# text = "你是一位专门从事教学的老师，有着丰富的写作和评阅经验。现给定评价量规：“Holistic Rating for Independent Writing \
# After reading each essay and completing the analytical rating form, assign a holistic score based on the rubric \
# below. For the following evaluations you will need to use a grading scale between 1 (minimum) and 6 \
# (maximum). As with the analytical rating form, the distance between each grade (e.g., 1-2, 3-4, 4-5) should \
# be considered equal. \
# SCORE OF 6: An essay in this category demonstrates clear and consistent mastery, although it may have a \
# few minor errors. A typical essay effectively and insightfully develops a point of view on the issue and \
# demonstrates outstanding critical thinking, using clearly appropriate examples, reasons, and other evidence to \
# support its position; the essay is well organized and clearly focused, demonstrating clear coherence and \
# smooth progression of ideas; the essay exhibits skillful use of language, using a varied, accurate, and apt \
# vocabulary and demonstrates meaningful variety in sentence structure; the essay is free of most errors in \
# grammar, usage, and mechanics. \
# SCORE OF 5: An essay in this category demonstrates reasonably consistent mastery, although it will \
# have occasional errors or lapses in quality. A typical essay effectively develops a point of view on the issue \
# and demonstrates strong critical thinking, generally using appropriate examples, reasons, and other evidence \
# to support its position; the essay is well organized and focused, demonstrating coherence and progression of \
# ideas; the essay exhibits facility in the use of language, using appropriate vocabulary demonstrates variety in \
# sentence structure; the essay is generally free of most errors in grammar, usage, and mechanics. \
# SCORE OF 4: An essay in this category demonstrates adequate mastery, although it will have lapses in \
# quality. A typical essay develops a point of view on the issue and demonstrates competent critical thinking, \
# using adequate examples, reasons, and other evidence to support its position; the essay is generally organized \
# and focused, demonstrating some coherence and progression of ideas exhibits adequate; the essay may \
# demonstrate inconsistent facility in the use of language, using generally appropriate vocabulary demonstrates \
# some variety in sentence structure; the essay may have some errors in grammar, usage, and mechanics. \
# SCORE OF 3: An essay in this category demonstrates developing mastery, and is marked by ONE OR \
# MORE of the following weaknesses: develops a point of view on the issue, demonstrating some critical \
# thinking, but may do so inconsistently or use inadequate examples, reasons, or other evidence to support its \
# position; the essay is limited in its organization or focus, or may demonstrate some lapses in coherence or \
# progression of ideas displays; the essay may demonstrate facility in the use of language, but sometimes \
# uses weak vocabulary or inappropriate word choice and/or lacks variety or demonstrates problems in \
# sentence structure; the essay may contain an accumulation of errors in grammar, usage, and mechanics. \
# SCORE OF 2: An essay in this category demonstrates little mastery, and is flawed by ONE OR MORE of \
# the following weaknesses: develops a point of view on the issue that is vague or seriously limited, and \
# demonstrates weak critical thinking, providing inappropriate or insufficient examples, reasons, or other \
# evidence to support its position; the essay is poorly organized and/or focused, or demonstrates serious \
# problems with coherence or progression of ideas; the essay displays very little facility in the use of \
# language, using very limited vocabulary or incorrect word choice and/or demonstrates frequent problems in \
# sentence structure; the essay contains errors in grammar, usage, and mechanics so serious that meaning is \
# somewhat obscured. \
# SCORE OF 1: An essay in this category demonstrates very little or no mastery, and is severely flawed by \
# ONE OR MORE of the following weaknesses: develops no viable point of view on the issue, or provides \
# little or no evidence to support its position; the essay is disorganized or unfocused, resulting in a disjointed or \
# incoherent essay; the essay displays fundamental errors in vocabulary and/or demonstrates severe flaws in \
# sentence structure; the essay contains pervasive errors in grammar, usage, or mechanics that \
# persistently interfere with meaning.”请根据给定的评价量规，为以下写作内容打分，分值由低到高分别为数字1，2，3，4，5，6共六种，\
# 直接给出最终得分，如数字：2，无需输出评价结果、评分理由等任何内容。以下为一篇满分6分的参考作文：“The author supports his arguement quite effectively, \
# though not without any flaws. The author effectively lists off the benefits of exploring Venus, and proper proposals for doing so, \
# however the complexity and unrealistic assumptions of the solutions as well as the negative descripton of Venus take away from its point rather than benefiting it. \
# The effective conveying of benefits helps to support its idea of risking danger for the reward of landing. The author describes \
# how Venus is relatable with earth which creates a connection between the reader and Venus, as well as creating a mood of hospitality \
# and familiarity. It also states that because Venus is the \"nearest option for a planetary visit\", it is a benefit to inhabit Venus first. \
# This persuasion effectivly uses logos to show the audience logical reasoning for why the scientists should endevour to research Venus.\
# The author's proposals for ways to accomplish these tasks help to build ethos in the writing, as it shows that the author knows about \
# the information that is displayed. The introduction of NASA also builds up this ethos, as to bring the audience to better trust in the author. \
# The examples of proposals also provide evidence for how such ideas could be accomplished, such as the ideas of \"systems that use mechanical parts\" \
# and therefore add to the logos of the paragraph, as the author logically explains why the proposals would be beneficial.\
# However in contrast with the effective support of the main idea, the author also convey's information and techniques that oppose his idea. \
# Firstly, the author makes assumptions about how much technology would have advanced, and because his proposal for a \"blimp-like vehicle\" \
# is so technologically advanced and seems outlansish, the mood created for the audience is incredulous and skeptical. \
# This does not benefit the writer's ideas because of the audiences mood, and therefore the author loses the audiences trust in proper solutions.\
# Also negatively impacting the main idea are his descriptions of Venus. This is because the author uses a lot of evidence to support how dangerous \
# Venus is, in direct contrast to what he should be supporting. Because of the logos used to show how dangerous Venus is, like \
# how it has \"temperatures average over 800 degrees\" the audience is put into a mood of impossibility and doubt. \
# Because of the mood of the audience, the audience is also less likely to understand why Venus could be beneficial if the landscape is so terribly trecherous. \
# In conclusion, the writer does a fairly effective job at expressing is ideas, in his building of ethos and pathos that help to support why Venus is so amazing, \
# and how to explore it, however fails by accidently creating a mood of unbelievablity, and therefore losing the audience to the uncertain nature of the situation. \
# If the author had attempted to create a mood that was more beneficial to persuading the audience, the passage would have been extremely effective in \
# persuading the audience of his thesis. ”，需要你评分作文内容如下："
    

#######################################实验组1(RGA-DAC)：仅使用RGA-DAC生成的评价量规#############################################
# text = "你是一位专门从事教学的老师，有着丰富的写作和评阅经验。现给定评价量规：“内容（1分）\
# 评价标准：文章是否有明确的主题和论点，以及论点的深度和广度。\
# 评分细则：\
# 论点明确，并能够从至少三个不同角度深入分析问题，展现出广度（1分）。\
# 论证（2分）\
# 评价标准：文章是否能够提供充分的论据支持论点，论证过程是否合理，以及论据的多样性和相关性。\
# 评分细则：\
# 论据至少涵盖三个方面，如事实、数据、案例等，且每个论据都与论点紧密相关，能够有力支持论点（2分）。\
# 语言表达（2分）\
# 评价标准：文章的语言是否准确流畅，是否使用丰富的词汇和句式，以及是否恰当运用修辞手法。\
# 评分细则：\
# 语言准确流畅，使用丰富的词汇和句式，恰当运用比喻、排比等修辞手法，使文章更具文采（2分）。\
# 结构（1分）\
# 评价标准：文章结构是否清晰，段落划分是否合理，段落之间是否有明确的逻辑联系。\
# 评分细则：\
# 文章结构清晰，段落划分合理，每个段落都有明确的主题句，段落之间有明确的逻辑联系，如因果、对比等（1分）。\
# 创意（1分）\
# 评价标准：文章是否具有新颖的观点和思考，以及创意的原创性和实用性。\
# 评分细则：\
# 创意新颖，能够提出独特的观点或解决方案，并具有一定的现实意义，如对当前社会问题的思考或对未来的展望（1分）。\
# 总评（6分）”请根据给定的评价量规，为以下写作内容打分，分值由低到高分别为数字1，2，3，4，5，6共六种，\
# 直接给出最终得分，如数字：2，无需输出评价结果、评分理由等任何内容。作文内容如下："

#######################################实验组2(RGA-DAC)：同时使用RGA-DAC生成的评价量规和参考答案#############################################
text = "你是一位专门从事教学的老师，有着丰富的写作和评阅经验。现给定评价量规：“内容（1分）\
评价标准：文章是否有明确的主题和论点，以及论点的深度和广度。\
评分细则：\
论点明确，并能够从至少三个不同角度深入分析问题，展现出广度（1分）。\
论证（2分）\
评价标准：文章是否能够提供充分的论据支持论点，论证过程是否合理，以及论据的多样性和相关性。\
评分细则：\
论据至少涵盖三个方面，如事实、数据、案例等，且每个论据都与论点紧密相关，能够有力支持论点（2分）。\
语言表达（2分）\
评价标准：文章的语言是否准确流畅，是否使用丰富的词汇和句式，以及是否恰当运用修辞手法。\
评分细则：\
语言准确流畅，使用丰富的词汇和句式，恰当运用比喻、排比等修辞手法，使文章更具文采（2分）。\
结构（1分）\
评价标准：文章结构是否清晰，段落划分是否合理，段落之间是否有明确的逻辑联系。\
评分细则：\
文章结构清晰，段落划分合理，每个段落都有明确的主题句，段落之间有明确的逻辑联系，如因果、对比等（1分）。\
创意（1分）\
评价标准：文章是否具有新颖的观点和思考，以及创意的原创性和实用性。\
评分细则：\
创意新颖，能够提出独特的观点或解决方案，并具有一定的现实意义，如对当前社会问题的思考或对未来的展望（1分）。\
总评（6分）”请根据给定的评价量规，为以下写作内容打分，分值由低到高分别为数字1，2，3，4，5，6共六种，\
直接给出最终得分，如数字：2，无需输出评价结果、评分理由等任何内容。以下为一篇满分6分的参考作文：“The author supports his arguement quite effectively, \
though not without any flaws. The author effectively lists off the benefits of exploring Venus, and proper proposals for doing so, \
however the complexity and unrealistic assumptions of the solutions as well as the negative descripton of Venus take away from its point rather than benefiting it. \
The effective conveying of benefits helps to support its idea of risking danger for the reward of landing. The author describes \
how Venus is relatable with earth which creates a connection between the reader and Venus, as well as creating a mood of hospitality \
and familiarity. It also states that because Venus is the \"nearest option for a planetary visit\", it is a benefit to inhabit Venus first. \
This persuasion effectivly uses logos to show the audience logical reasoning for why the scientists should endevour to research Venus.\
The author's proposals for ways to accomplish these tasks help to build ethos in the writing, as it shows that the author knows about \
the information that is displayed. The introduction of NASA also builds up this ethos, as to bring the audience to better trust in the author. \
The examples of proposals also provide evidence for how such ideas could be accomplished, such as the ideas of \"systems that use mechanical parts\" \
and therefore add to the logos of the paragraph, as the author logically explains why the proposals would be beneficial.\
However in contrast with the effective support of the main idea, the author also convey's information and techniques that oppose his idea. \
Firstly, the author makes assumptions about how much technology would have advanced, and because his proposal for a \"blimp-like vehicle\" \
is so technologically advanced and seems outlansish, the mood created for the audience is incredulous and skeptical. \
This does not benefit the writer's ideas because of the audiences mood, and therefore the author loses the audiences trust in proper solutions.\
Also negatively impacting the main idea are his descriptions of Venus. This is because the author uses a lot of evidence to support how dangerous \
Venus is, in direct contrast to what he should be supporting. Because of the logos used to show how dangerous Venus is, like \
how it has \"temperatures average over 800 degrees\" the audience is put into a mood of impossibility and doubt. \
Because of the mood of the audience, the audience is also less likely to understand why Venus could be beneficial if the landscape is so terribly trecherous. \
In conclusion, the writer does a fairly effective job at expressing is ideas, in his building of ethos and pathos that help to support why Venus is so amazing, \
and how to explore it, however fails by accidently creating a mood of unbelievablity, and therefore losing the audience to the uncertain nature of the situation. \
If the author had attempted to create a mood that was more beneficial to persuading the audience, the passage would have been extremely effective in \
persuading the audience of his thesis. ”，需要你评分作文内容如下："




import csv
import time

start_time = time.time()

example_num = 1156
data_file = "train{}.csv".format(example_num)
result_file = "result{}_instructor_rubric_ref.csv".format(example_num)

with open("./"+data_file) as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    
    # 读取标题行（如果有的话）
    headers = next(csvreader)
    print(f'Column names are {", ".join(headers)}')

    i = 0
    # 逐行读取数据
    for row in csvreader:
        # 打印每一行数据
        print(i, row[0], ",", row[2], end=", ")
        
        text2 = text + "\""+ row[1] +"\""
        #print(text2)
        
        response = client.chat.completions.create(
            model="glm-4-plus",  # 请填写您要调用的模型名称
            messages=[
                {"role": "user", "content": text2},
            ],
            stream=True,
        )
        
        result = ""
        for chunk in response:
            result += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="\n")
        
        with open("./"+result_file, "a") as f:
            f.write(row[0]+","+row[2]+","+result+"\n")
        i = i+1
        
        if i > example_num:
            break


end_time = time.time()
elapsed_time = end_time - start_time
print(f"程序耗时：{elapsed_time}秒")
with open("./"+result_file, "a") as f:
    f.write(f"Time elapsed: {elapsed_time} secs,,\n")