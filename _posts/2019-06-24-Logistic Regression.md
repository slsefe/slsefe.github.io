本文从线性回归到逻辑回归，从回归问题到分类问题，从二分类问题到多分类问题。

---
## 线性回归

- 假设函数：

$$h_\theta(x)=\theta^Tx$$

- 损失函数：

$$J(\theta_0,\theta_1,\ldots,\theta_n)=\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$$

- 加入L2正则项：

$$J(\theta)=\frac{1}{(2m}[\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2+\lambda\sum_{j=1}^{n}\theta_j^2]$$

- 优化算法（梯度下降）：

$$\theta\leftarrow\theta-\alpha\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x^{(i)}$$

---
## logistic regression

- 假设函数：

逻辑回归在线性回归的基础上对特征进行了**线性组合**，然后通过`sigmoid`函数将得分score映射为(0,1)之间的概率。

sigmoid函数：

$$g(x)=\frac{1}{1+e^{-x}}, g(x)\in(0,1)$$

$$g'(x)=g(x)(1-g(x))$$

故假设函数为：

$$h_\theta(x)=g(\theta_0+\theta_1x_1+\theta_2x_2+\theta_3x_1^2+\theta_4x_2^2)$$

逻辑回归本来是线性的，其非线性能力来自于组合特征（如$x_1^2,x_2^2$）

- 损失函数：

均方误差MSE是多个二次函数的叠加，非凸，可以作为评估指标，不能作为损失函数。

对于二分类，将逻辑回归的输出$h_\theta(x^{(i)})$看做$p(y^{(i)}=1\mid\theta;x^{(i)})$的概率，则$1-h_\theta(x^{(i)})$看做$p(y^{(i)}=0\mid\theta;x^{(i)})$的概率，合并为

$$p(y\mid x)=(h_\theta(x^{(i)}))^y(1-h_\theta(x^{(i)}))^{1-y}$$

则似然函数为：

$$\prod_{i=1}^m=(h_\theta (x^{(i)}))^{y^{(i)}}(1-h_\theta (x^{(i)}))^{1-y^{(i)}}$$

对数似然函数为：

$$\sum_{i=1}^m=y^{(i)}(h_\theta (x^{(i)}))+(1-y^{(i)})(1-h_\theta (x^{(i)}))$$

损失函数为：

$$J(\theta)=-\frac{1}{m}[y^{(i)}(h_\theta (x^{(i)}))+(1-y^{(i)})(1-h_\theta (x^{(i)}))]$$

加入L2正则项：

$$J(\theta)=-\frac{1}{m}[y^{(i)}(h_\theta (x^{(i)}))+(1-y^{(i)})(1-h_\theta (x^{(i)}))]+\frac{\lambda}{2m}\sum_{j=1}^n\theta_j^2$$

二元交叉熵损失函数，对数损失函数，凸函数。

- 优化算法（梯度下降）：

$$\theta_j\leftarrow\theta_j-\alpha\frac{\partial{J(\theta)}}{\partial{\theta_j}}$$

- 从二分类到多分类

1. 构建$\frac{N(N-1)}{2}$个`one vs one`二分类学习器
2. 构建$N$个`one vs rest`二分类学习器

- LR的优点
    - 可以输出分类的概率值
    - 可解释性强（权重代表重要性），可控度高
    - 训练快，特征工程之后效果提升高
    - 输出概率值可以做ranking model
    - 容易扩展，增加feature很容易
- LR的应用
    - CTR预估
    - 推荐系统的learning to rank
    - 分类场景

- 框架库
    - [Liblinear](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)
        - libsvm稀疏向量存储格式，海量数据下速度还可以
        - 高维度离散化特征，准确率逼近非线性切分
        - 参数调节比较方便
        - sklearn的LR实际上是liblinear封装的
    - [spark MLlib](http://spark.apache.org/mllib/)

- 算法调优
    - 合适的正则化：L1, L2, L1+L2
    - 正则化系数C
    - 收敛的阈值e，迭代轮数
    - 调整loss fuction给定不同权重
    - bagging或其他方式的模型融合
    - 最优化算法选择newton-cg, lbfgs, liblinear, sag
        - 小样本：liblinear
        - 大样本：sag
        - 多分类：newton-cg, lbfgs

### LR面试题

1. 样本不平衡问题的处理方式
    假设正负样本比为1:k，有以下几种处理办法：
    - 过采样：对训练集的正样本做插值产生新的正样本，如SMOTE
    - 欠采样：EasyEnsemble利用集成学习机制，将负样本划分为k份，分别与正样本训练k个学习器再进行集成
    - 使用原始训练集进行训练，预测时进行**阈值移动**
2. 下采样之后输出的数据概率如何变化，如何还原？

假设正样本数目为$m^+$，负样本数目为$m^-$，正负样本观测几率为$\frac{m^+}{m^-}$，假设训练集为真实样本总体的无偏估计，观测几率代表真实几率。于是，只要分类器的预测几率大于观测几率就应该判定为正类，即

$$若\frac{y}{1-y}>\frac{m^+}{m^-}则预测为正类$$

采样后正负样本数目一致，按照下式进行判断：

$$若\frac{y}{1-y}>1则预测为正类$$

故对于正样本数目小于负样本数目的训练数据来说，其对负样本下采样（欠采样）之后，正样本在数据中的占比提高，输出数据概率p变大。如果要还原，需要对输出概率除以采样率。

3. L1正则化和L2正则化
    - L1正则化
        - 形式：$\alpha\sum_{i=1}^{N}\abs{w_i}$
        - 截断效应
        - 认为参数服从laplace先验分布
    - L2正则化
        - 形式：$\gamma\sum_{i=1}^{N}\abs{w_i}$
- 
4. LR的使用场景
