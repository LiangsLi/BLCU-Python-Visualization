# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name :data
   Description :处理获取数据，传递给相关图表，避免多次读取文件
   Author :Liangs
   date：2017/11/28
-------------------------------------------------
"""
__author__ = 'Liangs'


def get_data_shirenguanxi():
    data_dict = {}
    html_before = '''
        <div class="bs-docs-section"> 
    	<h1 id="我是ID1" class="page-header">
    	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: BT2" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
    	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: third parties" data-anchorjs-icon="" style="font-family: anchorjs-icons;
                                            font-style: normal; font-variant-ligatures: normal;
                                            font-variant-caps: normal; font-weight: normal;
                                            line-height: inherit; position: absolute; margin-left: -1em;
                                            padding-right: 0.5em;">
         </a>图标题
        </h1>
        <p class="lead">图简短说明</p>
    	<div class="my-charts">
    	'''

    html_after = '''
        </div>
    	<p class="lead">图详细说明</p>
    	<h2 id="我是ID1.1">
    	<a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
        <a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
                                        font-variant-ligatures: normal; font-variant-caps: normal;
                                        font-weight: normal; line-height: inherit; position: absolute;
                                        margin-left: -1em; padding-right: 0.5em;">

        </a>图描述小标题
    	</h2>
        <p>我是描述 <code> 我是code/术语 </code> 我是描述 <a href="https://css-tricks.com/box-sizing/">我是链接</a>我是描述</p>
        <figure class="highlight">
            <pre><code class="language-scss" data-lang="scss">
                            <span class="nc">我是代码绿色</span>
                            <span class="na">我是代码蓝色</span>
            </code></pre>
        </figure>
        </div>
        '''
    nodes_early = [{'name': "宋之问", 'symbolSize': 50, "draggable": "True"},
                   {'name': "陈子昂", "symbolSize": 50, "draggable": "True"},
                   {'name': "乔知之", "symbolSize": 50, "draggable": "True"},
                   {'name': "李世民", "symbolSize": 50, "draggable": "True"},
                   {'name': "李峤", "symbolSize": 50, "draggable": "True"},
                   {'name': "王勃", "symbolSize": 50, "draggable": "True"},
                   {'name': "骆宾王", "symbolSize": 50, "draggable": "True"},
                   {'name': "魏徵", "symbolSize": 50, "draggable": "True"},
                   {'name': "李贤", "symbolSize": 50, "draggable": "True"},
                   {'name': "苏味道", "symbolSize": 50, "draggable": "True"},
                   {'name': "韦承庆", "symbolSize": 50, "draggable": "True"},
                   {'name': "沉佺期", "symbolSize": 50, "draggable": "True"},
                   {'name': "卢照邻", "symbolSize": 50, "draggable": "True"},
                   {'name': "杜审言", "symbolSize": 50, "draggable": "True"}, ]
    links_early = [{'source': '骆宾王', 'target': '李峤'}, {'source': '宋之问', 'target': '陈子昂'},
                   {'source': '杜审言', 'target': '韦承庆'}, {'source': '李世民', 'target': '魏徵'},
                   {'source': '宋之问', 'target': '李世民'}, {'source': '李峤', 'target': '宋之问'},
                   {'source': '骆宾王', 'target': '宋之问'}, {'source': '陈子昂', 'target': '乔知之'},
                   {'source': '骆宾王', 'target': '卢照邻'}, {'source': '李峤', 'target': '杜审言'},
                   {'source': '杜审言', 'target': '苏味道'}, {'source': '沉佺期', 'target': '李贤'},
                   {'source': '骆宾王', 'target': '沉佺期'}, {'source': '王勃', 'target': '骆宾王'},
                   {'source': '沉佺期', 'target': '宋之问'}, {'source': '沉佺期', 'target': '乔知之'},
                   {'source': '沉佺期', 'target': '陈子昂'}, {'source': '乔知之', 'target': '陈子昂'},
                   {'source': '宋之问', 'target': '杜审言'}, {'source': '宋之问', 'target': '沉佺期'},
                   {'source': '李峤', 'target': '骆宾王'}]
    data_dict['early'] = [html_before, html_after, nodes_early, links_early]

    nodes_middle = [{'name': '姚合', "symbolSize": 50, "draggable": "True"},
                    {'name': '孟郊', "symbolSize": 50, "draggable": "True"},
                    {'name': '白居易', "symbolSize": 50, "draggable": "True"},
                    {'name': '王建', "symbolSize": 50, "draggable": "True"},
                    {'name': '薛涛', "symbolSize": 50, "draggable": "True"},
                    {'name': '王涯', "symbolSize": 50, "draggable": "True"},
                    {'name': '贾岛', "symbolSize": 50, "draggable": "True"},
                    {'name': '柳宗元', "symbolSize": 50, "draggable": "True"},
                    {'name': '李绅', "symbolSize": 50, "draggable": "True"},
                    {'name': '吕温', "symbolSize": 50, "draggable": "True"},
                    {'name': '杨巨源', "symbolSize": 50, "draggable": "True"},
                    {'name': '权德舆', "symbolSize": 50, "draggable": "True"},
                    {'name': '郎士元', "symbolSize": 50, "draggable": "True"},
                    {'name': '韩愈', "symbolSize": 50, "draggable": "True"},
                    {'name': '元稹', "symbolSize": 50, "draggable": "True"},
                    {'name': '郑锡', "symbolSize": 50, "draggable": "True"},
                    {'name': '李端', "symbolSize": 50, "draggable": "True"},
                    {'name': '卢纶', "symbolSize": 50, "draggable": "True"},
                    {'name': '刘禹锡', "symbolSize": 50, "draggable": "True"},
                    {'name': '张籍', "symbolSize": 50, "draggable": "True"},
                    {'name': '李益', "symbolSize": 50, "draggable": "True"},
                    {'name': '张继', "symbolSize": 50, "draggable": "True"}]
    links_middle = [{'source': '孟郊', 'target': '李益'}, {'source': '柳宗元', 'target': '刘禹锡'},
                    {'source': '白居易', 'target': '刘禹锡'}, {'source': '姚合', 'target': '贾岛'},
                    {'source': '白居易', 'target': '李绅'}, {'source': '贾岛', 'target': '李益'},
                    {'source': '元稹', 'target': '杨巨源'}, {'source': '王建', 'target': '李益'},
                    {'source': '元稹', 'target': '薛涛'}, {'source': '李益', 'target': '卢纶'},
                    {'source': '张籍', 'target': '贾岛'}, {'source': '张籍', 'target': '白居易'},
                    {'source': '白居易', 'target': '韩愈'}, {'source': '白居易', 'target': '杨巨源'},
                    {'source': '韩愈', 'target': '贾岛'}, {'source': '孟郊', 'target': '韩愈'},
                    {'source': '韩愈', 'target': '柳宗元'}, {'source': '贾岛', 'target': '韩愈'},
                    {'source': '姚合', 'target': '张籍'}, {'source': '卢纶', 'target': '李端'},
                    {'source': '刘禹锡', 'target': '白居易'}, {'source': '姚合', 'target': '刘禹锡'},
                    {'source': '姚合', 'target': '王建'}, {'source': '王建', 'target': '张籍'},
                    {'source': '王建', 'target': '杨巨源'}, {'source': '张籍', 'target': '韩愈'},
                    {'source': '卢纶', 'target': '郎士元'}, {'source': '贾岛', 'target': '张籍'},
                    {'source': '张籍', 'target': '孟郊'}, {'source': '刘禹锡', 'target': '元稹'},
                    {'source': '刘禹锡', 'target': '张籍'}, {'source': '贾岛', 'target': '孟郊'},
                    {'source': '刘禹锡', 'target': '李绅'}, {'source': '李端', 'target': '郎士元'},
                    {'source': '韩愈', 'target': '李绅'}, {'source': '刘禹锡', 'target': '柳宗元'},
                    {'source': '权德舆', 'target': '张籍'}, {'source': '张继', 'target': '郎士元'},
                    {'source': '贾岛', 'target': '王建'}, {'source': '刘禹锡', 'target': '吕温'},
                    {'source': '李端', 'target': '郑锡'}, {'source': '元稹', 'target': '白居易'},
                    {'source': '元稹', 'target': '王建'}, {'source': '李端', 'target': '卢纶'},
                    {'source': '郎士元', 'target': '张继'}, {'source': '韩愈', 'target': '刘禹锡'},
                    {'source': '张籍', 'target': '王建'}, {'source': '张籍', 'target': '姚合'},
                    {'source': '孟郊', 'target': '张籍'}, {'source': '韩愈', 'target': '张籍'},
                    {'source': '白居易', 'target': '元稹'}, {'source': '李绅', 'target': '白居易'},
                    {'source': '韩愈', 'target': '王涯'}, {'source': '韩愈', 'target': '孟郊'},
                    {'source': '贾岛', 'target': '姚合'}, {'source': '孟郊', 'target': '王涯'},
                    {'source': '元稹', 'target': '刘禹锡'}, {'source': '卢纶', 'target': '李益'},
                    {'source': '白居易', 'target': '张籍'}]
    data_dict['middle'] = [html_before, html_after, nodes_middle, links_middle]

    nodes_high = [{'name': '钱起', 'symbolSize': 20, "draggable": "True"},
                  {'name': '崔国辅', 'symbolSize': 20, "draggable": "True"},
                  {'name': '张旭', 'symbolSize': 20, "draggable": "True"},
                  {'name': '贺知章', 'symbolSize': 20, "draggable": "True"},
                  {'name': '苏頲', 'symbolSize': 20, "draggable": "True"},
                  {'name': '韩翃', 'symbolSize': 20, "draggable": "True"},
                  {'name': '皇甫冉', 'symbolSize': 20, "draggable": "True"},
                  {'name': '李嘉右', 'symbolSize': 20, "draggable": "True"},
                  {'name': '岑参', 'symbolSize': 20, "draggable": "True"},
                  {'name': '严武', 'symbolSize': 20, "draggable": "True"},
                  {'name': '薛稷', 'symbolSize': 20, "draggable": "True"},
                  {'name': '刘方平', 'symbolSize': 20, "draggable": "True"},
                  {'name': '刘长卿', 'symbolSize': 20, "draggable": "True"},
                  {'name': '储光羲', 'symbolSize': 20, "draggable": "True"},
                  {'name': '张说', 'symbolSize': 20, "draggable": "True"},
                  {'name': '杜甫', 'symbolSize': 20, "draggable": "True"},
                  {'name': '高适', 'symbolSize': 20, "draggable": "True"},
                  {'name': '张谓', 'symbolSize': 20, "draggable": "True"},
                  {'name': '孟浩然', 'symbolSize': 20, "draggable": "True"},
                  {'name': '王昌龄', 'symbolSize': 20, "draggable": "True"},
                  {'name': '李隆基', 'symbolSize': 20, "draggable": "True"},
                  {'name': '李白', 'symbolSize': 20, "draggable": "True"},
                  {'name': '王维', 'symbolSize': 20, "draggable": "True"},
                  {'name': '张继', 'symbolSize': 20, "draggable": "True"}]
    links_high = [{'source': '李白', 'target': '王昌龄'}, {'source': '李白', 'target': '孟浩然'},
                  {'source': '皇甫冉', 'target': '刘方平'}, {'source': '储光羲', 'target': '王维'},
                  {'source': '杜甫', 'target': '岑参'}, {'source': '岑参', 'target': '王昌龄'},
                  {'source': '李白', 'target': '贺知章'}, {'source': '苏頲', 'target': '张说'},
                  {'source': '孟浩然', 'target': '崔国辅'}, {'source': '钱起', 'target': '王维'},
                  {'source': '李隆基', 'target': '张说'}, {'source': '张谓', 'target': '刘长卿'},
                  {'source': '张继', 'target': '皇甫冉'}, {'source': '高适', 'target': '杜甫'}, {'source': '李白', 'target': '杜甫'},
                  {'source': '苏頲', 'target': '李白'}, {'source': '王维', 'target': '王昌龄'},
                  {'source': '李嘉右', 'target': '皇甫冉'}, {'source': '杜甫', 'target': '李隆基'},
                  {'source': '严武', 'target': '杜甫'}, {'source': '韩翃', 'target': '张继'}, {'source': '杜甫', 'target': '李白'},
                  {'source': '贺知章', 'target': '张说'}, {'source': '刘长卿', 'target': '皇甫冉'},
                  {'source': '王昌龄', 'target': '王维'}, {'source': '皇甫冉', 'target': '张继'},
                  {'source': '孟浩然', 'target': '王昌龄'}, {'source': '高适', 'target': '王昌龄'},
                  {'source': '张继', 'target': '韩翃'}, {'source': '杜甫', 'target': '严武'}, {'source': '王维', 'target': '钱起'},
                  {'source': '杜甫', 'target': '孟浩然'}, {'source': '杜甫', 'target': '张旭'}, {'source': '钱起', 'target': '杜甫'},
                  {'source': '刘长卿', 'target': '李嘉右'}, {'source': '杜甫', 'target': '高适'},
                  {'source': '王昌龄', 'target': '高适'}, {'source': '李白', 'target': '张旭'}, {'source': '杜甫', 'target': '薛稷'},
                  {'source': '皇甫冉', 'target': '刘长卿'}, {'source': '王维', 'target': '孟浩然'},
                  {'source': '李嘉右', 'target': '刘长卿'}, {'source': '岑参', 'target': '李嘉右'},
                  {'source': '刘长卿', 'target': '张谓'}]
    data_dict['high'] = [html_before, html_after, nodes_high, links_high]

    nodes_late = [{'name': '杜荀鹤', 'symbolSize': 20, "draggable": "True"},
                  {'name': '陆龟蒙', 'symbolSize': 20, "draggable": "True"},
                  {'name': '崔珏', 'symbolSize': 20, "draggable": "True"},
                  {'name': '许浑', 'symbolSize': 20, "draggable": "True"},
                  {'name': '李商隐', 'symbolSize': 20, "draggable": "True"},
                  {'name': '罗隐', 'symbolSize': 20, "draggable": "True"},
                  {'name': '杜牧', 'symbolSize': 20, "draggable": "True"},
                  {'name': '张乔', 'symbolSize': 20, "draggable": "True"},
                  {'name': '吴融', 'symbolSize': 20, "draggable": "True"},
                  {'name': '黄滔', 'symbolSize': 20, "draggable": "True"},
                  {'name': '韩屋', 'symbolSize': 20, "draggable": "True"},
                  {'name': '陈陶', 'symbolSize': 20, "draggable": "True"},
                  {'name': '令狐楚', 'symbolSize': 20, "draggable": "True"},
                  {'name': '韦庄', 'symbolSize': 20, "draggable": "True"},
                  {'name': '皮日休', 'symbolSize': 20, "draggable": "True"},
                  {'name': '司空图', 'symbolSize': 20, "draggable": "True"},
                  {'name': '崔道融', 'symbolSize': 20, "draggable": "True"},
                  {'name': '刘驾', 'symbolSize': 20, "draggable": "True"},
                  {'name': '贯休', 'symbolSize': 20, "draggable": "True"},
                  {'name': '赵嘏', 'symbolSize': 20, "draggable": "True"}]
    links_late = [{'source': '刘驾', 'target': '张乔'}, {'source': '杜牧', 'target': '赵嘏', },
                  {'source': '罗隐', 'target': '陆龟蒙'}, {'source': '李商隐', 'target': '崔珏'},
                  {'source': '贯休', 'target': '韩屋'}, {'source': '罗隐', 'target': '韦庄'}, {'source': '杜牧', 'target': '李商隐'},
                  {'source': '韩屋', 'target': '许浑'}, {'source': '陆龟蒙', 'target': '吴融'}, {'source': '黄滔', 'target': '贯休'},
                  {'source': '张乔', 'target': '陈陶'}, {'source': '韦庄', 'target': '许浑'}, {'source': '贯休', 'target': '吴融'},
                  {'source': '许浑', 'target': '赵嘏'}, {'source': '李商隐', 'target': '杜牧'}, {'source': '贯休', 'target': '罗隐'},
                  {'source': '杜牧', 'target': '许浑'}, {'source': '赵嘏', 'target': '杜牧'}, {'source': '赵嘏', 'target': '许浑'},
                  {'source': '贯休', 'target': '皮日休'}, {'source': '韦庄', 'target': '贯休'},
                  {'source': '李商隐', 'target': '令狐楚'}, {'source': '皮日休', 'target': '陆龟蒙'},
                  {'source': '韦庄', 'target': '杜荀鹤'}, {'source': '罗隐', 'target': '贯休'}, {'source': '吴融', 'target': '韩屋'},
                  {'source': '陆龟蒙', 'target': '李商隐'}, {'source': '吴融', 'target': '贯休'},
                  {'source': '陆龟蒙', 'target': '皮日休'}, {'source': '杜荀鹤', 'target': '张乔'},
                  {'source': '许浑', 'target': '杜牧'}, {'source': '崔珏', 'target': '李商隐'},
                  {'source': '杜荀鹤', 'target': '罗隐'}, {'source': '司空图', 'target': '崔道融'},
                  {'source': '李商隐', 'target': '皮日休'}, {'source': '杜荀鹤', 'target': '陈陶'},
                  {'source': '贯休', 'target': '陈陶'}, {'source': '韩屋', 'target': '吴融'}]
    data_dict['late'] = [html_before, html_after, nodes_late, links_late]

    nodes = [{'name': '姚合'}, {'name': '杨玉环'}, {'name': '陆羽'}, {'name': '钱起'}, {'name': '裴度'}, {'name': '李观'},
             {'name': '孟郊'}, {'name': '李建'}, {'name': '李夷简'}, {'name': '许棠'}, {'name': '李泌'}, {'name': '白居易'},
             {'name': '韦渠牟'}, {'name': '灵澈'}, {'name': '王建'}, {'name': '秦系'}, {'name': '鱼玄机'}, {'name': '许浑'},
             {'name': '王质'}, {'name': '皇甫冉'}, {'name': '王播'}, {'name': '贾岛'}, {'name': '李谅'}, {'name': '柳宗元'},
             {'name': '宋之问'}, {'name': '郑谷'}, {'name': '崔备'}, {'name': '牛僧孺'}, {'name': '李绅'}, {'name': '马总'},
             {'name': '杨虞卿'}, {'name': '杨巨源'}, {'name': '郑虔'}, {'name': '李邕'}, {'name': '裴迪'}, {'name': '杨汝士'},
             {'name': '郎士元'}, {'name': '王乔'}, {'name': '岑参'}, {'name': '韩愈'}, {'name': '李逢吉'}, {'name': '元稹'},
             {'name': '王仲舒'}, {'name': '吉中孚'}, {'name': '刘方平'}, {'name': '刘长卿'}, {'name': '李端'}, {'name': '窦巩'},
             {'name': '李世民'}, {'name': '王勃'}, {'name': '杜甫'}, {'name': '储光羲'}, {'name': '崔玄亮'}, {'name': '皮日休'},
             {'name': '刘禹锡'}, {'name': '李渤'}, {'name': '张籍'}, {'name': '沉佺期'}, {'name': '高适'}, {'name': '张署'},
             {'name': '卢纶'}, {'name': '郑澣'}, {'name': '崔邠'}, {'name': '李澣'}, {'name': '张贲'}, {'name': '孟浩然'},
             {'name': '王起'}, {'name': '郑姻'}, {'name': '杨嗣复'}, {'name': '陆龟蒙'}, {'name': '杜牧'}, {'name': '李隆基'},
             {'name': '李白'}, {'name': '皎然'}, {'name': '张乔'}, {'name': '严维'}, {'name': '张祜'}, {'name': '李虞仲'},
             {'name': '韦丹'}, {'name': '王维'}, ]
    links_full = [{'source': '陆龟蒙', 'target': '皮日休'}, {'source': '白居易', 'target': '元稹'},
                  {'source': '刘禹锡', 'target': '白居易'}, {'source': '皮日休', 'target': '陆龟蒙'},
                  {'source': '白居易', 'target': '刘禹锡'}, {'source': '元稹', 'target': '白居易'},
                  {'source': '白居易', 'target': '崔玄亮'}, {'source': '白居易', 'target': '李逢吉'},
                  {'source': '皇甫冉', 'target': '刘长卿'}, {'source': '白居易', 'target': '牛僧孺'},
                  {'source': '白居易', 'target': '李渤'}, {'source': '白居易', 'target': '李绅'},
                  {'source': '白居易', 'target': '李建'}, {'source': '白居易', 'target': '杨汝士'},
                  {'source': '韩愈', 'target': '张籍'}, {'source': '刘禹锡', 'target': '裴度'},
                  {'source': '白居易', 'target': '裴度'}, {'source': '白居易', 'target': '张籍'},
                  {'source': '宋之问', 'target': '沉佺期'}, {'source': '姚合', 'target': '贾岛'},
                  {'source': '杜甫', 'target': '李白'}, {'source': '白居易', 'target': '李夷简'},
                  {'source': '韩愈', 'target': '孟郊'}, {'source': '李端', 'target': '郑姻'}, {'source': '刘禹锡', 'target': '元稹'},
                  {'source': '李端', 'target': '韦丹'}, {'source': '沉佺期', 'target': '宋之问'},
                  {'source': '杜甫', 'target': '郑虔'}, {'source': '元稹', 'target': '李谅'},
                  {'source': '白居易', 'target': '王仲舒'}, {'source': '刘长卿', 'target': '皇甫冉'},
                  {'source': '白居易', 'target': '李谅'}, {'source': '杜甫', 'target': '高适'}, {'source': '孟郊', 'target': '韩愈'},
                  {'source': '王维', 'target': '裴迪'}, {'source': '刘禹锡', 'target': '杨虞卿'},
                  {'source': '张贲', 'target': '皮日休'}, {'source': '皇甫冉', 'target': '刘方平'},
                  {'source': '韩愈', 'target': '张署'}, {'source': '杜牧', 'target': '许浑'}, {'source': '元稹', 'target': '李隆基'},
                  {'source': '皎然', 'target': '李泌'}, {'source': '李端', 'target': '卢纶'}, {'source': '卢纶', 'target': '李端'},
                  {'source': '元稹', 'target': '李渤'}, {'source': '杜甫', 'target': '王仲舒'}, {'source': '杜甫', 'target': '郑澣'},
                  {'source': '姚合', 'target': '李白'}, {'source': '张籍', 'target': '王建'}, {'source': '元稹', 'target': '李建'},
                  {'source': '白居易', 'target': '杨虞卿'}, {'source': '柳宗元', 'target': '刘禹锡'},
                  {'source': '白居易', 'target': '杨嗣复'}, {'source': '杜甫', 'target': '李渤'},
                  {'source': '张祜', 'target': '杨玉环'}, {'source': '皎然', 'target': '陆羽'},
                  {'source': '白居易', 'target': '崔邠'}, {'source': '李白', 'target': '李虞仲'},
                  {'source': '元稹', 'target': '窦巩'}, {'source': '王建', 'target': '张籍'}, {'source': '刘长卿', 'target': '秦系'},
                  {'source': '杜甫', 'target': '李世民'}, {'source': '白居易', 'target': '李澣'},
                  {'source': '郑谷', 'target': '杜甫'}, {'source': '贾岛', 'target': '姚合'}, {'source': '钱起', 'target': '郎士元'},
                  {'source': '杜甫', 'target': '王乔'}, {'source': '严维', 'target': '刘长卿'},
                  {'source': '白居易', 'target': '王质'}, {'source': '元稹', 'target': '杨巨源'},
                  {'source': '李白', 'target': '孟浩然'}, {'source': '皇甫冉', 'target': '郎士元'},
                  {'source': '白居易', 'target': '王起'}, {'source': '皎然', 'target': '韦渠牟'},
                  {'source': '杜甫', 'target': '岑参'}, {'source': '白居易', 'target': '王播'},
                  {'source': '郎士元', 'target': '皇甫冉'}, {'source': '韩愈', 'target': '马总'},
                  {'source': '张籍', 'target': '贾岛'}, {'source': '钱起', 'target': '王维'}, {'source': '孟郊', 'target': '李观'},
                  {'source': '韩愈', 'target': '李逢吉'}, {'source': '李端', 'target': '吉中孚'},
                  {'source': '李白', 'target': '李逢吉'}, {'source': '张乔', 'target': '许棠'},
                  {'source': '元稹', 'target': '李夷简'}, {'source': '白居易', 'target': '李邕'},
                  {'source': '杜牧', 'target': '王仲舒'}, {'source': '杜牧', 'target': '张祜'},
                  {'source': '刘禹锡', 'target': '张籍'}, {'source': '郑谷', 'target': '李白'},
                  {'source': '鱼玄机', 'target': '王勃'}, {'source': '白居易', 'target': '崔备'},
                  {'source': '储光羲', 'target': '张籍'}, {'source': '皎然', 'target': '灵澈'},
                  {'source': '刘长卿', 'target': '严维'}, ]
    nodes_full = []
    for i in nodes:
        size = 5
        nodes_full.append({"name": i.get('name'), "symbolSize": int(size), " category": "1"}, )
        for j in links_full:
            if i.get('name') == j.get('source'):
                # print(i.get('name'))
                size = size + 3
                for k in nodes_full:
                    if k.get('name') == i.get('name'):
                        k['symbolSize'] = size
                        if size >= 5 and size < 8:
                            k['category'] = '0'
                        elif size >= 8 and size < 11:
                            k['category'] = '1'
                        elif size >= 11 and size < 14:
                            k['category'] = '2'
                        elif size >= 14 and size < 17:
                            k['category'] = '3'
                        elif size >= 17 and size < 20:
                            k['category'] = '4'
                        elif size >= 20 and size < 23:
                            k['category'] = '5'
                        elif size >= 23 and size < 32:
                            k['category'] = '8'
                        else:
                            k['category'] = '10'
    category = [{'name': '0'}, {'name': '1'}, {'name': '2'}, {'name': '3'}, {'name': '4'}, {'name': '5'}, {'name': '8'},
                {'name': '10'}, ]
    data_dict['full'] = [html_before, html_after, nodes_full, links_full,category]

    print("get_data_shirenguanxi √")
    return data_dict


def get_data_shuowenjiezi():
    data_dict = {}
    # 添加表一数据：
    html_before = '''
    <div class="bs-docs-section"> 
	<h1 id="我是ID1" class="page-header">
	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: BT2" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: third parties" data-anchorjs-icon="" style="font-family: anchorjs-icons;
                                        font-style: normal; font-variant-ligatures: normal;
                                        font-variant-caps: normal; font-weight: normal;
                                        line-height: inherit; position: absolute; margin-left: -1em;
                                        padding-right: 0.5em;">
     </a>图标题
    </h1>
    <p class="lead">图简短说明</p>
	<div class="my-charts">
	'''

    html_after = '''
    </div>
	<p class="lead">图详细说明</p>
	<h2 id="我是ID1.1">
	<a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
    <a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
                                    font-variant-ligatures: normal; font-variant-caps: normal;
                                    font-weight: normal; line-height: inherit; position: absolute;
                                    margin-left: -1em; padding-right: 0.5em;">

    </a>图描述小标题
	</h2>
    <p>我是描述 <code> 我是code/术语 </code> 我是描述 <a href="https://css-tricks.com/box-sizing/">我是链接</a>我是描述</p>
    <figure class="highlight">
        <pre><code class="language-scss" data-lang="scss">
                        <span class="nc">我是代码绿色</span>
                        <span class="na">我是代码蓝色</span>
        </code></pre>
    </figure>
    </div>
    '''

    words = []
    values = []
    with open(r'app\all_data_files\shuowenjiezi\all-chars.txt', encoding='utf-8') as f:
        for line in f:
            temp = line.split(',')
            words.append(temp[0])
            values.append(temp[1])
    data_dict['charcloud'] = [html_before, html_after, words, values]


    # 表二：
    # html_before='''<p>test</p>'''
    # html_after='''<p>test end</p>'''
    data_dict['chartop10'] = [html_before, html_after, words[:10], values[:10]]
    # 表三：
    datalist = [['频次<=10', 2859], ['10<频次<=80', 1996], ['80<频次<=300', 1234], ['300<频次<=500', 403], ['500<频次<=700', 215],
                ['700<频次<=1000', 215], ['1000<频次<=2000', 309], ['2000<频次<=3000', 118], ['3000<频次<=5000', 95],
                ['5000<频次<=7000', 48], ['7000<频次<10000', 25], ['10000<频次<30000', 19]]
    keys = [item[0] for item in datalist]
    values = [item[1] for item in datalist]
    # html_before = '''<p>test</p>'''
    # html_after = '''<p>test end</p>'''
    data_dict['frequency&times'] = [html_before, html_after, keys, values]

    # 最后
    print("get_data_shuowenjiezi √")
    return data_dict

def get_data_canghaicihua():
    data_dict = {}
    # 添加表一数据：
    html_before = '''
        <div class="bs-docs-section"> 
    	<h1 id="我是ID1" class="page-header">
    	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: BT2" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
    	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: third parties" data-anchorjs-icon="" style="font-family: anchorjs-icons;
                                            font-style: normal; font-variant-ligatures: normal;
                                            font-variant-caps: normal; font-weight: normal;
                                            line-height: inherit; position: absolute; margin-left: -1em;
                                            padding-right: 0.5em;">
         </a>唐诗名词
        </h1>
        <p class="lead">名词高频前三十</p>
    	<div class="my-charts">
    	'''
    html_after = '''
        </div>
    	<p class="lead">图详细说明</p>
    	<h2 id="我是ID1.1">
    	<a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
        <a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
                                        font-variant-ligatures: normal; font-variant-caps: normal;
                                        font-weight: normal; line-height: inherit; position: absolute;
                                        margin-left: -1em; padding-right: 0.5em;">

        </a>图描述小标题
    	</h2>
        <p>我是描述</p>
        </div>
        '''

    nouns = []
    values = []
    with open(r'app\all_data_files\canghaicihua\n.txt', encoding='utf-8') as f:
        for line in f:
            temp = line.split(',')
            nouns.append(temp[0])
            values.append(temp[1])
        nouns = nouns[:30]
        values = values[:30]
    data_dict['nounfre'] = [html_before, html_after, nouns, values]

    # 表二
    html_before = '''
            <div class="bs-docs-section"> 
        	<h1 id="我是ID2" class="page-header">
        	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: BT2" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
        	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: third parties" data-anchorjs-icon="" style="font-family: anchorjs-icons;
                                                font-style: normal; font-variant-ligatures: normal;
                                                font-variant-caps: normal; font-weight: normal;
                                                line-height: inherit; position: absolute; margin-left: -1em;
                                                padding-right: 0.5em;">
             </a>唐诗地理名词
            </h1>
            <p class="lead">地理名词高频前三十</p>
        	<div class="my-charts">
        	'''
    html_after = '''
            </div>
        	<p class="lead">图详细说明</p>
        	<h2 id="我是ID2.1">
        	<a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
            <a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
                                            font-variant-ligatures: normal; font-variant-caps: normal;
                                            font-weight: normal; line-height: inherit; position: absolute;
                                            margin-left: -1em; padding-right: 0.5em;">

            </a>图描述小标题
        	</h2>
            <p>我是描述</p>
            </div>
            '''

    nouns = []
    values = []
    with open(r'app\all_data_files\canghaicihua\ns.txt', encoding='utf-8') as f:
        for line in f:
            temp = line.split(',')
            nouns.append(temp[0])
            values.append(temp[1])
        nouns = nouns[:30]
        values = values[:30]
    data_dict['geofre'] = [html_before, html_after, nouns, values]
    # 表三
    html_before = '''
                <div class="bs-docs-section"> 
            	<h1 id="我是ID3" class="page-header">
            	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: BT2" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
            	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: third parties" data-anchorjs-icon="" style="font-family: anchorjs-icons;
                                                    font-style: normal; font-variant-ligatures: normal;
                                                    font-variant-caps: normal; font-weight: normal;
                                                    line-height: inherit; position: absolute; margin-left: -1em;
                                                    padding-right: 0.5em;">
                 </a>唐诗时间名词
                </h1>
                <p class="lead">时间名词高频前三十</p>
            	<div class="my-charts">
            	'''
    html_after = '''
                </div>
            	<p class="lead">图详细说明</p>
            	<h2 id="我是ID3.1">
            	<a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
                <a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
                                                font-variant-ligatures: normal; font-variant-caps: normal;
                                                font-weight: normal; line-height: inherit; position: absolute;
                                                margin-left: -1em; padding-right: 0.5em;">

                </a>图描述小标题
            	</h2>
                <p>我是描述</p>
                </div>
                '''

    nouns = []
    values = []
    with open(r'app\all_data_files\canghaicihua\nt.txt', encoding='utf-8') as f:
        for line in f:
            temp = line.split(',')
            nouns.append(temp[0])
            values.append(temp[1])
        nouns = nouns[:30]
        values = values[:30]
    data_dict['timefre'] = [html_before, html_after, nouns, values]

    # 表四
    html_before = '''
                    <div class="bs-docs-section"> 
                	<h1 id="我是ID4" class="page-header">
                	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: BT2" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
                	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: third parties" data-anchorjs-icon="" style="font-family: anchorjs-icons;
                                                        font-style: normal; font-variant-ligatures: normal;
                                                        font-variant-caps: normal; font-weight: normal;
                                                        line-height: inherit; position: absolute; margin-left: -1em;
                                                        padding-right: 0.5em;">
                     </a>唐诗动词
                    </h1>
                    <p class="lead">动词高频前三十</p>
                	<div class="my-charts">
                	'''
    html_after = '''
                    </div>
                	<p class="lead">图详细说明</p>
                	<h2 id="我是ID4.1">
                	<a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
                    <a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
                                                    font-variant-ligatures: normal; font-variant-caps: normal;
                                                    font-weight: normal; line-height: inherit; position: absolute;
                                                    margin-left: -1em; padding-right: 0.5em;">

                    </a>图描述小标题
                	</h2>
                    <p>我是描述</p>
                    </div>
                    '''

    nouns = []
    values = []
    with open(r'app\all_data_files\canghaicihua\v.txt', encoding='utf-8') as f:
        for line in f:
            temp = line.split(',')
            nouns.append(temp[0])
            values.append(temp[1])
        nouns = nouns[:30]
        values = values[:30]
    data_dict['verbfre'] = [html_before, html_after, nouns, values]

    # 表五
    html_before = '''
                        <div class="bs-docs-section"> 
                    	<h1 id="我是ID5" class="page-header">
                    	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: BT2" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
                    	<a class="anchorjs-link " href="#我是ID1" aria-label="Anchor link for: third parties" data-anchorjs-icon="" style="font-family: anchorjs-icons;
                                                            font-style: normal; font-variant-ligatures: normal;
                                                            font-variant-caps: normal; font-weight: normal;
                                                            line-height: inherit; position: absolute; margin-left: -1em;
                                                            padding-right: 0.5em;">
                         </a>唐诗形容词
                        </h1>
                        <p class="lead">形容词高频前三十</p>
                    	<div class="my-charts">
                    	'''
    html_after = '''
                        </div>
                    	<p class="lead">图详细说明</p>
                    	<h2 id="我是ID5.1">
                    	<a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; line-height: inherit; position: absolute; margin-left: -1em; padding-right: 0.5em;"></a>
                        <a class="anchorjs-link " href="#我是ID1.1" aria-label="Anchor link for: third box sizing" data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
                                                        font-variant-ligatures: normal; font-variant-caps: normal;
                                                        font-weight: normal; line-height: inherit; position: absolute;
                                                        margin-left: -1em; padding-right: 0.5em;">

                        </a>图描述小标题
                    	</h2>
                        <p>我是描述</p>
                        </div>
                        '''

    nouns = []
    values = []
    with open(r'app\all_data_files\canghaicihua\adj.txt', encoding='utf-8') as f:
        for line in f:
            temp = line.split(',')
            nouns.append(temp[0])
            values.append(temp[1])
        nouns = nouns[:30]
        values = values[:30]
    data_dict['adjfre'] = [html_before, html_after, nouns, values]

    # 最后
    print("get_data_canghaicihua √")
    return data_dict