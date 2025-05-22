import requests

def check_safe_browsing(api_key, url):
    data = {
        "client": {"clientId": "urlscanner", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }
    res = requests.post(
        f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}",
        json=data,
    )
    result = res.json()
    return "safe" if result == {} else "unsafe"