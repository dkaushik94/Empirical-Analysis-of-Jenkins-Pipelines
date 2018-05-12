// this is a simple "Hello World" Jenkinsfile, intended to help you get started with Jenkinsfile syntax
// Jenkinsfiles are Groovy-based, but they allow for a wide variety of DSL steps as well (documented in DOCUMENTATION.MD)

// the 'node' DSL is used to specify which slaves to use to build the enclosed steps
// in our case, we're specifying the labels 'cloud&&centos', meaning we will only build the enclosed block on slaves with both 'cloud' and 'ubuntu' labels
// if node such slave is available, Jenkins will add this pipeline to the queue until a slave with both of these labels becomes available
// if you do not specify a label (e.g 'node { ... }'), any available slave will used

    //everything inside this block will build on a slave with the labels 'cloud' and 'centos'
    // the 'echo' DSL step allows you to echo strings out to the Jenkins console
    echo 'Hello World!'
    // the 'sh' DSL steps allows you to run Bourne shell script commands
    // note: for Windows builds, use the 'bat' DSL step, which executes batch script commands

