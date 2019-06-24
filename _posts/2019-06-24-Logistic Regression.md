### 线性回归
- 假设函数：$h_\theta(x)=\theta^Tx$
- 损失函数：$J(\theta_0,\theta_1,\ldots,\theta_n)=\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$
- 加入L2正则项：$J(\theta)=\frac{1}{(2m}[\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2+\lambda\sum_{j=1}^{n}\theta_j^2]$
- 优化算法（梯度下降）：$\theta\leftarrow\theta-\alpha\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x^{(i)}$