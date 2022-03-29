from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/download')
def survey():
    return render_template("download.html")

@app.route('/info')
def stats():
    return render_template("info.html")

@app.route('/downloader<int:uni>')
def downloadFile (uni):
    path = "parsed_text" + str(uni) + ".txt"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)