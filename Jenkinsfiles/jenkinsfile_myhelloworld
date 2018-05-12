stage 'build'
node {
	git 'https://github.com/fancapital/myhelloworld.git'
	sh '''
		make clean
		make
	    '''
}

stage 'Docker Push'
node {
	sh '''
		tag=`git tag|tail -n 1`
		imageid=`docker images | grep myhelloworld | awk '{print $3}'`
		docker rmi $imageid                
		docker build -t 118.178.135.157:5000/item/myhelloworld:$tag .
                docker login --username pftz --password Pftz8888 118.178.135.157:5000
                docker push 118.178.135.157:5000/item/myhelloworld:$tag

	   '''
}

stage 'Mail'
node {
	sh '''
tag=`git tag|tail -n 1`
/usr/sbin/sendmail -t <<EOF
From:Jenkins <yachuan.an@fancapital.com>
To:Anyachuan <yachuan.an@fancapital.com>
Subject:test mail
---------------------
Date:$(date +%Y%m%d)
Git Tag:$tag
---------------------
EOF
echo welcome
	   '''
}
