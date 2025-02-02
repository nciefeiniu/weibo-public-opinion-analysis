CSDN，52账号：灵海之森
微信公众号：西书北影。欢迎关注

环境：Python3.6

全新的微博爬虫三件套已发布，位于

https://github.com/stay-leave/weibo-crawler

基于网页端，字段和数据量更上一个台阶。

仅做学习交流使用！不收费，若发现搬运倒卖的，请私信我处理。

包含微博爬虫、LDA主题分析和情感分析三个部分。

新增话题热度、话题相似度部分。

新增地图可视化部分，数据由团队自行搜集。


1.微博爬虫

实现微博评论爬取和微博用户信息爬取，一天大概十万条。

![image](https://user-images.githubusercontent.com/58450966/147920881-f8e6f6ea-b389-417b-b13f-5d60829ecf40.png)

![image](https://user-images.githubusercontent.com/58450966/147920969-56bd4164-5599-4ecc-9918-55a42ab37b63.png)


2.LDA主题分析

实现文档主题抽取，包括数据清洗及分词、主题数的确定（主题一致性和困惑度）和最优主题模型的选择（暴力搜索）。

![image](https://user-images.githubusercontent.com/58450966/147921016-4f4bd003-4c68-4d51-82e3-eb5e14433960.png)


3.情感分析

实现评论文本的情感值计算，准确率超过97%，处于0到1之间。

![image](https://user-images.githubusercontent.com/58450966/147921147-90cd3019-a47f-496d-a783-b43d09aa1550.png)

![image](https://user-images.githubusercontent.com/58450966/147921200-db688b8e-2941-4a19-9aaa-aeabb3d9bab2.png)

4.话题热度计算

实现话题的热度的计算，同一时间内总和为1.

![image](https://user-images.githubusercontent.com/58450966/147921229-08e7ffea-c953-4efa-b52e-cdff40c615cc.png)


5.主题相似度计算

实现两个相邻时间片的话题的演化探测，以判断主题演化情况。

![image](https://user-images.githubusercontent.com/58450966/147921312-0917b2bf-d1ff-4076-933f-cb126f0fef16.png)

6.地图绘制

实现分省市情感均值、评论总数、新增确诊人数的地图可视化。

![{%F0EED5 @H@P5 1UKV~R4](https://user-images.githubusercontent.com/58450966/156149916-d1334422-3df7-416c-b9d5-317fd81323e4.png)



流程:
1.爬取数据: 爬取正文，爬取评论，爬取用户信息
2.清洗数据: 清洗正文，清洗评论
3.情感分析: 针对评论进行，将其输入Baidu-aip的接口，获得情感分类结果。
4.主题分析: 针对正文进行，将其按月份聚合，进行分词成TXT，导入lda进行训练，找到最优模型进行结果输出。
2.主题演化趋势: 根据主题分析结果，将关键词之间进行链接，绘制主题河流图。
主要就是这些。



## 详细的运行流程

### 爬虫运行步骤：

1. 获取微博的登录cookie
2. 把cookie保存在 `weibo-crawler/cookies.py` 中
3. 运行 `weibo_blog.py` (weibo-crawler目录里面)
4. 运行 `comment_crawler.py`  (weibo-crawler目录里面)
5. 运行 `user_info.py`  (weibo-crawler目录里面)
6. 运行 `data_cleaning.py`  (weibo-crawler目录里面)

### 情感分析运行步骤

1. 去百度申请开发者账号，申请自然语言处理

[https://console.bce.baidu.com/ai/#/ai/nlp/overview/index](https://console.bce.baidu.com/ai/#/ai/nlp/overview/index)

如下图：
![](./images/img.png)
![](./images/img_1.png)

把获取到的
AppID	
API Key	
Secret Key
填入到 `emotional_analysis/api_keys.py` 这个文件中

先修改 `情感分析_API版.py` 里面的文件
```python
save_file(run('../weibo-crawler/清洗评论/M3RcTmtVC.xls'), '三情感值.xlsx')
# 只需要修改  M3RcTmtVC.xls 这个，换为你自己目录下的文件
```
然后运行 `情感分析_API版.py`

同理  `情感分析_SDK版.py` 一样的


### LDA 运行步骤

1. 运行 `excel转txt.py`，请自己修改names
2. 运行 `分词处理.py` ，也是自己修改 a_na 的值为上一步的输出结果，也就是 `excel转txt结果` 目录下的文件
3. 运行 `LDA+超参.py` 即可

运行后会在这些目录下产生结果
- 主题txt
- 主题可视化
- 主题新闻数
- 分词结果
- 推文话题标签
