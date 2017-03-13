# Luhn-s-summarizer
A summarizer script based on Luhn's summarization algorithm

## Algorithm psuedocode :
	1) Calculate signficant words in the text by means of a min and maximum
	   ratio of occurence i.e ignore most frequent words and least frequent ones.  
	2) For each sentence in the text calculate its weight based on the number of keywords squared
	   divided by the windows size which is the maximum distance between two significant words.  
	3) sort sentences in descending order based on their weight and output the first n of them.
	

