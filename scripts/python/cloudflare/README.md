# Cloudflare Access Group IP Updater

This script dynamically updates a **Cloudflare Access Group** with the current IP address of a specified domain. It is designed to work with **Cloudflare Zero Trust** (Access) and can be automated using **GitHub Actions**.

---

## **Features**
- Fetches the current IP address of a domain using DNS resolution.
- Updates a Cloudflare Access Group with the resolved IP address.
- Includes verbose logging for easy debugging.
- Can be scheduled to run periodically using GitHub Actions.

---

## **Prerequisites**
1. **Cloudflare Zero Trust Account**:
   - Access to [https://one.dash.cloudflare.com](https://one.dash.cloudflare.com).
2. **Cloudflare API Token**:
   - A token with permissions to edit Access groups.
3. **Domain Name**:
   - The domain whose IP address you want to track.
4. **GitHub Repository**:
   - To store the script and run it via GitHub Actions.

---

## **Setup**

### **1. Create a Cloudflare API Token**
1. Go to [https://one.dash.cloudflare.com](https://one.dash.cloudflare.com).
2. Navigate to **Settings > API Tokens**.
3. Click **Create Token** and use the **Edit Cloudflare Zero Trust** template.
4. Configure the token with the following permissions:
   - Account > Access: Apps and Policies > Edit
5. Copy the token and store it securely.

### **2. Find Your Cloudflare Account ID**
1. Go to [https://one.dash.cloudflare.com](https://one.dash.cloudflare.com).
2. Navigate to **Access > Applications**.
3. Copy the **Account ID** from the URL (e.g., `abc123456789abc123456789abc12345`).

### **3. Find Your Cloudflare Access Group ID**
1. Go to [https://one.dash.cloudflare.com](https://one.dash.cloudflare.com).
2. Navigate to **Access > Groups**.
3. Click on the group you want to update.
4. Copy the **Access Group ID** from the URL (e.g., `abc123456789abc123456789abc12345`).

### **4. Add Secrets to GitHub**
1. Go to your GitHub repository.
2. Navigate to **Settings > Secrets and variables > Actions**.
3. Add the following secrets:
   - `CLOUDFLARE_API_TOKEN`: Your Cloudflare API token.
   - `CLOUDFLARE_ACCOUNT_ID`: Your Cloudflare Account ID.
   - `CLOUDFLARE_ACCESS_GROUP_ID`: The Access Group ID.
   - `DOMAIN`: The domain name (e.g., `example.com`).

---

## **How It Works**
1. The script resolves the domain's IP address using DNS.
2. It updates the specified Cloudflare Access Group with the resolved IP address.
3. The script is designed to run periodically via GitHub Actions.

---

## **Usage**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install Dependencies
Ensure you have Python 3.9+ installed. Install the required dependencies:

```bash
pip install requests
```

### 3. Run the Script Locally
Set the required environment variables and run the script:

```bash
export CLOUDFLARE_API_TOKEN="your-api-token"
export CLOUDFLARE_ACCOUNT_ID="your-account-id"
export CLOUDFLARE_ACCESS_GROUP_ID="your-access-group-id"
export DOMAIN="example.com"

python update_cloudflare_access.py
```

### 4. Automate with GitHub Actions
The repository includes a GitHub Actions workflow (.github/workflows/update-cloudflare-access.yml) that runs the script every hour. No additional setup is required if the secrets are configured.

Example Logs
When the script runs, you’ll see logs like this:

```
2023-10-10 12:00:00,000 - INFO - Starting script to update Cloudflare Access group...
2023-10-10 12:00:01,000 - INFO - Resolved IP for example.com: 93.184.216.34
2023-10-10 12:00:02,000 - INFO - Successfully updated Cloudflare Access group abc123 with IP 93.184.216.34
2023-10-10 12:00:03,000 - INFO - Script completed successfully.
```

## Troubleshooting
### Failed to Resolve IP:

Ensure the domain name is correct and accessible.

### Failed to Update Access Group:

Verify the API token has the correct permissions.

Check the Access Group ID and Account ID.

### API Errors:

Review the logs for detailed error messages from the Cloudflare API.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
[Cloudflare API Documentation][def1]

[GitHub Actions Documentation][def2]

[def1]: https://developers.cloudflare.com/api/
[def2]: https://docs.github.com/en/actions