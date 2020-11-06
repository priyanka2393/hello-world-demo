#!groovy
pipeline {
    agent {label 'docker-jnlp'}
    stages {
        stage('Get Source') {
          // copy source code from local file system and test
         // for a Dockerfile to build the Docker image
            steps{
               sh'''
               git ('https://github.com/priyanka2393/hello-world-demo.git')
               if (!fileExists("Dockerfile")) {
               error('Dockerfile missing.')
               }
               '''
         
       }
    }
       stage('Build Docker') {
         // build the docker image from the source code using the BUILD_ID parameter in image name
           steps{
               sh "docker build -t flask-app ."
      }
   }
       stage("run docker container"){
           steps{
             sh "docker run -p 8000:8000 --name flask-app -d flask-app "
           }
       }
    }
}
