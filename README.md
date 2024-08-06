# FastAPI Application with MongoDB and PostgreSQL

This README provides a step-by-step guide to set up MongoDB, PostgreSQL, and integrate your FastAPI application with RapidAPI.

### The main components of this project are:

- app/routers/items.py: Contains the API routes for item management
- app/database.py: Handles database connections (SQLAlchemy and MongoDB)
- app/models.py: Defines the SQLAlchemy models


### Install dependencies:
pip install -r requirements.txt -U


## Prerequisites

- Homebrew installed on macOS
- Python 3.8+ installed
- Virtual environment (venv) setup
- FastAPI and Uvicorn installed
- Setup MongoDB

### Install MongoDB

```bash
brew tap mongodb/brew
brew install mongodb-community@5.0
```

### Start MongoDB Service

```bash
brew services start mongodb/brew/mongodb-community
```

### Add MongoDB to PATH

```bash
export PATH="/opt/homebrew/opt/mongodb-community@5.0/bin:$PATH"
```

### Reload the shell configuration:

```bash
source ~/.zshrc
```

### Create Admin User in MongoDB

```bash
mongosh
```

Connect to MongoDB:

```bash
mongosh
```

Switch to the admin database and create an admin user:

```javascript
use admin
db.createUser({
user: "admin",
pwd: "password",
roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
})
```

Enable authentication by editing the mongod.conf file:

```yaml
security:
authorization: "enabled"
```

### Restart MongoDB service:

```bash
brew services restart mongodb/brew/mongodb-community
```

### Connect to MongoDB with authentication:

```bash
mongosh -u "admin" -p "password" --authenticationDatabase "admin"
```

### Create Database and Collection in MongoDB
Switch to the desired database and create a collection:

```javascript
use rag_db
db.createCollection("items")
```

### Import data from a CSV file:

```bash
mongoimport --db rag_db --collection items --type csv --headerline --file /Users/pravinjayasinghe/president_state.csv --username admin --password password --authenticationDatabase admin
```

## Setup PostgreSQL

### Install PostgreSQL

```bash
brew install postgresql
```

### Start PostgreSQL Service

```bash
brew services start postgresql
```

### Create Database and User

```bash
psql postgres
```

```bash
psql postgres
```

### Create a new database and user:

```sql
CREATE DATABASE rag_db;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE rag_db TO myuser;
```

## Running the FastAPI Application

### Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start FastAPI Application
```bash
bash run.sh
```

