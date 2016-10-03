"""
Test driver configuration.

Configuration of the SP Test driver
"""
from config_common import Config as CommonConfig

class Config(CommonConfig):
    """
    Defines the parameter (SP-) base for all config classes
    """
    # TODO: move to abstract or higher
    def param_base(self):
        return 'http://webui.samltest.fed-lab.org:8087/'

    """
    Parameters are set in the config() method. Make sure you call the Superclass config() first to have the
    defaults initialized.
    """

    def config(self):
        super(Config,self).config()
        
        self.DO_NOT_VALIDATE_TLS = True     # Do not validate TLS certificates
        self.PORT = 8087
        self.METADATA = [
            {'metadata': [('https://identinetics.github.io/saml2test2.conf/split/testidp01SamltestFed-labOrg_idpShibboleth.xml',)],
             'class': 'saml2.mdstore.MetaDataExtern'}
        ]

        # Each key in CONFIG represents an entity to be configured with pysaml2:
        # https://github.com/rohe/pysaml2/blob/master/doc/howto/config.rst
        self.CONFIG = {}
        self.CONFIG.update({
            'acs-post': {
                'cert_file': 'pki/mycert.pem',
                'description': 'Basic SP',
                'entityid': self.BASE + 'basic/sp.xml',
                'key_file': 'pki/mykey.pem',
                'name_form': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [
                                (self.BASE + 'acs/post', 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST')],
                            'discovery_response': [
                                (self.BASE + 'disco',
                                 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery'
                                 '-protocol')],
                            'single_logout_service': [
                                (self.BASE + 'slo',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP')]}}},
            },

            'acs-redirect': {
                'cert_file': 'pki/mycert.pem',
                'description': 'Basic SP',
                'entityid': self.BASE + 'basic/sp.xml',
                'key_file': 'pki/mykey.pem',
                'name_form': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [
                                (self.BASE + 'acs/redirect', 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect')],
                            'discovery_response': [
                                (self.BASE + 'disco',
                                 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery'
                                 '-protocol')],
                            'single_logout_service': [
                                (self.BASE + 'slo',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP')]}}},
            },

            'acs-artifact': {
                'cert_file': 'pki/mycert.pem',
                'description': 'Basic SP',
                'entityid': self.BASE + 'basic/sp.xml',
                'key_file': 'pki/mykey.pem',
                'name_form': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [
                                (self.BASE + 'acs/artifact', 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact')],
                            'discovery_response': [
                                (self.BASE + 'disco',
                                 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery'
                                 '-protocol')],
                            'single_logout_service': [
                                (self.BASE + 'slo',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP')]}}},
            },

            'acs-ecp': {
                'cert_file': 'pki/mycert.pem',
                'description': 'Basic SP',
                'entityid': self.BASE + 'basic/sp.xml',
                'key_file': 'pki/mykey.pem',
                'name_form': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [
                                (self.BASE + 'ecp', 'urn:oasis:names:tc:SAML:2.0:bindings:PAOS')],
                            'discovery_response': [
                                (self.BASE + 'disco',
                                 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery'
                                 '-protocol')],
                            'single_logout_service': [
                                (self.BASE + 'slo',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP')]}}},
            },

            'coco': {
                'cert_file': 'pki/mycert.pem',
                'description': 'CoCo SP',
                'entity_category': [
                    'http://www.geant.net/uri/dataprotection-code-of-conduct/v1'],
                'entityid': self.BASE + 'coco/sp.xml',
                'key_file': 'pki/mykey.pem',
                'name_form': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [
                                (self.BASE + 'acs/redirect',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'),
                                (self.BASE + 'acs/post',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'),
                                (self.BASE + 'acs/artifact',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact'),
                                (self.BASE + 'ecp',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:PAOS')],
                            'discovery_response': [(
                                self.BASE + 'disco',
                                'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery'
                                '-protocol')],
                            'single_logout_service': [
                                (self.BASE + 'slo',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP')]},
                        'name': 'Code of Conduct SP',
                        'optional_attributes': ['displayName',
                                                'schacHomeOrganization'],
                        'required_attributes': [
                            'eduPersonPrincipalName',
                            'eduPersonScopedAffiliation',
                            'mail']}},
            },

            'required': {
                'cert_file': 'pki/mycert.pem',
                'description': 'Required Attributes SP',
                'entityid': self.BASE + 'required/sp.xml',
                'key_file': 'pki/mykey.pem',
                'name_form': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [
                                (self.BASE + 'acs/redirect',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'),
                                (self.BASE + 'acs/post',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'),
                                (self.BASE + 'acs/artifact',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact'),
                                (self.BASE + 'ecp',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:PAOS')],
                            'discovery_response': [
                                (self.BASE + 'disco',
                                 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol')],
                            'single_logout_service': [
                                (self.BASE + 'slo',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP')]},
                        'name': 'SP that requires attributes',
                        'optional_attributes': ['displayName',
                                                'schacHomeOrganization'],
                        'required_attributes': [
                            'eduPersonPrincipalName',
                            'eduPersonScopedAffiliation',
                            'mail']}},
            },

            'rs': {
                'cert_file': 'pki/mycert.pem',
                'description': 'RS SP',
                'entity_category': [
                    'http://refeds.org/category/research-and-scholarship'],
                'entityid': self.BASE + 'rs/sp.xml',
                'key_file': 'pki/mykey.pem',
                'name_form': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [
                                (self.BASE + 'acs/redirect',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'),
                                (self.BASE + 'acs/post',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'),
                                (self.BASE + 'acs/artifact',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact'),
                                (self.BASE + 'ecp',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:PAOS')],
                            'discovery_response': [
                                (self.BASE + 'disco',
                                 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery'
                                 '-protocol')],
                            'single_logout_service': [
                                (self.BASE + 'slo',
                                 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP')]}}},
            }}
        )
