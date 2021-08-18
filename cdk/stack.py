from aws_cdk import aws_s3, core


class CharliesProjectStack(core.Stack):
    def __init__(
        self, scope: core.Construct, construct_id: str, identifier: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        my_bucket = aws_s3.Bucket(
            scope=self,
            id=f"my-bucket-{identifier}",
            removal_policy=core.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
