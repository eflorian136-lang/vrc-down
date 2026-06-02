import sys

def simulate_downloader(url):
    print(f"--- Starte Test für: {url} ---")
    
    if "twitch.tv" not in url:
        print("Fehler: Keine gültige Twitch-URL.")
        return

    # Hier simulieren wir die Logik aus deiner VideoEngine.py
    print("1. Analysiere Playlist...")
    print("2. Extrahiere Stream-Segmente...")
    print("3. Downloader-Status: Bereit.")
    print("--- Download-Simulation erfolgreich ---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        simulate_downloader(sys.argv[1])
    else:
        print("Bitte gib eine URL an: python3 test_downloader.py <URL>")
