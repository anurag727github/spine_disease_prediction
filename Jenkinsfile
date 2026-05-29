pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\ANURAG\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat '"%PYTHON%" train.py'
            }
        }

        stage('Verify Model') {
            steps {
                bat 'dir models'
            }
        }
    }
}