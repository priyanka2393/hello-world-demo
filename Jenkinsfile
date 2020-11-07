pipeline {
environment {
imagename = "priyankat23/flaskapp"
registryCredential = 'priyankat23'
dockerImage = ''
}
agent any
stages {
stage('Cloning Git') {
steps {
git([url: 'https://github.com/priyanka2393/hello-world-demo', branch: 'master'])
}
}
stage('Building image') {
steps{
script {
dockerImage = docker.build imagename
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
script {
bat "docker run -p 8000:8000 --name priyankat23/flaskapp -d priyankat23/flaskapp"
 }
}
}
}
}
