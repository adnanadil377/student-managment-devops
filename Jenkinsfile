pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'adnan23bcs35'
        ROLL_NUMBER = '2023bcs0035'
        FRONTEND_IMAGE = "${DOCKER_HUB_USERNAME}/${ROLL_NUMBER}_frontend"
        BACKEND_IMAGE = "${DOCKER_HUB_USERNAME}/${ROLL_NUMBER}_backend"
        DOCKER_HUB_REGISTRY = 'https://registry.hub.docker.com'
        DOCKER_CREDENTIALS_ID = 'dockerhub-token'
        GIT_COMMIT_TAG = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo '========== Checking out source code from GitHub =========='
                    checkout scm
                    echo "Repository checked out successfully"
                    echo "Commit: ${GIT_COMMIT_TAG}"
                }
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                script {
                    echo '========== Building Backend Docker Image =========='
                    sh '''
                        cd backend
                        docker build -t ${BACKEND_IMAGE}:latest -t ${BACKEND_IMAGE}:${GIT_COMMIT_TAG} .
                        echo "Backend image built: ${BACKEND_IMAGE}:latest"
                        echo "Backend image tagged: ${BACKEND_IMAGE}:${GIT_COMMIT_TAG}"
                    '''
                }
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                script {
                    echo '========== Building Frontend Docker Image =========='
                    sh '''
                        cd frontend
                        docker build -t ${FRONTEND_IMAGE}:latest -t ${FRONTEND_IMAGE}:${GIT_COMMIT_TAG} .
                        echo "Frontend image built: ${FRONTEND_IMAGE}:latest"
                        echo "Frontend image tagged: ${FRONTEND_IMAGE}:${GIT_COMMIT_TAG}"
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo '========== Pushing Docker Images to Docker Hub =========='
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin
                            
                            echo "Pushing Backend Image..."
                            docker push ${BACKEND_IMAGE}:latest
                            docker push ${BACKEND_IMAGE}:${GIT_COMMIT_TAG}
                            echo "Backend images pushed successfully"
                            
                            echo "Pushing Frontend Image..."
                            docker push ${FRONTEND_IMAGE}:latest
                            docker push ${FRONTEND_IMAGE}:${GIT_COMMIT_TAG}
                            echo "Frontend images pushed successfully"
                            
                            docker logout
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo '========== Pipeline Completed Successfully =========='
            echo "Frontend Image: ${FRONTEND_IMAGE}:latest"
            echo "Backend Image: ${BACKEND_IMAGE}:latest"
        }
        failure {
            echo '========== Pipeline Failed =========='
            echo "Build failed. Please check logs above."
        }
        always {
            cleanWs()
        }
    }
}
