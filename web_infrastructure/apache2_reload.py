#!/usr/bin/python
#coding: utf-8 -*-

# (c) 2015, Enrique Conci <qmax.mail@gmail.com>
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: apache2_reload
version_added: 1.6
author: "Enrique Conci"
short_description: Execute reload activities in Apache2 webserver
description:
   - Verify the vhosts configuration.
   - Reload.
   - Hard-Restart.
   - Graceful Restart.
   - Stop.
   - Start.
options:
   action:
     description:
        - indicate the desired action to be executed.
     choices: ['configtest', 'reload', 'restart', 'graceful', 'start', 'stop']
     default: check-config

'''

EXAMPLES = '''
# Reload apache
- apache2_reload: action=reload

# Graceful apache restart
- apache2_reload: action=graceful
'''

def get_bin(module):
    apache_bin=module.get_bin_path("apachectl")
    if apache_bin is None:
        module.fail_json(msg="apachectl binary not found")
    else:
        return apache_bin

def apache_run(module, apache_bin):
    action = module.params['action']
    result, stdout, stderr = module.run_command("%s %s" % (apache_bin, action))
    if result !=0:
        module.fail_json(msg="Action Failed: %s" % (stdout))
    else:
        module.exit_json(changed = False, result = "Success")



def main():
    module = AnsibleModule(
        argument_spec = dict(
            action = dict(default='graceful', choices=['configtest', 'reload', 'restart', 'graceful', 'start', 'stop'])
        ),
    )

    apache_run(module,get_bin(module))

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()