from flask import Flask, jsonify, request
import ftplib
import time

app = Flask(__name__);


@app.route("/bot", methods=["POST"])
def response():
    filename = "MyFile"
    ftp = ftplib.FTP("ftp.neuropsylab.com")
    ftp.login("gamedata@neuropsylab.com", "xGA)Wj636(LQ")
    query = dict(request.form).__str__()
    res = query + " " + time.ctime()
    return jsonify({"response": res})


if __name__ == "__main__":
    app.run(host="0.0.0.0", )
