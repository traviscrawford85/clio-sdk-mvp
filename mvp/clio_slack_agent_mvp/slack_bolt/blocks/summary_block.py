def make_summary_block(summary: str) -> list[dict]:
    return [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*🧠 Channel Summary:*"}
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": summary}
        }
    ]
