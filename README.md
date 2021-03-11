## 环境配置

### 开发环境
我们推荐使用Anaconda来创建环境。
```shell
# 导出依赖环境到freeze.yml文件
conda env export > freeze.yml
# 根据freeze来直接创建项目的运行环境
conda env create -f freeze.yml
```
### 线上运行环境
