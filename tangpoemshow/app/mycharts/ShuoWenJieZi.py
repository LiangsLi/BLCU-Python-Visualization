# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name :ShuoWenJieZi
   Description :说文解字页面，柱状图，折线图，词云图，饼图，水滴图
   Author :Liangs
   date：2017/11/29
-------------------------------------------------
"""
__author__ = 'Liangs'

from pyecharts import Bar, Line, Liquid, WordCloud, Pie, Overlap, Page, Style
from app.mycharts.constants import WIDTH, HEIGHT


def create_charts(data):
    # data字典格式(三个表的情况下)：
    # {'charcloud':[str:表一的前描述,str:表一的后描述,数据1,数据2,...,数据n],'...':[...]}
    html = ''
    page = Page()
    style = Style(width=900, height=600)
    # 本页面包含：1：所有字的词云charcloud(两个数据chars,values)、
    # 表一：
    # 获取表一的数据
    html_before = data['charcloud'][0]
    html_after = data['charcloud'][1]
    chars = data['charcloud'][2]
    values = data['charcloud'][3]
    wordcloud = WordCloud("唐诗用字云图", **style.init_style)
    wordcloud.add("字云", chars, values, word_size_range=[10, 100], shape='pentagon')
    java_script = wordcloud.render_embed()
    html += html_before + java_script + html_after
    page.add(wordcloud)
    # 表二：
    html_before=data['chartop10'][0]
    html_after=data['chartop10'][1]
    chars=data['chartop10'][2]
    values=data['chartop10'][3]
    bar=Bar("唐诗高频十字",**style.init_style)
    bar.add("柱状图",chars,values)
    java_script=bar.render_embed()
    html += html_before + java_script + html_after
    page.add(bar)
    # 表三:
    html_before = data['frequency&times'][0]
    html_after = data['frequency&times'][1]
    keys = data['frequency&times'][2]
    values = data['frequency&times'][3]
    line = Line("唐诗字频-字数", **style.init_style)
    line.add("字频--字数", keys, values, is_smooth=True, is_fill=True, area_opacity=0.2, is_datazoom_show=True,
              datazoom_type="both", datazoom_range=[0, 60], xaxis_interval=1, yaxis_formatter="字", xaxis_name="频次",
              yaxis_name="字数", xaxis_name_pos="end", yaxis_name_pos="end", is_more_utils=True)
    java_script=line.render_embed()
    html += html_before + java_script + html_after
    page.add(line)
    # 最后
    script = page.get_js_dependencies()
    return html, script
