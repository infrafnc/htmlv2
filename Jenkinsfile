pipeline {
  checkout scm
  environment {
    registry = "kaique5247/front"
    registryCredential = 'DockerHub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
            sh "kubectl set image deployment htmlv2 htmlv2=${dockerImage} --record"
        	sh "kubectl rollout status deployment/htmlv2"
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}
