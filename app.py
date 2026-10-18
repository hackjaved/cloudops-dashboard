
from flask import Flask, jsonify
from datetime import datetime, timezone
from markupsafe import escape
import os

app = Flask(__name__)

APP_NAME = "CloudOps Dashboard"
APP_VERSION = "1.0.0"


def get_environment():
    return os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    environment = escape(get_environment())

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>CloudOps Dashboard</title>

        <style>
            body {{
                background: #f3f6fb;
                font-family: Arial, sans-serif;
                padding: 40px;
            }}

            .dashboard {{
                background: white;
                max-width: 650px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px #ddd;
            }}

            h1 {{
                color: #1769aa;
            }}

            .status {{
                color: #188038;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="dashboard">
            <h1>CloudOps Dashboard</h1>

            <h3 class="status">
                Application Status: Healthy
            </h3>

            <p>Environment: {environment}</p>
            <p>Version: {APP_VERSION}</p>

            <p>
                Welcome to your Azure DevOps
                learning project!
            </p>

            <p>
                Health API:
                <a href="/health">/health</a>
            </p>

            <p>
                Application Info:
                <a href="/api/info">/api/info</a>
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": get_environment(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.route("/api/info")
def app_info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": get_environment(),
        "platform": "Python Flask",
        "project": "21-Day Azure DevOps Challenge"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
