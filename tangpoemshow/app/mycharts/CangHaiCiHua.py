from pyecharts import Bar, Line, Liquid, WordCloud, Pie, Overlap, Page, Style
from app.mycharts.constants import WIDTH, HEIGHT


def create_charts(data):
    # data字典格式(三个表的情况下)：
    # {'nouns':[str:表一的前描述,str:表一的后描述,数据1,数据2,...,数据n],'...':[...]}
    html = ''
    page = Page()
    style = Style(width=900, height=600)
    # 本页面包含：1：noun(两个数据noun,values)、
    # 表一：
    # 获取表一的数据
    html_before = data['nounfre'][0]
    html_after = data['nounfre'][1]
    keys = data['nounfre'][2]
    values = data['nounfre'][3]
    line = Line("唐诗词频--名词", **style.init_style)
    line.add("词频--名词", keys, values, is_smooth=True, is_fill=True, area_opacity=0.2, is_datazoom_show=True,
             datazoom_type="both", datazoom_range=[0, 60], xaxis_interval=1, xaxis_name="名词",
             yaxis_name="词频", xaxis_name_pos="end", yaxis_name_pos="end", is_more_utils=True)
    java_script = line.render_embed()
    html += html_before + java_script + html_after
    page.add(line)

    #表二
    html_before = data['geofre'][0]
    html_after = data['geofre'][1]
    keys = data['geofre'][2]
    values = data['geofre'][3]
    line = Line("唐诗词频--地理名词", **style.init_style)
    line.add("词频--地理名词", keys, values, is_smooth=True, is_fill=True, area_opacity=0.2, is_datazoom_show=True,
             datazoom_type="both", datazoom_range=[0, 60], xaxis_interval=1, xaxis_name="地理名词",
             yaxis_name="词频", xaxis_name_pos="end", yaxis_name_pos="end", is_more_utils=True)
    java_script = line.render_embed()
    html += html_before + java_script + html_after
    page.add(line)

    # 表三
    html_before = data['timefre'][0]
    html_after = data['timefre'][1]
    keys = data['timefre'][2]
    values = data['timefre'][3]
    line = Line("唐诗词频--地理名词", **style.init_style)
    line.add("词频--时间名词", keys, values, is_smooth=True, is_fill=True, area_opacity=0.2, is_datazoom_show=True,
             datazoom_type="both", datazoom_range=[0, 60], xaxis_interval=1, xaxis_name="时间名词",
             yaxis_name="词频", xaxis_name_pos="end", yaxis_name_pos="end", is_more_utils=True)
    java_script = line.render_embed()
    html += html_before + java_script + html_after
    page.add(line)

    # 表四
    html_before = data['verbfre'][0]
    html_after = data['verbfre'][1]
    keys = data['verbfre'][2]
    values = data['verbfre'][3]
    line = Line("唐诗词频--动词", **style.init_style)
    line.add("词频--动词", keys, values, is_smooth=True, is_fill=True, area_opacity=0.2, is_datazoom_show=True,
             datazoom_type="both", datazoom_range=[0, 60], xaxis_interval=1, xaxis_name="动词",
             yaxis_name="词频", xaxis_name_pos="end", yaxis_name_pos="end", is_more_utils=True)
    java_script = line.render_embed()
    html += html_before + java_script + html_after
    page.add(line)

    # 表五
    html_before = data['adjfre'][0]
    html_after = data['adjfre'][1]
    keys = data['adjfre'][2]
    values = data['adjfre'][3]
    line = Line("唐诗词频--xrc", **style.init_style)
    line.add("词频--形容词", keys, values, is_smooth=True, is_fill=True, area_opacity=0.2, is_datazoom_show=True,
             datazoom_type="both", datazoom_range=[0, 60], xaxis_interval=1, xaxis_name="形容词",
             yaxis_name="词频", xaxis_name_pos="end", yaxis_name_pos="end", is_more_utils=True)
    java_script = line.render_embed()
    html += html_before + java_script + html_after
    page.add(line)

    script = page.get_js_dependencies()
    return html, script