# DJ-Snake
An implementation combining JDE and Deep Snake
一个结合JDE算法和Deep Snake的目标追踪+分割实现
## 配置环境(conda)
先进入`Towards-Realtime-MOT-master`文件夹再运行`conda`
```
cd Towards-Realtime-MOT-master
conda env create -f jde_env.yaml
```
如果不行的话就打开来一个个装吧😅
## 运行
按道理来说是可以用`python demo.py --input-video filename`来运行的，但是上次试了好像不行，那就去`Towards-Realtime-MOT-master`文件夹打开`demo.py`第78行改`--input-video`参数的default值吧
然后一路上会有很多关于找不到文件的报错，找到相应位置代码后改成自己电脑上的路径就好了
