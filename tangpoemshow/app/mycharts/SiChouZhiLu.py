# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name :SiChouZhiLu
   Description :
   Author :Liangs
   date：2017/12/8
-------------------------------------------------
"""
__author__ = 'Liangs'

from pyecharts import Bar, Line, Liquid, WordCloud, Pie, Overlap, Page, Style,GeoLines
from app.mycharts.constants import WIDTH, HEIGHT



style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=False,
    symbol=['arrow', 'arrow'],
    symbol_size=1,
    line_width=3,
    line_curve=0.2,
    line_opacity=0.6,
    # legend_text_color="#eee",
    legend_pos="center",
    geo_effect_symbol="arrow",
    geo_effect_symbolsize=5,
    label_color=['#B9D3EE', '#C5C1AA', '#DB7093', '#B4EEB4', '#CD8162', '#FFEC8B', '#CD96CD'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#00CDCD",
    item_color='#CD5C5C',
    legend_text_color='#CD5C5C'
)


def create_charts(data):
    style = Style(width=900, height=900)
    page = Page()
    html=''
    charts = GeoLines("丝绸之路", **style.init_style)

    data_eastnorth = [
        ['西安市', '彬县'],
        ['彬县', '泾川县'],
        ['泾川县', '固原市'],
        ['固原市', '靖远县'],
        ['靖远县', '武威市'],
        ['武威市', '张掖市']
    ]
    charts.add("东段北线", data_eastnorth, **style_geo)

    data_eastmid = [
        ['西安市', '彬县'],
        ['彬县', '泾川县'],
        ['泾川县', '平凉市'],
        ['平凉市', '会宁县'],
        ['会宁县', '兰州市'],
        ['兰州市', '武威市'],
        ['武威市', '张掖市']

    ]
    charts.add("东段中线", data_eastmid, **style_geo)

    data_eastsouth = [
        ['西安市', '凤翔县'],
        ['凤翔县', '天水市'],
        ['天水市', '陇西县'],
        ['陇西县', '临夏市'],
        ['临夏市', '乐都县'],
        ['乐都县', '西宁市'],
        ['西宁市', '张掖市']
    ]
    charts.add("东段南线", data_eastsouth, **style_geo)

    data_hexizoulang = [
        ['张掖', '酒泉'],
        ['酒泉', '玉门'],
        ['玉门', '瓜州']
    ]
    charts.add("河西走廊", data_hexizoulang, geo_cities_coords={
        '张掖': [100.45, 38.93],
        '酒泉': [98.500685, 39.740023],
        '玉门': [97.055736, 40.296519],
        '瓜州': [95.793335, 40.530274]
    }, **style_geo)


    data_westnorth = [
        ['瓜州', '哈密'],
        ['哈密', '伊川'],
        ['伊川', '吉木萨尔'],
        ['吉木萨尔', '乌鲁木齐'],
        ['乌鲁木齐', '伊宁'],
        ['伊宁', '碎叶']
    ]
    charts.add("中段北道", data_westnorth, geo_cities_coords={
        '瓜州': [95.793335, 40.530274],
        '哈密': [93.52294, 42.833441],
        '伊川': [91.435282, 43.430981],
        '吉木萨尔': [89.181374, 44.004888],
        '乌鲁木齐': [87.62214, 43.831179],
        '伊宁': [81.283092, 43.916546],
        '碎叶': [75.283092, 43.831179]
    }, **style_geo)

    data_westmid = [
        ['瓜州', '敦煌'],
        ['敦煌', '玉门关'],
        ['玉门关', '高昌'],
        ['高昌', '焉耆'],
        ['焉耆', '库车'],
        ['库车', '阿克苏'],
        ['阿克苏', '喀什'],
        ['喀什', '大宛']
    ]
    charts.add("中段中道",data_westmid, geo_cities_coords={
        '瓜州': [95.793335, 40.530274],
        '敦煌': [94.6806, 40.148308],
        '玉门关': [93.871678, 40.360147],
        '高昌': [89.192459, 42.948971],
        '焉耆': [86.588696, 42.065708],
        '库车': [82.969034, 41.723448],
        '阿克苏': [80.258894, 41.175899],
        '喀什': [75.975982,39.542678],
        '大宛': [70.258894, 41.175899]
    }, **style_geo)

    data_westsouth = [
        ['瓜州', '敦煌'],
        ['敦煌', '阳关'],
        ['阳关', '若羌县'],
        ['若羌县', '且丰县'],
        ['且丰县', '和田'],
        ['和田', '莎车'],
        ['莎车', '葱岭']
    ]
    charts.add("中段南道", data_westsouth, geo_cities_coords={
        '瓜州': [95.793335, 40.530274],
        '敦煌': [94.6806, 40.148308],
        '阳关': [94.060858, 39.940913],
        '若羌县': [89.060858, 39.940913],
        '且丰县': [86.560858, 38.540919],
        '和田': [79.933681, 37.121827],
        '莎车': [77.249562, 38.422871],
        '葱岭': [72.249562, 37.921827]

    }, **style_geo)
    page.add(charts)
    html=charts.render_embed()

    script = page.get_js_dependencies()
    return html, script