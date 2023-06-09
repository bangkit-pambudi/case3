# CASE 3
Requirement : Docker Version 4.15

How To run
## 1. Docker Build

``` bash
docker build -t money-flow-index .
```

## 2. Docker run
``` bash
docker run -i -t <container id>
or
docker run -i -t <container id> /bin/bash
```

Example :
``` bash
docker run -i -t f6afe9e5ba3f
or
docker run -i -t f6afe9e5ba3f /bin/bash
```

## 3. Copy sample.csv to docker system
``` bash
docker cp <path-input> <images-id>:/app/sample.csv
```

``` bash
docker cp /home/bagas/sample.csv 4b26266ccf25:/app/sample.csv
```

## 4. Run program python
``` bash
docker exec <images-id> python app.py <m> <path-input-docker> <path-output-docker>
```

``` bash
docker exec 4b26266ccf25 python app.py 5 "/app/sample.csv" "/app"
```

## 5. Copy sample_output_m.csv to host file
``` bash
docker cp  <images-id>:/app/sample_output_m.csv <path-input>
```

``` bash
docker cp  4b26266ccf25:/app/sample_output_5.csv /home/bagas/sample_output_5.csv
```

