# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:06:08 2016

@author: skybolt
"""

from utilities import *


def get_keywords(word_list , min_ratio=0.001, max_ratio=0.5) :
    """this method takes a word list and returns a set of keywords """
    assert (min_ratio < 1 and max_ratio < 1)
    
    count_dict = {}    
    for word in word_list:
        count_dict.setdefault(word , 0)
        count_dict[word] +=1
    print len(word_list)
    keywords = set()
    for word , cnt in count_dict.items():
        word_percentage = count_dict[word]* 1.0 / len (word_list)
       # print word_percentage
        if word_percentage <= max_ratio and word_percentage >=min_ratio:
            keywords.add(word)
    return keywords
        
	
def get_sentence_weight (sentence , keywords):
    """ this method take a sentence string and a set of keywords and
    returns weight of the sentence """
    sen_list = sentence.split(' ')
    window_start = 0; window_end = -1;
    
    #calculating window start
    for i in range(len(sen_list)):
        if sen_list[i] in keywords:
            window_start = i
            break
    
    #calculating window end
    for i in range(len(sen_list) - 1 , 0 , -1) :
        if sen_list[i] in keywords:
            window_end = i
            break
    
    if window_start > window_end :
        return 0
    
    window_size = window_end - window_start + 1
    
    #calculate number of keywords
    keywords_cnt =0
    for w in sen_list :
        if w in keywords:
            keywords_cnt +=1
    
    return keywords_cnt*keywords_cnt *1.0 / window_size

def summarize(in_file_name ,out_file_name ,  max_no_of_sentences = 10):
    
    txt = get_text_from_file(in_file_name)
    word_list = get_words(txt)
    keywords = get_keywords(word_list , 0.05 , 0.5)
    
    sentence_list = get_sentences(txt)
    #print sentence_list
    sentence_weight = []

    for sen in sentence_list :
        sentence_weight.append ((get_sentence_weight(sen , keywords) ,sen))
            
    sentence_weight.sort(reverse = True)
    #print sentence_weight
    ret_list = []
    ret_cnt = min(max_no_of_sentences  , len(sentence_list))
    
    for i in range (ret_cnt) :
        ret_list.append ('* ' + sentence_weight[i][1] +'.')
    
    out = open (out_file_name , 'w')
    for s in ret_list:
        out.write(s +'\n')
    
    return ret_list
    
    
    
slist = summarize ('text' ,'summary' ,  10)
for s in slist :
    print s
    
    
    
    
        
    
    
