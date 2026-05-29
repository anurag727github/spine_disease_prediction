pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Verify Model') {
            steps {
                bat 'dir models'
            }
        }
    }
}