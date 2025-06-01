"""Billing API Module"""


# Tag: Bills

def bill_index():
    """Return the data for all Bills"""
    # Endpoint: GET /bills.json
    pass


def bill_destroy():
    """Delete or void a Bill"""
    # Endpoint: DELETE /bills/{id}.json
    pass


def bill_show():
    """Return the data for a single Bill"""
    # Endpoint: GET /bills/{id}.json
    pass


def bill_update():
    """Update a single Bill"""
    # Endpoint: PATCH /bills/{id}.json
    pass


def bill_preview():
    """Returns the pre-rendered html for the Bill"""
    # Endpoint: GET /bills/{id}/preview.json
    pass



# Tag: Billable Clients

def billableclient_index():
    """Return the data for all BillableClients"""
    # Endpoint: GET /billable_clients.json
    pass



# Tag: Billable Matters

def billablematter_index():
    """Return the data for all BillableMatters"""
    # Endpoint: GET /billable_matters.json
    pass


def billablematter_ids():
    """Returns the unique identifiers of all BillableMatter"""
    # Endpoint: GET /billable_matters/ids.json
    pass



# Tag: Bill Themes

def billtheme_index():
    """Return the data for all BillThemes"""
    # Endpoint: GET /bill_themes.json
    pass


def billtheme_update():
    """Update a single BillTheme"""
    # Endpoint: PATCH /bill_themes/{id}.json
    pass



# Tag: Interest Charges

def interestcharge_index():
    """Return the data for all InterestCharges"""
    # Endpoint: GET /interest_charges.json
    pass


def interestcharge_destroy():
    """Delete a single InterestCharge"""
    # Endpoint: DELETE /interest_charges/{id}.json
    pass



# Tag: Line Items

def lineitem_index():
    """Return the data for all LineItems"""
    # Endpoint: GET /line_items.json
    pass


def lineitem_destroy():
    """Delete a single LineItem"""
    # Endpoint: DELETE /line_items/{id}.json
    pass


def lineitem_update():
    """Update a single LineItem"""
    # Endpoint: PATCH /line_items/{id}.json
    pass



# Tag: Outstanding Client Balances

def outstandingclientbalance_index():
    """Return the data for all OutstandingClientBalances"""
    # Endpoint: GET /outstanding_client_balances.json
    pass


