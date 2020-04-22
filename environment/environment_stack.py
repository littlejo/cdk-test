from aws_cdk import (
    core,
    aws_ec2 as _ec2
)


class EnvironmentStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, name_extension: str, stage:str, tags:[], conf: dict, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        resource_name = name_extension+"-vpc.main"

        self.vpc = _ec2.Vpc(self, 
            resource_name,
            cidr=conf["vpc"]["cidr"],
            max_azs=conf["vpc"]["max_az"],
            subnet_configuration=[
            _ec2.SubnetConfiguration(
                subnet_type=_ec2.SubnetType.ISOLATED,
                name=conf["vpc"]["subnet_name"],
                cidr_mask=conf["vpc"]["subnet_mask"]
              )
            ],
            )
            
        core.CfnOutput(self, "Output", 
            export_name="VPC-{}".format(stage),
            value=self.vpc.vpc_id)
