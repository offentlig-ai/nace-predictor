#!/usr/bin/env groovy

node {
    def app

    def app_name = 'ai-lab-nace-poc'
    def namespace = 'ai-lab-nace-poc'
    def cluster = 'oera-q.local'
    def yaml_path = "https://repo.adeo.no/repository/raw/nais/${app_name}/${env.BUILD_ID}/nais.yaml"

    try {
        stage('Clean workspace') {
            cleanWs()
        }

        stage('Checkout code') {
            checkout scm
        }

        stage('Copy certificate bundle and aws credentials') {
            sh "cp /etc/ssl/certs/ca-bundle.crt ca-bundle.crt"
            sh "cp /var/lib/jenkins/.awg/credentials aws-credentials"
        }

        stage('Build react app') {
            sh "chmod +x scripts/buildReactApp.sh"
            sh "./scripts/buildReactApp.sh"
        }

        stage('Build docker image') {
            app = docker.build("${app_name}", "-f Dockerfile.jenkins .")
        }

        stage('Upload nais.yaml to nexus server') {
            sh "curl -s -S --upload-file nais.yaml ${yaml_path}"
        }

        stage('Push docker image') {
            docker.withRegistry('https://repo.adeo.no:5443', 'nexus-credentials') {
                app.push("${env.BUILD_ID}")
            }
        }

        stage('Deploy app to nais') {
            sh "curl --fail -k -d '{\"application\": \"${app_name}\", \"version\": \"${env.BUILD_ID}\", \"skipFasit\": true, \"namespace\": \"${namespace}\", \"manifesturl\": \"${yaml_path}\"}' https://daemon.nais.${cluster}/deploy"
        }
    } catch(e) {
        echo "Build failed"
        throw e
    } finally {
        sh "docker rmi -f \$(docker images | grep 'repo.adeo.no:5443/${app_name}' | awk '{print \$3}') | true"
    }
}