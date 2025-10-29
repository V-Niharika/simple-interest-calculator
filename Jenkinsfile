pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'niharika345/simple-interest-app'
        DOCKER_USER  = 'niharika345'
        DOCKER_PASS  = 'Niharika@03'
    }

    stages {
        stage('Clone Repository') {
    steps {
        echo '📥 Cloning repository (main branch)...'
        git branch: 'main', url: 'https://github.com/sreenitha-1967/subscription-tracker1.git'
    }
}


        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                bat '''
                    docker build -t %DOCKER_IMAGE%:%BUILD_NUMBER% .
                '''
            }
        }

        stage('Login & Push to Docker Hub') {
            steps {
                echo '📤 Pushing image to Docker Hub...'
                bat '''
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker push %DOCKER_IMAGE%:%BUILD_NUMBER%
                    docker tag %DOCKER_IMAGE%:%BUILD_NUMBER% %DOCKER_IMAGE%:local
                    docker push %DOCKER_IMAGE%:local
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '🚀 Deploying to Kubernetes...'
                bat '''
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful! Visit your app using NodePort or LoadBalancer IP.'
        }
        failure {
            echo '❌ Build Failed! Check the Jenkins console output for details.'
        }
    }
}

