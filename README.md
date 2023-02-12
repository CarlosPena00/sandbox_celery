# My Celery Sandbox

```sh
mamba env create
mamba activate celery
pip-sync requirements-dev.txt
pre-commit install

# After update `setup.cfg`
pip-compile setup.cfg --resolver backtracking -o requirements.txt
pip-compile setup.cfg --resolver backtracking -o requirements-dev.txt --extra dev
```

## Run
```sh
# start docker:
sh scripts/00_start.sh

# start worker(s):
sh scripts/01_worker.sh

# start client:
sh scripts/02_client.sh
```
