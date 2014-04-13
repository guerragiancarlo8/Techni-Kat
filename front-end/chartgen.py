line_chart = pygal.Line()
line_chart.title = 'Opening Price' + keyword
line_chart.x_labels = map(str, range(2002, 2013))

line_chart.add('Chrome',  [])

line_chart.render()
