"""A Python Pulumi program"""

import pulumi
import os
import pulumi_docker as docker

stack = pulumi.get_stack()

# Pull the backend image
backend_image_name = "backend"
backend = docker.RemoteImage(
    f"{backend_image_name}_image",
    name="pulumi/tutorial-pulumi-fundamentals-backend:latest",
)

# Pull the frontend image
frontend_image_name = "frontend"
frontend = docker.RemoteImage(
    f"{frontend_image_name}_image",
    name="pulumi/tutorial-pulumi-fundamentals-frontend:latest",
)

# Pull the MongoDB image
mongo_image = docker.RemoteImage(
    "mongo_image",
    name="pulumi/tutorial-pulumi-fundamentals-database-local:latest",
)