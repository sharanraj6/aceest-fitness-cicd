# ACEest Fitness & Gym - DevOps Pipeline

This repository contains the foundational Flask web application and automated CI/CD pipeline configurations for the ACEest Fitness & Gym platform. This project demonstrates proficiency in Version Control, Containerization (Docker), and CI/CD orchestration using GitHub Actions and Jenkins.

---

## 1. Local Setup and Execution Instructions

To run this application locally on your machine (macOS, Linux, or Windows), follow these steps:

### Prerequisites
* Python 3.9+ installed
* Git installed
* Docker Desktop installed and running

### Setup Steps
1. **Clone the repository:**
   <pre>
   git clone https://github.com/sharanraj6/aceest-fitness-cicd.git
   cd aceest-devops-assignment
   </pre>
3. **Create and Activate a Virtual Environment:**
   <pre>
   On macOS/Linux: 
        python3 -m venv venv 
        source venv/bin/activate 
   On Windows:
        python -m venv venv
        venv\Scripts\activate
   </pre>

5. **Install Dependencies:**
   <pre>
   pip install -r requirements.txt
   </pre>
7. **Run the Flask Application:**
   <pre>
   python app.py
   </pre>

## The application will now be accessible in your web browser at: http://localhost:5000

## 2. Manual Testing Instructions

To manually validate the application's internal logic and container health before pushing code, use the following commands:

### A. Run Unit Tests (Local)
Ensure your virtual environment is active and dependencies are installed, then run the Pytest suite:
    pytest test_app.py -v
You should see a report indicating that all test cases have passed successfully.

### B. Run Docker Container Testing (Local)
To verify that the application works inside its containerized environment ("write once, run anywhere"):

   1. **Build the Docker image:**
    docker build -t aceest-flask-app:latest .

   2. **Run the tests inside the container:**
    docker run aceest-flask-app:latest pytest test_app.py

   3. **(Optional) Run the app via Docker:**
    docker run -p 5000:5000 aceest-flask-app:latest

## 3. CI/CD Pipeline & Integration Logic

This project utilizes a dual-layered CI/CD approach leveraging both GitHub Actions and Jenkins to ensure code integrity, environmental consistency, and rapid delivery.

### Phase 1: Continuous Integration via GitHub Actions
The ".github/workflows/main.yml" file dictates the automated pipeline. Upon every push or pull_request to the main branch, a GitHub-hosted runner automatically executes the following:

    1.Build & Lint: Checks out the code, sets up Python, installs dependencies, and checks app.py for syntax and styling errors using Flake8.

    2.Docker Image Assembly: Triggers a docker build using the provided Dockerfile, confirming the application can be successfully containerized.

    3.Automated Container Testing: Runs the Pytest suite inside the newly built Docker container to guarantee environment stability.

### Phase 2: Secondary BUILD & Quality Gate via Jenkins
A Jenkins server is integrated to handle the primary BUILD phase, acting as a secondary validation layer for controlled environments.

    1. Integration: Jenkins is linked to this GitHub repository via the Git plugin.

    2. Trigger: Configured with "Poll SCM" (or GitHub Webhooks) to detect new commits.

    3. Execution Strategy: Jenkins pulls the latest source code and executes a clean build environment shell script:
        pip install -r requirements.txt
        pytest test_app.py
        docker build -t aceest-flask-app:latest

    4. Outcome: If the code compiles, passes tests, and builds into a Docker image successfully, the Jenkins BUILD is marked as passing, ensuring the artifact is ready for the deployment stage.

## 4. Sample Jenkins Screenshot (Running Locally)
   <img width="750" height="750" alt="Screenshot 2026-04-03 at 17 52 17" src="https://github.com/user-attachments/assets/9e90f58e-7530-4c9e-b84a-dbcb4505155e" />

## 5. The ACEest Functional Fitness System Web UI Screenshot
   <img width="750" height="750" alt="Screenshot 2026-04-03 at 17 53 20" src="https://github.com/user-attachments/assets/2769d5a3-f738-428e-ac20-557f3999bc98" />


