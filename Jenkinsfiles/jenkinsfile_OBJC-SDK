node('iMac') {
        stage 'Checkout'
            checkout scm	

        stage 'Pre-Build'
            sh 'pod install'

        stage 'Build'
            sh 'xcodebuild -workspace "OAuth1Tester.xcworkspace" -scheme "OAuth1Tester"  ONLY_ACTIVE_ARCH=NO' 
                stage 'Test'
            sh 'xcodebuild -workspace "OAuth1Tester.xcworkspace" -scheme "OAuth1Tester" -sdk iphonesimulator -destination "platform=iOS Simulator,name=iPhone 6s,OS=9.3" test'
        }