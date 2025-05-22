import os
from flask import Flask, request, jsonify
from backend.scanners.virustotal import scan_virustotal

app = Flask(__name__)

# Read VirusTotal API key from environment variable
VT_API_KEY = os.getenv("VT_API_KEY")

@app.route('/scan', methods=['POST'])
def scan_url():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    if not VT_API_KEY:
        return jsonify({"error": "VirusTotal API key not configured."}), 500

    vt_result = scan_virustotal(VT_API_KEY, url)

    # Placeholder: Add other scans here as needed

    result = {
        "url": url,
        "virustotal": vt_result
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
