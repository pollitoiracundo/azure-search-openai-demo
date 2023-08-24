pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                /* `make check` returns non-zero on test failures,
                * using `true` to allow the Pipeline to continue nonetheless
                */
                sh 'azd -h'  
            }
        }
    }
}
