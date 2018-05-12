// lien vers git en https
final	String	GIT_LINK 		=	'https://github.com/franck-cussac/myapp'

// nom de la branche à récupérer
final	String	BRANCH_NAME 		= 	'master'

// nom du dossier dans le repository dans lequel se trouve le projet
final	String	DIRECTORY 		= 	'myapp'

// nom du job ansible
final	String	ANSIBLE_JOB_NAME	= 	''


stage ("\u2600 Checkout Sources")
        {
                node('master')
                {
                        git branch: BRANCH_NAME, url: GIT_LINK
                }
        }

stage ("\u2600 Build/Compile")
        {
                node('master')
                {
                        dir(DIRECTORY)
                        {
                                sh "echo $PATH"
                                sh "cocos compile -p android"
                        }
                        stash name: 'source'
                }
        }

stage ("\u2600 Run Technical Tests (Unit Tests)")
        {
            
        }

stage ("\u2600 Archive/Install Artifacts (Nexus)")
        {
            
        }
stage ("\u2600 Deployment to Dev Env")
        {
                
        }
