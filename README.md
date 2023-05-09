# play_with_python
python刷题记录

### 项目实用方法
#### 准备工作
- pycharm (必须)*(本工程)*
- 安装一个:(必须)[cpeditor](https://cpeditor.org/zh/docs/)
- 安装一个浏览器插件:(必须)
  - git:[Competitive Companion](https://github.com/jmerle/competitive-companion)
  - chrome store:[Competitive Companion](https://chrome.google.com/webstore/detail/competitive-companion/cjnmckjndlpiamhfimnnjmnckgghkjbl)
- [cf_tool](https://github.com/liuliangcan/cf-tool):(可选)你可能想直接用cpeditor提交cf，需要这个命令行工具
    - 原项目不再维护，但不支持pypy64,因此我重新编译了这个项目，使它支持pypy64，可以直接使用这个exe:~/tools/cf_tool
#### 配置
- pycharm: 这个就不说了，下载工程后找个路径打开。（若放在F:\play_with_code\play_with_python下，那么后边的配置会非常简单)
- cpeditor: 下载完成后直接导入我的配置文件tools/cp_editor/play_python_in_disk_f_code.cpeditor
  - 若你的py工程不是上述位置，则需要单独修改文件路径相关的配置，包括：
    1. 设置-文件路径-默认路径-file
    2. 设置-语言-python-Python模板-模板路径
    3. (可选)设置-扩展-CF Tool
- Competitive Companion: 直接安装即可。
- cf-tool: 需要初始化 `cf config`，具体[教程](https://github.com/liuliangcan/cf-tool#usage)。