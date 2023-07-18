IMAGE_TAG?=$(shell echo `git rev-parse --short HEAD`)
DOCKER_PW=$(shell echo `aws ecr get-login-password --region ap-southeast-1 --profile devaccess`)
ECR_REPO=699324607567.dkr.ecr.ap-southeast-1.amazonaws.com
CONTAINER_NAME=socketio-loading-test

.PHONY: build

build:
	@docker login -u AWS -p $(DOCKER_PW) $(ECR_REPO)
	# docker build -t ${CONTAINER_NAME}:$(IMAGE_TAG) .
	# docker tag ${CONTAINER_NAME}:$(IMAGE_TAG) $(ECR_REPO)/${CONTAINER_NAME}:$(IMAGE_TAG)
	docker push $(ECR_REPO)/${CONTAINER_NAME}:$(IMAGE_TAG)
