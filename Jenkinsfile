pipeline {
    environment {
    }
    agent {
        kubernetes {
            // Define the pod template
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: python-build-pod
spec:
  containers:
  - name: python
    image: "739457818465.dkr.ecr.us-east-2.amazonaws.com/python:3.12.3-alpine3.19"
    command:
    - cat
    tty: true
"""
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                container("python"){
                    sh 'apk add git'
                    sh 'python3 -m pip install -r test_requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                container("python"){
                    sh 'python3 -m unittest discover tests'
                }
            }
        }
    }

    post {
        always {
            sendNotificationsToCloudAEye true
        }
    }
}





