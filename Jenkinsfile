pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'your_dockerhub_username'
        DOCKERHUB_PASS = credentials('dockerhub-pass')
        IMAGE = "${DOCKERHUB_USER}/simple-interest-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/simple-interest-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-pass') {
                        docker.image("${IMAGE}:${BUILD_NUMBER}").push()
                        docker.image("${IMAGE}:${BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
