import requests

def scan_virustotal(api_key, url):
    vt_url = "https://www.virustotal.com/api/v3/urls"
    headers = {"x-apikey": api_key}
    
    # Submit the URL to VirusTotal for scanning
    response = requests.post(vt_url, headers=headers, data={"url": url})
    
    if response.status_code == 200:
        scan_id = response.json()["data"]["id"]
        report_url = f"{vt_url}/{scan_id}"
        report = requests.get(report_url, headers=headers).json()
        
        if "data" in report:
            stats = report["data"]["attributes"]["last_analysis_stats"]
            return stats
        else:
            return {"error": "Report data unavailable"}
    else:
        return {"error": response.text}
