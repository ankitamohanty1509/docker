pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ankitamohanty1509/flask1:latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url:'https://github.com/ankitamohanty1509/docker.git',branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }
}
