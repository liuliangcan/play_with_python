# play_with_python
python刷题记录
- 这个项目组合了几个工具，可以方便的打cf/atc/cc/acw/牛客..等主流平台。
- 主要是省去local test case的复制粘贴工作。
### 项目食用方法
#### 准备工作
- pycharm (必须)*(本工程)*
- 安装一个:(必须)[cpeditor](https://cpeditor.org/zh/docs/)
- 安装一个浏览器插件:(必须)
  - git:[Competitive Companion](https://github.com/jmerle/competitive-companion)
  - chrome store:[Competitive Companion](https://chrome.google.com/webstore/detail/competitive-companion/cjnmckjndlpiamhfimnnjmnckgghkjbl)
- [cf_tool](https://github.com/liuliangcan/cf-tool):(可选)你可能想直接用cpeditor提交cf，需要这个命令行工具
    - 原项目不再维护，但不支持pypy64，因此我重新编译了这个项目，使它支持pypy64，可以直接使用这个exe:~/tools/cf_tool
#### 配置
- pycharm: 这个就不说了，下载工程后找个路径打开。（若放在F:\play_with_code\play_with_python下，那么后边的配置会非常简单)
- cpeditor: 下载完成后直接导入我的配置文件tools/cp_editor/play_python_in_disk_f_code.cpeditor
  - 若你的py工程不是上述位置，则需要单独修改文件路径相关的配置，包括：
    1. 选项-设置-文件路径-默认路径-file
    2. 选项-设置-语言-python-Python模板-模板路径
    3. (可选)选项-设置-扩展-CF Tool
- Competitive Companion: 直接安装即可。
- cf-tool: 需要初始化 `cf config`，具体[教程](https://github.com/liuliangcan/cf-tool#usage)。
  - 先login
  - 然后 add a template,当然选pypy 64,其余的模板文件路径啥的随便选，反正我们也不用cf tool创建模板；文件后缀是py。
  - 然后 set default template，设置我们刚才add的那项即可。

#### 使用
1. 打开cpeditor和pycharm等着。
2. 用装好插件的chrome打开一道cf题目。
3. 点击右上角的Competitive Companion绿色图标。
4. 2秒后cpeditor会自动new出新的模板文件，包括本题的case。
5. 切换到cpeditor  ctrl+s会把文件保存到本地(注意保存到~/file/)。
6. 切换到pycharm ~/file路径下找到这个文件。
7. 敲代码。
8. 切到cpeditor，点击运行测试。
9. 若你配置了cf tool，那么可以直接提交。(当然仅限于cf题目)
---
#### 打lc。
- tools/leetgo 这个路径下是lc命令行工具[leetgo](https://github.com/j178/leetgo),大佬开发的。
- 但我还不熟练。使用方式见大佬的git。
- 有一点小bug:
  - 工具可以自动读取浏览器的cookie来登录，但是若你的登录权限已过期，它识别不出来，需要你再登一次浏览器。
  - 若你装了多浏览器，最好手动退出到只剩一个。否则工具找到第一个“自认合法”的浏览器就不继续了。
- 总之别忘了leetgo init

#### 题外话
- 为了方便我在模板文件里import了好多不一定用到的头，但是这其实是占运行时间的，在acw上尤甚。如果卡时间可以尝试删除没用的。


---
- 20231021:搞到gitee上