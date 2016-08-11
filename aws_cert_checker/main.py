#!/usr/bin/env python2.7

import sys
import logging
import argparse
import datetime
import boto3


ONE_DAY_IN_SECS = 86400


def main_exec():
    logger = logging.getLogger(__name__)

    # Set up command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("cert_name",
                        help="Name of the certificate that you want to check")
    parser.add_argument("expiration_buffer_secs",
                        type=int,
                        help="How much time left you want to count as expired, in seconds")
    args = parser.parse_args()

    # Set up the AWS client
    client = boto3.client('iam')

    # Return value
    has_expired = False
    cert_found = False

    # Execute the certificate check
    response = client.list_server_certificates()
    for cert in response['ServerCertificateMetadataList']:
        if cert['ServerCertificateName'] == args.cert_name:
            cert_found = True
            expiration_delta = \
                    cert['Expiration'].replace(tzinfo=None) - datetime.datetime.utcnow()

            if (int(expiration_delta.total_seconds())) < args.expiration_buffer_secs:
                has_expired = True

    # Exit with appropriate code
    if not cert_found:
        print("certificate-not-found")
        sys.exit(2)

    elif has_expired:
        print("certificate-expired")
        sys.exit(1)

    else:
        print("certificate-valid")
        sys.exit(0)


if __name__ == '__main__':
    main_exec()

