# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from gcdt.gcdt_openapi import get_openapi_defaults, get_openapi_scaffold_min, \
    get_openapi_scaffold_max, validate_tool_config

from gcdt_yugen import read_openapi


def test_scaffolding_default():
    spec = read_openapi()
    # note: yugen currently has no defaults

    yugen_defaults = get_openapi_defaults(spec, 'yugen')
    assert yugen_defaults == {}
    # validate_tool_config(spec, {'kumo': yugen_defaults})


def test_scaffolding_sample_min():
    spec = read_openapi()
    expected_sample = {
        'api': {
            'apiKey': '916Chdzdtc7idRgsPaJKABC12345EXAMPLE',
            'description': 'API Gateway for my-service',
            'name': 'my-service-api',
            'targetStage': 'dev'
        }
    }

    yugen_sample = get_openapi_scaffold_min(spec, 'yugen')
    assert yugen_sample == expected_sample
    validate_tool_config(spec, {'yugen': yugen_sample})


def test_scaffolding_sample_max():
    spec = read_openapi()
    expected_sample = {
        'api': {
            'apiKey': '916Chdzdtc7idRgsPaJKABC12345EXAMPLE',
            'cacheClusterEnabled': True,
            'cacheClusterSize': '0.5',
            'description': 'API Gateway for my-service',
            'methodSettings': '"methodSettings": {"/path/to/resource/GET": {"cachingEnabled": false}}',
            'name': 'my-service-api',
            'targetStage': 'dev'
        },
        'customDomain': {
            'basePath': u'string',
            'certificateArn': u'string',
            'certificateName': 'infra-glomex-cloud',
            'domainName': 'my-service-qa-eu-west-1.dev.mes.glomex.cloud',
            'hostedDomainZoneId': 'ABCDEF123456',
            'route53Record': 'my-service-qa-eu-west-1.dev.mes.glomex.cloud'
        },
        'lambda': {
            'entries': [
                {
                    'alias': 'ACTIVE',
                    'name': 'my-service',
                    'swaggerRef': 'my-serviceUri'
                }
            ]
        }
    }

    yugen_sample = get_openapi_scaffold_max(spec, 'yugen')
    assert yugen_sample == expected_sample
    validate_tool_config(spec, {'yugen': yugen_sample})
