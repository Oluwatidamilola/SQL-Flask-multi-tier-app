# SQL-Flask-multi-tier-app

SQL-Flask Multi-Tier Application with CI/CD and Snyk Integration
This project is a multi-tier Flask web application that integrates seamlessly with a PostgreSQL database, is containerized using Docker, and is orchestrated with Kubernetes. It incorporates CI/CD pipelines and Snyk security scanning for robust, secure, and automated application deployment.

Features
RESTful Flask API: Implements core application logic and database interactions.
PostgreSQL Integration: Uses SQLAlchemy for ORM-based database operations.
Containerized Deployment: Built with Docker for portability and reproducibility.
Kubernetes Ready: Includes YAML manifests for deploying, scaling, and exposing the app.
NGINX Ingress Controller: Configured for external access to the application.
Snyk Security Scanning: Integrated dependency, Docker image, and Kubernetes configuration scans to ensure application security.

CI/CD Automation: Uses GitHub Actions for automated builds, tests, scans, and deployments.


Project Structure

`SQL-Flask-multi-tier-app/
├── app.py                          # Main Flask application entry point
├── wsgi.py                         # WSGI entry point for production servers like Gunicorn
├── models.py                       # SQLAlchemy models for database schema
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker image definition
├── flask-app-deployment.yaml       # Kubernetes deployment manifest
├── flask-app-service.yaml          # Kubernetes service manifest
├── flask-app-ingress.yaml          # Kubernetes ingress manifest
├── db-secrets.yaml                 # Kubernetes secrets for database credentials
├── sealed-db-secrets.yaml          # Encrypted secrets for secure Kubernetes storage
├── postgres-exporter.yaml          # Deployment for Prometheus Postgres Exporter
├── encryption-config.yaml          # Encryption configuration for Kubernetes secrets
└── .github/workflows/ci-cd.yml     # GitHub Actions workflow for CI/CD`

Prerequisites
Ensure the following are installed on your system:

Python 3.9+
PostgreSQL 13+
Docker
Kubernetes (with kubectl configured and nginx-ingress installed)
Snyk CLI (for security scanning)
Setup
1. Clone the Repository

git clone https://github.com/your-username/sql-flask-multi-tier-app.git
cd sql-flask-multi-tier-app
2. Create a Virtual Environment

python -m venv .venv
source .venv/bin/activate
3. Install Dependencies

pip install -r requirements.txt
4. Configure the Database
Set up a PostgreSQL instance and update the DATABASE_URL in db-secrets.yaml or config.py:

DATABASE_URL: "postgresql://<username>:<password>@<host>:<port>/<database>"
5. Run the Application Locally
Start the Flask development server:

flask run
Access the application at http://127.0.0.1:5000.

Using Docker
Build the Docker Image

docker build -t dgurutester/flask-app:latest .
Run the Container

docker run -d -p 5000:5000 dgurutester/flask-app:latest
Access the application at http://localhost:5000.

Deploying to Kubernetes
1. Apply Secrets
Ensure the database credentials are securely stored using Kubernetes secrets:
kubectl apply -f db-secrets.yaml

2. Deploy the Application
Deploy the Flask app, service, and ingress:
kubectl apply -f flask-app-deployment.yaml
kubectl apply -f flask-app-service.yaml
kubectl apply -f flask-app-ingress.yaml

3. Verify the Deployment
Check if all pods are running:
kubectl get pods

4. Access the Application
Update your /etc/hosts file to include:
<ingress_external_ip> flask-app.local
Access the application at http://flask-app.local.

Monitoring with Prometheus
Deploy the PostgreSQL Exporter:

kubectl apply -f postgres-exporter.yaml
Access Prometheus metrics at:

http://<external-ip>:9187/metrics
CI/CD Automation with GitHub Actions
The CI/CD pipeline is defined in .github/workflows/ci-cd.yml. It automates:

Code Checkout and Python Setup:
Ensures the repository is cloned and Python 3.9 is configured.
Dependency Installation and Testing:
Installs dependencies and runs tests using pytest.
Security Scanning with Snyk:
Scans Python dependencies, Docker images, and Kubernetes manifests for vulnerabilities.
Docker Image Build and Push:
Builds the Docker image and pushes it to Docker Hub.
Kubernetes Deployment:
Deploys the application to a Kubernetes cluster.
Triggering the Pipeline
The pipeline runs on:

Push events to the main branch.
Pull requests targeting the main branch.
Secrets Configuration
Add the following secrets to your GitHub repository:

SNYK_TOKEN: API token for Snyk authentication.
DOCKER_USER: Docker Hub username.
DOCKER_PASS: Docker Hub password.
KUBECONFIG: Kubernetes configuration file content.
Security with Snyk
Dependency Scanning
The pipeline includes:


snyk test --file=requirements.txt --package-manager=pip
This scans Python dependencies for known vulnerabilities.

Docker Image Scanning
The pipeline also scans Docker images:

snyk container test dgurutester/flask-app:latest
Kubernetes Configuration Scanning
Snyk ensures Kubernetes manifests are secure:

snyk iac test flask-app-deployment.yaml
Environment Variables
The app supports the following environment variables:

DATABASE_URL: PostgreSQL database connection string.
FLASK_ENV: Set to production or development.
SECRET_KEY: Secret key for Flask session management.
Contributing
We welcome contributions to this project. To contribute:

Fork the repository.
Create a feature branch:

git checkout -b feature/new-feature
Commit changes:

git commit -m "Add new feature"
Push to your fork:

git push origin feature/new-feature
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Flask for the web framework.
PostgreSQL for the database.
Docker and Kubernetes for containerization and orchestration.
Snyk for security scanning.
Prometheus and nginx-ingress for monitoring and traffic management.
This README.md provides a comprehensive guide to setting up, deploying, and maintaining the project, including its CI/CD and security workflows with Snyk. Let me know if you need further clarifications or adjustments!
