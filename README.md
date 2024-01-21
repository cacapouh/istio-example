### Istioインストール

https://istio.io/latest/docs/setup/getting-started/#download

```
curl -L https://istio.io/downloadIstio | sh -
istioctl install --set profile=demo -y
```

### Dockerビルド

```
docker build . -t simple-app
minikube image load simple-app:latest 
```

### デプロイ

```
helm install simple-app ./helm
```

### アクセス

```
minikube tunnel
export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')

curl -v "http://$INGRESS_HOST:$INGRESS_PORT"
```
