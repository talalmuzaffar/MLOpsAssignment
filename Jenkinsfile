pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'a1_image'
        DOCKERFILE_PATH = 'D:/Sem7/MLOPS/assignment/MLOpsAssignment/DockerFile'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git branch: 'master', url: 'https://github.com/talalmuzaffar/MLOpsAssignment.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    bat 'docker build -t ${env.DOCKER_IMAGE} -f ${env.DOCKERFILE_PATH} .'
                }
            }
        }
    }

