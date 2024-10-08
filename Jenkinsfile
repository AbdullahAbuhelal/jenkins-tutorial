pipeline {
    agent { docker { image 'python:3.12.7-alpine3.20' } }
    stages {
        stage('build') {
            environment {
                HOME="."
            }
            steps {
                sh 'python --version'
            }
        }
    }
}