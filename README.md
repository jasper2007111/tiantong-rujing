# 天童如净

天童如净禅师，日本曹洞宗开山祖师道元的师父，南宋时期人，和北方万松行秀并称曹洞宗二大宗匠。国内曹洞宗主要传自万松行秀一派，而天童如净多不为国人所知，语录序中这句，正是我的初衷吧。

>  使灯灯相续师之名愈久而愈隆

## 语录
最早是因为去宁波天童禅寺，得到了一本线装的繁体版本。或许是古文而且是繁体的缘故，有阅读障碍。后来在孔夫子上淘到了一本小开本的带拼音的，但是这个版本存在缺少页面的问题，而且很多异体字没有的，于是就有了自己编辑一个版本的初衷。

主要参照了台大佛学图书馆的[《 如净和尚语录》CBETA 电子版](http://buddhism.lib.ntu.edu.tw/BDLM/sutra/chi_pdf/sutra19/T48n2002A.pdf)，另外也参考了天童寺出版的《天童如净禅师语录》。

### 如净和尚语录
![](./如净和尚语录.png)

对应下载`如净和尚语录.pdf`，这个版本主要使用Python脚本（generate.py）根据`book.txt`自动生成带拼音的`book.html`。可以通过浏览器打开`book.html`生成PDF版本，目前PDF是使用苹果的Safrai生成的，对比Chrome生成的版本，个人更喜欢这个。

这个版本后续会一直维护，虽然目前利用分词技术解决了大量多音字的拼音问题，但少部分的拼音仍旧存在问题。遇到错误时一方面可以提交Issues。另一方面也可以修改`book.txt`, 提交给我。比如这个句子中：`今古寥寥白晝<ruby py="cháng">長</ruby>`的`長`在自动生成时会生成`zhǎng`，实际应该是`cháng `。可以使用`ruby`标签包裹，`py`是对应的拼音。生成时，将会使用标签的拼音。另外某些汉字没有拼音，这时可以将`py`设置为`-`，生成时不会显示拼音。

脚本使用了以下开源项目：

- [OpenCC](https://github.com/BYVoid/OpenCC)，处理简繁体的转换。
- [jieba](https://github.com/fxsjy/jieba)，主要处理分词。
- [python-pinyin](https://github.com/mozillazg/python-pinyin)，生成拼音，目前存在如果时繁体词组时，无法生成正确的拼音，所以使用了OpenCC来处理繁体转简体的问题。
- [jinja2](https://docs.jinkan.org/docs/jinja2/index.html)，模版。

目前发现参考版本都没有处理某些明显的断句错误，整理的时候有意把发现的断句错误给修正了。修正时主要从其他禅师语录以及一些已经整理好的资料作为参考，避免个人的主观认知错误。

为了便于随时手机阅读，目前生成的PDF尺寸为A6（105mmx148mm），其他的尺寸可以通过对应的`.html`文件自行生成。

### 天童如净禅师语录

这个是稍早前使用排版软件手动生成的版本，虽然经过很多次的修正，问题已不大，考虑到脚本生成的便利和准确性，此版本后续将不再维护。

***这个版本基本上保持了传统版本的原貌，可以作为原本对照参考。***

### 道元《宝庆记》研究
《宝庆记》是道元禅师与如净禅师的一些对话集，可以从另一个角度来了解如净禅师。这个浙大华雪梅的研究论文，附录部分有《宝庆记》完整文字。网上找了一个带日文的电子版，核对了下内容基本一致，所以值得参考。

## 其他

### 塔铭
塔铭是了解一位禅师生平重要的资料。

- 天童大休，天童大休禅师是雪窦足庵禅师的师父。
- 雪窦足庵，雪窦足庵禅师是如净禅师的师父。
- 天池雪屋韶，天池雪屋禅师是目前国内的资料中明确师从如净禅师的一位。
- 天宁禅寺虚照禅师，这个金元时期的一位曹洞宗禅师，元朝的开国功臣刘秉忠的师父，刘秉忠曾今是一名僧侣，后期还俗。

#### 攻媿集
天童大休、雪窦足庵塔铭均出自《攻媿集》，因为目前的资料都没有断句，所以一块顺带的也对其他几篇塔铭做了断句校对，不过并未完全，后续会适当的修正。比较巧合的是里面有如净禅师曾经主持后的明州瑞岩、台州瑞岩，也刚好作为了解。

### 禅师语录
这里面收集了一些禅师语录，主要是为了方便手机和平板阅读。
- 汾阳善昭，汾阳善昭禅师是临济宗第六代祖师，他开启了禅师对公案的解读，同时也是一代宗师，他的弟子石霖楚圆门下诞生了临济宗的黄龙派和杨歧派，继而形成了后世所熟悉的五家七宗的局面。汾阳善昭舍利塔目前依旧存在，在汾阳市区海虹塔寺内。汾阳善昭也是除了临济禅师、赵州禅师外在北方声名远扬的一位禅师。
- 临济义玄，临济宗的开宗祖师，他的语录也称《临济录》，临济禅师在石家庄市正定县弘法临济院弘法，这也是临济宗名称的来源。目前禅师的塔依旧在临济寺内，临济寺位于正定古城靠近南门，交通方便，值得去打卡参拜。
- 赵州从谂，也就是大名鼎鼎的赵州禅师，赵州禅师也是在北方弘法，在石家庄市赵县，禅师的舍利塔目前在柏林禅寺内，在赵县还有赵州桥这样为大家耳熟能详的景点。
- 松源崇岳，如净禅师参学过的一位著名禅师，属于临济宗杨歧派。