 pipeline {
        agent any
        stages{
        stage("Docker build") {
            steps {
             sh "docker build -t zwidny/zblog ."
            }
        }
        stage("Docker push") {
            steps {
             sh "docker push zwidny/zblog"
            }
        }
        stage("Deploy to staging") {
            steps {
                sh "docker run -d -v /tmp:/tmp -v /home/zwidny/repos/zblog/src:/repos/zblogs/src -e CONF_DIR='zblog' -e SECRET_KEY='9ve^pp)#y2zazn(1t-6^wlp*9*!gqm5w13=w4+$nl)cn0&f(0+' --name zblog zwidny/zblog"
            }
        }
 }
}
