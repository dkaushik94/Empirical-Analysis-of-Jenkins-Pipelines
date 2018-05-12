node {
        stage 'Load a file from GitHub'
        def helloworld = fileLoader.fromGit('examples/fileLoader/helloworld', 
                'https://github.com/escoem/workflow-remote-loader-plugin.git', 'master', null, '')
        
        stage 'Run method from the loaded file'


    helloworld.printHello()
    //git 'https://github.com/escotests/githubtests.git'
    checkout scm
    
    def changeLogSets = currentBuild.rawBuild.changeSets
    for (int i = 0; i < changeLogSets.size(); i++) {
        def entries = changeLogSets[i].items
        for (int j = 0; j < entries.length; j++) {
            def entry = entries[j]
            echo "${entry.commitId} by ${entry.authorEmail} on ${new Date(entry.timestamp)}: ${entry.msg}"
        }
    }
    helloworld.printHello()
}
