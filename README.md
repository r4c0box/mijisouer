# mijisouer
command line fo mijisou

just a demo for practice

it is a command line tools for mijisou(<u>https://mijisou.com/</u>)



require:

* python2.x
* requests



Usage: base.py [options]



Options:

  -h, --help            show this help message and exit

  -q QUERY, --query=QUERY

​                        words to query

  -p PAGENO, --page=PAGENO

​                        page to search	



example:

python base.py -q site:10086.cn -p 1

it returns 

```
--------------0
title:移动139邮箱
url_pre:https://mijisou.com/url_proxy?proxyurl=http://www.baidu.com/link?url=aX8el_eB5PiKxSvqSLhTyF1L6AhMUprp6wJ3EpXMtl3&amp;token=994b16d7957fcace8871fd7bf0f53fb44b22906cde2734d9ab81b4ec44a12b5b
url_nuder:http://mail.10086.cn/
content:139邮箱是中国移动提供的电子邮件业务，以手机号@139.com作为邮箱地址，来邮短信及时提醒； 同时提供WEB、WAP、短彩信、APP等多种方式，随时随地收发邮件。 无线音乐手机支付号簿管家开放平台 中国移动 - mail.10086.cn - 2019-2-21 - 快照
engine:['baidu', 'bing', 'sogou']
--------------1
title:中国移动官方网站
url_pre:https://mijisou.com/url_proxy?proxyurl=http://www.baidu.com/link?url=lri8lSzjAaI2H3N5BZqw39r-WN4FNGMBXiT5NpGduJe&amp;token=6fc70c69fef4197e90be70009ed201d241504876895295ea7db371ba76667c44
url_nuder:http://www.10086.cn/
content:[图文]中国移动官方网站为您提供业务介绍，手机话费充值查询，套餐资费介绍及网上查询办理，号码购买，优惠购机，积分查询，优惠活动等网上自助服务。 中国移动 - www.10086.cn/i... - 2017-6-29 - 快照
engine:['baidu', 'sogou']
--------------2
title:首页_中国移动积分商城
url_pre:https://mijisou.com/url_proxy?proxyurl=http://www.baidu.com/link?url=iZHEiEFEybaiTAJf15JyKhAGKWJG7yilS0GtUMkV4fq&amp;token=c759f8ba745043f259be16e2e4c54da7e81b1b3349dc77a8ab2f69750f3c6c47
url_nuder:http://jf.10086.cn/
content:全部礼品分类 首页 我能兑换 排行榜 现金+ 商城优选 积分互兑 品牌专区 乐享生活 基础通信 &gt; 基础通信 话费直充 流量包 流量加油包 短信包 彩信包 ...
engine:['baidu', 'bing']
--------------3
title:中国移动官方网站
url_pre:https://mijisou.com/url_proxy?proxyurl=http://www.baidu.com/link?url=0x57-bHKRHUWHLhjK1ZWtDuJGLLQbEg8DvJhT2J3_HW&amp;token=cd0add0cc1fafd3503db487245b1a384bed502cb5c032bad05913ceb5f3c7307
url_nuder:http://gd.10086.cn/
content:2019-2-19 · 中国移动官方网站为您提供业务介绍，手机话费充值查询，套餐资费介绍及网上查询办理，号码购买，优惠购机，积分查询，优惠活动等网上自助服务。
engine:['baidu', 'bing']
--------------4
title:网上营业厅-网上营业厅-河南移动
url_pre:http://service.ha.10086.cn/
url_nuder:http://service.ha.10086.cn/
content:移动业务办理是对中国移动的产品进行在线申请、定制、变更等操作。为您提供部分移动增值业务和附加业务的申请和取消服务。话费服务是指中国移动向客户提供移动话费查询、...
engine:['bing', 'sogou']
...
```

U can also use tools like ag to grep informations:

python base.py -q site:qq.com -p 1 | ag "url|title"

it will returns

```
title:登录QQ邮箱
url_pre:https://mail.qq.com/
url_nuder:http://mail.qq.com
title:微信网页版
url_pre:https://mijisou.com/url_proxy?proxyurl=http://www.baidu.com/link?url=j7isd-iVAjAvD_LHw-Tp57F-2LVcuVw9PUgeQiTdIxO&amp;token=2fe6e19b5b8f7e23dc01edc7c38feb495c565d2db0f7d2f32b4db4a8bb1f089e
url_nuder:https://wx.qq.com/
title:地下城与勇士-DNF-官方网站-腾讯游戏-格斗网游王者之作,300...
url_pre:https://mijisou.com/url_proxy?proxyurl=http%3A//www.so.com/link%3Fm%3DaCQ%252FxGdmEiTvSre8CFZ2tdCLIQphNt6seNnTxgt2N6FBcEhLe5OjTMuvdoWz2ywTQthME531l2k8Di6ObGE7X7w%253D%253D&amp;token=6ab05d92a6ee0d5298eb1ff846ced8e2e706cac12fc98a67a4596ae4cb10abfa
url_nuder:http://dnf.qq.com
...
```

