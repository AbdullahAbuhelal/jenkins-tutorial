pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install -r requirements.txt
                '''
            }
        }
        stage('Testing') {
            steps {
                echo "Testing.."
                sh '''
                cd jenkins_django
                python3 -m pytest --junitxml=reports/results.xml
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
    post {
        always {
            junit '/home/jenkins/workspace/my_first_pipeline/jenkins_django/reports/results.xml'
        }
    }
}
