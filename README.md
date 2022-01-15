# DJ-Snake
An implementation combining JDE and Deep Snake

一个结合JDE算法和Deep Snake的目标追踪+分割实现
## 配置环境(conda)

**python版本为3.7，另外还要安装[ffmpeg工具](https://www.ffmpeg.org/download.html)并添加到环境变量**

先进入`Towards-Realtime-MOT-master`文件夹再运行`conda`
```
cd Towards-Realtime-MOT-master
conda env create -f jde_env.yaml
```
如果不行的话就打开来一个个装吧😅

`lib`文件夹下是一些pip装不上的包，可以直接用这里的包来本地安装

Deep Snake那边`snakenet/lib/csrc`里面的包可能是要自行编译的，可以参考：

**切记编译之前要进入自己的虚拟环境！！**

[官方环境配置](https://github.com/zju3dv/snake/blob/master/INSTALL.md)

[snake项目pytorch环境编译](https://blog.csdn.net/huangzhaoyu123/article/details/108528100)

[CVPR2020分割算法Deep Snake的配置](https://blog.csdn.net/qq_17783559/article/details/112848170)

[Windows下安装 pycocotools](https://www.jianshu.com/p/8658cda3d553)

[Cython 安装报错以及解决途径](https://blog.csdn.net/weixin_41632154/article/details/80746428)

[小白跑deep snake(巨详细)](https://blog.csdn.net/qq_44941395/article/details/115834970)
## 运行
运行的`demo.py`在`Towards-Realtime-MOT-master`里面

按道理来说是可以用`python demo.py --input-video filename`来运行的，但是上次试了好像不行，那就去`Towards-Realtime-MOT-master`文件夹打开`demo.py`第78行改`--input-video`参数的default值吧

然后一路上会有很多关于找不到文件的报错，找到相应位置代码后改成自己电脑上的路径就好了
