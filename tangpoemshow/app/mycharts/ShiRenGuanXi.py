# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name :ShiRenGuanXi
   Description :
   Author :Liangs
   date：2017/12/4
-------------------------------------------------
"""
__author__ = 'Liangs'

from pyecharts import Graph, Page, Style


def create_charts(data):
    page = Page()
    style = Style(width=900, height=900)
    html = ''

    html_before = data['full'][0]
    html_after = data['full'][1]
    nodes_full = data['full'][2]
    links_full = data['full'][3]
    category=data['full'][4]
    chart = Graph("全唐诗人关系图", **style.init_style)
    chart.add("", nodes_full, links_full,category, line_color='#aaa', label_pos="center",
              is_label_show=True, graph_repulsion=1000, is_legend_show=True,
              line_curve=0.4, label_text_color="#000", graph_layout='circular',
              label_emphasis_textcolor='#000')
    java_script = chart.render_embed()
    html += html_before + java_script + html_after
    page.add(chart)

    # style = Style(width=900, height=600)

    html_before = data['early'][0]
    html_after = data['early'][1]
    nodes_early = data['early'][2]
    links_early = data['early'][3]

    chart = Graph("初唐诗人关系图", **style.init_style)
    chart.add("", nodes_early, links_early, line_color='#aaa', label_pos="center", is_label_show=True,
              graph_repulsion=1000, is_legend_show=False, line_curve=0.2, label_text_color=None)
    java_script = chart.render_embed()
    html += html_before + java_script + html_after
    page.add(chart)

    html_before = data['middle'][0]
    html_after = data['middle'][1]
    nodes_middle = data['middle'][2]
    links_middle = data['middle'][3]
    chart = Graph("中唐诗人关系图", **style.init_style)
    chart.add("", nodes_middle, links_middle, line_color='#aaa', label_pos="center", is_label_show=True,
              graph_repulsion=1000, is_legend_show=False, line_curve=0.2, label_text_color=None)
    java_script = chart.render_embed()
    html += html_before + java_script + html_after
    page.add(chart)

    html_before = data['high'][0]
    html_after = data['high'][1]
    nodes_high = data['high'][2]
    links_high = data['high'][3]
    chart = Graph("盛唐诗人关系图", **style.init_style)
    chart.add("", nodes_high, links_high, line_color='#aaa', label_pos="center", is_label_show=True,
              graph_repulsion=1000, is_legend_show=False, line_curve=0.2, label_text_color=None)
    java_script = chart.render_embed()
    html += html_before + java_script + html_after
    page.add(chart)

    html_before = data['late'][0]
    html_after = data['late'][1]
    nodes_late = data['late'][2]
    links_late = data['late'][3]
    chart = Graph("晚唐诗人关系图", **style.init_style)
    chart.add("", nodes_late, links_late, line_color='#aaa', label_pos="center", is_label_show=True,
              graph_repulsion=1000, is_legend_show=False, line_curve=0.2, label_text_color=None)
    java_script = chart.render_embed()
    html += html_before + java_script + html_after
    page.add(chart)




    # 最后
    script = page.get_js_dependencies()
    return html, script