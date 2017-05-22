# chat-python

It is a typing practice through the file of the 'lyrics.txt'  
And analyzes the content of the typing.
> Changing the file 'lyrics.txt' will change the typing content.

### main.py
Allows you to type the contents of the file 'lyrics.txt' line by line.  
calculate typing time and length by one line, record the result in 'Score-record.txt' file.
> Repeatedly, you will know your score better.

### test.py
Save scores and information about 'lyrics.txt', in 'Statistical_Value.csv'  

#### AnalysisScore.py
Returns the average score of the file 'lyrics.txt'.

#### AnalysisLyrics.py
Save the data below in the file 'Statistical_Value.csv'.
- Typing score from 'AnalysisScore.py'
- Number of characters in line
- The ratio of Korean to English
- Number of spaces
- The number of characters with a foot (complexity)

#### R
![](R/Rplot.png)  
Analyze the 'Statistical_Value.csv' file, analyze the relationship between the data obtained from 'AnalysisLyrics.py' and the typing score.  
<pre><code>
> all [, -1] %>% cor
              AVscore        KEP    Linelen    Spacelen  complexity
AVscore     1.0000000  0.3891366 -0.6516162 -0.46269420  0.22641782
KEP         0.3891366  1.0000000 -0.2419969  0.14275028  0.70893567
Linelen    -0.6516162 -0.2419969  1.0000000  0.74986696 -0.20604870
Spacelen   -0.4626942  0.1427503  0.7498670  1.00000000  0.05701685
complexity  0.2264178  0.7089357 -0.2060487  0.05701685  1.00000000
</code></pre>
> This is my experiment.

#### Forward
If you know what you're missing, you can learn that part.  
Learning the insufficient part can offset the insufficient part.  
Now this is a trivial conclusion, but this program will change.
