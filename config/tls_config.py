import ssl
import os

def get_tls_context():
    """
    Configures and returns a TLS context for secure communication.
    """
    cert_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../certs"))
    ca_file = os.path.join(cert_dir, "ca.pem")
    cert_file = os.path.join(cert_dir, "ultrain.crt")
    key_file = os.path.join(cert_dir, "ultrain.key")

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(ca_file)
    context.load_cert_chain(cert_file, key_file)
    return context
