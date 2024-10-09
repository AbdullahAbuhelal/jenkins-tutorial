pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers{
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test'){
            steps{
                script{
                    sh 'cd jenkins_django'
                    sh '''
                    python3 venv venv
                    source venv/bin/activate
                    '''
                    sh 'pip install pytest==7.4.2'
                    sh 'pytest'
                }
            }
       }
        stage('Start app') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Abdullah
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
}
