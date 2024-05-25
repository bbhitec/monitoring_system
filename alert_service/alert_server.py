from alert_service import AlertService

from flask import Flask, jsonify, request
import asyncio

STATUS_BAD_REQUEST  = 400
STATUS_OK           = 200



app = Flask(__name__)

# define server route to accept alerts
@app.route('/notify', methods=['POST'])
async def receive_alert():

    # receive the alert text
    data = request.get_json()
    message = data.get('text')
    if not message:
        return jsonify({'error': 'Invalid request'}), STATUS_BAD_REQUEST

    # notify all valid alert channels
    await alert_service.send_alert(message)

    return jsonify({'status': 'success'}), STATUS_OK


alert_service = None

if __name__ == '__main__':

    # config the notification channels
    alert_service = AlertService()

    # run the local server to accept alerts
    print("Starting Alert Server")
    app.run(port=5000)