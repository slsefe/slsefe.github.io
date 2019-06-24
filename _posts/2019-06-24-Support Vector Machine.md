SVM是一种二分类模型，它的基本模型是定义在特征空间上的间隔最大的线性分类器，间隔最大使它不同于感知机；SVM包含的核方法使它成为实质上的非线性分类器。支持向量机的学习策略就是间隔最大化，可形式化为一个求解凸二次规划的问题，等价于正则化的合页损失函数的最小化问题。

支持向量机包含线性可分支持向量机、线性支持向量机、非线性支持向量机。

### 线性可分SVM

对于分类任务，所有判别式模型的目标都是找到一个决策边界。决策边界在数据低维时可能是一条线，一个平面，到高维时就变成一个超平面。一般来说，符合条件的能够将正负样本分开的决策边界存在多条，如何从存在的多个决策边界选出一条最优的决策边界呢？这里的最优又是如何衡量的呢？不同的算法有不同的处理方法。决策树中`ID3`和`C4.5`都是选择使得**结点切分后信息增益最大化**，增大信息量的过程实际上是一个熵减的过程，也是一个减少不确定性的过程，换言之，使得节点划分后能够在当前的所有划分可能性中每一个子结点中的类别数尽可能少。类似的，`CART`算法选择使用**基尼指数最小化**作为树的生成准则，一个或者多个数据集或者数据子集的基尼指数表示了这个数据集或者数据子集中样本类别的纯度，换言之，也是希望结点划分后的子结点中尽量含有少的样本种类。对于`knn`算法来说，**样本之间的距离**成为度量样本是否是同一类别可能的指标。对于LDA来说更是如此，它将样本投影到一条直线上，要求**同类样本的距离尽可能小，同时不同类样本之间的距离尽可能大**。而对于朴素贝叶斯来说，计算的则是最大后验概率，作为一种生成模型，它需要估计样本的分布的先验概率，条件概率，选择最有可能的输出作为最终的输出。由此可见，**这里`SVM`的分离超平面需要在将正负样本划分正确的情况下，使不同类别的样本尽可能远离此分类超平面，已达到足够大的分类正确置信度。**

对于给定的数据集`D`，假设存在一个分离超平面$w^Tx+b=0$可以将正负样本分开（这里只考虑线性可分二分类问题），这里$w$是超平面的法向量，指向正类的方向，$b$是原点距离超平面的距离，则由$w$和$b$可以唯一确定一个超平面。对于任一点$x_i$，$|w^Tx_i+b|$表示其到超平面的距离，易知对于正样本$wx+b>0$，负样本$wx+b<0$，那么我们的分类决策函数为$f(x)=sign(wx+b)$。我们选择使正负样本的`label`分别为+1和-1，那么我们可以通过分类决策函数与样本`label`的符号是否一致来判断对当前样本的分类是否正确，即用$y_i(w^Tx_i+b)$的正负来表示分类正确与否，绝对值表示分类的确信度（实质为样本点到分类超平面的距离，越远越好）。

定义超平面$(w,b)$关于样本点$(x_i,y_i)$函数间隔为：

$$\hat{\gamma}_i=y_i(w^Tx_i+b)=y_if(x_i)$$

定义超平面$(w,b)$关于训练集D的函数间隔为D中所有样本函数间隔的最小值：

$$\hat{\gamma}=\min{i=1,\dots,N}\hat{\gamma}_i$$

函数间隔可以表示分类预测的正确性及确信度。通过单位化法向量，使$\begin{Vmatrix}w\end{Vmatrix}=1$，这时函数间隔变为几何间隔。超平面$(w,b)$关于样本点$(x_i,y_i)$几何间隔为：

$$\gamma_i=y_i\frac{w^Tx_i+b}{\begin{Vmatrix}w\end{Vmatrix}}$$

定义超平面$(w,b)$关于训练集D的几何间隔为D中所有样本几何间隔的最小值：

$$\gamma=\min{i=1,\dots,N}\\gamma_i$$

则函数间隔和几何间隔有下面的关系：

$$\gamma=\frac{\hat{\gamma}}{\begin{Vmatrix}w\end{Vmatrix}}$$

如果$\begin{Vmatrix}w\end{Vmatrix}=1$，那么函数间隔和几何间隔相等。如果超平面参数w和b成比例改变，函数间隔也成比例改变，而几何间隔不变。

则最大间隔分类器的求解转换为以下约束最优化问题：

$$\max_{w,b}\gamma$$
$$s.t. y_i\frac{w^Tx_i+b}{\begin{Vmatrix}w\end{Vmatrix}}\ge\gamma, i=1,2,ldots,N$$

考虑到几何间隔和函数间隔的关系，改写为：

$$\max_{w,b}\frac{\hat{\gamma}}{\begin{Vmatrix}w\end{Vmatrix}}$$
$$s.t. y_i{w^Tx_i+b}\ge\hat{\gamma}, i=1,2,ldots,N$$

函数间隔$\hat{\gamma}$的改变对对优化问题没有影响，令$\hat{\gamma}=1$，上式改写为：

$$\max_{w,b}\frac{1}{\begin{Vmatrix}w\end{Vmatrix}}$$
$$s.t. y_i{w^Tx_i+b}-1\ge0, i=1,2,ldots,N$$

将最大化问题转变为最小化问题：

$$\min_{w,b}\frac{1}{2}{\begin{Vmatrix}w\end{Vmatrix}}^2$$
$$s.t. y_i{w^Tx_i+b}-1\ge0, i=1,2,ldots,N$$

这是带有限制条件的最小化优化问题，构造拉格朗日函数：

$$L(w,b,\alpha)=\frac{1}{2}{\begin{Vmatrix}w\end{Vmatrix}}^2-\sum_{i=1}^N\alpha_i(y_i(w^Tx_i+b)-1)$$

分别对$w$和$b$求导

$$\frac{\partial L}{\partial w}=\begin{Vmatrix}w\end{Vmatrix}-\sum_{i=1}^N\alpha_iy_ix_i$$

$$\frac{\partial L}{\partial b}=-\sum_{i=1}^N\alpha_iy_i$$

令上面两个式子为0得：

$$\vec{w}^*=\sum_{i=1}^N\alpha_iy_ix_i$$

这里的$\vec{w}^*$可以看做支持向量的线性组合，只有当$x_i$为支持向量时$\alpha_i \neq 0$，而$y_i$取值为{-1,+1}，表示$x_i$为正的支持向量还是负的支持向量。

$$\sum_{i=1}^N\alpha_iy_i=0$$

将$\vec{w}^*$带入$L(w,b,\alpha)$中得：

$$L=\frac{1}{2}\sum_{i=1}^N\alpha_iy_ix_i\sum_{j=1}^N\alpha_jy_jx_j-\sum_{i=1}^N\alpha_i[y_i(\sum_{j=1}^N\alpha_jy_jx_jx_i+b)-1]$$

$$L=\frac{1}{2}\sum_{i=1}^N\alpha_iy_ix_i\sum_{j=1}^N\alpha_jy_jx_j-\sum_{i=1}^N\alpha_iy_ix_i\sum_{j=1}^N\alpha_jy_jx_j-\sum_{i=1}^N\alpha_iy_ib+\sum_{i=1}^N\alpha_i$$

由于$\sum_{i=1}^N\alpha_iy_i=0$，则

$$L=-\frac{1}{2}\sum_{i=1}^N\alpha_iy_ix_i\sum_{j=1}^N\alpha_jy_jx_j+\sum_{i=1}^N\alpha_i$$

$$L=\sum_{i=1}^N\alpha_i-\frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N\alpha_i\alpha_jy_iy_j(x_i)^Tx_j$$

$$L=\sum_{i=1}^N\alpha_i-\frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N\alpha_i\alpha_jy_iy_j(x_i \cdot x_j)$$

故L取决于$(x_i \cdot x_j)$

将$\vec{w}^*$带入决策函数$f(x)=sign(w^*x+b^*)$中得：

$$f(x)=sign(\sum_{i=1}^N\alpha_iy_i(x_i \cdot x)+b^*)$$

这里的$x_i$为支持向量，即对于样本点$(x,y)$，其预测结果只需要计算其与支持向量的内积即可。

### 非线性SVM

令核函数为：

$$K(\vec{x_i},\vec{x_j})=\left \langle \phi (\vec{x_i}),\phi(\vec{x_j}) \right \rangle$$

则

$$L=\sum_{i=1}^N\alpha_i-\frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N\alpha_i\alpha_jy_iy_jK(x_i,x_j)$$

$$f(x)=sign(\sum_{i=1}^N\alpha_iy_iK(x_i,x)+b^*)$$

### SVM的另一种解释

SVM可以看做最小化以下目标函数

$$L=\sum_{i=1}^N[1-y_i(w^Tx_i+b)]_++\lambda{\begin{Vmatrix}w\end{Vmatrix}}^2$$

第一项为经验损失，称为合页损失函数，下标`+`表示以下取正值的函数：

$$
[z]_+=\begin{cases}
z, & \text{ if } z>0 \\ 
0, & \text{ if } z\leq0 
\end{cases}
$$

表示对于距离超平面大于等于1的样本点，其损失为0，否则其损失为$1-y_i(w^Tx_i+b)$

第二项使用系数为$\lambda$的$w$的`L2`范数作为正则项。

### SVM用作多分类

`one vs one`和`one vs rest`

损失函数：

$$L_i=\sum_{j\neq{y_i}}max(0,(w_j^Tx_i+b)-(w_{y_j}^Tx_i+b-\Delta))$$

这里$(w_j^Tx_i+b)$表示错误样本，$w_{y_j}^Tx_i+b$表示正确样本，$\Delta$表示错误样本至少到正确样本的距离。如果大于$\Delta$，损失为0，否则计算损失。

$$L=\frac{1}{N}\sum_iL_i+\lambda R(w)$$

整体的损失为所有样本的平均损失加上正则项。

### 参考资料
- 李航《统计学习方法》
- [理解SVM的三重境界](https://blog.csdn.net/v_july_v/article/details/7624837)