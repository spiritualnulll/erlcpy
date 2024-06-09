import requests # obviously
import colorama # just used for initalization
import time # ratelimitssssss
from colorama import Fore, Style # For logging

colorama.init(autoreset=True)

class erlc:
    def __init__(self, server_key, global_key=None, debug=False):
        self.base_url = "https://api.policeroleplay.community/v1/"
        self.server_key = server_key
        self.global_key = global_key
        self.debug = debug
        self.headers = {"Server-Key": self.server_key}
        if self.global_key:
            self.headers["Authorization"] = self.global_key
        self.rate_limits = {}

    def log(self, message, color=Fore.BLUE, style=Style.DIM):
        if self.debug:
            print(f"{color}{style}{message}")

    def log_request(self, endpoint):
        self.log(f"Requesting: {self.base_url + endpoint}")

    def log_response(self, response):
        if response.status_code == 200:
            self.log("Response received", color=Fore.GREEN, style=Style.NORMAL)
        elif response.status_code == 403:
            self.log("[ERLC] INVALID KEY PROVIDED!", color=Fore.RED, style=Style.NORMAL)
        elif response.status_code == 429:
            self.log("[ERLC] RATE LIMIT EXCEEDED!", color=Fore.RED, style=Style.NORMAL)
        else:
            self.log(f"Unexpected status code: {response.status_code}", color=Fore.RED, style=Style.NORMAL)

    def update_rate_limits(self, response):
        headers = response.headers
        if "X-RateLimit-Bucket" in headers:
            bucket = headers["X-RateLimit-Bucket"]
            self.rate_limits[bucket] = {
                "limit": int(headers.get("X-RateLimit-Limit", 0)),
                "remaining": int(headers.get("X-RateLimit-Remaining", 0)),
                "reset": int(headers.get("X-RateLimit-Reset", 0))
            }
            self.log(f"Updated rate limits for bucket: {bucket}", color=Fore.YELLOW, style=Style.NORMAL)

    def check_rate_limit(self, bucket):
        if bucket in self.rate_limits:
            limits = self.rate_limits[bucket]
            if limits["remaining"] <= 0:
                reset_time = limits["reset"] - int(time.time())
                if reset_time > 0:
                    self.log(f"Rate limit exceeded. Waiting for {reset_time} seconds.", color=Fore.RED, style=Style.NORMAL)
                    time.sleep(reset_time)
    
    def get_response(self, endpoint):
        self.log_request(endpoint)
        try:
            response = requests.get(self.base_url + endpoint, headers=self.headers)
            self.update_rate_limits(response)
            self.log_response(response)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                return "403"
            elif response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 1))
                self.log(f"Retrying after {retry_after} seconds.", color=Fore.YELLOW, style=Style.NORMAL)
                time.sleep(retry_after)
                return self.get_response(endpoint)
            else:
                return None
        except requests.exceptions.RequestException as e:
            self.log(f"Network error: {e}", color=Fore.RED, style=Style.NORMAL)
            return None

    def server_info(self):
        return self.get_response("server")

    def players(self):
        return self.get_response("server/players")

    def joinlogs(self):
        return self.get_response("server/joinlogs")

    def queuelist(self):
        return self.get_response("server/queue")

    def killlogs(self):
        return self.get_response("server/killlogs")

    def command_logs(self):
        return self.get_response("server/commandlogs")

    def modcalls(self):
        return self.get_response("server/modcalls")

    def bans(self):
        return self.get_response("server/bans")

    def vehicles(self):
        return self.get_response("server/vehicles")

    def cmd(self, cmd):
        self.log_request("server/command")
        data = {'commandstring': cmd}
        try:
            response = requests.post(self.base_url + "server/command", headers=self.headers, json=data)
            self.update_rate_limits(response)
            self.log_response(response)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                return "403"
            elif response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 1))
                self.log(f"Retrying after {retry_after} seconds.", color=Fore.YELLOW, style=Style.NORMAL)
                time.sleep(retry_after)
                return self.cmd(cmd)
            else:
                return None
        except requests.exceptions.RequestException as e:
            self.log(f"Network error: {e}", color=Fore.RED, style=Style.NORMAL)
            return None
