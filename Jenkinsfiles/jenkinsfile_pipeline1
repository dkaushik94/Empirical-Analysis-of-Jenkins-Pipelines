node {
   
   	stage 'Etapa 1'
       echo 'Intentando mostrar JAVA_HOME'
       echo 'Note que estos valores están en comillas simples: JAVA_HOME ${env.JAVA_HOME}'   
       echo "Ahora en comillas dobles: JAVA_HOME es ${env.JAVA_HOME}"   
   	stage 'Checkout'
   		git url: 'https://github.com/ryepesg/pipeline1.git'
   	stage 'Build'
   		sh './build.sh'
   	stage 'Deploy'
   		sh './deployment.sh'
  
}
