import requests
import socket
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Environment variables (set in GitHub Actions secrets)
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID")
ACCESS_GROUP_ID = os.getenv("CLOUDFLARE_ACCESS_GROUP_ID")
DOMAIN = os.getenv("DOMAIN")

def get_domain_ip(domain):
    """Resolve the domain's IP address."""
    try:
        ip = socket.gethostbyname(domain)
        logger.info(f"Resolved IP for {domain}: {ip}")
        return ip
    except Exception as e:
        logger.error(f"Failed to resolve IP for {domain}: {e}")
        raise

def update_cloudflare_access_group(zone_id, group_id, ip):
    """Update the Cloudflare Access group with the new IP."""
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/access/groups/{group_id}"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {
        "include": [
            {
                "ip": {
                    "ip": ip
                }
            }
        ]
    }

    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        logger.info(f"Successfully updated Cloudflare Access group {group_id} with IP {ip}")
        logger.debug(f"API Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to update Cloudflare Access group: {e}")
        logger.error(f"API Response: {response.json()}")
        raise

def main():
    logger.info("Starting script to update Cloudflare Access group...")
    
    # Fetch the domain's IP address
    domain_ip = get_domain_ip(DOMAIN)
    
    # Update the Cloudflare Access group
    update_cloudflare_access_group(ZONE_ID, ACCESS_GROUP_ID, domain_ip)
    
    logger.info("Script completed successfully.")

if __name__ == "__main__":
    main()