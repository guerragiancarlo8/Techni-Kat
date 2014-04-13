import flask
from searchHandler import SearchHandler
from bloombergjson import Bloomberjson


#create app here:

app = flask.Flask(__name__)


@app.route("/")
def root():
	return flask.render_template("index.html")

@app.route('/query', methods=['POST'])
def query():
	result=[]
	keyword = #placeholder?
	sh = SearchHandler()
	sh.search(keyword) # send the query and save the results in example.txt
	bloom = Bloomberjson()
	result = bloom.getJson()

	

if __name__ == "__main__":
	app.run(debut=True)