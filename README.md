# hello-world-demo
Dockerized hello-world python application on Jenkins pipeline

## Console Output
'''

Started by user Priyanka T. 
Obtained Jenkinsfile from git https://github.com/priyanka2393/hello-world-demo
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\Hello-world_pipeline
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git.exe rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/priyanka2393/hello-world-demo # timeout=10
Fetching upstream changes from https://github.com/priyanka2393/hello-world-demo
 > git.exe --version # timeout=10
 > git --version # 'git version 2.28.0.windows.1'
 > git.exe fetch --tags --force --progress -- https://github.com/priyanka2393/hello-world-demo +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
Checking out Revision 3c4d50f87c85ba6b40d6af424b4c2978d2fd74e6 (refs/remotes/origin/master)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f 3c4d50f87c85ba6b40d6af424b4c2978d2fd74e6 # timeout=10
Commit message: "Update Jenkinsfile"
 > git.exe rev-list --no-walk 94831876e0a0e8b8809f38e32ca5797420d398e0 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Cloning Git)
[Pipeline] git
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git.exe rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/priyanka2393/hello-world-demo # timeout=10
Fetching upstream changes from https://github.com/priyanka2393/hello-world-demo
 > git.exe --version # timeout=10
 > git --version # 'git version 2.28.0.windows.1'
 > git.exe fetch --tags --force --progress -- https://github.com/priyanka2393/hello-world-demo +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
Checking out Revision 3c4d50f87c85ba6b40d6af424b4c2978d2fd74e6 (refs/remotes/origin/master)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f 3c4d50f87c85ba6b40d6af424b4c2978d2fd74e6 # timeout=10
 > git.exe branch -a -v --no-abbrev # timeout=10
 > git.exe branch -D master # timeout=10
 > git.exe checkout -b master 3c4d50f87c85ba6b40d6af424b4c2978d2fd74e6 # timeout=10
Commit message: "Update Jenkinsfile"
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Building image)
[Pipeline] script
[Pipeline] {
[Pipeline] isUnix
[Pipeline] bat

C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\Hello-world_pipeline>docker build -t priyankat23/flaskapp . 
#1 [internal] load .dockerignore
#1 transferring context: 2B 0.0s done
#1 DONE 0.1s

#2 [internal] load build definition from Dockerfile
#2 transferring dockerfile: 32B done
#2 DONE 0.1s

#3 [internal] load metadata for docker.io/library/python:3.6
#3 DONE 0.4s

#4 [1/4] FROM docker.io/library/python:3.6@sha256:62ada7d65aa310020e5278a99...
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 22.40kB 0.2s done
#5 DONE 0.2s

#4 [1/4] FROM docker.io/library/python:3.6@sha256:62ada7d65aa310020e5278a99...
#4 CACHED

#6 [2/4] COPY .  /Hello_world
#6 DONE 0.2s

#7 [3/4] WORKDIR /Hello_world
#7 DONE 0.1s

#8 [4/4] RUN pip install -r requirements.txt
#8 2.411 Collecting Flask==1.1.2
#8 2.498   Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
#8 2.679 Collecting Jinja2>=2.10.1
#8 2.697   Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
#8 2.850 Collecting click>=5.1
#8 2.866   Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
#8 2.970 Collecting itsdangerous>=0.24
#8 2.988   Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
#8 3.112 Collecting Werkzeug>=0.15
#8 3.131   Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
#8 3.349 Collecting MarkupSafe>=0.23
#8 3.382   Downloading MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl (27 kB)
#8 3.534 Installing collected packages: MarkupSafe, Jinja2, click, itsdangerous, Werkzeug, Flask
#8 4.098 Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0
#8 DONE 4.6s

#9 exporting to image
#9 exporting layers
#9 exporting layers 0.3s done
#9 writing image sha256:04fd117f29cc2025c207f8b1d8fc20ebcca8f14002569fdb61db15cecc682ac9 done
#9 naming to docker.io/priyankat23/flaskapp done
#9 DONE 0.3s
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Deploy Image)
[Pipeline] script
[Pipeline] {
[Pipeline] withEnv
[Pipeline] {
[Pipeline] withDockerRegistry
$ docker login -u priyankat23 -p ******** https://index.docker.io/v1/
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
Login Succeeded
[Pipeline] {
[Pipeline] isUnix
[Pipeline] bat

C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\Hello-world_pipeline>docker tag priyankat23/flaskapp priyankat23/flaskapp:33 
[Pipeline] isUnix
[Pipeline] bat

C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\Hello-world_pipeline>docker push priyankat23/flaskapp:33 
The push refers to repository [docker.io/priyankat23/flaskapp]
13d17c7f371f: Preparing
5f70bf18a086: Preparing
7654bb7855a4: Preparing
00b1a6ab6acd: Preparing
28c41b4dd660: Preparing
36957997ca7a: Preparing
5c4d527d6b3a: Preparing
a933681cf349: Preparing
f49d20b92dc8: Preparing
fe342cfe5c83: Preparing
630e4f1da707: Preparing
9780f6d83e45: Preparing
36957997ca7a: Waiting
5c4d527d6b3a: Waiting
a933681cf349: Waiting
f49d20b92dc8: Waiting
fe342cfe5c83: Waiting
630e4f1da707: Waiting
9780f6d83e45: Waiting
5f70bf18a086: Layer already exists
28c41b4dd660: Layer already exists
00b1a6ab6acd: Layer already exists
36957997ca7a: Layer already exists
a933681cf349: Layer already exists
5c4d527d6b3a: Layer already exists
f49d20b92dc8: Layer already exists
fe342cfe5c83: Layer already exists
630e4f1da707: Layer already exists
9780f6d83e45: Layer already exists
7654bb7855a4: Pushed
13d17c7f371f: Pushed
33: digest: sha256:93953db29eec5b3e9ab24178a40f0960a2226665742aedd33ee9492020bdffe8 size: 2843
[Pipeline] isUnix
[Pipeline] bat

C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\Hello-world_pipeline>docker tag priyankat23/flaskapp priyankat23/flaskapp:latest 
[Pipeline] isUnix
[Pipeline] bat

C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\Hello-world_pipeline>docker push priyankat23/flaskapp:latest 
The push refers to repository [docker.io/priyankat23/flaskapp]
13d17c7f371f: Preparing
5f70bf18a086: Preparing
7654bb7855a4: Preparing
00b1a6ab6acd: Preparing
28c41b4dd660: Preparing
36957997ca7a: Preparing
5c4d527d6b3a: Preparing
a933681cf349: Preparing
5c4d527d6b3a: Waiting
36957997ca7a: Waiting
a933681cf349: Waiting
f49d20b92dc8: Preparing
fe342cfe5c83: Preparing
630e4f1da707: Preparing
9780f6d83e45: Preparing
f49d20b92dc8: Waiting
fe342cfe5c83: Waiting
9780f6d83e45: Waiting
7654bb7855a4: Layer already exists
5f70bf18a086: Layer already exists
13d17c7f371f: Layer already exists
00b1a6ab6acd: Layer already exists
28c41b4dd660: Layer already exists
a933681cf349: Layer already exists
36957997ca7a: Layer already exists
fe342cfe5c83: Layer already exists
5c4d527d6b3a: Layer already exists
f49d20b92dc8: Layer already exists
630e4f1da707: Layer already exists
9780f6d83e45: Layer already exists
latest: digest: sha256:93953db29eec5b3e9ab24178a40f0960a2226665742aedd33ee9492020bdffe8 size: 2843
[Pipeline] }
[Pipeline] // withDockerRegistry
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Remove Unused docker image)
[Pipeline] script
[Pipeline] {
[Pipeline] bat

C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\Hello-world_pipeline>docker run -p 8000:8000 --name flaskapp -d priyankat23/flaskapp 
b4041b24fb109b083e77dcf49e35bd51699da66539278e13ad9cbfd1e58b0c04
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
'''
