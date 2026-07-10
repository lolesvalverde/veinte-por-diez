pipeline {
    agent any

    environment {
        IMAGE_NAME = 'veinte-por-diez-backend'
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Detect Changes') {
            steps {
                echo 'Checking for backend changes...'
            }
        }

        stage('Backend Test') {
            when {
                anyOf {
                    changeset "backend/**"
                    changeset "Jenkinsfile"
                    branch "main"
                }
            }
            steps {
                echo 'Setting up Python virtual environment and running tests...'
                sh '''
                    python3 -m venv backend/.venv
                    backend/.venv/bin/pip install -r backend/requirements.txt
                    # Run backend tests
                    backend/.venv/bin/pytest backend/
                '''
            }
        }

        stage('Build Backend Docker Image') {
            when {
                anyOf {
                    changeset "backend/**"
                    changeset "Jenkinsfile"
                    branch "main"
                }
            }
            steps {
                echo 'Building backend Docker image...'
                // Build context is root of the repository to allow backend/Dockerfile to access frontend/
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest -f backend/Dockerfile .'
            }
        }

        stage('Inspect Image Artifact') {
            when {
                anyOf {
                    changeset "backend/**"
                    changeset "Jenkinsfile"
                    branch "main"
                }
            }
            steps {
                echo 'Inspecting built container image...'
                sh 'docker inspect ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
