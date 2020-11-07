pipeline {
environment {
//imagename = "yenigul/hacicenkins"
registryCredential = '2393'
dockerImage = ''
}
agent any
stages {
stage('Cloning Git') {
steps {
git ( 'https://github.com/priyanka2393/hello-world-demo.git)
}
}
stage('Building image') {
steps{
script {
sh "docker build -t flask-app ."
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
