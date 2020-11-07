pipeline {
environment {
registryCredential = '2393'
dockerImage = ''
}
agent any
stages {
stage('Cloning Git') {
steps {
git([url: 'https://github.com/priyanka2393/hello-world-demo.git', branch: 'master'])
}
}
stage('Building image') {
steps{
script {
dockerImage = docker build -t flask-app .
}
}
}
stage('Deploy Image') {
steps{
script {
docker.withRegistry( '', registryCredential ) {
dockerImage.push("$BUILD_NUMBER")
dockerImage.push('latest')
}
}
}
}
stage('Remove Unused docker image') {
steps{
sh "docker rmi $imagename:$BUILD_NUMBER"
sh "docker rmi $imagename:latest"
}
}
}
}
