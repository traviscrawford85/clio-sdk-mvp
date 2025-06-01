"""Court Rules API Module"""


# Tag: Jurisdictions To Triggers

def jurisdictionstotrigger_index():
    """Return the data for all triggers"""
    # Endpoint: GET /court_rules/jurisdictions/{jurisdiction_id}/triggers.json
    pass


def jurisdictionstotrigger_show():
    """Return the data for the trigger"""
    # Endpoint: GET /court_rules/jurisdictions/{jurisdiction_id}/triggers/{id}.json
    pass



# Tag: Jurisdictions

def jurisdiction_index():
    """Return the data for all jurisdictions"""
    # Endpoint: GET /court_rules/jurisdictions.json
    pass


def jurisdiction_show():
    """Return the data for the jurisdiction"""
    # Endpoint: GET /court_rules/jurisdictions/{id}.json
    pass



# Tag: Matter Dockets

def matterdocket_index():
    """Return the data for all matter dockets"""
    # Endpoint: GET /court_rules/matter_dockets.json
    pass


def matterdocket_create():
    """Creates a matter docket"""
    # Endpoint: POST /court_rules/matter_dockets.json
    pass


def matterdocket_preview():
    """Preview calendar dates for the docket"""
    # Endpoint: GET /court_rules/matter_dockets/preview.json
    pass


def matterdocket_destroy():
    """Deletes the requested matter docket"""
    # Endpoint: DELETE /court_rules/matter_dockets/{id}.json
    pass


def matterdocket_show():
    """Return the data for the matter docket"""
    # Endpoint: GET /court_rules/matter_dockets/{id}.json
    pass



# Tag: Service Types

def servicetype_index():
    """Return the data for all service types"""
    # Endpoint: GET /court_rules/service_types.json
    pass


def servicetype_show():
    """Return the data for the service type"""
    # Endpoint: GET /court_rules/service_types/{id}.json
    pass


