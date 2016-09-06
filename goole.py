http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=199701&ctid=320
[size=14.6667px]昨天收到拒信，来贴面筋~
1.白人小哥，判断一个matrix是不是这种形式:
从左上到右下的斜线上数字相同，并且matrix要是正方形，比如
1，5，3，4
0，1，5，3
9，0，1，5
2，9，0，1
Follow up: 假如matrix太大了，不能全部存在内存里，一次只能读一部分怎么办
. visit 1point3acres.com for more.
2.白人大哥，有这样的一个List，list里面有好几个item：比如[(1,2,3), (1,2), (2,4), (2)]里面有4个item,每个item有一些数字（无duplicate）
把他partition，并且，分成的份数最少，规则是，他们必须要有相同的元素才能在一份中，比如这个例子可以分成：
[[(1,2,3), (1,2,),(2)], [(2,4)]] 或者[[(1,2,3), (1,2,)], [(2)，(2,4)]] 都是分成了两份。

3. 白人大叔，给你一个新的字母顺序规则，比如ole 表示o后面才可以出现l, l后面才可以出现 e.
给你一个string，满足这个字母顺序的的话返回true 否则返回false，不在这个规则顺序中的字母可以忽略. 就是说除了ole其他字母都不用管。

比如如下的string：
Google 返回 true
Elle 返回false（因为l有出现在e的后面）

Follow up 假设现在 这个string特别大，每台机器有一部分这个string，怎么处理

4.国人小哥
题目一：
给你一个 String和一个数字max,比如：
“happy new year new year”           max =2
Max表示最长的可以有几个单词（要是在string中连续的单词）。返回所有的可能单词和次数
这个例子返回：

happy 1
new 2
year 2
happy new 1
new year 2
year new 1


题目2:
两个string，第二个比第一个多一个字母，找出这个字母。
比如 string1： abcd   string2 abecd   得出e
题目不知道解释的清不清楚，如果大家有疑问在楼下问我~ 另外求问各位大神，因为感觉和面试官交流还可以，
题目都有给出比较不错的解，hr在拿到面试官的reviews后说looks positive。但是hc没有过。hr也没有说原因。
可能是哪些方面还需加强呢？谢谢大家啦~~~



补充内容 (2016-8-19 04:16):
我的思路在第三楼~ 欢迎讨论~
补充内容 (2016-8-19 05:08):
第二题没解释清楚，A和B要是包含关系，才可以在一份里。比如（1，2，4）和（1，2）在一份里。（1，2，4）和（1，5）不在一份里。



第一题：
判断第一行和第一列的数字，坐标为（i,j），然后每次判断（i+1, j+1）的数字（不越界的话）是不是和（i， j）一样。
follow up 我用了一个HashMap, key是坐标pair, value是值。按行读取，每次读到一个（i, j）判断（i-1, j-1）在不在hashmap中。需要override pair class 的 equal 和 hash 函数，来不及写override只写了主要部分，但是跟面试官说了。

第二题：
函数要这么写： public  List<List<Set<>>> getAnswer(List<Set<>> input)。 （面试官提示我的= =） 鏉ユ簮涓€浜�.涓夊垎鍦拌鍧�. 
开始时把input 按照Set的size排序，size大的在前面。然后一遍for循环。尝试把每个item加入output中（output也要走一遍循环），如果output走到结束也没加入到output，说明这个item要自立门户，加入output中。

第三题：
以帖子里面例子为例，先把ole建立一个hashmap, value是他们的index，key-value则是： o-0, l-1, e-2
for循环一遍这个string，每次遇到一个在hashmap里面的字母，check一下这个index是不是比之前遇到的那个index小。

followup：有N台机器，每台有1/N的片断（substring）。 同时开始计算，首先每台机器内部这个substring要是合法的。 每台机器有一个start_index, end_index，
记录的是本机器中这个substring，在hashmap中的， 第一个字母，最后一个字母的index。 吧所有的start_index. end_index放在一起，看是不是in order。 
这里要注意 start_index end_index 初始值， 我设置成了（-1， -1）。 因为 如果你设置成（0，0）该substring不含有ole、比如这个substring是xyz，会出问题。
（这个地方面试官提示我的）


第四题
第一小题：
这题我就是暴力解答的。每遇到一个新的词放入hashmap. 写完了讨论下复杂度，面试官就问了下能不能优化，也没让我想，也没提示，就说那下一题。
第二小题：
先问了下是不是这两个string 除了多出来的一位， 其他字母顺序是不是一样的。 如果一样的话，因为有一个string多一位，那一旦遇到字母不同，返回长一点那个string的当前字母就可以了。
如果不是顺序的，就把短一点的放入hashmap. value是该字幕出现的个数。 然后for循环一遍长一点string。每次把这个字母value-1。 遇到不在hashmap或者 value <0 说明就是要找的那个string。. 涓€浜�-涓夊垎-鍦帮紝鐙鍙戝竷
