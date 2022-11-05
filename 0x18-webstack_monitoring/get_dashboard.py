#!/usr/bin/python3
"""
    Retrives a list of dashboards with details.
    Run in bash:
     DD_SITE="us.datadoghq.com" DD_API_KEY="xxx" DD_APP_KEY="xxx" python3 get_dashboard.py
"""
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi


configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(
        filter_shared=False
    )

    print(response)
