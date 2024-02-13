DOCKER_ID := $(shell docker ps -aq)
DOCKER_IMAGE_ID := $(shell docker images -q)
DOCKER_VOLUME := $(shell docker volume ls -q)
PWD := $(shell pwd)
FE_VOL_PATH := $(PWD)/srcs/frontend/tools/srcs
FE_DB_VOL_PATH := $(PWD)/srcs/frontend/frontend_db/frontend_db_vol

all:
	sed -i '' 's|^\(FE_DB_VOL_PATH\).*|FE_DB_VOL_PATH=$(FE_DB_VOL_PATH)|' './srcs/.env'
	sed -i '' 's|^\(FE_VOL_PATH\).*|FE_VOL_PATH=$(FE_VOL_PATH)|' './srcs/.env'
	docker compose -f srcs/compose.yaml up -d

up:
	docker compose -f srcs/compose.yaml up -d

down:
	docker compose -f srcs/compose.yaml down

re: fclean
	make all

fclean:
	$(if $(DOCKER_ID), docker rm -f $(DOCKER_ID))
	$(if $(DOCKER_IMAGE_ID), docker rmi $(DOCKER_IMAGE_ID))
	$(if $(DOCKER_VOLUME), docker volume rm $(DOCKER_VOLUME))
	docker system prune -af
	rm -rf $(FE_DB_VOL_PATH)/*

django:
	docker compose -f srcs/compose.yaml run -it django sh

.PHONY: all up down re fclean