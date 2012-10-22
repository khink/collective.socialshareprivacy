from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.socialshareprivacy


COLLECTIVE_SOCIALSHAREPRIVACY = PloneWithPackageLayer(
    zcml_package=collective.socialshareprivacy,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.socialshareprivacy:testing',
    name="COLLECTIVE_SOCIALSHAREPRIVACY")

COLLECTIVE_SOCIALSHAREPRIVACY_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_SOCIALSHAREPRIVACY, ),
    name="COLLECTIVE_SOCIALSHAREPRIVACY_INTEGRATION")

COLLECTIVE_SOCIALSHAREPRIVACY_FUNCTIONAL = FunctionalTesting(
    bases=(COLLECTIVE_SOCIALSHAREPRIVACY, ),
    name="COLLECTIVE_SOCIALSHAREPRIVACY_FUNCTIONAL")
