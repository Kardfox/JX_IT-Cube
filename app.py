import flask

app = flask.Flask(
    __name__,
    static_url_path="/server-storage",
    static_folder="storage"
)

@app.get("/")
def main():
    return flask.render_template("main.html")

@app.get("/favicon.ico")
def return_icon():
    return app.send_static_file("favicon.ico")