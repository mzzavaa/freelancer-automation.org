.PHONY: serve build new-daily

serve:
	hugo server -D --bind 0.0.0.0

build:
	hugo --minify

new-daily:
	@date=$$(date +%Y-%m-%d) && \
	read -p "Slug: " slug && \
	hugo new daily/$${date}-$${slug}.md
