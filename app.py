from flask import Flask, request, make_response
import json
from flask_cors import cross_origin
import os
app = Flask(__name__)

# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():

    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

# processing the request from dialogflow
def processRequest(req):

    sessionID=req.get('responseId')

    result = req.get("queryResult")
    parameters = result.get("parameters")
    cust_name=parameters.get("cust_name")
    #print(cust_name)
    fulfillmentMessages= "Hello "+cust_name+" hope you have a great day ahead"
    return {
        "fulfillmentMessages": fulfillmentMessages
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
