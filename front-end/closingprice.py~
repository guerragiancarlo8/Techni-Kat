from bloombergjson import Bloombergjson
import pygal

result = []
bloom = Bloombergjson()
result = bloom.getJson()
openPricedataSet=[]
closePricedataSet=[]
for d in result:

	if '"MSFT US Equity"' in d['ticker']:
		openPricedataSet.append(d['open_price'])
		closePricedataSet.append(d['last_price'])
	
		
	
	

line_chart = pygal.Line()
line_chart.title = 'Microsoft Open and Closing Price from 2002 to 2013'
line_chart.x_labels = map(str, range(2002, 2013))

line_chart.add('MSFT',  openPricedataSet)
line_chart.add('MSFT', closePricedataSet)

line_chart.render_to_file('line_chart_close.svg')
