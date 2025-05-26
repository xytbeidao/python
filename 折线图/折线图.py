from pyecharts.charts import Line
line = Line()
line.add_xaxis(["中国","新西兰","澳大利亚","美国"])
line.add_yaxis("GDP",[40,30,20,10])
line.render()