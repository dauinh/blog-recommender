# Deploy guide


https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images
```
docker image tag blog-recommender-api:latest \
us-central1-docker.pkg.dev/blog-recommender-431918/demo/blog-recommender-api:latest
```

```
docker push us-central1-docker.pkg.dev/blog-recommender-431918/demo/blog-recommender-api:latest
```

https://cloud.google.com/run/docs/deploying#gcloud
```
gcloud run deploy blog-recommender-api \
--image us-central1-docker.pkg.dev/blog-recommender-431918/demo/blog-recommender-api:latest \
--platform managed --allow-unauthenticated
```

https://cloud.google.com/run/docs/configuring/services/environment-variables#console
