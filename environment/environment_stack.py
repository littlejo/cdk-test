from aws_cdk import (
    core,
    aws_ec2 as _ec2
)


class EnvironmentStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, name_extension: str, stage:str, tags:[], **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        resource_name = name_extension+"-vpc.main"

        self.vpc = _ec2.Vpc(self, 
            resource_name,
            cidr="10.0.0.0/23",
            max_azs=2,
            # configuration will create 3 groups in 2 AZs = 6 subnets.
            subnet_configuration=[
                #_ec2.SubnetConfiguration(
                #subnet_type=_ec2.SubnetType.PUBLIC,
                #name="Public",
                #cidr_mask=24
            #),
            #_ec2.SubnetConfiguration(
            #    subnet_type=_ec2.SubnetType.PRIVATE,
            #    name="Private",
            #    cidr_mask=24
            #), 
            _ec2.SubnetConfiguration(
                subnet_type=_ec2.SubnetType.ISOLATED,
                name="Isolated",
                cidr_mask=24
            )
            ],
            # nat_gateway_provider=_ec2.NatProvider.gateway(),
            #nat_gateways=2,
            )
            
        core.CfnOutput(self, "Output", 
            export_name="VPC-{}".format(stage),
            value=self.vpc.vpc_id)
