#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import tunet

from six.moves import urllib

username = 'username'
password = 'password'

def is_auth_online():
  try:
    result = tunet.auth4.checklogin()
    if not result.get('username'):
      print('not online (auth)')
      return False
    else:
      print('{:s} is online (auth)'.format(result.get('username')))
      return True
  except (tunet.NotLoginError, urllib.error.URLError) as e:
    if isinstance(e, tunet.NotLoginError):
      print('not login')
      return False
    else:
      print('URLError: {:s}'.format(e))
      exit(1)

def is_net_online():
  try:
    result = tunet.net.checklogin()
    if not result.get('username'):
      print('not online (net)')
      return False
    else:
      print('{:s} is online (net)'.format(result.get('username')))
      return True
  except (tunet.NotLoginError, urllib.error.URLError) as e:
    if isinstance(e, tunet.NotLoginError):
      print('not login')
      return False
    else:
      print('URLError: {:s}'.format(e))
      exit(1)

def get_auth_online():
  try:
    result = tunet.auth4.login(username, password, net=True)
    print('return:', result.get('error'))
    print('result:', result.get('res'))
    print('message:', result.get('error_msg'))
    if result.get('error') == 'ok' or \
      result.get('error') == 'ip_already_online_error':
      exit(0)
    else:
      exit(1)
  except urllib.error.URLError as e:
    print('URLError: {:s}'.format(e))
    exit(1)

def get_net_online():
  try:
    result = tunet.net.login(username, password)
    print('message:', result['msg'])
    if 'is successful' in result['msg'] or \
      'has been online' in result['msg'] or \
      'are not online' in result['msg']:
      exit(0)
    else:
      exit(1)
  except urllib.error.URLError as e:
    print('URLError: {:s}'.format(e))
    exit(1)

if __name__ == '__main__':
  if not is_auth_online():
    print('getting auth online...')
    get_auth_online()
  if not is_net_online():
    print('getting net online...')
    get_net_online()
