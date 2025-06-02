welcome_blocks = [
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "\ud83d\udc4b *Welcome to the Ledyard Law AI Assistant!* I'm here to help you stay organized and informed.\nHere's what I can do for you:"}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\ud83d\udccb Create Tasks:* Use `/task` followed by your task description."}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*\ud83e\udde0 Summarize Channel Activity:* Click the button below to get a concise summary of recent discussions."},
        "accessory": {
            "type": "button",
            "text": {"type": "plain_text", "text": "Summarize Now"},
            "action_id": "summarize_channel"
        }
    },
    {
        "type": "image",
        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/onboardingComplex.jpg",
        "alt_text": "task creation demo"
    },
    {"type": "divider"},
    {
        "type": "context",
        "elements": [
            {"type": "mrkdwn", "text": "\ud83d\udd0d Use `/task list` to see all tasks.\n\ud83e\udd16 Type *help* in DM or `/task help` for help."}
        ]
    }
]