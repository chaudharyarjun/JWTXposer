import requests
import pyfiglet
import re
import jwt
import time
import json
import urllib.parse
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from urllib.parse import urlparse, parse_qs, unquote
from concurrent.futures import ThreadPoolExecutor


console = Console()


def show_banner():
    banner = pyfiglet.figlet_format("JWTXposer")
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print("[bold yellow] Automated JWT Extraction & Analysis Tool for Bug Bounty Hunters [/bold yellow]\n")
    console.print("[bold magenta] Developed with love by Chaudhary_S4h4b [/bold magenta]\n")

def main(target):
    show_banner() 
    console.print(f"\n[cyan][*] Fetching Wayback URLs for {target}...[/cyan]")
  
  
WAYBACK_URL = "https://web.archive.org/cdx/search/cdx?url=*.{target}&output=text&fl=original&collapse=urlkey"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; JWT-Finder/1.0; +https://github.com/yourusername/jwt_finder)"}

JWT_REGEX = re.compile(r'eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}')  # General JWT pattern


JUICY_FIELDS = ["email", "username", "password", "api_key", "access_token", "session_id", "role", "scope"]


def fetch_wayback_urls(target, retries=3):
    """Fetch archived URLs from Wayback Machine with retry mechanism."""
    url = WAYBACK_URL.format(target=target)
    for attempt in range(retries):
        try:
            console.log(f"[*] Fetching URLs... Attempt {attempt + 1}")
            response = requests.get(url, headers=HEADERS, timeout=30)
            if response.status_code == 200:
                return response.text.splitlines()
            console.log(f"[!] Attempt {attempt + 1}: Received HTTP {response.status_code}")
        except requests.exceptions.RequestException as e:
            console.log(f"[!] Attempt {attempt + 1} failed: {e}")
            time.sleep(5)
    return []


def extract_jwt_from_url(url):
    """Extract JWT tokens from query parameters or raw URL."""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    for key, values in query_params.items():
        for value in values:
            decoded_value = unquote(value)
            if re.match(JWT_REGEX, decoded_value):
                console.print(f"[green][+] JWT Found in URL Parameter:[/green] {decoded_value}")
                return decoded_value

    decoded_url = unquote(url)
    match = JWT_REGEX.search(decoded_url)
    if match:
        console.print(f"[blue][+] JWT Found in Full URL:[/blue] {match.group(0)}")
        return match.group(0)

    return None


def check_url_status(url):
    """Check if the URL is still live (HTTP 200, 301, 302)."""
    try:
        response = requests.head(url, headers=HEADERS, allow_redirects=True, timeout=10)
        if response.status_code in [200, 301, 302]:
            return url
    except requests.exceptions.RequestException:
        pass
    return None


def decode_jwt(token):
    """Decode JWT token without verifying signature."""
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded
    except jwt.exceptions.DecodeError:
        return None


def analyze_jwt(decoded_data):
    """Highlight juicy fields in JWT payload."""
    juicy_info = {key: value for key, value in decoded_data.items() if key in JUICY_FIELDS}
    return juicy_info


def save_results(results):
    """Save extracted JWTs and decoded data to a file."""
    with open("jwt_results.json", "w") as f:
        json.dump(results, f, indent=4)
    console.print("\n[green][+] Results saved in jwt_results.json[/green]")


def main(target):
    console.print(f"\n[cyan][*] Fetching Wayback URLs for {target}...[/cyan]")
    urls = fetch_wayback_urls(target)
    if not urls:
        console.print("[red][!] No URLs found.[/red]")
        return

    console.print(f"[green][+] Retrieved {len(urls)} URLs.[/green]")

    jwt_tokens = {}
    for url in urls:
        token = extract_jwt_from_url(url)
        if token:
            jwt_tokens[url] = token

    if not jwt_tokens:
        console.print("[red][!] No JWT tokens found.[/red]")
        return

    console.print(f"[yellow][+] Found {len(jwt_tokens)} JWT tokens.[/yellow]")

    live_urls = []
    with ThreadPoolExecutor(max_workers=10) as executor: # You can increase threads based on your requirements 
        results = executor.map(check_url_status, jwt_tokens.keys())
        live_urls = [url for url in results if url]

    if not live_urls:
        console.print("[red][!] No live URLs containing JWTs.[/red]")
        return

    console.print(f"[green][+] {len(live_urls)} live URLs with JWTs identified.[/green]")

    decoded_results = {}
    for url in live_urls:
        decoded_data = decode_jwt(jwt_tokens[url])
        if decoded_data:
            juicy_data = analyze_jwt(decoded_data)
            decoded_results[url] = {"jwt": jwt_tokens[url], "decoded": decoded_data, "juicy": juicy_data}

    save_results(decoded_results)


    table = Table(title="Extracted JWTs & Juicy Info")
    table.add_column("URL", style="cyan", no_wrap=True)
    table.add_column("JWT", style="magenta")
    table.add_column("Decoded Data", style="green")

    for url, data in decoded_results.items():
        table.add_row(url, data["jwt"], json.dumps(data["juicy"], indent=2))

    console.print(table)


if __name__ == "__main__":
    show_banner()
    target_domain = input("Enter the target domain (e.g., api.example.com): ")
    main(target_domain)
