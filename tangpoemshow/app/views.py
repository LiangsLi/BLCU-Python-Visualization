from flask import render_template
import app.mycharts as new_charts
from . import app
from . import data

dataForShuoWenJieZi = data.get_data_shuowenjiezi()
dataForShiRenGuanXi=data.get_data_shirenguanxi()
dataForCangHaiCiHua = data.get_data_canghaicihua()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/shuowenjiezi')
def shuowenjiezi():
    html, js = new_charts.ShuoWenJieZi.create_charts(dataForShuoWenJieZi)
    return render_template('bootstrapBase.html', page_title='说文解字', theme='说文解字', theme_description='仓颉之初作书也，盖依类象形，故谓之文。其后形声相益，即谓之字。文者，物象之本；字者，言孳乳而寖多也。',
                           mychart=html, script_list=js)

@app.route('/canghaicihua')
def canghaicihua():
    html, js = new_charts.CangHaiCiHua.create_charts(dataForCangHaiCiHua)
    return render_template('bootstrapBase.html', page_title='沧海词话', theme='沧海词话', theme_description='仓颉之初作书也，盖依类象形，故谓之文。其后形声相益，即谓之字。文者，物象之本；字者，言孳乳而寖多也。',
                           mychart=html, script_list=js, n = 5, name = ['名词', '地理名词', '时间名词', '动词', '形容词'])


@app.route('/shirenguanxi')
def shirenguanxi():
    html,js=new_charts.ShiRenGuanXi.create_charts(dataForShiRenGuanXi)
    return render_template('bootstrapBase.html', page_title='桃花潭水', theme='桃花潭水', theme_description='仓颉之初作书也，盖依类象形，故谓之文。其后形声相益，即谓之字。文者，物象之本；字者，言孳乳而寖多也。',
                           mychart=html, script_list=js)

@app.route('/sichouzhilu')
def sichouzhilu():
    html,js=new_charts.SiChouZhiLu.create_charts(None)
    return render_template('bootstrapBase.html', page_title='丝绸之路', theme='丝绸之路', theme_description='仓颉之初作书也，盖依类象形，故谓之文。其后形声相益，即谓之字。文者，物象之本；字者，言孳乳而寖多也。',
                           mychart=html, script_list=js)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
