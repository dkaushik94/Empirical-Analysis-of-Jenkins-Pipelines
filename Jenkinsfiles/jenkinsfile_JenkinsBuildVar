pipeline {
	agent {
		node {
			label 'windows'
			customWorkspace "C:/work/${BRANCH_NAME}"
		}
	}
	options { timestamps() }

	environment{
		MAJOR_VERSION = 1
		MINOR_VERSION = 0
		HOTFIX_VERSION = 0
		VERSION_PREFIX = "${MAJOR_VERSION}.${MINOR_VERSION}.${HOTFIX_VERSION}"
		VERSION_SHA = "sha${ GIT_COMMIT.substring(0,7).toUpperCase() }"
		BUILD_NUMBER = "${env.VER_TRAAS}"
		DISPLAY_VERSION = VersionNumber( versionNumberString: "-b${BUILD_NUMBER}${VERSION_SHA}" , versionPrefix: "${VERSION_PREFIX}", worstResultForIncrement: 'NOT_BUILT' )
		PACKAGE_VERSION = VersionNumber( versionNumberString: "${BUILD_NUMBER}" , versionPrefix: "${VERSION_PREFIX}", worstResultForIncrement: 'NOT_BUILT' )
	}

	stages {
		stage('Prepare') {
			steps {
				script {
					instance = Jenkins.getInstance()
					globalNodeProperties = instance.getGlobalNodeProperties()
					envVarsNodePropertyList = globalNodeProperties.getAll(hudson.slaves.EnvironmentVariablesNodeProperty.class)
					envVars = null
					envVars = envVarsNodePropertyList.get(0).getEnvVars()
					envVars.put("VER_TRAAS", env.VER_TRAAS + 1 )
					instance.save()

					currentBuild.displayName = "${DISPLAY_VERSION}"
				}
                echo "Commit: ${GIT_COMMIT}"
				echo "SHA Substring: ${VERSION_SHA}"
			}
		}
		stage('Build') {
			parallel {
				stage('Build 1') {
					steps {
                        echo "${PACKAGE_VERSION}"
					}
				}
				stage('Build 2') {
					steps {
                        echo "${PACKAGE_VERSION}"
                    }
				}
			}
		}
	}
}