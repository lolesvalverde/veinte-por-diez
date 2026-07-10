pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: jenkins-agent
spec:
  containers:
    - name: python
      image: python:3.11-slim
      command: ['cat']
      tty: true
    - name: docker
      image: docker:latest
      command: ['cat']
      tty: true
      env:
        - name: DOCKER_HOST
          value: tcp://localhost:2375
    - name: dind
      image: docker:dind
      securityContext:
        privileged: true
      env:
        - name: DOCKER_TLS_CERTDIR
          value: ""
'''
        }
    }

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
                container('python') {
                    echo 'Setting up Python virtual environment and running tests...'
                    sh '''
                        python3 -m venv backend/.venv
                        backend/.venv/bin/pip install -r backend/requirements.txt
                        # Run backend tests
                        backend/.venv/bin/pytest backend/
                    '''
                }
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
                container('docker') {
                    echo 'Building backend Docker image using DinD sidecar...'
                    // Build context is root of the repository to allow backend/Dockerfile to access frontend/
                    sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest -f backend/Dockerfile .'
                }
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
                container('docker') {
                    echo 'Inspecting built container image...'
                    sh 'docker inspect ${IMAGE_NAME}:${IMAGE_TAG}'
                    sh 'docker push lvalverderodriguez/${IMAGE_NAME}:${IMAGE_TAG}'
                }
            }
        }

        stage('Register Artifact in CloudBees Unify') {
            when {
                anyOf {
                    changeset "backend/**"
                    changeset "Jenkinsfile"
                    branch "main"
                }
            }
            steps {
                echo 'Registering build artifact in CloudBees Unify...'
                registerBuildArtifactMetadata(
                    name: 'veinte-por-diez-backend',
                    version: "${IMAGE_TAG}",
                    // Required parameter pointing to where the built artifact resides
                    url: 'https://hub.docker.com/repository/docker/lvalverderodriguez/${IMAGE_NAME}'
                )
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
