# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------

import os

# Follow the style of "<OWNER>/<REPO>"
REPO = "dapr/dapr"

# yml file name of github action workflow"
WORKFLOW_NAME = "dapr-test.yml"

# Github access token. Must cover the scope of dapr repo"
# Replace it when running locally
ACCESS_TOKEN = os.getenv("GITHUB_TOKEN")

# Parameters brought when accessing github API
GITHUB_API_PARAMETER = {"per_page": "100"}

# Target to output logs
OUTPUT_TARGET = "log.txt"
