// I've tried this method to aviod need a Mustache dependency. Similar to how they do it here: https://github.com/projen/projen/blob/main/src/python/python-project.ts
// Otherwise I'll capitulate and do Mustache.

module.exports = function python_pod(options) {
  console.log(options.name)
  return `

# LM REVIEW: Would be possible to customise the name of this file based on project
# name if needed, using projen. E.g. the p2d-ingress project would have a skaffold/p2d-ingress-pod.yml file
apiVersion: v1
kind: Pod
metadata:
  name: python
  labels:
    app: python
spec:
  containers:
    - name: python
      image: ${options.name}
      ports:
        # LM REVIEW: Name/port can be passed in as options from projen here if needed
        - name: 
          containerPort: ${options.defaultDockerPort}
          protocol: TCP
`
};