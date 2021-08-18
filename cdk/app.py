#!/usr/bin/env python3
import os

from aws_cdk import core
from stack import CharliesProjectStack

identifier = os.environ["IDENTIFIER"]

app = core.App()

app_stack = CharliesProjectStack(
    app, f"CharliesProjectStack-{identifier}", identifier=identifier
)

for k, v in {"OWNER": os.environ["OWNER"], "IDENTIFIER": identifier}.items():
    core.Tags.of(app_stack).add(k, v, apply_to_launched_instances=True)

app.synth()
