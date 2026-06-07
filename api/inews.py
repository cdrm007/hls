from http.server import BaseHTTPRequestHandler
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. GANTIKAN URL DI BAWAH dengan URL Raw 'inews.txt' dari GitHub anda sendiri
        github_raw_url = "https://raw.githubusercontent.com/USERNAME/REPO-ANDA/main/inews.txt"
        
        try:
            # 2. Ambil URL iNews terkini dari fail teks di GitHub
            with urllib.request.urlopen(github_raw_url) as response:
                m3u8_url = response.read().decode('utf-8').strip()
            
            # 3. Lakukan HTTP 302 Redirect terus ke m3u8 asli iNews
            self.send_response(302)
            self.send_header('Location', m3u8_url)
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Ralat mengambil URL dari GitHub")
