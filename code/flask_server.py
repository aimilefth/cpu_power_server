from flask import Flask, request, Response
import json
import os
import power_scraper as ps   # renamed import for clarity

app = Flask(__name__)

# Initialize the power scraper; 
# The power_scraper class definition requires a device_id in its __init__.
power_scraper = ps.power_scraper()

@app.route('/api/cpu_power', methods=['POST'])
def power_service():
    """
    Endpoint to return CPU power metrics by measuring energy consumption over a short sleep interval.
    """
    data = power_scraper.cpu_get_power()
    return Response(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    # Let the port be configurable via an environment variable, defaulting to 5000
    port = int(os.getenv('PORT', 5000))
    # Run the Flask app on host='0.0.0.0' so that it's accessible from outside the container
    app.run(host='0.0.0.0', port=port)
