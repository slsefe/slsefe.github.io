## 线性回归
- 假设函数：
$h_\theta(x)=\theta^Tx$
- 损失函数：
$J(\theta_0,\theta_1,\ldots,\theta_n)=\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$
- 加入L2正则项：
$J(\theta)=\frac{1}{(2m}[\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2+\lambda\sum_{j=1}^{n}\theta_j^2]$
- 优化算法（梯度下降）：
$\theta\leftarrow\theta-\alpha\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x^{(i)}$
## logistic regression
- 假设函数：
逻辑回归在线性回归的基础上对特征进行了**线性组合**，然后通过`sigmoid`函数将得分score映射为(0,1)之间的概率。
sigmoid函数：
$$g(x)=\frac{1}{1+e^{-x}}, g(x)\in(0,1)$$
$$g^'(x)=g(x)(1-g(x))$$
故假设函数为：
$$h_\theta(x)=g(\theta_0+\theta_1x_1+\theta_2x_2+\theta_3x_1^2+\theta_4x_2^2)$$
逻辑回归本来是线性的，其非线性能力来自于组合特征（如$x_1^2,x_2^2$）
- 损失函数：
均方误差MSE是多个二次函数的叠加，非凸，可以作为评估指标，不能作为损失函数。
对于二分类，将逻辑回归的输出$h_\theta(x^{(i)})$看做$p(y^{(i)}=1\mid\theta;x^{(i)})$的概率，则$1-h_\theta(x^{(i)})$看做$p(y^{(i)}=0\mid\theta;x^{(i)})$的概率，合并为$p(y\minx)=(h_\thetax^{(i)})^y(1-h_\thetax^{(i)})^{1-y}$
则似然函数为：
$$\prod_{i=1}^m=(h_\theta x^{(i)})^{y^{(i)}}(1-h_\theta x^{(i)})^{1-y^{(i)}}$$
对数似然函数为：
$$\sum_{i=1}^m=y^{(i)}(h_\theta x^{(i)})+(1-y^{(i)})(1-h_\theta x^{(i)})$$
损失函数为：
$$J(\theta)=-\frac{1}{m}[y^{(i)}(h_\theta x^{(i)})+(1-y^{(i)})(1-h_\theta x^{(i)})]$$
加入L2正则项：
$$J(\theta)=-\frac{1}{m}[y^{(i)}(h_\theta x^{(i)})+(1-y^{(i)})(1-h_\theta x^{(i)})]+\frac{\lambda}{2m}\sum_{j=1}^n\theta_j^2$$
二元交叉熵损失函数，对数损失函数，凸函数。
- 优化算法（梯度下降）：
$$\theta_j\leftarrow\theta_j-\alpha\frac{\partial{J(\theta)}}{\partial{\theta_j}}$$


