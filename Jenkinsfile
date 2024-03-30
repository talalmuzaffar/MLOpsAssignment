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
    
    post {
        success {
            // Send email notification when the pipeline succeeds
            emailext (
                subject: 'Jenkins Pipeline Succeeded',
                body: 'The Jenkins pipeline has succeeded. Code was pushed/merged into the master branch.',
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                replyTo: '',
                to: 'malikfaizan9066@gmail.com'
            )
        }
        failure {
            // Send email notification when the pipeline fails
            emailext (
                subject: 'Jenkins Pipeline Failed',
                body: 'The Jenkins pipeline has failed. Code was pushed/merged into the master branch.',
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                replyTo: '',
                to: 'malikfaizan9066@gmail.com'
            )
        }
    }
}
