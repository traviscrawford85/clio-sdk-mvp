from invoke import task
import subprocess
import platform

@task
def start_oauth(c):
    """Start OAuth server (localhost:8001)"""
    subprocess.Popen(["python", "-m", "services.oauth_server"])
    print("🔑 OAuth server running on http://localhost:8001")

@task
def start_api(c):
    """Start Clio FastAPI app (localhost:8000)"""
    c.run("uvicorn clio_fastapi_app.main:app --reload --port 8000", pty=True)

@task
def start_mock_server(c):
    """Start generated Clio mock server (localhost:8002)"""
    c.run("uvicorn generated_server.clio_server.main:app --reload --port 8002", pty=True)

@task
def start_all(c):
    """Start all app servers (OAuth, FastAPI client, Mock server)"""
    start_oauth(c)
    start_mock_server(c)
    start_api(c)

@task
def kill_ports(c):
    """Kill servers on all defined ports (8000, 8001, 8002)"""
    ports = [8000, 8001, 8002]
    system = platform.system()
    for port in ports:
        if system == "Windows":
            cmd = f'for /f "tokens=5" %%a in (\'netstat -aon ^| findstr :{port}\') do taskkill /F /PID %%a'
        else:
            cmd = f"lsof -ti:{port} | xargs kill -9"
        subprocess.call(cmd, shell=True)
    print("🛑 Servers on ports 8000, 8001, and 8002 have been terminated.")
