
pipeline {
    agent any
    stages {

        stage('api'){
          steps{
            script{

            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-api-${STACK}.turvo.com/health > result"
            def output=readFile('result').trim()
            echo "$output"
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }

            }
          }
        }

        stage('event'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-event-${STACK}.turvo.net/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('track'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-track-${STACK}.turvo.com/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }

        stage('orders'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} https://${ENV}-app-${STACK}.turvo.com/api/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }

        stage('items'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-items-${STACK}.turvo.com/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('contracts'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-contracts-${STACK}.turvo.com/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('unity'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-unity-${STACK}.turvo.net/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('presence'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-presence-${STACK}.turvo.com/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('notify'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-notify-${STACK}.turvo.net/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('core'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-core-${STACK}.turvo.net/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('http'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-http-${STACK}.turvo.com/health"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('edi'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-edi-${STACK}.turvo.net/edi/info"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
        stage('bdi'){
          steps{
            script{
            sh"curl -s -o response.txt -w %{http_code} http://${ENV}-bdi-${STACK}.turvo.net//bdi/1/test"
            def output=readFile('result').trim()
            if("$output" == "200"){
                currentBuild.result = "SUCCESS"
            }else{
                 echo "$output"
                 currentBuild.result = "FAILURE"

            }
            }
          }
        }
    }
}
        
