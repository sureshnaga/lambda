pipeline{
	agent any
	stages{
	stage('Setup & Build'){
	steps{
		sh 'pip install --target . pymysql '
		sh "zip -r function.zip ."
		sh "chmod 777 function.zip"
		}
		}
	stage(deploy){
	steps{
		sh "aws s3 cp function.zip s3://kalai-lambda"
		sh "aws lambda update-function-code  --function-name demolambda --s3-bucket kalai-lambda --s3-key function.zip"
	}
	}
	}
}
