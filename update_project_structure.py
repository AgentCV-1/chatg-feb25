import os
import shutil

# Define paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")
INFRA_DIR = os.path.join(ROOT_DIR, "infra")

# 1️⃣ DELETE UNNECESSARY `database/` FOLDER (if exists)
DATABASE_DIR = os.path.join(ROOT_DIR, "database")
if os.path.exists(DATABASE_DIR):
    print(f"Deleting {DATABASE_DIR}...")
    shutil.rmtree(DATABASE_DIR)

# 2️⃣ RENAME `services/` → `controllers/`
SERVICES_DIR = os.path.join(BACKEND_DIR, "services")
CONTROLLERS_DIR = os.path.join(BACKEND_DIR, "controllers")
if os.path.exists(SERVICES_DIR):
    print(f"Renaming {SERVICES_DIR} → {CONTROLLERS_DIR}...")
    os.rename(SERVICES_DIR, CONTROLLERS_DIR)

# 3️⃣ RENAME `core/` → `settings/`
CORE_DIR = os.path.join(BACKEND_DIR, "core")
SETTINGS_DIR = os.path.join(BACKEND_DIR, "settings")
if os.path.exists(CORE_DIR):
    print(f"Renaming {CORE_DIR} → {SETTINGS_DIR}...")
    os.rename(CORE_DIR, SETTINGS_DIR)

# 4️⃣ MOVE `config.py` FROM `core/` TO `settings/`
OLD_CONFIG_PATH = os.path.join(CORE_DIR, "config.py")
NEW_CONFIG_PATH = os.path.join(SETTINGS_DIR, "config.py")
if os.path.exists(OLD_CONFIG_PATH):
    print(f"Moving {OLD_CONFIG_PATH} → {NEW_CONFIG_PATH}...")
    shutil.move(OLD_CONFIG_PATH, NEW_CONFIG_PATH)

# 5️⃣ RENAME `infra/cloud-configs/` → `infra/deployments/`
OLD_DEPLOYMENTS_DIR = os.path.join(INFRA_DIR, "cloud-configs")
NEW_DEPLOYMENTS_DIR = os.path.join(INFRA_DIR, "deployments")
if os.path.exists(OLD_DEPLOYMENTS_DIR):
    print(f"Renaming {OLD_DEPLOYMENTS_DIR} → {NEW_DEPLOYMENTS_DIR}...")
    os.rename(OLD_DEPLOYMENTS_DIR, NEW_DEPLOYMENTS_DIR)

# 6️⃣ CREATE MISSING DIRECTORIES
MISSING_DIRS = [
    os.path.join(BACKEND_DIR, "db", "models"),
    os.path.join(BACKEND_DIR, "middleware"),
    os.path.join(BACKEND_DIR, "tests"),
]
for directory in MISSING_DIRS:
    if not os.path.exists(directory):
        print(f"Creating directory {directory}...")
        os.makedirs(directory)

# 7️⃣ CHECK `docker-compose.yml` AND ADD MONGO SERVICE IF MISSING
DOCKER_COMPOSE_PATH = os.path.join(INFRA_DIR, "docker-compose.yml")

MONGO_SERVICE = """
  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
"""

if os.path.exists(DOCKER_COMPOSE_PATH):
    with open(DOCKER_COMPOSE_PATH, "r") as f:
        docker_compose_content = f.read()

    if "mongodb" not in docker_compose_content:
        print(f"Adding MongoDB service to {DOCKER_COMPOSE_PATH}...")
        with open(DOCKER_COMPOSE_PATH, "a") as f:
            f.write("\n" + MONGO_SERVICE)

print("\n✅ Project structure successfully updated!")
