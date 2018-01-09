# This file acts as a template for a custom Check_MK check.
# Place this file under /usr/share/check_mk/checks/ to make Check_MK use it.
# If you want to use the output of the Check_MK agent make sure to name this file after the correct section.
# For further information check out https://mathias-kettner.de/checkmk_devel_agentbased.html.
# For developing SNMP checks have a look at https://mathias-kettner.de/checkmk_devel_snmpbased.html.

# possible Check_MK status codes
CHECKMK_OK = 0
CHECKMK_WARN = 1
CHECKMK_CRITICAL = 2
CHECKMK_UNKNOWN = 3


# the function that executes the actual check
def check_mycheck(
        item,  # the item that the monitoring data belongs to
        params,  # parameters for this check
        info  # the agent output
):
    return (
        CHECKMK_OK,  # status code
        "The service is OK",  # status description
        [  # performance data, required if has_perfdata is set to True at check registration
            ('value', 1, 5, 10, 0, 10)  # variable name, actual value, warning level, critical level, minimum, maximum
        ]
    )


# the function that decides if this check is suitable for a host
def inventory_mycheck(
        info  # the agent output
):
    return []  # returns a list of items that can be monitored by this check

# registration of check
check_info["mycheck"] = {
    'check_function': check_mycheck,  # the check function implemented above
    'has_perfdata': True,  # set to True if check delivers performance data (data that can be visualized over time)
    'inventory_function': inventory_mycheck,  # the inventory implemented above or no_inventory_possible if inventory is not supported
    'service_description': 'Service description %s',  # description of service, %s will be replaced with item name
    "snmp_info": (  # OID is required when your monitoring data comes from SNMP
        ".1.2.3.4.5.6.7",  # base OID
        ["1", "2", "3"]  # array of sub OIDs to retrieve
    )
}