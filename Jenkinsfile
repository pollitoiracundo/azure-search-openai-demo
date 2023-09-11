pipeline {
    agent { dockerfile true }
    environment {
        //EXAMPLE_CREDS = credentials('example-credentials-id')
        AZURE_ENV_NAME="poc2"
        AZURE_FORMRECOGNIZER_RESOURCE_GROUP="RG-Hibbett-AI"
        AZURE_FORMRECOGNIZER_SERVICE="cog-fr-eux4lr2kz4si4"
        AZURE_LOCATION="eastus"
        AZURE_OPENAI_CHATGPT_DEPLOYMENT="chat"
        AZURE_OPENAI_EMB_DEPLOYMENT="embedding"
        AZURE_OPENAI_GPT_DEPLOYMENT="davinci"
        AZURE_OPENAI_RESOURCE_GROUP="RG-Hibbett-AI"
        AZURE_OPENAI_SERVICE="cog-eux4lr2kz4si4"
        AZURE_RESOURCE_GROUP="RG-Hibbett-AI"
        AZURE_SEARCH_INDEX="gptkbindex"
        AZURE_SEARCH_SERVICE="gptkb-eux4lr2kz4si4"
        AZURE_SEARCH_SERVICE_RESOURCE_GROUP="RG-Hibbett-AI"
        AZURE_STORAGE_ACCOUNT="steux4lr2kz4si4"
        AZURE_STORAGE_CONTAINER="content"
        AZURE_STORAGE_RESOURCE_GROUP="RG-Hibbett-AI"
        AZURE_SUBSCRIPTION_ID="6eb935f1-c27d-497d-ab06-53bd6b01c811"
        AZURE_TENANT_ID="48c33123-f1b5-454b-8f27-f4f468ccc4a0"
        BACKEND_URI="https://app-backend-eux4lr2kz4si4.azurewebsites.net"
    }
    stages {
        stage('Check docker image') {
            steps {
                sh 'node --version'
                sh 'python3 --version'
                sh 'azd -version'
            }
        }
        stage('Check sources') {
            steps {
                sh 'pwd'
                sh 'ls -la'  
            }
        }
    }
}
