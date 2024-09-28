token=glrt-9JZZc9iKNGLk-jSw3uvr
url="http://172.31.122.120"

docker exec -ti gitlab-runner \
	gitlab-runner register \
	--non-interactive \
	--executor "docker" \
	--docker-image docker:latest \
	--url ${url} \
	--token ${token}