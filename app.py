import flask
import utils


app = flask.Flask(
    __name__,
    static_url_path="/storage",
    static_folder="storage"
)

@app.get("/")
def main():
    return flask.render_template("main.html")

@app.get("/about")
def about():
    return "It's a coool project"

@app.post("/render")
def render():
    file = flask.request.data
    image = utils.simplest_render(file)
    return flask.send_file(image, mimetype='image/png')

@app.get("/favicon.ico")
def return_icon():
    flask.url_for
    return app.send_static_file("favicon.ico")