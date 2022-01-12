#!/bin/bash
echo "Checking dependencies"
# Check if Minikube is installed
if ! command -v minikube &>/dev/null; then
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  rm minikube-linux-amd64
fi
echo "Starting Minikube.. "
if ! minikube status >/dev/null 2>&1; then
  minikube start
fi

echo "Setting context to Minikube"
kubectl config use-context minikube
echo "Your Kubernetes context has been set to use Minikube rather than prod or staging"

# Check if Skaffold is installed
if ! command -v skaffold &>/dev/null; then
  echo "Installing Skaffold"
  curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64 && sudo install skaffold /usr/local/bin/
  rm skaffold
fi

#Starting Skaffold
skaffold dev
