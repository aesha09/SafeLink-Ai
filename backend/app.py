import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from scanners.google_safebrowsing import scan_google_safebrowsing
from scanners.virustotal import scan_virustotal
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
load_dotenv()
# Create the Flask app


# Load API keys from environment variables
VT_API_KEY = os.getenv("VT_API_KEY")
GS_API_KEY = os.getenv("GS_API_KEY")

@app.route('/scan', methods=['POST'])
def scan_url():
    data = request.get_json()
    url = data.get("url") if data else None

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    if not VT_API_KEY:
        return jsonify({"error": "VirusTotal API key not configured."}), 500

    if not GS_API_KEY:
        return jsonify({"error": "Google Safe Browsing API key not configured."}), 500

    # Perform scans
    vt_result = scan_virustotal(VT_API_KEY, url)
    gs_result = scan_google_safebrowsing(GS_API_KEY, url)

    result = {
        "url": url,
        "virustotal": vt_result,
        "google_safe_browsing": gs_result
    }
    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
