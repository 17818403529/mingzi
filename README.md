## mingzi
这是一个用来生成随机中文姓名的包。

This is a library for developers to use to generate random Chinese names.

本包全部使用python标准模块，不依赖于标准Python发行版之外的模块或包。

This package uses all standard python modules and does not rely on modules or packages outside the standard Python distribution.


## Project Origin

几个月以前，作者在对一个中学的数据库进行测试时，需要用到大量的随机中文姓名，发现似乎缺少能很好地满足这一需求的包，因而开始了这个项目。

A few months ago, the author was testing a high school database with a large number of random Chinese names, and found that there seemed to be a lack of packages that could meet this need well, so started the project.

## Installation

```{python}
pip install mingzi
```


## Quick Start

```{python}
from mingzi import *
mingzi()
>>> ['崔依梅']
mingzi()
>>> ['崔曦']
```


## Batch Production

您可以通过控制```volume```参数来控制输出的随机姓名的数量，从而批量得到多个姓名。

You can get multiple names in batches by controlling the ```volume``` parameter to control the number of random names that are output.

```{python}
mingzi(volume=5)
>>> [['温悠', '女'], ['李嘉茵', '女'], ['孟虚', '男'], ['王俊', '男'], ['周伦', '男']]
```


## Output Gender Information

像世界上大多数其他国家一样，你可以从我们中国人的姓名大致知道其性别。为了满足开发中的实际需要，你可以通过 ```show_gender``` 参数来控制是否输出姓名的性别信息。

Like in most other countries in the world, you can roughly know our Chinese person's gender from their name. In order to meet the practical needs of development, you can use the ```show_gender``` parameter to control whether to output the gender information of the name.

```{python}
mingzi(volume=5, show_gender=True)
>>> [['范若翰', '男'], ['邓铭锵', '男'], ['刘贝韵', '女'], ['施喆', '男'], ['陈楚悦', '女']]
```


## Proportion of Female Names

你可以通过 ```female_rate``` 参数来控制生成女性姓名的概率，进而控制最终姓名列表中女性姓名所占的比例，这一参数默认为0.49，即为中国目前(2024年)人口女性比例。

You can control the probability of generating female names by the ```female_rate``` parameter, and then control the proportion of female names in the final name list. This parameter defaults to 0.49, which is the proportion of women in China's current (2024) population.

```{python}
mingzi(volume=10, female_rate=0.8, show_gender=True)
>>> [['徐育', '女'], ['蔡裳', '女'], ['徐筱', '女'], ['张濯', '男'], ['章松芬', '女'], ['杨熙岩', '男'], ['陈楚菱', '女'], ['阳笛', '女'], ['陈贝韵', '女'], ['杨邦', '男']]
```

显而易见，如果这一参数为0，那么就只输出男性姓名。

Obviously, if this parameter is 0, then only the male name is printed.

```{python}
mingzi(volume=10, female_rate=0, show_gender=True)
>>> [['黄云诺', '男'], ['林祯卓', '男'], ['余东', '男'], ['刘书', '男'], ['陈茂彦', '男'], ['王柒', '男'], ['梁明泉', '男'], ['张秦齐', '男'], ['杨信霖', '男'], ['唐澈', '男']]
```

反过来说，如果这一参数为1，那么就只输出女性姓名。

Conversely, if this parameter is 1, only the female name is printed.

```{python}
mingzi(volume=10, female_rate=1, show_gender=True)
>>> [['梁偌瑾', '女'], ['徐莉菲', '女'], ['胡丹', '女'], ['张楚悦', '女'], ['刘若娜', '女'], ['祝楚', '女'], ['李梓琪', '女'], ['孟嘉茵', '女'], ['刘嘉茵', '女'], ['蔡雯', '女']]
```


## Probability of Different Surnames

中国人的姓名由姓氏和名字组成，中国人的姓氏对应于欧美姓名中的“last name”，不同的姓氏在人口中占有不同的比例。你以笔者的姓氏，“李姓”为例，这个比例大概在百分之七左右，在设计这个包的时候，这一点得到了妥善的考虑：不同的姓氏在输出数据中占有的不同的比例，具体参考于当前的人口统计数据。

Chinese names consist of surnames and first names, Chinese surnames correspond to the "last name" in European and American names, and different surnames occupy different proportions in the population. If you take the author's last name, "李" for example, the percentage is around seven percent, which was properly taken into account when designing the package: different surnames account for different percentages in the output data, specific to the current demographic data.

如果你是国人的话，你能从如下测试数据中很容易地发现，这和我们的日常经验是相符的。

If you are a Chinese, you can easily see from the following test data, which is consistent with our daily experience.

```{python}
mingzi(volume=100)
>>> ['刘灏风', '叶松', '宋恬', '赵秦齐', '何怡芬', '余伟', '唐平', '吴忆狄', '黄书', '于琪纯', '傅娴', '罗菲', '徐宇', '张风', '李雁楚', '童虞', '李虚', '陈稹', '宋语', '陈拾', '刘彰', '潘任', '孙晨纶', '汤元', '江永茂', '张生', '贾昭美', '韦科', '吴哲', '王盛', '徐娅', '朱诗', '胡鑫', '姜翠', '魏谚', '梁泽商', '王嘉茵', '孙拾', '秦艳', '傅娴', '刘菁', '周蒙', '韦曦', '李痴', '吴偌瑾', '谢雄', '李宇军', '胡佳禾', '程丽', '史鸣哲', '陈若翰', '锺宁', '史自昊', '罗书琴', '潘觅', '孙璥', '陈泽商', '舒莉', '薛聪', '张锋玮', '杨熙岩', '王泰骞', '孙娥', '楼函', '魏妮', '向珅南', '高蓝', '吴若娜', '李茂', '马群', '陈君', '王青熙', '易新菱', '叶令', '王舞', '王茂彦', '李纹窈', '陈旭平', '李万信', '孔松樱', '苗松芬', '田希嫣', '张奕', '李林', '蓝慕巧', '李觅蕴', '孔希嫣', '罗州', '马行', '汤宇', '苏晴茹', '陈阳', '杨梓琪', '陈赫', '王霄', '郭霆', '刘雅妙', '刘秦恒', '王纹窈', '马峰']

```

然而，你可以通过```alt_surname```参数来人为控制输出中姓氏的组成，这是个参数是一个默认为空的列表。如果此列表非空，那么输出的姓名的姓氏仅仅从这个列表中给出，而且每个备选项出现的概率均等。

However, you can artificially control the composition of the surname in the output with the ```alt_surname``` parameter, which is a list that defaults to empty. If the list is not empty, then the last name of the output name is given only from this list, and each alternative appears with equal probability.

以下将输出10个姓氏为“李”的姓名。

The following will output 10 names with the last name "李".

```{python}
mingzi(mingzi(volume=10, alt_surname=["李"]))
>>> ['李朋', '李松樱', '李绿', '李林灏', '李纹珊', '李媛倚', '李璇兰', '李薇', '李忆狄', '李鹃']
```

以下将输出100个姓氏为“李”，或者“张”，或者“王”的姓名，其中每个姓氏出现的概率为33%。

The following will output 100 names with the surname "李", "张", or "王", each of which has a 33% probability of occurrence.

```{python}
mingzi(volume=25, alt_surname=["李","张","王"])
>>> ['王清媛', '李茂', '张媛倚', '王荷菲', '李玫', '王馥', '张澈', '张瑾', '王咏', '王好', '李奕宗', '王豆', '李晴茹', '张苑', '王雅惠', '李舒志', '张冰', '李豆', '李楚悦', '张听', '李羽', '张滨义', '张荷菲', '李熙岩', '张林灏']
```


## Complex Surname

少数中国人的姓氏由两个汉字组成，也就是“复姓”，复姓人口在中国占有的比例很少，只有大概千分之一，然而你可以通过调整```com_rate```参数的大小，来调整这一比例，来提高输出数据中复姓姓名的比例，这在某些情形，你比如说为一个武侠游戏生成测试数据和素材，是很有必要的。

A few Chinese surnames are composed of two Chinese characters, namely "compound surname". The proportion of compound surname population in China is very small, only about one thousand. However, you can adjust this proportion by adjusting the size of ```com_rate``` parameter, so as to increase the proportion of compound surname in output data. It is necessary for you to generate test data and material for, say, a martial arts game.

```{python}
mingzi(volume=10, com_rate=0.9)
>>> ['申屠素卿', '单于怡芬', '呼延莎', '刘清滢', '姚玥', '公良雁楚', '吴嘉茵', '夏侯凌', '公羊冰', '巫马昶']

```


## Single Names

绝大多数中国人的名字是单字名或者双字名，此包也仅仅生成这两种类型的名字。你可以通过 ```single_rate``` 来控制输出的姓名中单字名的比例，这个变量的缺省值为0.14，即为目前统计数据显示的中国单字名在全部人口中所占的比例。

The vast majority of Chinese names are single-word or double-word names, and this package generates only those two types of names. You can control the proportion of single names in the output by ```single_rate```. The default value of this variable is 0.14, which is the proportion of Chinese single names in the total population as shown in the current statistics.

```{python}
mingzi(volume=10, single_rate=0.7)
>>> ['魏炫灿', '康文芝', '赵贻', '张南', '杜靖', '罗茵', '杨凯', '周燕', '谷浦宇', '陈君']

```
