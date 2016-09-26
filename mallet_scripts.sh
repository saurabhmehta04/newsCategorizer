
/home/joseph/mallet-2.0.7/bin/mallet import-dir --input text/ --output /home/joseph/Desktop/Project_Topic_Modelling/topic-input-news_articles.mallet --keep-sequence --remove-stopwords

/home/joseph/mallet-2.0.7/bin/mallet train-topics --input /home/joseph/Desktop/Project_Topic_Modelling/topic-input-news_articles.mallet --num-topics 30 --output-doc-topics /home/joseph/Desktop/Project_Topic_Modelling/doc-topics-news_articles.txt --output-topic-keys /home/joseph/Desktop/Project_Topic_Modelling/topic-keys-news_articles.txt --random-seed 1