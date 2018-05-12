node {//运行节点
    stage('SCM') {//运行阶段
    //从github上拉取代码
        git 'https://github.com/graduationTongbao/tongbao.git'
    }
    stage('build') {
    //用Maven来打包
        def mvnHome = tool 'M3'//之前配置的Maven工具
        sh "${mvnHome}/bin/mvn -B clean package"//maven的清理和打包
    }
    stage('deploy') {
        sh "mv target/tongbao.war /usr/local/tomcat/apache-tomcat-9.0.0.M15/webapps"
    }
}
