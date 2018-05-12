pipeline {
    agent label:'pt-lt0104'
    stages {
        stage ('Delete old file')
        {
            steps {
                bat '''
                del /q "c:\\logs\\jenkins\\*.csv"
                del /q "c:\\logs\\jenkins\\*.html"
                del /q "c:\\logs\\jenkins\\*Finish*"
                del /q "c:\\logs\\jenkins\\*.xml"
                '''
                }
        }

        stage ('Kill Old GRAS')
        {
	steps{
            bat '''
		tasklist /FI "IMAGENAME eq GRAS.exe" 2>NUL | find /I /N "GRAS.exe">NUL
		if "%ERRORLEVEL%"=="0" echo Programm is running	 | taskkill /f /im GRAS.exe	


		'''
	    }
        }

        stage ('Run GRAS')
        {
		 steps {
        	    bat '''
			cd "c:\\Program Files (x86)\\Marvell\\GRAS"
		        GRAS.exe "C:\\work\\TestCI.xml" -s -jo "c:\\logs\\jenkins" -jv cisco_tesla_bx_v2.3 -dp
			'''
		}
        }
    }
}
