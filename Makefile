.DEFAULT_GOAL := help

.PHONY: clean help requirements

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  api-cient                 Update the auto-generated Python REST API Client"
	@echo "  requirements              Install the python requirements"
	@echo ""

# Which branch of the blockstore repo to fetch the API spec file from
BLOCKSTORE_API_VERSION=openapi-spec

api-client:
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.0.0-beta3 generate \
		--input-spec https://raw.githubusercontent.com/open-craft/blockstore/${BLOCKSTORE_API_VERSION}/api-spec.yaml \
		--generator-name python \
		--skip-validate-spec \
		--config /local/api-client-config.yaml \
		-DapiTests=false -DapiDocs=false \
		-DmodelTests=false -DmodelDocs=false \
		--output /local/
	# See also the .openapi-generator-ignore file to understand how the above
	# is used to selectively replace files.

requirements:
	pip install -qr requirements/base.txt --exists-action w
