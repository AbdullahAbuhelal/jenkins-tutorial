pipeline {
    agent { docker { image 'python:3.12.7-alpine3.20' } }
    stages {
        stage('build') {
            steps {
                echo 'python --version'
                python main.py
            }
        }
    }
}