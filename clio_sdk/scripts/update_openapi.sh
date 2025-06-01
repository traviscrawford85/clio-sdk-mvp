#!/bin/bash
set -e

# Paths
OPENAPI_JSON="openapi_sdk.yaml"
CLIENT_TARGET="clio_sdk/clio_client"
CONFIG_YAML="openapi-python-client-config.yaml"

# Cleanup previous client
echo "🧹 Cleaning old OpenAPI client at $CLIENT_TARGET..."
rm -rf "$CLIENT_TARGET"
mkdir -p "$CLIENT_TARGET"

# Generate new client
echo "🚀 Generating OpenAPI client using config $CONFIG_YAML..."
openapi-python-client generate \
  --path "$OPENAPI_JSON" \
  --output "$CLIENT_TARGET" \
  --config "$CONFIG_YAML"

echo "✅ Done. Client written to $CLIENT_TARGET"
