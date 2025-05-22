import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w.text
    except Exception as e:
        return str(e)