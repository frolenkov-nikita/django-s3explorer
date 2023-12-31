from django.views.generic import TemplateView
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)

        cd.update(
            {'s3_key': settings.S3_EXPLORER_AWS_ACCESS_KEY_ID,
             's3_secret': settings.S3_EXPLORER_AWS_SECRET_ACCESS_KEY,
             's3_bucket': settings.S3_EXPLORER_BUCKET_NAME}
        )

        return cd

# import boto3
#
#
# client = boto3.client(
#     'sts',
#     aws_access_key_id='',
#     aws_secret_access_key='',
# )
#
#
# resp = client.get_session_token(
#     DurationSeconds=900,
# )