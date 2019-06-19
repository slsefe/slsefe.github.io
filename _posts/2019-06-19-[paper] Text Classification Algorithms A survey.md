这篇论文是2019年4月发表在information上的一篇关于文本分类算法的综述类长文，对于新手入门文本分类领域有比较好的指引作用。文中将文本分类划分为四个阶段，即特征提取，降维，分类模型训练，模型评估，对应的有四个方面的内容，即文本预处理方法，降维算法，存在的分类算法和模型的评估指标。

本博客只简要介绍文本分类涉及的技术，关于更多细节请参考原论文和论文给出的GitHub。由于版权问题，本文不使用原论文中的图片，如需查看，请参考原论文。

1. 介绍
    - 文本分类系统包含的四个层级：
        - document level
        - paragraph level
        - sentence level
        - sub-sentense level
    - 文本分类任务的四个流程：
        1. 特征提取
        2. 降维（有时不需要）
        3. 分类模型训练
        4. 分类模型评估
2. Text Preprocessing 文本预处理
    - Text Cleaning and Pre-processing 文本清洗和预处理
        - **tokenization** 分词
        - stop words 去停用词
        - capitalization 大写字母小写化
        - Slang and Abbreviation 俚语和缩写
            - 将俚语转换为正式表达
            - 将缩写进行全写化
        - Noise Removal 去除噪音字符
            - 去除标点符号和特殊字符
        - Spelling Correction 拼写纠正：
            - 基于hash和上下文敏感
            - 使用Trie和Damerau–Levenshtein distance
        - Stemming 词干提取
            - 语态和时态归一化，名词单复数归一化
        - Lemmatization 引理化
            - 将一个词的后缀替换为另一个词的后缀或者去掉一个词的后缀
    - Syntactic Word Representation 基于句法的词表示
        - 结合句法和语义知识
        - **N-Gram N元语法**
            - BoW是1-gram的文本表示，包含了词的重要度信息，失去了词的顺序（句法）信息
            - 二元语法、三元语法增加了词的顺序，但没有解决单词的语义信息
        - Syntactic N-Gram 基于句法依存的N元语法
            - 使用句法依存树而不是文本线性结构来定义
    - **Weighted Words 基于权重的词表示**
        - Bag of Words (BoW)
            - 做法：根据文档中单词出现的频率进行编码表示
            - 缺点：1.没有考虑单词的语序问题；2.常见词对表示结果的影响太大；3.没有考虑单词的语义
        - **Term Frequency-Inverse Document Frequency (TF-IDF)
            - 做法：减弱文本库中常用词的影响
            - 缺点：对每个单词单独表示，不能解释单词之间的相似性
    - **Word Embedding 词嵌入**
        - Word2Vec
            - Google 2013年的工作
            - 三层神经网络（两个隐藏层），基于上下文相似的两个词的表示应该相似，为每个词创建了一个高维向量。
            - CBoW:使用multiple context words 预测 current word
            - Skip-gram：使用current 预测 multiply context words
        - Global Vectors for Word Representation (GloVe)
            - Stanford 2014年的工作
            - 基于全局词的共现关系在wikipedia 2014，Gigawords 5，Common Crawl，Twitter数据集上训练得到了50,100,200,300维词向量。
        - FastText
            - Facebook 2016年的工作
            - Word2Vec和GloVe为每个词训练了一个不同的词向量，忽略了单词是由一个个字母组成的事实。Facebook将每个词表示为由n个字符组成的bag。
            - 在维基百科上使用Skip-gram模型训练得到了294种语言的300维预训练词向量
        - Contextualized Word Representations 基于上下文的词表示
            - 基于context2vec
            - 使用双向语言模型训练
            - 也叫ELMo
    - 局限性：尽管CBoW和Skip-gram可以保持句子的句法和语义信息，但是如何保持连贯文档的完整意义仍然存在问题。
3. Dimensionality Reduction 降维
    - Component Analysis
        - Principal Component Analysis (PCA)
        - Independent Component Analysis (ICA)
    - Linear Discriminant Analysis (LDA)
    - Non-Negative Matrix Factorization (NMF)
    - Random Projection
        - Random Kitchen Sinks
        - Johnson Lindenstrauss Lemma
    - Autoencoder
        - General Framework
        - Conventional Autoencoder Architecture
        - Recurrent Autoencoder Architecture
    - T-distributed Stochastic Neighbor Embedding (t-SNE)
4. 文本分类算法
    - 传统方法：Rocchio Classification
    - 集成算法：
        - boosting
        - bagging
    - 传统&仍然流行的算法：
        - LR
        - NB
        - KNN
        - SVM
    - 基于树的算法
        - 决策树
        - 随机森林
    - 基于神经网络
        - DNN
        - RNN
        - CNN
        - DBN
        - HAN
5. 评估方法
    - 存在的问题
        - 缺乏标准的数据收集流程
        - 训练集和测试集的划分方式
        - 不同实验中使用不同的性能指标
    - 分类任务传统评估指标
        - confusion matrix 混淆矩阵
        - accuracy 正确率
        - precision 精确率
        - recall 召回率
        - F1-score
    - macro-averaging & micro-averaging
    - F-score
    - Matthews Correlation Coefficient (MCC)
    - Receiver Operating Characteristics (ROC)
    - Area Under ROC Curve (AUC)











