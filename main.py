# Import needed modules from osc4py3
import py_eureka_client.eureka_client as eureka_client
from flask import Flask, request, jsonify

ESSENTIA_SERVER_PORT = 9090

eureka_client.init(
    eureka_server="http://user:password@localhost:8761",
    app_name="ESSENTIA-SERVICE",
    instance_port=ESSENTIA_SERVER_PORT

)
app = Flask(__name__)

@app.route('/audio_analysis', methods=['POST'])
def audio_analysis():
    print("audio_analysis():")
    data = request.get_json()
    print(data)
    return jsonify(data)

@app.route('/audio/test', methods=['GET'])
def audio_test():
    print("audio_test():")
    return jsonify({"message": "audio_test()"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=ESSENTIA_SERVER_PORT)
            



