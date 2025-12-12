# Installation & Setup Guide

Complete guide for installing and setting up the Mighty Networks Python SDK.

## Prerequisites

- Python 3.7 or higher
- pip package manager
- Mighty Networks API token

## Installation Methods

### Method 1: Install from Source (Recommended for Development)

```bash
# Navigate to the SDK directory
cd mighty-networks-sdk

# Install in editable mode
pip install -e .
```

This allows you to make changes to the code and see them immediately without reinstalling.

### Method 2: Standard Installation

```bash
# Install from source
pip install .
```

### Method 3: Install Dependencies Only

```bash
# Production dependencies
pip install -r requirements.txt

# Development dependencies (includes testing tools)
pip install -r requirements-dev.txt
```

## Getting Your API Token

1. Log in to your Mighty Network as an admin
2. Go to Settings → Integrations
3. Find or create an API token
4. Copy the token (keep it secure!)

## First Steps

### 1. Create a Python script

```python
# my_script.py
from mighty_networks_sdk import MightyNetworksClient

# Initialize the client
client = MightyNetworksClient(api_token="your_api_token_here")

# Test the connection
try:
    spaces = client.spaces.list(network_id=12345)
    print(f"Successfully connected! Found {len(spaces['items'])} spaces")
except Exception as e:
    print(f"Error: {e}")
```

### 2. Run your script

```bash
python my_script.py
```

## Environment Variables (Recommended)

Instead of hardcoding your API token, use environment variables:

### On macOS/Linux:

```bash
# Add to ~/.bashrc or ~/.zshrc
export MIGHTY_NETWORKS_TOKEN="your_api_token_here"
export MIGHTY_NETWORKS_ID="your_network_id"
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

### On Windows:

```cmd
# Set environment variable
setx MIGHTY_NETWORKS_TOKEN "your_api_token_here"
setx MIGHTY_NETWORKS_ID "your_network_id"
```

### Use in Python:

```python
import os
from mighty_networks_sdk import MightyNetworksClient

api_token = os.getenv("MIGHTY_NETWORKS_TOKEN")
network_id = int(os.getenv("MIGHTY_NETWORKS_ID"))

client = MightyNetworksClient(api_token=api_token)
```

## Configuration Options

```python
client = MightyNetworksClient(
    api_token="your_token",
    base_url="https://api.mn.co",  # Default API URL
    timeout=30  # Request timeout in seconds
)
```

## Verify Installation

Run this script to verify everything is working:

```python
from mighty_networks_sdk import MightyNetworksClient
from mighty_networks_sdk.exceptions import AuthenticationError

def verify_installation():
    """Verify SDK installation and configuration."""
    print("Mighty Networks SDK - Installation Verification")
    print("=" * 50)

    # Check if token is set
    api_token = input("Enter your API token: ")
    network_id = int(input("Enter your network ID: "))

    try:
        # Initialize client
        client = MightyNetworksClient(api_token=api_token)
        print("✓ Client initialized successfully")

        # Test API call
        spaces = client.spaces.list(network_id=network_id)
        print(f"✓ API connection successful!")
        print(f"✓ Found {len(spaces['items'])} spaces in your network")

        # List spaces
        print("\nYour Spaces:")
        for space in spaces['items']:
            print(f"  - {space['name']} (ID: {space['id']})")

        print("\n✅ Installation verified successfully!")
        return True

    except AuthenticationError:
        print("✗ Authentication failed. Check your API token.")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    verify_installation()
```

## Development Setup

For contributing or developing:

```bash
# Clone repository
git clone https://github.com/yourusername/mighty-networks-sdk.git
cd mighty-networks-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .

# Type checking
mypy mighty_networks_sdk/
```

## Common Issues

### ImportError: No module named 'mighty_networks_sdk'

**Solution**: Make sure you've installed the package:
```bash
pip install -e .
```

### Authentication Error

**Solution**: Verify your API token is correct and has not expired.

### Connection Timeout

**Solution**: Increase timeout:
```python
client = MightyNetworksClient(api_token="your_token", timeout=60)
```

### SSL Certificate Error

**Solution**: Update your certificates or use:
```python
import requests
requests.packages.urllib3.disable_warnings()
```

## Next Steps

1. Read the [Quick Start Guide](QUICKSTART.md)
2. Check out [Examples](examples/)
3. Review the [API Reference](API_REFERENCE.md)
4. Join our community discussions

## Support

- 📖 [Documentation](README.md)
- 🐛 [Report Issues](https://github.com/yourusername/mighty-networks-sdk/issues)
- 💬 [Discussions](https://github.com/yourusername/mighty-networks-sdk/discussions)

## Uninstallation

```bash
pip uninstall mighty-networks-sdk
```
