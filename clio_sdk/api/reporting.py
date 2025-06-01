"""Reporting API Module"""


# Tag: Reports

def report_index():
    """Return the data for all Reports"""
    # Endpoint: GET /reports.json
    pass


def report_create():
    """Create a new Report"""
    # Endpoint: POST /reports.json
    pass


def report_show():
    """Return the data for a single Report"""
    # Endpoint: GET /reports/{id}.json
    pass


def report_download():
    """Download the completed Report"""
    # Endpoint: GET /reports/{id}/download.json
    pass



# Tag: Report Presets

def reportpreset_index():
    """Return the data for all ReportPresets"""
    # Endpoint: GET /report_presets.json
    pass


def reportpreset_create():
    """Create a new ReportPreset"""
    # Endpoint: POST /report_presets.json
    pass


def reportpreset_destroy():
    """Delete a single ReportPreset"""
    # Endpoint: DELETE /report_presets/{id}.json
    pass


def reportpreset_show():
    """Return the data for a single ReportPreset"""
    # Endpoint: GET /report_presets/{id}.json
    pass


def reportpreset_update():
    """Update a single ReportPreset"""
    # Endpoint: PATCH /report_presets/{id}.json
    pass


def reportpreset_generate_report():
    """Generate a new report for a given preset"""
    # Endpoint: POST /report_presets/{id}/generate_report.json
    pass



# Tag: Report Schedules

def reportschedule_index():
    """Return the data for all ReportSchedules"""
    # Endpoint: GET /report_schedules.json
    pass


def reportschedule_create():
    """Create a new ReportSchedule"""
    # Endpoint: POST /report_schedules.json
    pass


def reportschedule_destroy():
    """Delete a single ReportSchedule"""
    # Endpoint: DELETE /report_schedules/{id}.json
    pass


def reportschedule_show():
    """Return the data for a single ReportSchedule"""
    # Endpoint: GET /report_schedules/{id}.json
    pass


def reportschedule_update():
    """Update a single ReportSchedule"""
    # Endpoint: PATCH /report_schedules/{id}.json
    pass


