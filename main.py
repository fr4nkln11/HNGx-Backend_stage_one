from datetime import datetime, timedelta
from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def get_info(slack_name: str | None = None,
                   track: str | None = None):

    current_day = datetime.utcnow().strftime("%A")

    utc_time = (datetime.utcnow() + timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%SZ")

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "status_code": 200
    }

    return response_data
