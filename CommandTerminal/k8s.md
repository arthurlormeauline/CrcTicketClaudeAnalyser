sync with flux : fluxctl sync --k8s-fwd-ns ft-usages-teamusages-apps-dev

restart : kubectl rollout restart deploy tb-facade

changer son name space quand kubens down :  kubectl config set-context --current --namespace=ft-transverse-camunda-dev 
 