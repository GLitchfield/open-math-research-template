.PHONY: check test wayfinder review-doctor

check:
	@python3 --version
	@git --version

test: check
	@python3 -m unittest discover -s scripts -p 'test_*.py'
	@python3 scripts/wayfinder_status.py >/dev/null
	@python3 -m py_compile scripts/adversarial_review.py scripts/wayfinder_status.py

wayfinder:
	@python3 scripts/wayfinder_status.py

review-doctor:
	@python3 scripts/adversarial_review.py doctor
