from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


project_folder = Path(__file__).parent
os.chdir(project_folder)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nClock stopped.")
finally:
    server.server_close()
