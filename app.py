from http.server import BaseHTTPRequestHandler, HTTPServer
import json


INVENTORY = [
    {"id": 1, "name": "keyboard", "quantity": 12},
    {"id": 2, "name": "mouse", "quantity": 20},
]


def get_inventory():
    """Return the current inventory list."""
    return INVENTORY


def get_health_status():
    """Return the health status of the service."""
    return {"status": "unhealthy"}


class InventoryHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response_body = json.dumps(get_health_status()).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response_body)
            return

        if self.path != "/inventory":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return

        response_body = json.dumps(get_inventory()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response_body)


def run_server():
    server = HTTPServer(("127.0.0.1", 8000), InventoryHandler)
    print("Inventory API running at http://127.0.0.1:8000/inventory")
    server.serve_forever()


if __name__ == "__main__":
    run_server()