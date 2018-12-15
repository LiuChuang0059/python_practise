# 1

### 1. plt.sca()

> subplot()返回它所创建的Axes对象，我们可以将它用变量保存起来，然后用sca()交替让它们成为当前Axes对象，并调用plot()在其中绘图。


```python

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2

x = np.linspace(0, 3, 100)
for i in xrange(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))

```


### 2. ply.gca()

> 使用plt.gca获取当前坐标轴信息.

```python

axes = plt.gca()
axes.set_xlim([x_min,x_max])
axes.set_ylim([y_min,y_max])
axes.set(xlabel="$X_1$", ylabel="$X_2$")

```


### 3. plt.contour([X, Y,] Z, [levels], **kwargs) --绘制等高线 无颜色填充
* X, Y : array-like, optional;The coordinates of the values in Z.X and Y must both be 2-D with the same shape as Z (e.g. created via numpy.meshgrid()),

* Z : array-like(N, M) .The height values over which the contour is drawn.


### 4. plt.contourf([X, Y,] Z, [levels], **kwargs) -- 颜色填充





### 5. plt.scatter
```python
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train.ravel(), s=50, cmap=plt.cm.Spectral, edgecolors='black');

```
* c: 点的颜色 接收A sequence of n numbers to be mapped to colors using cmap and norm.  转换y 的格式
* s: 表示  x点的大小 ，可以表示为x的函数
* edgecolors : 边框颜色
* cmap = plt.cm.Spectral实现的功能是给label为1的点一种颜色，给label为0的点另一种颜色。 可以 自定义颜色


```python
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
# 等高线，8 代表分成8个部分。线款
plt.clabel(C, inline=True, fontsize=10)
# 绘制高度数字
```






























