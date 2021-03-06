#!/usr/bin/env python2
from __future__ import print_function
import owncloud
import unidecode
import uuid
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', help='Server instance', default='transfer.digilab.nfa.cz')
parser.add_argument('-u', '--user', help='Username', required=True)
parser.add_argument('-p', '--password', help='Password', required=True)
parser.add_argument('-n', '--name', help='Name of the directory', required=True)
parser.add_argument('-d', '--dir', help='Path where to create a shared directory', default='DIGILAB/DROP_BOX')
args = parser.parse_args()

name = unidecode.unidecode(args.name.decode('utf8')).strip().replace(' ', '_').upper()
dst_dir = '{0}/{1}_{2}'.format(args.dir, name, uuid.uuid4().hex)
oc = owncloud.Client('https://{0}'.format(args.server))
oc.login(args.user, args.password)
oc.mkdir(dst_dir)
link_info = oc.share_file_with_link(dst_dir, public_upload=True)
oc.logout()

print('{0} : {1}'.format(name, link_info.get_link()), end='')
