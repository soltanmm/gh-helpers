#!/usr/bin/env python

from common import get

notifications = get('/repos/grpc/grpc/notifications').json()
for notification in notifications:
  if not notification['unread']:
    continue
  if notification['reason'] == 'mention':
    issue_number = notification['subject']['url'].split('/')[-1]
    print 'https://github.com/grpc/grpc/issues/{}'.format(issue_number)
