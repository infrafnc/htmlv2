node {
    checkout scm

    // Pega o commit id para ser usado de tag (versionamento) na imagem
    sh "git rev-parse --short HEAD > commit-id"
    tag = readFile('commit-id').replace("\n", "").replace("\r", "")
    
    // configura o nome da aplicação, o endereço do repositório e o nome da imagem com a versão
    appName = "htmlv2"
    imageName = "${appName}:${tag}"

    // Configuramos os estágios
    
    stage "Build"
    	docker.withRegistry('kaique5247/front', 'DockerHub') {
        	def customImage = docker.build("${imageName}")

    stage "Push"
        customImage.push() 

    stage "Deploy PROD"
        input "Deploy to PROD?"
        customImage.push('latest')
        sh "kubectl set image deployment htmlv2 htmlv2=${imageName} --record"
        sh "kubectl rollout status deployment/htmlv2"
	}
}
