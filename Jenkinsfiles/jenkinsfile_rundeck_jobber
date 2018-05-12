// Rundeck's CLI tool is installed in master
node('master') {

    stage(" =~ Archive Sources =~ "){
        timestamps {
            checkout scm
            stash name: "rundeck-scripts"
        }
    }

    stage(' =~ Rundeck Tasks =~ ') {

        dir("rundeck-scripts") {
           unstash "rundeck-scripts"
        }
 
        // Helps to switch to the relevant dir to execute needed scripts
	dir ("rundeck-scripts") {
	    sh "./rundeck_job.sh"

	    // Call external Python script to get status of Rundeck job
            // project name and job id is hard-coded for testing convenience :-((
            // Why not use the same script with additional parmater to start the job ?
            sh "python ./getRundeckJobStatus.py pipeline_poc 5c970e5b-8d36-4a28-8b5f-905a9c81949e"
        
            // why this doesn't work ?
            // def rdjob_status = sh(returnStdout: true, script: 'python ./getRundeckJobStatus.py pipeline_poc 5c970e5b-8d36-4a28-8b5f-905a9c81949e')

            def rdjob_file = fileExists('jobinfo.txt')

            if (rdjob_file) {
                def rdjob_status = readFile('jobinfo.txt')
                env.RDJOB_STATUS = rdjob_status
                echo "Status of rundeck job (parsed from jobinfo) ==>"
                echo "${rdjob_status}"
            } else if (!rdjob_file) {
                env.RDJOB_STATUS = "UNKNOWN"
                echo " ==> Rundeck job status could not be ascertained !!!"
            }
        }

	// Cleanup stashed sources
	dir ("rundeck-scripts") {
            deleteDir()
        }
    }
}



node('linux') {
    if (env.RDJOB_STATUS =~ /failed/) {
        stage(' =!~ RUNDECK JOB FAILED =!~ ') {
            echo " ==> Rundeck job failed, check job logs in Rundeck "
        }
    } else if (env.RDJOB_STATUS =~ /succeeded/) {
        stage(' =~ Env Dump =~ ') {
            echo " ==> Rundeck job passed "
            sh 'env > env_vars.txt'
            def envdump = readFile('env_vars.txt')
            echo " =~> [Start]: Dumping environment variables =~> "
            echo "${envdump}"
            echo " =~> [End]: Dumping environment variables =~> "
        }
    } else {
        stage(' =*~ RUNDECK CFG UPSET =*~ ') {
            echo " ==> Rundeck job status unavailable, check configuration in Rundeck "
        }
    }
}
