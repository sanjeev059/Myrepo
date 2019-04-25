
pipeline {
    agent any


    environment{
             stack = "delta"
             env = "union"
             spec = "analytics-05,analytics-06,baseflow-54,presence-02,dashboard-02,documents-01,documents-20,messenger-01,notifications-01,notifications-02,notifications-27,postUpdate-04,shipmentSearch-01,sidebarMessenger-01,sharing-05,sharing-06,smoke-02,smoke-03,smoke-07,smoke-11,orders-01,contracts-01,timeline-01,timeline-06,tasks-01"
             execlude = "payments,drivers,tags.systemTags,baseflow-55,baseflow-64,baseflow-53,baseflow-60,calendar-01,analytics-02,notifications-20"
             bus_rule = "phanindra.v@turvo.com/Temp@123"
             git_ref = "refs/heads/develop"
        }

    stages {

        stage('DB Automation'){
          steps{
            script{
            slackSend (channel: "#release-engg", color: '#FFFF00', message: "nightly build started\nbuild_url:(${env.BUILD_URL})")
            git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/api.git'
            def commit = sh 'git rev-parse HEAD > commit'
            def commit1 = readFile('commit').trim()

            def jobBuild = build job: 'mysql-db-automation',propagate: true, parameters: [[$class: 'StringParameterValue', name: 'STACK', value: "${env}"]]
            def jobResult = jobBuild.getResult()
            slackSend (channel: "#release-engg", color: '#FFFF00', message: "•Build of 'mysql-db-automation'\n •returned result: ${jobResult}\n•${commit1}")
            def reslog = jobBuild.rawBuild.log
            println reslog
            if (jobResult != 'SUCCESS') {
                slackSend (channel: "#release-engg", color: '#FFFF01', message: "•Build of 'mysql-db-automation'\n •returned result: ${jobResult}\n•${commit1}")
                error("mysql-db-automatio failed with result: ${jobResult}")
                    }



            def jobBuild1 = build job: 'mongeez-db-automation',propagate: true, parameters: [[$class: 'StringParameterValue', name: 'STACK', value: "${env}"]]
            def jobResult1 = jobBuild.getResult()
            slackSend (channel: "#release-engg", color: '#FFFF00', message: "•Build of 'mongeez-db-automation'\n •returned result: ${jobResult}\n•${commit1}")
            echo "Build of 'mysql-db-automation' returned result: ${jobResult}"
            if (jobResult != 'SUCCESS') {
            slackSend (channel: "#release-engg", color: '#FFFF01', message: "•Build of 'mongeez-db-automation'\n •returned result: ${jobResult}\n•${commit1}")
                        error("testJob failed with result: ${jobResult}")
                    }



            git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/api.git'
            def commit_core = sh 'git rev-parse HEAD > commit_core'
            def commit_core_res = readFile('commit_core').trim()

            def jobBuild2 = build job: 'connect-core-db-automation',propagate: true, parameters: [[$class: 'StringParameterValue', name: 'STACK', value: "${env}"]]
            def jobResult2 = jobBuild.getResult()
            slackSend (channel: "#release-engg", color: '#FFFF00', message: "•Build of 'connect-core-db-automation'\n •returned result: ${jobResult}\n•${commit_core_res}")
            echo "Build of 'mysql-db-automation' returned result: ${jobResult}"
            //def buildResult['testJob'] = jobResult
            if (jobResult != 'SUCCESS') {
            slackSend (channel: "#release-engg", color: '#FFFF01', message: "•Build of 'connect-core-db-automation'\n •returned result: ${jobResult}\n•${commit_core_res}")
                        error("testJob failed with result: ${jobResult}")
            }
          }
        }
/*
        stage('platform') {
            steps {
              script{
              git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/api.git'
              def commit = sh 'git rev-parse HEAD > commit'
              def commit1 = readFile('commit').trim()
              echo "$commit1"
              sh "date +%Y-%m-%d > result";
              def output=readFile('result').trim()
              echo "$output";
                    build job: 'api-build', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "api"], [$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                    build job: 'api-promote', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "api"], [$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]
                    build job: 'api-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "api"], [$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value:"$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]
                    //build job: 'solo-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "api"], [$class: 'StringParameterValue', name: 'SCOPE', value: "private"],[$class: 'StringParameterValue', name: 'STACK', value: "hd-343"],[$class: 'StringParameterValue', name: 'VERSION', value:"${output}_nightly_1"]]

                    build job: 'event-build', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "event"], [$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                    build job: 'event-promote', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "event"], [$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]
                    build job: 'event-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "event"], [$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value:"$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]
                   // build job: 'solo-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "event"], [$class: 'StringParameterValue', name: 'SCOPE', value: "private"],[$class: 'StringParameterValue', name: 'STACK', value: "hd-343"],[$class: 'StringParameterValue', name: 'VERSION', value:"${output}_nightly_1"]]

                  build job: 'track-build', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "track"], [$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                  build job: 'track-promote', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "track"], [$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]
                  build job: 'track-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "track"], [$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value:"$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]
                  //build job: 'solo-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "track"], [$class: 'StringParameterValue', name: 'SCOPE', value: "private"],[$class: 'StringParameterValue', name: 'STACK', value: "hd-343"],[$class: 'StringParameterValue', name: 'VERSION', value:"${output}_nightly_1"]]



            }
        }
      }
        stage('Connect-core') {
            steps {
                    script{

                    git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/tc/core.git'
                    def commit = sh 'git rev-parse HEAD > commit'
                    def commit1 = readFile('commit').trim()
                    echo "commit1"

                    sh "date +%Y-%m-%d > result";
                    def output=readFile('result').trim()
                    echo "$output";

                    build job: 'connect-core-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "core"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                    build job: 'connect-core-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "core"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                    build job: 'connect-core-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "core"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                    //build job: 'solo-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "core"], [$class: 'StringParameterValue', name: 'SCOPE', value: "private"],[$class: 'StringParameterValue', name: 'STACK', value: "hd-343"],[$class: 'StringParameterValue', name: 'VERSION', value:"${output}_nightly_1"]]


                        }
                }
        }

        //connect http

        stage('Connect-http') {
            steps {
                    script{
                    git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/tc/http.git'
                    def commit = sh 'git rev-parse HEAD > commit'
                    def commit1 = readFile('commit').trim()
                    echo "$commit1"
                    sh "date +%Y-%m-%d > result";
                    def output=readFile('result').trim()
                    echo "$output";
                    build job: 'connect-http-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "http"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                    build job: 'connect-http-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "http"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly"]]
                    build job: 'connect-http-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "http"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly"]]
                    //build job: 'solo-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "http"], [$class: 'StringParameterValue', name: 'SCOPE', value: "private"],[$class: 'StringParameterValue', name: 'STACK', value: "hd-343"],[$class: 'StringParameterValue', name: 'VERSION', value:"${output}_nightly_1"]]


                        }
                }
        }

//connet edi

          stage("Connect-edi") {
              steps {
                      script{
                      git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/tc/edi.git'
                      def commit = sh 'git rev-parse HEAD > commit'
                      def commit1 = readFile('commit').trim()
                      echo "$commit1"
                      sh "date +%Y-%m-%d > result";
                      def output=readFile('result').trim()
                      echo "$output";
                      build job: 'connect-edi-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "edi"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                      build job: 'connect-edi-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "edi"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                      build job: 'connect-edi-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "edi"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                      //build job: 'solo-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "edi"], [$class: 'StringParameterValue', name: 'SCOPE', value: "private"],[$class: 'StringParameterValue', name: 'STACK', value: "hd-343"],[$class: 'StringParameterValue', name: 'VERSION', value:"${output}_nightly_1"]]


                          }
                  }
          }

          //connect bdi

          stage("Connect-bdi") {
              steps {
                      script{
                      git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/tc/bdi.git'
                      def commit = sh 'git rev-parse HEAD > commit'
                      def commit1 = readFile('commit').trim()
                      echo "$commit1"
                      sh "date +%Y-%m-%d > result";
                      def output=readFile('result').trim()
                      echo "$output";
                      build job: 'connect-bdi-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "bdi"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                      build job: 'connect-bdi-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "bdi"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                      build job: 'connect-bdi-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "connect"], [$class: 'StringParameterValue', name: 'SERVICE', value: "bdi"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                      //build job: 'solo-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "bdi"], [$class: 'StringParameterValue', name: 'SCOPE', value: "private"],[$class: 'StringParameterValue', name: 'STACK', value: "hd-343"],[$class: 'StringParameterValue', name: 'VERSION', value:"${output}_nightly_1"]]


                          }
                  }
          }

        stage("orders") {
            steps {
                        script{
                        git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/orders.git'
                        def commit = sh 'git rev-parse HEAD > commit'
                        def commit1 = readFile('commit').trim()
                        echo "$commit1"
                        sh "date +%Y-%m-%d > result";
                        def output=readFile('result').trim()
                        echo "$output";
                        build job: 'platform-orders-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "orders"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                        build job: 'platform-orders-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "orders"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                        build job: 'platform-orders-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "orders"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]

                          }
                }
            }

                stage("Contracts"){
                steps{
                script{
                git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/contracts.git'
                def commit = sh 'git rev-parse HEAD > commit'
                def commit1 = readFile('commit').trim()
                echo "$commit1"
                sh "date +%Y-%m-%d > result";
                def output=readFile('result').trim()
                echo "$output";
                build job: 'platform-contracts-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "contracts"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                build job: 'platform-contracts-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "contracts"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                build job: 'platform-contracts-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "contracts"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                    }
                  }

                }
                stage("items"){
                steps{
                script{
                git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/items.git'
                def commit = sh 'git rev-parse HEAD > commit'
                def commit1 = readFile('commit').trim()
                echo "$commit1"
                sh "date +%Y-%m-%d > result";
                def output=readFile('result').trim()
                echo "$output";
                build job: 'platform-items-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "items"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                build job: 'platform-items-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "items"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                build job: 'platform-items-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "items"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]

                  }
                }
              }
                stage("unity"){
                steps{
                script{
                    cleanWs()
                git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/unity.git'
                def commit = sh 'git rev-parse HEAD > commit'
                def commit1 = readFile('commit').trim()
                echo "$commit1"
                sh "date +%Y-%m-%d > result";
                def output=readFile('result').trim()
                echo "$output";
                build job: 'platform-unity-build', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "unity"],[$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
                build job: 'platform-unity-promote', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "unity"],[$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
                build job: 'platform-unity-deploy', parameters: [[$class: 'StringParameterValue', name: 'APPLICATION', value: "platform"], [$class: 'StringParameterValue', name: 'SERVICE', value: "unity"],[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value: "$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]


                  }
                }
                }
        stage("Presence") {
            steps {

            script{
            git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/presence.git'
            def commit = sh 'git rev-parse HEAD > commit'
            def commit1 = readFile('commit').trim()
            echo "$commit1"
            sh "date +%Y-%m-%d > result";
            def output=readFile('result').trim()
            echo "$output";
            build job: 'presence-build', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "presence"], [$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
            build job: 'presence-promote', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "presence"], [$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
            build job: 'presence-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "presence"], [$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value:"$stack"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]

            }
            }
        }
        stage("Notify") {
            steps {
            script{
            git branch: 'develop', url: 'ssh://git@lab.turvo.net:7999/dev/notify.git'
            def commit = sh 'git rev-parse HEAD > commit'
            def commit1 = readFile('commit').trim()
            echo "$commit1"
            sh "date +%Y-%m-%d > result";
            def output=readFile('result').trim()
            echo "$output";
            build job: 'notify-build', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "notify"], [$class: 'StringParameterValue', name: 'GIT_TARGET', value: "$commit1"]]
            build job: 'notify-promote', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "notify"], [$class: 'StringParameterValue', name: 'BUILD_VERSION', value: "$commit1"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value: "${output}_nightly_1"]]
            build job: 'notify-deploy', parameters: [[$class: 'StringParameterValue', name: 'ROLE', value: "notify"], [$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],[$class: 'StringParameterValue', name: 'STACK', value:"${stack}"],[$class: 'StringParameterValue', name: 'RELEASE_VERSION', value:"${output}_nightly_1"]]


            }
            }
        }

        stage("Wait Stack to Come Up") {
            steps {
            script{

                sleep time: 15, unit: 'MINUTES'
            }
            }
        }

        stage("Health Check") {
            steps {
            script{
                build job: 'fusion-health-checker', parameters: [string(name: 'ENV', value: 'union'), string(name: 'STACK', value: 'delta')]
                build job: 'fusion-health-checker', parameters: [string(name: 'ENV', value: 'union'), string(name: 'STACK', value: 'delta')]
                build job: 'fusion-health-checker', parameters: [string(name: 'ENV', value: 'union'), string(name: 'STACK', value: 'delta')]

            }
            }
        }


        stage("Smoke testing") {
            steps {
            script{

            build job: 'quality-aws-smoke-infra',  propagate: true, parameters:
            [[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],
            [$class: 'StringParameterValue', name: 'STACK', value: "$stack"],
            [$class: 'StringParameterValue', name: 'SPEC', value:"$spec"],
            [$class: 'StringParameterValue', name: 'RE_RUN_FAILED', value:"2"],
            [$class: 'StringParameterValue', name: 'SELINIUM_ADDRESS', value:"http://ec2-54-202-137-102.us-west-2.compute.amazonaws.com:4444/wd/hub/"],
            [$class: 'StringParameterValue', name: 'EXCLUDE', value:"$execlude"],
            [$class: 'StringParameterValue', name: 'BUSINESS_RULES', value:"$bus_rule"],
            [$class: 'StringParameterValue', name: 'MAX_INSTANCES', value:"10"],
            [$class: 'StringParameterValue', name: '	GIT_TARGET', value:"$git_ref"],
            ]
            slackSend (channel: "#release-engg", color: '#00FF00', message: "Test Report: http://ci.turvo.net:8080/job/quality-aws-smoke-infra/lastBuild/allure/ ")

            }
            }

        }

         stage("Regression") {
            steps {
            script{

            build job: 'quality-aws-infra-regression',  propagate: true, parameters:
            [[$class: 'StringParameterValue', name: 'ENVIRONMENT', value: "${env}"],
            [$class: 'StringParameterValue', name: 'STACK', value: "$stack"],
            [$class: 'StringParameterValue', name: 'SPEC', value:"$spec"],
            [$class: 'StringParameterValue', name: 'RE_RUN_FAILED', value:"2"],
            [$class: 'StringParameterValue', name: 'SELINIUM_ADDRESS', value:"http://ec2-54-202-137-102.us-west-2.compute.amazonaws.com:4444/wd/hub/"],
            [$class: 'StringParameterValue', name: 'EXCLUDE', value:"$execlude"],
            [$class: 'StringParameterValue', name: 'BUSINESS_RULES', value:"$bus_rule"],
            [$class: 'StringParameterValue', name: 'MAX_INSTANCES', value:"10"],
            [$class: 'StringParameterValue', name: '	GIT_TARGET', value:"$git_ref"],
            ]

            slackSend (channel: "#release-engg", color: '#00FF00', message: "Test Report: http://ci.turvo.net:8080/job/quality-aws-infra-regression/lastBuild/allure/ ")

            }
            }

        }
    }
    post {

        success{
            slackSend (channel: "#release-engg", color: '#00FF00', message: "SUCCESSFUL: Job '[${env.BUILD_NUMBER}]'\n${env.BUILD_URL})")
        }
        failure {
      slackSend (channel: "#release-engg", color: '#FF0000', message: "FAILED: Job '${env.BUILD_NUMBER}]'\n(${env.BUILD_URL})")
        }
        aborted{
                 slackSend (channel: "#release-engg", color: '#000000', message: "ABORTED: Job '[${env.BUILD_NUMBER}]'\n(${env.BUILD_URL})")

        }
    } */
}
}
}
