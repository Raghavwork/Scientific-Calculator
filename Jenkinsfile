pipeline {
    agent any

    environment {
        IMAGE_NAME = "raghav2805/scientific_calculator"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'master',
                url: 'https://github.com/Raghavwork/Scientific-Calculator.git'
            }
        }

        stage('Install Dependencies') {
    	    steps {
        sh '''
        python3 -m venv venv
        . venv/bin/activate
        pip install pyinstaller
        '''
    }
}

stage('Build Executable') {
    steps {
        sh '''
        . venv/bin/activate
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

        stage('Login & Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh '''
                ansible-playbook ansible/deploy.yml -i ansible/inventory.ini
                '''
            }
        }
    }

    post {
        success {
            mail to: 'raghavgoyal492.2805@gmail.com',
                 subject: 'Jenkins Build Success',
                 body: 'Scientific Calculator pipeline executed successfully.'
        }

        failure {
            mail to: 'raghavgoyal492.2805@gmail.com',
                 subject: 'Jenkins Build Failed',
                 body: 'Check Jenkins console output.'
        }
    }
}
