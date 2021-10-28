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
                                     cleanRemote: true,
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
                        username: 'root',
                        encryptedPassphrase: "$SSH_PASS"
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
