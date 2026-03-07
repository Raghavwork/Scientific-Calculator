pipeline {
    agent any

    environment {
        IMAGE_NAME = "raghav2805/scientific_calculator"
    }

    triggers {
        pollSCM('H/1 * * * *')
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/raghav2805/Scientific_calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install pyinstaller
                '''
            }
        }

        stage('Build Executable') {
            steps {
                sh '''
                pyinstaller --onefile calculator.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                 usernameVariable: 'USERNAME',
                                 passwordVariable: 'PASSWORD')]) {

                    sh '''
                    echo $PASSWORD | docker login -u $USERNAME --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }
    }
}
