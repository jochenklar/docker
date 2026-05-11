c = get_config()  # noqa: F821

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'jupyter/base-notebook:latest'
c.DockerSpawner.network_name = 'jupyterhub-network'

c.JupyterHub.hub_ip = '0.0.0.0'
c.DockerSpawner.hub_ip_connect = 'host.docker.internal'

c.DockerSpawner.volumes = {
    'jupyterhub-user-data': '/home/jovyan'
}

c.JupyterHub.authenticator_class = "dummy"
c.DummyAuthenticator.password = "test"
