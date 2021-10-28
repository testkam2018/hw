pipeline {
 agent any
  stages {
    stage('Build'){
      steps {
       echo 'dd3'
      }
    }
   stage ('DeployToServ'){
    steps {
      sshPublisher(
        failOnError: true,
        publishers: [
           sshPublisherDesc(
           configName: 'apache',
                  sshCredentials: [
                        username: 'root',
                        encryptedPassphrase: "$SSH_PASS"
                                ], 
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: '*/*',
                                        remoteDirectory: '/usr/share/httpd/noindex'
                                        
                                    )
                                ]
                            )
                        ]
                    )
      sshPublisher(
        failOnError: true,
        publishers: [
           sshPublisherDesc(
           configName: 'apache',
                  sshCredentials: [
                        username: 'cloud_user',
                        encryptedPassphrase: "$USERPASS"
                                ], 
                                transfers: [
                                    sshTransfer(
                                        execCommand: 'systemctl restart httpd'
                                        
                                    )
                                ]
                            )
                        ]
                    )
     
    }
   }
  }
  
  
  
}
