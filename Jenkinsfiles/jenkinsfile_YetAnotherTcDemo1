node {
	stage 'Checkout'
		checkout scm

	stage 'Build'
		bat 'nuget restore src\YetAnotherTcDemo1\YetAnotherTcDemo1.sln'
		bat "\"${tool 'MSBuild'}\" src\YetAnotherTcDemo1\YetAnotherTcDemo1.sln /p:Configuration=Release /p:Platform=\"Any CPU\" /p:ProductVersion=1.0.0.${env.BUILD_NUMBER}"

	stage 'Archive'
		archive 'src/YetAnotherTcDemo1/YetAnotherTcDemo1/bin/Release/**'

}