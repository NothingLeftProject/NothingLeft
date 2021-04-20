<p align="center">
    <a href="https://nothingleftproject.github.io/ProjectDocs">
      <img alt="NothingLeftWiki" src="./backend/data/image/NothingLeftLogo2.jpg">
    </a>
  </p>

<h1 align="center">
    <b>NothingLeft</b>
  </h1>
<p align="center">
    A time management system based on GTD.
</p>
<p align="center">
  <a href="https://nothingleftproject.github.io/ProjectDocs">ProjectDocument</a> | 
  <a href="https://nothingleftproject.github.io/ProjectDocs/#/usage/README">Usage</a>
</p>
<p align="center">
    <img src="https://svg.hamm.cn/badge.svg?key=License&&value=Apache2.0">
    <img src="https://svg.hamm.cn/badge.svg?key=Status&&value=InDeveloping">
    <img src="https://svg.hamm.cn/badge.svg?key=Version&&value=dev-0.6">
</p>

# NothingLeft-Backend
- NothingLeft经典系统-后端


## 简介-Introduction
- Other languages: 
  - [English](./README_en.md)


### 使用-Usage
- 准备好mongoDB和Memcached
- python3 -m pip install flask pymongo pymemcache socket
- git clone https://github.com/NothingLeftProject/NothingLeft
- 修改setting.json中的databaseSettings中的mongodb和memcached中的address->default分别为数据库的对应地址
- 将setting.json中的hostIP清空
- python3 run.py即可启动
- 更多请查看本项目的[Wiki](https://nothingleftproject.github.io/ProjectDocs/#/usage/README)

### 关于GTD-About GTD:
- Getting Things Done is a kind of time management system which was proposed by David Allen. Usually, we abbreviate Getting Things Done as GTD.
- [Gtd-Introduction](./GTD.md)


### 设计-Design
- 那么，这个项目是如何使用，或者说工作的呢
- **交互（前端）**
  - 首先，我们需要一个可视化的交互口以便用户操作，而这种可视化的交互口是可以有很多种实现方式的。在这里，我就对一些初级阶段需要实现的交互方式进行列举和说明
    - ***1、网页/WEB端***：不得不说，web工具真的是很好用，轻量简洁。我个人目前考虑使用flutter来实现，不过我还不会js，但我会努力的，有人愿意也可以联系我一起开发
    - ***2、DUEROS语音交互***：通过语音交互，你可以很方便的对inbox进行整理、分类、规划等等，而DUEROS的各种设备销量都很不错，其对第三方技能开发的支持也很友善，因此我会在DUEROS上做一个技能，然后用户可以连接到公用或自己的服务器来使用
    - ***3、xiaolan/wukong-robot语音交互***：xiaolan和wukong-robot都是运行在各种DIY设备上的语音交互机器人，但它们与DUEROS的区别就是其都由广大开发者制作的。而其中的xiaolan就是我做的一个，虽然没有wukong厉害，但我会加油的
- **后端**
  - 很明显，后端就是支持整个软件运行的部分，其重要性显而易见
  - 那么关于后端我是打算使用python来编写的（毕竟我python比较熟），而且用python做后端的软件也不少，就比如「Instagram」
  - 后端包括了「服务端」和「基本业务」
    - 服务端就是给DUEROS等更多的非自有前端（如WEB端就是自有前端）的一个接口，用户也可以根据自己的喜好，按照我们提供的API接口来开发自己喜欢的交互方式
    - 而基本业务就是最底层的部分了。基本业务其实就是完全配合GTD，再加上一些创新的实现
- 到这里，相信你已经对本项目有了一定的认识，如果您想要了解更多，请查看我们的[Wiki](https://nothingleftproject.github.io/NothingLeft/)


## 更多-More

### 贡献者-Contributors
- Lan_zhijiang(我)
- 当然也欢迎大家来一起开发
  - DingTalk: 18680171381
  - Email: lanzhijiang@foxmail.com
  - Wechat：18680171381
  - QQ: 1481605673

### 想法区(完成即清除)
- 分类-trashList中的stuff状态自动变成cancel
- maintainer需要去监控各种动向，并根据不同的动向做出不同决策以自动维护整个系统
  - 变更即通知maintainer
  - 根据明显的stuff特征自动分类
  - 自动生成行动链
  - 提供行动模板（共享市场规划）
- 使用memecached加快运行速度
- 多语言支持
- 前端颜色与系统设置 or 本地时间 同步
- 注意！因为API的验证设置，必须要使请求时间戳与本地同步误差在5min以内
  - 但同时，stuff的createDate仍然需要按照客户端本地时间，这是为了用户的体验所必须的
- 考虑支持为stuff添加附件，achieved的则自动删除文件（设置中可以设置更多关于附件留存，大小限制的决策）

### 提交记录-Commit Log
- 基本完成了user的全部内容，配合数据库
- 基本完成了http服务器，接入了user的一部分内容
- 第一次测试后端，开始第一次调试——user部分
  - 添加了启动检查数据库
  - 修复了各种各样的bug
- 调试成功，完整的http实现，测试成功了login功能
- 添加了建议、理念等的信息收集处(./research)
- 完成了在centos系统上的启动调试
- 完成了logout/signup/login功能并且调试没有问题
- 完成了root初始化的调试，没有问题
- 修了一堆关于user操作的bug
- 调试并完成了user_delete
- 修复了一堆关于user_info_update的bug
- 调试修复pass了user_info_update
- 测试修复pass了user_info_get_all
- 测试修复pass了user_info_get_one_multi
- 测试修复pass了user_get_permissions
- 测试修复pass新修复的安全bug
- 修复了一些因账户不存在的bug
- 测试修复pass了user_write_permissions
- 测试修复pass了user_edit_permissions
- 再修复pass了在全初始下的数据库建立及setup
- 废弃user_manager中的loginUsers判断法，以isOnline为准，修了一堆bug
- 写了个add_stuff和modify_stuff并修改了一些东西，适配了一些东西
- 添加了get_many_stuffs并修了一些InboxManager里的bugs
- 完成了InboxManager基本功能，未经调试，修复了一些显而易见的bug
- 修复sign_up bug，通过了其dev-0.6下的测试
- stuff支持了自定义属性
- stuff支持了事件(event)分割及其状态设置
- 又又又修了一堆bug
- log支持级别打印和路径设置
- 修复关于用户注册及其用户组和发现的一系列问题
- 测试修复并pass了以下功能：
  - stuff_add
  - stuff_modify
  - stuff_get
  - stuff_get_id_from_condition
  - stuff_delete_many
  - stuff_get_id_from_preset
- 测试修复pass还更新了stuff_generate_preset_list
- 还修了一堆问题
- 更新新的预设列表，优化算法
- 修复并pass了:
  - stuff_delete_many_custom_attribute 
  - stuff_add_events
  - stuff_set_event_status
  - stuff_get_event_status
  - stuff_remove_events
  - stuff_remove_event_status
- AchievedPoint: 测试完基本的InboxManager功能
- 添加了inbox归档功能
- 优化md5加密性能并修复Enc...一个bug