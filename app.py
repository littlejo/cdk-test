#!/usr/bin/env python3

from aws_cdk import core

import json

from environment.environment_stack import EnvironmentStack


# Read global configuration file 
with open('environment/environment_conf.json') as config_file: 
    global_conf = json.load(config_file)


app = core.App()
stage = app.node.try_get_context("stage")

if stage is None :
    stage = "default"

print("# Deploy stage [{}]".format(stage))


common_tags = []
common_tags.append( core.CfnTag( key="Project", value=global_conf["global"]["project"]))
common_tags.append( core.CfnTag( key="Stage", value=stage))



EnvironmentStack(app, "environment-{}".format(stage), tags=common_tags, name_extension=global_conf["global"]["extension"]+stage, stage=stage, conf=global_conf )

app.synth()
